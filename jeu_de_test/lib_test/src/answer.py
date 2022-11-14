ans = {
    "getClient": {'Adress mail': 'wi@hotmail.fr', 'Age': 23, 'Nom': 'Lalis', 'Prenom': 'William', 'id': 2},
    "catFilm": [
                {
                    "intitule": "Action", 
                    "location": "/categorieFilm/1"
                }, 
                {
                    "intitule": "Science-Fiction", 
                    "location": "/categorieFilm/2"
                }, 
                {
                    "intitule": "Comedie", 
                    "location": "/categorieFilm/3"
                }, 
                {
                    "intitule": "Drame", 
                    "location": "/categorieFilm/4"
                }, 
                {
                    "intitule": "Thriller", 
                    "location": "/categorieFilm/5"
                }, 
                {
                    "intitule": "string", 
                    "location": "/categorieFilm/7"
                }
            ],
    "catId": {
                "description": "Des histoires qui s'affranchissent des limites du réel",
                "id": 2,
                "intitule": "Science-Fiction"
                },
    "catIdFilm": {
                    "categorie": "Action",
                    "location": "/film/1",
                    "titre": "Deadpool 1"
                },
    "postFilm": {
                "titre": "testFilm",
                "categorie": [
                    1
                ],
                "acteur_film": "test acteur",
                "annee_realisation": "2022",
                "duree": "99999",
                "resume_film": "flask-restx",
                "age_min": 99
                },
    "getFilmId": {
                "acteur film": "Ryan Reynolds",
                "age minimum": 16,
                "annee realisation": "2016",
                "categorie": "Action ",
                "duree": "2h30",
                "id": 1,
                "resume film": "Un gars qui veut sauver le monde mais pas trop",
                "titre": "Deadpool 1"
                },
    "postFilmIdPayload": {
                "titre": "test_titre",
                "categorie": [
                    0
                ],
                "acteur_film": "test_acteur_film",
                "annee_realisation": "test_annee_realisation",
                "duree": "test_duree",
                "resume_film": "test_resume_film",
                "age_min": 0
                },
   "postFilmIdAns" : {
                    'acteur film': 'test_acteur_film', 
                    'id': '12', 
                    'titre': 'test_titre'
                    },

    "putFilmIdPayload": {
                "titre": "string",
                "categorie": [
                    0
                ],
                "acteur_film": "string",
                "annee_realisation": "string",
                "duree": "string",
                "resume_film": "string",
                "age_min": 0
                },
    "putFilmIdAns": {'acteurs film': 'string', 'age minimum': 0, 'année réalisation': 'string', 'durée': 'string', 'resume film': 'string', 'titre': 'string'}

} 
