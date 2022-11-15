Dossier de test.

Pour executer un test complet, executer le script test.sh

Ce script réinitialise la base de donnée avant et après le test pour éviter les conflits.

La fonction de test se décomponse en 4 sous-parties:
    *Test get
    *Test post
    *Test put
    *Test delete

Pour effectuer des tests singuliers, utiliser les fonctions xxx_assert(). 
(xxx = la requête à tester Cf. librairie de test).


Si le script test.sh ne fonctionne pas, il est possible d'executer le fichier main.py dans le dossier ./src. 
Cependant la base de donnée se verra modifier et une nouvelle execution du test relèvera des erreurs.


Amélioration possible :
    Ajouter une vérification en passant par la base de données afin de permettre une prise en compte de la modification des données.
