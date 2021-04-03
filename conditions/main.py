# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
# factors
#weather = ["rainy", "sunny", "windy", "neutral"]
#time_of_day = ["day", "night"]
#milk_cow = True
#location = ["pasture", "cowshed"]
#season = ["winter", "spring", "summer", "fall"]
#slurry_tank = True
#grass_status = True

def farm_action(weather, time_day, milk_cow, location, season, slurry_tank, grass_status):
    if (time_day == 'night' or weather == 'rainy') and location == 'pasture':
        print('take cows to cowshed')
    elif milk_cow == True:
        if location == 'cowshed':
            print('milk cows')
        else:
            print('take the cows to cowshed')
            print('milk cows')
            print('take cows back to pasture')
    elif (location == 'cowshed' and weather != 'sunny' or 'windy') and slurry_tank == True:
        print('fertilize pasture')
    elif grass_status == True and season == 'spring' and weather == 'sunny' and location != 'pasture':
        print('mow grass')
    else:
        print('wait')
        


farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True) #Fertilize pasture
farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True) #wait
farm_action('windy', 'night', True, 'cowshed', 'winter', True, True) #milk cows
farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)  # take cows to cowshed, milk the cows, take cows back to pasture
farm_action('sunny', 'day', False, 'cowshed', 'spring', False, True)  # mow grass

