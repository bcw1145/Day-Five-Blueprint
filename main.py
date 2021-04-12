from country import get_countries, get_answer, get_countries_list
url = "https://www.iban.com/currency-codes"

countries = get_countries(url)
country_infos = []
get_countries_list(countries, country_infos)
get_answer(country_infos)
