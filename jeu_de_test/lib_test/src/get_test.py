from .init import *

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

    assert(response.json()[0] == ans["catIdFilm"])
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
    
    print(response.json())
    assert(response.json()==ans["getFilmId"])
    
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

    answer = [{'location': '/film/deletedFilm/1', 'titre': 'Forest Gump'}, {'location': '/film/deletedFilm/2', 'titre': 'test1'}]
    assert(response.json() == answer)
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def get_film_id_assert():
    print("\nTest get film/id :")

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

def get_client_id_assert():

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
    #get_film_deletedFilm_id_assert()
    get_film_id_assert()
    get_client_id_assert()
    get_clients_id_film_assert()
    print()


if __name__ == "__main__":
    get_assert()