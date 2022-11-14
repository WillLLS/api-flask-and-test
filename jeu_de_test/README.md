Dossier de test.

Pour executer un test complet, executer le script test.sh

Ce script réinitialise avant et après le test pour éviter les conflits.

La fonction de test se décomponse en 4 sous-parties:
    - Test get
    - Test post
    - Test put
    - Test delete

Pour effectuer des tests singuliers, utiliser les fonctions xxx_assert(). 
(xxx = la requête à tester Cf. librairie de test).

Amélioration possible :
    Ajouter une vérification en passant par la base de données
