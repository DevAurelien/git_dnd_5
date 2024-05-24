import requests
from pprint import pprint
from random import choice

lien_api_dnd = "https://www.dnd5eapi.co"
dico_menu_api = requests.get(lien_api_dnd + "/api").json()  # ?name=Acid+Arrow

# Recuperation et rangement des requêtes API en dico URL

dict_races_api = requests.get(lien_api_dnd + dico_menu_api["races"]).json()
liste_url_races = [lien_api_dnd + dict_races_api["results"][i]["url"] for i in range(len(dict_races_api["results"]))]


liste_dico_all_race = [requests.get(races).json() for races in liste_url_races]

if __name__ == "__main__":
    # pprint(liste_dico_all_race[0])
    pass
# print([lien_api_dnd + all_races for all_races in liste_url_races])

# dico_race_url = {}
# liste_races_en = []
# for el in dict_races_api["results"]:
#     dico_race_url[el["name"]] = el["url"]
#     liste_races_en.append(el["name"])
#
# race_aleatoire_complete = [requests.get(lien_api_dnd + dico_race_url[choice(liste_races_en)]).json()]
#
# pprint(race_aleatoire_complete[0])
