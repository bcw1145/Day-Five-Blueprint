import os
import requests
from bs4 import BeautifulSoup


def get_countries(url):
    os.system("clear")
    country_result = requests.get(url)
    country_soup = BeautifulSoup(country_result.text, "html.parser")
    return country_soup.find_all("tr")


def get_name_code(country):
    try:
        country_name, country_currency, country_code, country_num = country.find_all(
            "td")
        if country_currency.get_text() == 'No universal currency':
            pass
        else:
            return {
                "name": country_name.get_text(),
                "code": country_code.get_text()
            }

    except:
        pass


def get_countries_list(countries, country_infos):
    for country in countries:
        country_info = get_name_code(country)
        if country_info:
            country_infos.append(country_info)

    print("Hello! Please choose select a country by a number:")
    for num in range(len(country_infos)):
        print(f"# {num} {country_infos[num]['name']}")


def get_answer(country_infos):
    a = input("#: ")
    try:
        num = int(a)
        if num > len(country_infos):
            print("Choose a number from a list.")
            get_answer(country_infos)
        else:
            print(f"You choose {country_infos[num]['name']}")
            print(f"The currency code is {country_infos[num]['code']}")

    except:
        print("That wasn't a number.")
        get_answer(country_infos)
