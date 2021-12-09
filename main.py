# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string
import time

import geonamescache
import random as r

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)


def generate():
    length = 20
    colors = ["Rouge", "Bleu", "Vert", "Jaune", "Violet", "Orange", "Rose", "Marron", "Gris", "Cyan", "Turquoise",
              "Bordeau", "Argent", "Mauve", "Blanc", "Noir"]

    f_ville = open("ville.sql", "w")
    f_convention = open("convention.sql", "w")
    f_parking = open("parking.sql", "w")
    f_voiture = open("voiture.sql", "w")

    gc = geonamescache.GeonamesCache()
    c = gc.get_cities()
    fr_cities = [c[key]['name'] for key in list(c.keys()) if c[key]['countrycode'] == 'FR']

    for i in range(length):
        code_postal = r.sample(range(10000), length)
        habitants = r.randrange(0, 10000000)
        num_conv = r.sample(range(1000), length)
        places = r.randrange(0, 100000)
        num_parking = r.sample(range(100), length)
        places_parking = r.randrange(0, 10000)
        place_type = r.randrange(0, 3)
        imma = r.choice(string.ascii_uppercase) + r.choice(string.ascii_uppercase) + "-" + \
               str(r.randrange(0, 9)) + str(r.randrange(0, 9)) + str(r.randrange(0, 9)) + \
               "-" + r.choice(string.ascii_uppercase) + r.choice(string.ascii_uppercase)

        query_ville = "INSERT INTO $T VALUES($0, $1, $2);" + "\n"
        query_ville = query_ville.replace("$T", "Ville") \
            .replace("$0", str(code_postal.__getitem__(i))) \
            .replace("$1", "'" + fr_cities.__getitem__(r.randrange(0, len(fr_cities))) + "'") \
            .replace("$2", "'" + str(habitants) + "'")

        query_convention = "INSERT INTO $T VALUES($0, $1, $2, $3);" + "\n"
        query_convention = query_convention.replace("$T", "Convention") \
            .replace("$0", str(num_conv)) \
            .replace("$1", "'" + random_date("1/1/2020 1:30 AM", "09/12/2021 5:30 AM", 1) + "'") \
            .replace("$2", str(places)) \
            .replace("$3", str(code_postal))

        query_parking = "INSERT INTO $T VALUES($0, $1, $2, $3);" + "\n"
        query_parking = query_parking.replace("$T", "Parking") \
            .replace("$0", str(num_parking)) \
            .replace("$1", str(places_parking)) \
            .replace("$2", "'" + ("VOITURE" if place_type == 0 else ("DEUX_ROUES" if place_type == 1 else "BUS")) + "'") \
            .replace("$3", str(num_conv))

        query_voiture = "INSERT INTO $T VALUES($0, $1, $2, $3);" + "\n"
        query_voiture = query_voiture.replace("$T", "Voiture") \
            .replace("$0", "'" + imma + "'") \
            .replace("$1", "'" + colors.__getitem__(r.randrange(0, len(colors))) + "'") \
            .replace("$2", "-") \
            .replace("$3", str(num_parking))

        print("SQL tuple in ville.sql successfully generated")
        f_ville.write(query_ville)

        print("SQL tuple in convention.sql successfully generated")
        f_convention.write(query_convention)

        print("SQL tuple in parking.sql successfully generated")
        f_parking.write(query_parking)

        print("SQL tuple in voiture.sql successfully generated")
        f_voiture.write(query_voiture)

    f_ville.close()
    f_convention.close()
    f_parking.close()
    f_voiture.close()

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
