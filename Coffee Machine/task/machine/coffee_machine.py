import sys


class CoffeeMachine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550
    state = 'init'
    question = None

    def __init__(self):
        self.state = 'selecting'
        self.question = 'Write action (buy, fill, take, remaining, exit):'
        print(self.question)

    def calling(self, action):
        if self.state == 'buy':
            self.buy(action)
        elif self.state.startswith('fill'):
            self.fill(action)

        if self.state == 'selecting':
            if action == 'buy':
                self.question = '\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:'
                print(self.question)
                self.state = 'buy'
                return
            elif action == 'fill':
                print()
                self.fill(action)
                return
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.remaining()
            print()
            print('Write action (buy, fill, take, remaining, exit):')

    def remaining(self):
        print(f'''
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
${self.money} of money
        ''')
        self.state = 'selecting'
        #return self.calling()

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0
        #return self.calling()

    def fill(self, action):
        if self.state == 'selecting':
            print('Write how many ml of water do you want to add:')
            self.state = 'fill_water'
        elif self.state == 'fill_water':
            self.water += int(action)
            print('Write how many ml of milk do you want to add:')
            self.state = 'fill_milk'
        elif self.state == 'fill_milk':
            self.milk += int(action)
            print('Write how many grams of coffee beans do you want to add:')
            self.state = 'fill_coffee'
        elif self.state == 'fill_coffee':
            self.beans += int(action)
            print('Write how many disposable cups do you want to add:')
            self.state = 'fill_cups'
        else:
            self.cups += int(action)
            self.state = 'selecting'
        #return self.calling()

    def buy(self, action):
        type_of_coffee = action
        if type_of_coffee == '1':
            if self.water >= 250 and self.beans >= 16 and self.cups > 0:
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
            elif self.water < 250:
                print('Sorry, not enough water!')
            elif self.beans < 16:
                print('Sorry, not enough beans!')
            elif self.cups == 0:
                print('Sorry, not enough cups!')
        elif type_of_coffee == '2':
            if self.water >= 350 and self.beans >= 20 and self.milk >= 75 and self.cups > 0:
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
            elif self.water < 350:
                print('Sorry, not enough water!')
            elif self.beans < 20:
                print('Sorry, not enough beans!')
            elif self.cups == 0:
                print('Sorry, not enough cups!')
            elif self.milk < 75:
                print('Sorry, not enough milk!')
        elif type_of_coffee == '3':
            if self.water >= 200 and self.beans >= 12 and self.milk >= 100 and self.cups > 0:
                print('I have enough resources, making you a coffee!')
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
            elif self.water < 200:
                print('Sorry, not enough water!')
            elif self.beans < 12:
                print('Sorry, not enough beans!')
            elif self.cups == 0:
                print('Sorry, not enough cups!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')
        elif type_of_coffee == 'back':
            self.state = 'selecting'
        self.state = 'selecting'


coffee = CoffeeMachine()

while True:
    value = input()
    if value != 'exit':
        coffee.calling(value)
    else:
        break
