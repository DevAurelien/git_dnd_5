import import_api
from deep_translator import GoogleTranslator


def traduire(t): return GoogleTranslator(source='auto', target='fr').translate(t)


class Race:
    def __init__(self, nom, ability_bonuses, age, alignment, languages, language_desc, size, size_description, speed,
                 starting_proficiencies, subraces, traits, url, FOR, DEX, CON, INT, SAG, CHA):
        self.nom = nom
        self.ability_bonuses = ability_bonuses
        self.desc_age = age
        self.desc_alignment = alignment
        self.desc_language = language_desc
        self.languages = languages
        self.size = size
        self.desc_size_description = size_description
        self.speed = speed
        self.starting_proficiencies = starting_proficiencies
        self.subraces = subraces
        self.traits = traits
        self.url = url
        self.FOR = FOR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.SAG = SAG
        self.CHA = CHA


def create_classe_race(liste_dico_all_race):
    dico_objet_race = {}
    for element in liste_dico_all_race:
        FOR, DEX, CON, INT, SAG, CHA = 0, 0, 0, 0, 0, 0
        dic_en = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        nom = traduire(element["name"]) if element["name"] != "Dragonborn" else "Sangdragon"
        speed = element["speed"]
        speed = round(speed / 3.281) if speed != 25 else 7.5
        ability_bonuses = element["ability_bonuses"]
        for el in ability_bonuses:
            dic_en[el["ability_score"]["name"]] += el["bonus"]
        FOR, DEX, CON, INT, SAG, CHA = dic_en["STR"], dic_en["DEX"], dic_en["CON"], dic_en["INT"], dic_en["WIS"], \
            dic_en["CHA"]
        #
        age = traduire(element["age"])  # description de l'age
        alignment = traduire(element["alignment"])  # description de l'alignement
        languages = element["languages"]
        language_desc = traduire(element["language_desc"])
        size = element["size"]
        size_description = traduire(element["size_description"])
        speed = element["speed"]
        starting_proficiencies = element["starting_proficiencies"]
        subraces = element["subraces"]
        traits = element["traits"]
        url = element["url"]

        objet = Race(nom, ability_bonuses, age, alignment, languages, language_desc, size, size_description, speed,
                     starting_proficiencies, subraces, traits, url, FOR, DEX, CON, INT, SAG, CHA)
        dico_objet_race[nom] = objet

        print(objet.desc_age)

    # print(f"{nom}/ {ability_bonuses}/ {age}/ {alignment}/ {language_desc}/ {size}/ {size_description}/ {speed}/ {starting_proficiencies}/ {subraces}/ {traits}/ {url}")
    return dico_objet_race


dico_objet_race = create_classe_race(import_api.liste_dico_all_race)

# print(dico_objet_race)
