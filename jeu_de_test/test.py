from colorama import Fore, Style
import requests
from lib_test.src.answer import ans


url="http://127.0.0.1:5000"

def get_categorieFilm_assert():

    print("\nTest get  categorieFilm :")

    _url = url + '/categorieFilm'
    response = requests.get(_url)

    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    assert(response.json()[1]==ans["catFilm"][1])
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def post_categorieFilm_assert():

    print("\nTest post categorieFilm :")

    body = {"intitule": "testCategorie", "description": "..."}

    _url = url + '/categorieFilm'
    response = requests.post(_url, json=body)

    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    assert(response.json() == body)
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def get_categorieFilm_id_assert():
    print("\nTest get categorieFilm/id :")

    _url = url + '/categorieFilm/2'
    response = requests.get(_url)

    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    assert(response.json()==ans["catId"])
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def get_categorieFilm_id_film_assert():
    print("\nTest get categorieFilm/id/film :")

    _url = url + '/categorieFilm/1/film'
    response = requests.get(_url)

    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    assert(response.json()[0]==ans["catIdFilm"])
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def get_clients_assert():

    print("\nTest get clients :")

    _url = url + "/clients"
    response = requests.get(_url)

    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return
    
    for i in range(3):
        assert(response.json()[i]==ans["getClient"][i])
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def post_client_assert():

    print("\nTest post client :")

    body = {"nom_client" : "testNom", "prenom": "testPrenom","email" : "test@email.iot", "age": 1}
    _url = url + "/clients" 
    response = requests.post(_url, json=body)

    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    assert(response.json() == body)
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def delete_categorieFilm_id_assert():
    print("\nTest delete Categorie :")

    _url = url + "/categorieFilm/3" 
    response = requests.delete(_url)

    if response.status_code == 404:
        print("Error 404: Check the database")
        return

    print("Answer :", response.json())
    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    assert(response.json() == {})
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def post_film_edit_assert():
    
    print("\nTest post film edit :")

    _url = url + "/film/edit" 
    response = requests.post(_url, json=ans["postFilm"])

    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    test = {'acteur film': 'test acteur', 'titre': 'testFilm'}
    assert(response.json() == test)
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def get_film_id_assert():
    
    print("\nTest get film id :")

    _url = url + "/film/1"
    response = requests.get(_url)

    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return
    
    assert(response.json()==ans["getFilmId"])
    
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

## TODO

def put_categorieFilm_id_assert():
    pass

def put_film_id_assert():
    pass

def delete_film_id_assert():
    pass

def put_categorieFilm_id_assert():
    
    print("\nTest put categoreFilm id :")

    _url = url + "/categorieFilm/5" 
    body = {"intitule": "testIntitule", "description": "testDescription"}
    response = requests.put(_url, json=body)

    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    assert(response.json() == body)
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def get_film_deletedFilm_assert():
    print("\nTest get deletedFilm :")

    _url = url + "/film/deletedFilm" 
    response = requests.get(_url)

    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    assert(response.json() == [])
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def get_film_id_assert():
    print("\nTest get film id :")

    _url = url + "/film/1" 
    response = requests.get(_url)

    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    assert(response.json() == ans["getFilmId"])
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def put_film_id_assert():
        
    print("\nTest put film id :")

    _url = url + "/film/1" 
    payload = ans["putFilmIdPayload"]
    response = requests.put(_url, json=payload)

    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    assert(response.json() == ans["putFilmIdAns"])
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def post_film_edit_assert():
        
    print("\nTest post film edit :")

    _url = url + "/film/edit" 
    response = requests.post(_url, json=ans["postFilmIdPayload"])

    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    assert(response.json() == ans["postFilmIdAns"])
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def get_film_deletedFilm_id_assert():
    pass

def get_assert():

    print(Fore.CYAN + """
    ##################
    ### GET ASSERT ###
    ##################    
    """, Style.RESET_ALL, end="")

    get_categorieFilm_assert()
    get_categorieFilm_id_assert()
    get_categorieFilm_id_film_assert()
    get_film_deletedFilm_assert()
    get_film_deletedFilm_id_assert()
    get_film_id_assert()

def put_assert():

    print(Fore.CYAN + """
    ##################
    ### PUT ASSERT ###
    ##################    
    """, Style.RESET_ALL, end="") 

    put_categorieFilm_id_assert() 
    put_film_id_assert()

def post_assert():

    print(Fore.CYAN + """
    ###################
    ### POST ASSERT ###
    ###################   
    """, Style.RESET_ALL, end="")
    
    post_categorieFilm_assert()
    #post_client_assert()
    post_film_edit_assert()

def delete_assert():
    
    delete_categorieFilm_id_assert()


################################################################################

def get_client_id():

    print("\nTest get client/id :")

    _url = url + "/clients/2" 
    response = requests.get(_url)

    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    answer = {'Adress mail': 'wi@hotmail.fr', 'Age': 23, 'Nom': 'Lalis', 'Prenom': 'William', 'id': 2}
    assert(response.json() == answer)
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def put_client_id():
            
    print("\nTest put clients/id :")

    _url = url + "/clients/2" 
    
    payload = {"nom": "Lalis", "prenom": "William", "email": "william.lalis@etu.univ-orleans.fr","age": 22}
    response = requests.put(_url, json=payload)
    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    answer = {'age': 22, 'email': 'william.lalis@etu.univ-orleans.fr', 'nom': 'Lalis', 'prenom': 'William'}
    assert(response.json() == answer)
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def delete_clients_id_assert():
    print("\nTest delete clients/id :")

    _url = url + "/clients/2" 
    response = requests.delete(_url)

    if response.status_code == 404:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        print(Fore.RED + f"\t\tError 404: Check the database.", Style.RESET_ALL)
        return
    if response.status_code == 500:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        print(Fore.RED + "\t\t-Error 500: message internal server error, verify return", Style.RESET_ALL)
        return
    
    try:
        assert(response.status_code==500)
        print(Fore.RED + "\t -Status code 500... message internal server error, verify return", Style.RESET_ALL)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    answer = {}
    assert(response.json() == answer)
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def get_clients_id_film_assert():

    print("\nTest get client/id/film :")

    _url = url + "/clients/2/film" 
    response = requests.get(_url)

    try:
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    answer = [{'titre': 'Shutter Island'}, {'titre': 'Once upon a time in Hollywood'}, {'titre': 'Django'}]
    assert(response.json() == answer)
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def post_clients_id_film_assert():
        
    print("\nTest post film edit :")

    _url = url + "/clients/2/film" 
    payload = {"idFilm": 3}
    response = requests.post(_url, json=payload)

    try:
        assert(response.status_code==201)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    if response.json() == {}:
        print(Fore.MAGENTA + "\t -test answer not passed : {} - verify return", Style.RESET_ALL)
        return 

    assert(response.json() == payload)
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

post_clients_id_film_assert()