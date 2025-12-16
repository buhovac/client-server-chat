import asyncio
import json
import logging
import websockets

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("chat_server")

clients = {}  # ws -> {"username": str, "room": str | None}
rooms = {"general": set()}  # room -> set(ws)


async def send_json(ws, data: dict):
    try:
        await ws.send(json.dumps(data))
    except websockets.exceptions.ConnectionClosed:
        pass


async def send_error(ws, msg: str):
    await send_json(ws, {"type": "error", "message": msg})


async def broadcast(room: str, data: dict, exclude=None):
    if room not in rooms: return
    targets = [ws for ws in rooms[room] if ws != exclude]
    if not targets: return
    msg = json.dumps(data)
    await asyncio.gather(*[ws.send(msg) for ws in targets], return_exceptions=True)


def get_client(ws):
    return clients.get(ws)


async def handle_action(ws, data: dict):
    action = data.get("action")
    if not action: return await send_error(ws, "Missing 'action'")

    handlers = {
        "register": handle_register,
        "create_room": handle_create_room,
        "join_room": handle_join_room,
        "leave_room": handle_leave_room,
        "send_message": handle_send_message,
        "list_rooms": lambda ws, _: send_json(ws, {"type": "rooms_list", "rooms": list(rooms.keys())})
    }

    if action in handlers:
        await handlers[action](ws, data)
    else:
        await send_error(ws, f"Unknown action '{action}'")


async def handle_register(ws, data):
    username = data.get("username")
    if not username: return await send_error(ws, "Missing 'username'")
    if any(c["username"] == username for c in clients.values()): return await send_error(ws, "Username taken")

    clients[ws] = {"username": username, "room": "general"}
    rooms["general"].add(ws)
    logger.info(f"Registered '{username}' in 'general'")

    await send_json(ws, {"type": "system", "event": "registered", "username": username, "room": "general"})
    await send_json(ws, {"type": "rooms_list", "rooms": list(rooms.keys())})
    await broadcast("general", {"type": "system", "event": "user_joined", "room": "general", "username": username},
                    exclude=ws)


async def handle_create_room(ws, data):
    if not (info := get_client(ws)): return await send_error(ws, "Register first")
    room = data.get("room")
    if not room: return await send_error(ws, "Missing 'room'")
    if room in rooms: return await send_error(ws, "Room exists")

    rooms[room] = set()
    logger.info(f"Created '{room}' by '{info['username']}'")
    await send_json(ws, {"type": "rooms_list", "rooms": list(rooms.keys())})


async def handle_join_room(ws, data):
    if not (info := get_client(ws)): return await send_error(ws, "Register first")
    new_room = data.get("room")
    if not new_room: return await send_error(ws, "Missing 'room'")
    if new_room not in rooms: return await send_error(ws, "Room not found")

    old_room = info["room"]
    if old_room and ws in rooms.get(old_room, set()):
        rooms[old_room].remove(ws)
        await broadcast(old_room,
                        {"type": "system", "event": "user_left", "room": old_room, "username": info["username"]},
                        exclude=ws)

    rooms[new_room].add(ws)
    info["room"] = new_room
    logger.info(f"'{info['username']}' joined '{new_room}'")

    await send_json(ws, {"type": "system", "event": "room_changed", "room": new_room})
    await broadcast(new_room,
                    {"type": "system", "event": "user_joined", "room": new_room, "username": info["username"]},
                    exclude=ws)


async def handle_leave_room(ws, data):
    if not (info := get_client(ws)): return await send_error(ws, "Register first")
    room = info["room"]
    if not room: return

    if ws in rooms.get(room, set()): rooms[room].remove(ws)
    info["room"] = None
    logger.info(f"'{info['username']}' left '{room}'")

    await send_json(ws, {"type": "system", "event": "left_room", "room": room})
    await broadcast(room, {"type": "system", "event": "user_left", "room": room, "username": info["username"]},
                    exclude=ws)


async def handle_send_message(ws, data):
    if not (info := get_client(ws)): return await send_error(ws, "Register first")
    text = data.get("text")
    if not text: return await send_error(ws, "Empty message")
    room = info["room"]
    if not room: return await send_error(ws, "Not in a room")

    payload = {"type": "message", "room": room, "from": info["username"], "text": text}
    logger.info(f"Message from '{info['username']}' in '{room}': {text}")
    await broadcast(room, payload)


async def handle(ws):
    logger.info(f"New connection from {ws.remote_address}")
    try:
        async for msg in ws:
            try:
                data = json.loads(msg)
                await handle_action(ws, data)
            except json.JSONDecodeError:
                await send_error(ws, "Invalid JSON")
    finally:
        if (info := clients.pop(ws, None)):
            room = info["room"]
            if room and ws in rooms.get(room, set()):
                rooms[room].remove(ws)
                await broadcast(room,
                                {"type": "system", "event": "user_left", "room": room, "username": info["username"]})
            logger.info(f"Disconnected '{info['username']}'")
        else:
            logger.info("Disconnected unregistered client")


async def main():
    async with websockets.serve(handle, "localhost", 6789):
        logger.info("Server at ws://localhost:6789")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
