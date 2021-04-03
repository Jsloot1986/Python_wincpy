# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
def alphabetical_order(list1):
    return sorted(list1)

def won_golden_globe(name, movie_list):
    movie_name_list = [x.lower() for x in movie_list]
    if name in movie_name_list:
        return True
    else:
        return False 
    
def remove_toto_albums(movie_list, toto_list):
    new_list = [elem for elem in movie_list if elem not in toto_list]
    return new_list

movie_list = ["Falling in Between", "Valley of the Dolls", "Goodbye, Mr. Chips", "Fahrenheit", "Fiddler on the Roof", "Cinderella Liberty", "Old is New", "Jaws", "Star Wars", "Superman", "E.T.", "Memories of a Geisha"]
movie_name = ["Memories of a Geisha", "Jaws", "Star Wars", "E.T."]
toto_list = ["Fahrenheit", "The Seventh One", "Falling in Between", "Old is New"]

print(alphabetical_order(movie_list))
print(won_golden_globe("jaws", movie_name))
print(remove_toto_albums(movie_list, toto_list))

