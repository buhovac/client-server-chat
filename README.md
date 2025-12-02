# client-server-chat
IFOSUP Exercises

## Partie Serveur

Le serveur sera une CLI. Il doit maintenir une structure de données centrale en mémoire (pas de db externe !) pour cartographier les clients connectés aux salons auxquels ils appartiennent. 

Il doit démarrer avec un salon par défaut auquel tous les clients sont initialement affectés. 

Par facilité, les utilisateurs ne peuvent pas se trouver dans plusieurs salons en même temps.

Le serveur doit inclure un système de journalisation (logging). 

Il doit être implémenté de manière asynchrone et non-bloquante pour gérer la concurrence.

Vous devrez créer un Protocole Applicatif en JSON, structurant les actions que le serveur peut faire :
•  Créer un salon ;
•  Rejoindre un salon ;
•  Quitter un salon ;
•  Envoyer un message ;
•  Recevoir un message.

## Partie Client

Le client disposera d’une interface graphique claire et ergonomique. 

Il doit être implémenté en mode asynchrone. 

Le client doit pouvoir indiquer l’adresse IP et le port de connexion au serveur, ainsi que son nom d’utilisateur unique pour s’identifier sur le serveur.

Le client doit afficher la liste des salons actifs sur le serveur. 

Le client ne peut utiliser qu’un salon actif à la fois. 

La connexion à un autre salon le déconnectera de l’ancien.


