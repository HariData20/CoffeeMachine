# Write your code here
"""


def what_i_have(water, milk, beans, cups, money):
    print('\nThe coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{beans} of coffee beans')
    print(f'{cups} od disposable cups')
    print(f'{money} of money')


def buy_option(water, milk, beans, cups, money):
    type_of_coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')

    if int(type_of_coffee) == 1:
        if water >= 250 and beans >= 16 and cups > 0:
            print('I have enough resources, making you a coffee!')
            water -= 250
            beans -= 16
            money += 4
            cups -= 1
            what_i_have(water, milk, beans, cups, money)
        elif water < 250:
            print('Sorry, not enough water!')
        elif beans < 16:
            print('Sorry, not enough beans!')
        elif cups == 0:
            print('Sorry, not enough cups!')
    elif int(type_of_coffee) == 2:
        if water >= 350 and beans >= 20 and milk >= 75 and cups > 0:
            print('I have enough resources, making you a coffee!')
            water -= 350
            milk -= 75
            beans -= 20
            money += 7
            cups -= 1
            what_i_have(water, milk, beans, cups, money)
        elif water < 350:
            print('Sorry, not enough water!')
        elif beans < 20:
            print('Sorry, not enough beans!')
        elif cups == 0:
            print('Sorry, not enough cups!')
        elif milk < 75:
            print('Sorry, not enough milk!')
    elif int(type_of_coffee) == 3:
        if water >= 200 and beans >= 12 and milk >= 100 and cups > 0:
            print('I have enough resources, making you a coffee!')
            water -= 200
            milk -= 100
            beans -= 12
            money += 6
            cups -= 1
            what_i_have(water, milk, beans, cups, money)
        elif water < 200:
            print('Sorry, not enough water!')
        elif beans < 12:
            print('Sorry, not enough beans!')
        elif cups == 0:
            print('Sorry, not enough cups!')
        elif milk < 100:
            print('Sorry, not enough milk!')
    elif type_of_coffee == 'back':
        return 1


def fill_option(water, milk, beans, cups, money):
    water += int(input('Write how many ml of water do you want to add:'))
    milk += int(input('Write how many ml of milk do you want to add:'))
    beans += int(input('Write how many grams of coffee beans do you want to add:'))
    cups += int(input('Write how many disposable cups of coffee do you want to add:'))



def take_option(money):
    print(f'I gave you ${money}')
    money = 0
    return money


def main():

    while True:
        option = input('\nWrite action (buy, fill, take, remaining, exit):')
        if option == 'buy':
            if buy_option(water, milk, beans, cups, money):
                continue

        elif option == 'fill':
            what_i_have(water, milk, beans, cups, money)
        elif option == 'take':

            what_i_have(water, milk, beans, cups, money)
        elif option == 'remaining':
            what_i_have(water, milk, beans, cups, money)
        elif option == 'exit':
            sys.exit()


if __name__ == "__main__":
    main()

import sys


def what_i_have(water1, milk1, beans1, cups1, money1):
    print('\nThe coffee machine has:')
    print(f'{water1} of water')
    print(f'{milk1} of milk')
    print(f'{beans1} of coffee beans')
    print(f'{cups1} od disposable cups')
    print(f'{money1} of money')


water = 400
milk = 540
beans = 120
cups = 9
money = 550

while True:
    option = input('\nWrite action (buy, fill, take, remaining, exit):')
    if option == 'buy':
        type_of_coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')

        if type_of_coffee == '1':
            if water >= 250 and beans >= 16 and cups > 0:
                print('I have enough resources, making you a coffee!')
                water -= 250
                beans -= 16
                money += 4
                cups -= 1
            elif water < 250:
                print('Sorry, not enough water!')
            elif beans < 16:
                print('Sorry, not enough beans!')
            elif cups == 0:
                print('Sorry, not enough cups!')
        elif type_of_coffee == '2':
            if water >= 350 and beans >= 20 and milk >= 75 and cups > 0:
                print('I have enough resources, making you a coffee!')
                water -= 350
                milk -= 75
                beans -= 20
                money += 7
                cups -= 1

            elif water < 350:
                print('Sorry, not enough water!')
            elif beans < 20:
                print('Sorry, not enough beans!')
            elif cups == 0:
                print('Sorry, not enough cups!')
            elif milk < 75:
                print('Sorry, not enough milk!')
        elif type_of_coffee == '3':
            if water >= 200 and beans >= 12 and milk >= 100 and cups > 0:
                print('I have enough resources, making you a coffee!')
                water -= 200
                milk -= 100
                beans -= 12
                money += 6
                cups -= 1
            elif water < 200:
                print('Sorry, not enough water!')
            elif beans < 12:
                print('Sorry, not enough beans!')
            elif cups == 0:
                print('Sorry, not enough cups!')
            elif milk < 100:
                print('Sorry, not enough milk!')
        elif type_of_coffee == 'back':
            continue
        #continue
    elif option == 'fill':
        water += int(input('Write how many ml of water do you want to add:'))
        milk += int(input('Write how many ml of milk do you want to add:'))
        beans += int(input('Write how many grams of coffee beans do you want to add:'))
        cups += int(input('Write how many disposable cups of coffee do you want to add:'))

    elif option == 'take':
        print(f'I gave you ${money}')
        money = 0

    elif option == 'remaining':
        what_i_have(water, milk, beans, cups, money)
    elif option == 'exit':
        sys.exit()  """