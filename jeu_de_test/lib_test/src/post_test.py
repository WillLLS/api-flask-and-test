from src.init import *

def post_categorieFilm_assert():

    print("\nTest post categorieFilm :")

    body = {"intitule": "testCategorie", "description": "..."}

    _url = url + '/categorieFilm'
    response = requests.post(_url, json=body)

    try:
        assert(response.status_code==201)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    assert(response.json() == body)
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def post_client_assert():

    print("\nTest post client :")

    body = {"nom_client" : "testNom", "prenom": "testPrenom","email" : "test@email.iot", "age": 1}
    _url = url + "/clients" 
    response = requests.post(_url, json=body)

    try:
        assert(response.status_code==201)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    assert(response.json() == body)
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def post_film_edit_assert():
    
    print("\nTest post film edit :")

    _url = url + "/film/edit" 
    response = requests.post(_url, json=ans["postFilm"])

    try:
        assert(response.status_code==201)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    assert(response.json() == {})
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def post_clients_id_film_assert():
        
    print("\nTest post client/id/film :")

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
        print(Fore.YELLOW + "\t -test answer not passed : {} - verify return", Style.RESET_ALL)

        return 

    assert(response.json() == payload)
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)


def post_assert():

    print(Fore.CYAN + """
    ###################
    ### POST ASSERT ###
    ###################   
    """, Style.RESET_ALL, end="")
    
    post_categorieFilm_assert()
    #post_client_assert()
    post_film_edit_assert()
    post_clients_id_film_assert()
    print()


if __name__ == "__main__":
    post_assert()
