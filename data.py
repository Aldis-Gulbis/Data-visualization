import os

def open_file():
    if os.path.exists("Prices.csv"):
        fails = open("Prices.csv", "a", encoding = "utf-8")

    else:
        fails = open("Prices.csv", "a", encoding="utf-8")
        fails.write("Valsts nosaukums;Benzīna cena (€/L);Dīzeļdegvielas cena (€/L);Datums\n")

    return fails


def append(petrol_price, diesel_price, country, date):
    fails = open_file()
    fails.write(f"{country};{float(petrol_price)};{float(diesel_price)};{date}\n")
    fails.close()