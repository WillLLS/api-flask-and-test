from src.init import *

def delete_categorieFilm_id_assert():
    print("\nTest delete Categorie :")

    _url = url + "/categorieFilm/3" 
    response = requests.delete(_url)

    if response.status_code == 404:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        print(Fore.RED + "\t\tError 404: Check the database.", Style.RESET_ALL)
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
        assert(response.status_code==200)
        print(Fore.GREEN + "\t -test status code passed.", Style.RESET_ALL)
    except:
        print(Fore.RED + "\t -test status code not passed.", Style.RESET_ALL)
        return

    answer = {}
    assert(response.json() == answer)
    print(Fore.GREEN + "\t -test answer passed.", Style.RESET_ALL)

def delete_assert():

    print(Fore.CYAN + """
    #####################
    ### DELETE ASSERT ###
    ##################### 
    """, Style.RESET_ALL, end="")
    
    #delete_categorieFilm_id_assert()
    delete_clients_id_assert()

if __name__=="__main__":
    delete_assert()