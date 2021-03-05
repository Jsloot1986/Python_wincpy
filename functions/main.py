# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

def greet(name):
    return 'Hello, ' + name + '!'

print(greet('Bob'))

def add(number1, number2, number3):
    return number1 + number2 + number3

print(add(2, 4, 6.5))

def positive(number):
 if number >= 0:
     return True
 else:
     return False

def negative(number):
 if number < 0:
     return True
 else:
     return False



print(positive(20))
print(positive(-1))
print(positive(0))
print(negative(10))
print(negative(-10))
print(negative(0))

