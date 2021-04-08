class Character:
    name = ''
    power = 0
    energy = 100

    def eat(self, food=5):
        while self.energy != 100:
            if self.energy < 100:
                print('\nУ вас сейчас меньше 100% энергии.')
                eat_food = input('Вы можете подкрепиться(да или нет)')
                if eat_food == 'да' and self.energy < 100:
                    self.energy += food
                    print('Стало', self.energy, 'энергии.')
                else:
                    print('Это ваш выбор, но он может вам еще аукнуться...')
                    break

    def do_exercise(self, hours=1):
        while self.energy > 0 and self.power != 100:
            if self.energy > 0:
                print('Вы можете подкачаться и увеличить свою силу.')
                do_exer = input('Хотите стать сильнее?(да или нет)')
                if do_exer == 'да':
                    self.power += hours * 5
                    self.energy -= hours * 5
                    print('Теперь ваша сила равна', self.power)
                    print('И ваша энергия равна', self.energy)
                else:
                    print('Вы выбрали быть бездельником... Что ж герой из вас так себе.')
                    break


peter = Character()
peter.name = 'Peter Parker'
print('Мы создали нового персонаж, его зовут -', peter.name)
peter.energy = 90
print('У него сейчас столько энергии:', peter.energy)
peter.alias = 'Spider-Man'
print('Этот герой всем известен под псевдонимом -', peter.alias)
peter.power = 70
print('Его сила равна', peter.power)
#peter.eat()
#peter.do_exercise()

def main():
     while True:
       choice = int(input('\nЕсли хотите увеличить энергию введите 1\nЕсли хотите увеличить силу введите 2\n'))
       if choice == 1:
         peter.eat()
       elif choice == 2:
         peter.do_exercise(int(input('Введите сколько часов вы хотите потренить: ')))

main()

# bruce = Character()
# bruce.name = 'Bruce Wayne'
# bruce.power = 75
# bruce.energy = 100
# bruce.alias = 'Batman'
# print('\nСоздан второй персонаж -', bruce.name)
# print('У него сейчас столько энергии:', bruce.energy)
# print('Этот герой всем известен под псевдонимом -', bruce.alias)
# print('Его сила равна', bruce.power)