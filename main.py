# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string
import time

from geonamescache import GeonamesCache
import random as r

from names import get_first_name
from names import get_last_name


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y %I:%M %p', prop)


def generate():
    length = 25
    colors = ["Rouge", "Bleu", "Vert", "Jaune", "Violet", "Orange", "Rose", "Marron", "Gris", "Cyan", "Turquoise",
              "Argent", "Blanc", "Noir"]
    chocolate = ['MILKA', 'KINDER', 'LINDT', 'FERRERO', 'NUTELLA', 'M et S', 'TOBLERONE', 'KITKAT', 'MARS', 'LION',
                 'CELEBRATIONS', 'LU', 'MIKADO', 'BOUNTY', 'TWIX', 'MON_CHERI', 'SNICKERS']
    cars = ["Renault", "Peugeot", "Citroen", "BMW", "Mercedes", "Audi", "Tesla", "Dacia", "Ferrari", "Honda", "Jeep",
            "Kia", "Lamborghini",
            "Mitsubishi", "Nissan", "Opel", "Porsche", "Seat", "Toyota", "Volvo", "Volkswagen"]

    li_imma = []

    f_ville = open("ville.sql", "w")
    f_convention = open("convention.sql", "w")
    f_parking = open("parking.sql", "w")
    f_voiture = open("voiture.sql", "w")
    f_visiteur = open("visiteur.sql", "w")
    f_accompagnateur = open("accompagnateur.sql", "w")
    f_assist = open("assist.sql", "w")
    f_exposant = open("exposant.sql", "w")
    f_va_exposer = open("vaexposer.sql", "w")
    f_produit = open("produit.sql", "w")
    f_expose = open("expose.sql", "w")
    f_all = open("all.sql", "w")

    gc = GeonamesCache()
    c = gc.get_cities()
    fr_cities = [c[key]['name'] for key in list(c.keys()) if c[key]['countrycode'] == 'FR']

    code_postal = r.sample(range(10000, 99999), length)
    habitants = r.randrange(1, 10000000)
    num_conv = r.sample(range(1, 1000), length)
    places = r.randrange(10, 100000)
    num_parking = r.sample(range(1, 100), length)
    places_parking = r.randrange(1, 10000)
    num_vis = r.sample(range(1000, 10000), length)
    num_acco = r.sample(range(1000, 10000), length)
    num_loto = r.sample(range(100, 10000), length)
    num_expo = r.sample(range(1, 1000), length)
    stand = r.randrange(1, 1000)
    num_prod = r.sample(range(1, 10000), length)
    qs = r.randrange(0, 100000)
    poids = r.randrange(10, 2000)

    for i in range(length):
        marque = str(chocolate.__getitem__(r.randrange(0, len(chocolate))))
        place_type = r.randrange(0, 5)
        vip = r.randrange(0, 5)

        while True:
            imma = r.choice(string.ascii_uppercase) + r.choice(string.ascii_uppercase) + "-" + \
                   str(r.randrange(0, 9)) + str(r.randrange(0, 9)) + str(r.randrange(0, 9)) + \
                   "-" + r.choice(string.ascii_uppercase) + r.choice(string.ascii_uppercase)
            if not li_imma.__contains__(imma):
                break

        query_ville = "INSERT INTO $T VALUES($0, $1, $2);" + "\n"
        query_ville = query_ville.replace("$T", "Ville") \
            .replace("$0", str(code_postal.__getitem__(i))) \
            .replace("$1", "'" + str(fr_cities.__getitem__(r.randrange(0, len(fr_cities)))).replace("'", " ") + "'") \
            .replace("$2", str(habitants))

        query_convention = "INSERT INTO $T VALUES($0, $1, $2, $3);" + "\n"
        query_convention = query_convention.replace("$T", "Convention") \
            .replace("$0", str(num_conv.__getitem__(i))) \
            .replace("$1",
                     "'" + random_date("1/1/2020 1:30 AM", "09/12/2021 5:30 AM", r.random()).split(" ").__getitem__(
                         0) + "'") \
            .replace("$2", str(places)) \
            .replace("$3", str(code_postal.__getitem__(i)))

        query_parking = "INSERT INTO $T VALUES($0, $1, $2, $3);" + "\n"
        query_parking = query_parking.replace("$T", "Parking") \
            .replace("$0", str(num_parking.__getitem__(i))) \
            .replace("$1", str(places_parking)) \
            .replace("$2", "'" + ("VOITURE" if place_type <= 2 else ("DEUX_ROUES" if place_type == 3 else "BUS")) + "'") \
            .replace("$3", str(num_conv.__getitem__(i)))

        query_voiture = "INSERT INTO $T VALUES($0, $1, $2, $3);" + "\n"

        if r.randrange(0, 4) == 0:
            query_voiture = "INSERT INTO $T(imma, marque, numPark) VALUES($0, $2, $3);" + "\n"

        if r.randrange(0, 4) == 0:
            query_voiture = "INSERT INTO $T(imma, coul, numPark) VALUES($0, $1, $3);" + "\n"

        query_voiture = query_voiture.replace("$T", "Voiture") \
            .replace("$0", "'" + imma + "'") \
            .replace("$1", "'" + colors.__getitem__(r.randrange(0, len(colors))) + "'") \
            .replace("$2", "'" + str(cars.__getitem__(r.randrange(0, len(cars)))) + "'") \
            .replace("$3", str(num_parking.__getitem__(i)))

        if r.randrange(0, 2) == 0:
            query_visiteur = "INSERT INTO $T VALUES($0, $1, $2);" + "\n"
            query_visiteur = query_visiteur.replace("$2", "'" + str(imma) + "'")
        else:
            query_visiteur = "INSERT INTO $T(numVis, typePass) VALUES($0, $1);" + "\n"

        query_visiteur = query_visiteur.replace("$T", "Visiteur") \
            .replace("$0", str(num_vis.__getitem__(i))) \
            .replace("$1", "'VIP'" if vip < 1 else "'Standard'")

        query_accompagnateur = "INSERT INTO $T VALUES($0, $1, $2);" + "\n"
        query_accompagnateur = query_accompagnateur.replace("$T", "Accompagnateur") \
            .replace("$0", str(num_acco.__getitem__(i))) \
            .replace("$1", "'" + get_first_name() + "'") \
            .replace("$2", "'" + get_last_name() + "'")

        query_assist = "INSERT INTO $T VALUES($0, $1, $2, $3);" + "\n"
        query_assist = query_assist.replace("$T", "Assist") \
            .replace("$0", str(num_conv.__getitem__(i))) \
            .replace("$1", str(num_vis.__getitem__(i))) \
            .replace("$2", str(num_acco.__getitem__(i))) \
            .replace("$3", str(num_loto.__getitem__(i)))

        query_exposant = "INSERT INTO $T VALUES($0);" + "\n"
        query_exposant = query_exposant.replace("$T", "Exposant") \
            .replace("$0", str(num_expo.__getitem__(i)))

        query_vaexposer = "INSERT INTO $T VALUES($0, $1, $2);" + "\n"
        query_vaexposer = query_vaexposer.replace("$T", "Vaexposer") \
            .replace("$0", str(num_conv.__getitem__(i))) \
            .replace("$1", str(num_expo.__getitem__(i))) \
            .replace("$2", str(stand))

        query_produit = "INSERT INTO $T VALUES($0, $1, $2, $3, $4);" + "\n"
        query_produit = query_produit.replace("$T", "Produit") \
            .replace("$0", "'" + marque + "'") \
            .replace("$1", str(num_prod.__getitem__(i))) \
            .replace("$2", "'" + "NOM_PRODUIT" + "'") \
            .replace("$3", str(qs)) \
            .replace("$4", str(poids))

        query_expose = "INSERT INTO $T VALUES($0, $1, $2);" + "\n"
        query_expose = query_expose.replace("$T", "Expose") \
            .replace("$0", str(num_expo.__getitem__(i))) \
            .replace("$1", "'" + marque + "'") \
            .replace("$2", str(num_prod.__getitem__(i)))

        print("SQL tuple in ville.sql successfully generated")
        f_ville.write(query_ville)

        print("SQL tuple in convention.sql successfully generated")
        f_convention.write(query_convention)

        print("SQL tuple in parking.sql successfully generated")
        f_parking.write(query_parking)

        print("SQL tuple in voiture.sql successfully generated")
        f_voiture.write(query_voiture)

        print("SQL tuple in visiteur.sql successfully generated")
        f_visiteur.write(query_visiteur)

        print("SQL tuple in accompagnateur.sql successfully generated")
        f_accompagnateur.write(query_accompagnateur)

        print("SQL tuple in assist.sql successfully generated")
        f_assist.write(query_assist)

        print("SQL tuple in exposant.sql successfully generated")
        f_exposant.write(query_exposant)

        print("SQL tuple in vaexposer.sql successfully generated")
        f_va_exposer.write(query_vaexposer)

        print("SQL tuple in produit.sql successfully generated")
        f_produit.write(query_produit)

        print("SQL tuple in expose.sql successfully generated")
        f_expose.write(query_expose)

    f_ville.close()
    f_convention.close()
    f_parking.close()
    f_voiture.close()
    f_visiteur.close()
    f_accompagnateur.close()
    f_assist.close()
    f_exposant.close()
    f_va_exposer.close()
    f_produit.close()
    f_expose.close()

    f_ville = open("ville.sql")
    f_convention = open("convention.sql")
    f_parking = open("parking.sql")
    f_voiture = open("voiture.sql")
    f_visiteur = open("visiteur.sql")
    f_accompagnateur = open("accompagnateur.sql")
    f_assist = open("assist.sql")
    f_exposant = open("exposant.sql")
    f_va_exposer = open("vaexposer.sql")
    f_produit = open("produit.sql")
    f_expose = open("expose.sql")

    all_concat = f_ville.read() + f_convention.read() + f_parking.read() + f_voiture.read() + f_visiteur.read() + \
                 f_accompagnateur.read() + f_assist.read() + f_exposant.read() + f_va_exposer.read() + f_produit.read() + \
                 f_expose.read()
    f_all.write(all_concat)

    f_all.close()

    # for j in range(456):
    #     first = get_first_name()
    #     last = get_last_name()
    #     bdate = random_date("1/1/1970 1:30 PM", "1/1/2020 1:30 PM", random.random()).split(" ").__getitem__(0)
    #     city = US_cities.__getitem__(random.randrange(0, len(US_cities), 1))
    #
    #     if random.randint(0, 1) == 0:
    #         f.write("INSERT INTO Endette VALUES('" + str(j + 1) + "', '" + first + "', '" + last + "', '" + str(
    #             city) + "', TRUE);\n")
    #     else:
    #         f.write("INSERT INTO Endette VALUES('" + str(j + 1) + "', '" + first + "', '" + last + "', '" + str(
    #             city) + "', FALSE);\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    generate()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/