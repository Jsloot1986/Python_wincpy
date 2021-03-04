# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
leek_price_str = str(leek_price)

order = 'leek 4'
index_of_leek = order.find("4")
number_of_leek = order[5]
total_leek = int(number_of_leek)
sum_total = leek_price * total_leek


print(f'The total price of {number_of_leek} kilo of leek.')
print(f'Leek costs {leek_price_str} euro per kilo. \n the total price is {sum_total} euro')

broccoli = 2.34
broccoli_order = 1.6

total_price_broccoli = broccoli * broccoli_order

print(f'{float(broccoli_order)} kg broccoli costs {round(total_price_broccoli, 2)} euro')


