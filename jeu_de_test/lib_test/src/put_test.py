from src.init import *

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

def put_client_id():
            
    print("\nTest put client/id :")

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

def put_assert():

    print(Fore.CYAN + """
    ##################
    ### PUT ASSERT ###
    ##################    
    """, Style.RESET_ALL, end="") 

    put_categorieFilm_id_assert() 
    put_film_id_assert()
    put_client_id()

if __name__=="__main__":
    put_assert()