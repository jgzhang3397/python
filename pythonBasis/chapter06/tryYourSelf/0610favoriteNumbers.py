# Modify your program from Exercise 6-2 (page 99) 
# so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.

favorite_numbers = {
    'superman': [5, 6, 7],
    'batman' : [9],
    'spiderman' : [2, 0],
    'ironman' : [100],
    'black widow' : [69],
}

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1 :
        print(name.title() + "'s favorite numbers are:")
        for number in numbers:
            print(number)
    else:
        print(name.title() + "'s favorite number is:")
        for number in numbers:
            print(number)
    print('\n')


