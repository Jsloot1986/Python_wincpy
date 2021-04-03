from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'


""" Write your functions here. """
def shortest_names(countries):
    new_list = []
    for i in countries:
        if len(i) <= 4:
            new_list.append(i)
            continue
        else:
            continue
    return new_list

def most_vowels(countries):
    max_len = 0
    res = ''
    newlist = []
    for i in countries:
        vow_len = len([el for el in i if el in ['a', 'e', 'i', 'o', 'u']])
        if vow_len > max_len:
            max_len = vow_len
            res = i
            countrylist = (res, max_len)
            newlist.insert(0, countrylist)
        else:
            continue
    return newlist[0:3]

def alphabet_set(countries):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counted_countries = []
    count = 0
    for country in countries:
        country = country.lower()
        count_letters = len([ch for ch in country if ch in alphabet])
        if count_letters > count:
            count = count_letters
            count_country = (country, count)
            counted_countries.insert(0, count_country)
        else:
            continue
    return counted_countries
                 


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()

    """ Write the calls to your functions here. """
    print(shortest_names(countries))
    print(most_vowels(countries))
    print(alphabet_set(countries))