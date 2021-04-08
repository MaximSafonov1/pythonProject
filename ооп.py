import random


class Character:
    def __init__(self, name, alias, power, energy=100):
        self.name = name
        self.alias = alias
        self.power = power
        self.energy = energy
        self.backpack = []
        self.status = ''
        self.foes = ['Грабители', 'Песочный человек', 'Доктор осьминог', 'Зеленый гоблин']

    def eat(self, food=5):
        if self.energy < 100:
            while self.energy != 100:
                if self.energy < 100:
                    print('\nУ вас сейчас меньше 100% энергии.')
                    eat_food = input('Вы можете подкрепиться(да или нет): ')
                    if eat_food == 'да' and self.energy <= 95:
                        self.energy += food
                        print('Стало', self.energy, 'энергии.')
                    elif eat_food == 'да' and self.energy == 96:
                        self.energy += 4
                        print('Стало', self.energy, 'энергии.')
                    elif eat_food == 'да' and self.energy == 97:
                        self.energy += 3
                        print('Стало', self.energy, 'энергии.')
                    elif eat_food == 'да' and self.energy == 98:
                        self.energy += 2
                        print('Стало', self.energy, 'энергии.')
                    elif eat_food == 'да' and self.energy == 99:
                        self.energy += 1
                        print('Стало', self.energy, 'энергии.')
                    else:
                        print('Это ваш выбор, но он может вам еще аукнуться...')
                        break
        else:
            print('У вас максимум энергии')

    def do_exercise(self, hours):
        while self.energy > 0 and self.power != 100:
            if self.energy > 0:
                self.power += hours * 2
                self.energy -= hours * 2
                print('Теперь ваша сила равна', self.power)
                print('И ваша энергия равна', self.energy)
                break

    def beat_up(self, foe):
        print('Наступила ночь и вы решили заступить на геройскую службу.')
        print('Вы забрались на самый высокий небоскреб, чтобы найти злодеев.')
        self.foes = random.choice(self.foes)
        if self.foes == 'Грабители':
            print('И вот в далеке вы видете как двое преступников пытаются ограбить банк!')
            print('Скорее нужна ваша помощь, иначе грабители могут улизнуть!')
            battle = input('Ринуться в бой?(да или нет): ')
            if battle == 'да':
                print('\nВы выбрали путь героя! Вперед!')
                if not isinstance(foe, Character):
                    return
                if foe.power < self.power:
                    self.status = 'Ха! Преступники пойманы и справделивость восстановлена!\nТеперь можно и отдохнуть...'
                    foe.status = 'Сук... Он надрал нам зад...\nКак же я ненавижу этого паукааа!!'
                    self.foes.remove('Грабители')
                else:
                    print('Кажется, я не дооценил врага... \nСпасаюсь бегством!')
            elif self.foes == 'Песочный человек':
                print(
                    'Хмм... Что это за песчанная буря посреди Нью-Йорка? Страно, она еще и движется за инкасаторской машиной...')
                print('Как я сразу не догодался?! Это же песочник! Быстрее в погоню!')
                battle = input('Ринуться в бой?(да или нет): ')
                if battle == 'да':
                    print('\nВы выбрали путь героя! Вперед!')
                    if not isinstance(foe, Character):
                        return
                    if foe.power < self.power:
                        self.status = 'Фуух... Это было нелегко! Но я справился! Этот песочный посыпался))\nТеперь можно и отдохнуть...'
                        foe.status = 'Да как так то!! Опять он победил меня(\nКак же я ненавижу этого паукааа!!'
                        self.foes.remove('Песочный человек')
                    else:
                        print('Кажется, я не дооценил врага... \nСпасаюсь бегством!')
            elif self.foes == 'Доктор осьминог':
                print(
                    'Вы слышите это?\nКажется показалось... А нет стоп, что это за металический скрежет?\nКак будто большой железный осьминог бежит где-то...')
                print('Как я сразу не догодался?! Это же Доктор осьминог! Быстрее в погоню!')
                battle = input('Дать люлей этому моллюску?(да или нет): ')
                if battle == 'да':
                    print('\nВы выбрали путь героя! Вперед!')
                    if not isinstance(foe, Character):
                        return
                    if foe.power < self.power:
                        self.status = 'Охх, сегодня я был как никогда хорош) Таких люлей еще никто не получал!\nТаак еще вся ночь впереди, а враги закончились. Пойдука я Мэрри Джейн наведаю...'
                        foe.status = 'После такого унижения лучше залечь на дно...\nКак же я ненавижу этого паукааа!!'
                        self.foes.remove('Доктор осьминог')
                    else:
                        print('Кажется, я не дооценил врага... \nСпасаюсь бегством!')
            elif self.foes == 'Зеленый гоблин':
                print('Кажется сегодня все тихо, можно и домой пойти поспать.')
                print('Эй! Что зааа...')
                print('Зеленый гоблин: "Хахах, что не ожидал такого восьминогий!"')
                battle = input('Нет, ну это уже наглость! Надо покончить с этим гоблинсом навсегда!(да или нет): ')
                if battle == 'да':
                    print('\nВы выбрали путь героя! Вперед!')
                    if not isinstance(foe, Character):
                        return
                    if foe.power < self.power:
                        self.status = 'Хаха, что думал победить, зеленый? Не в этот раз!'
                        foe.status = 'Ну елки-палки! План же был идеальный!\nКак же я ненавижу этого паукааа!!'
                        self.foes.remove('Зеленый гоблин')
                    else:
                        print('Кажется, я не дооценил врага... \nСпасаюсь бегством!')
            else:
                print('Тьфу на вас... Я то думал, вы настоящий герой, а вы оказывается трус...')


peter = Character('Peter Parker', 'Spider-Man', 80)
print('Мы создали нового персонаж, его зовут -', peter.name)
print('\nУ него сейчас столько энергии:', peter.energy)
print('\nЭтот герой всем известен под псевдонимом -', peter.alias)
print('\nЕго сила равна', peter.power)
peter.backpack.append('Костюм человека-паука, вебшутеры, бутерброд и 10 долларов')
print('\nЧто же в рюкзаке и паучка? Сейчас узнаем:', peter.backpack)

evils = Character('Джон и Уилл', 'грабители', 30)


def main():
    while True:
        choice = int(input('\nЕсли хотите увеличить энергию введите 1\nЕсли хотите увеличить силу введите 2\nЕсли хотите погеройствовать введите 3\nЕсли хотите выйти введите 4\n'))
        if choice == 1:
            peter.eat()
        elif choice == 2:
            print('Вы можете подкачаться и увеличить свою силу.')
            do_exer = input('Хотите стать сильнее?(да или нет): ')
            if do_exer == 'да':
                peter.do_exercise(int(input('Введите сколько часов вы хотите потренить: ')))
            else:
                print('Вы выбрали быть бездельником... Что ж герой из вас так себе.')
        elif choice == 3:
            peter.beat_up(evils)
            print('\nЧеловек-паук:', peter.status)
            print('\nГрабители:', evils.status)
        else:
            print('До свидания) Возвращайтесь скорее совершать геройские дела!')
            break


main()

# bruce = Character('Bruce Wayne', 'Batman', 85)
# print('\n\nСоздан второй персонаж -', bruce.name)
# print('\nУ него сейчас столько энергии:', bruce.energy)
# print('\nЭтот герой всем известен под псевдонимом -', bruce.alias)
# print('\nЕго сила равна', bruce.power)
# bruce.backpack.append('Костюм летучей мыши, крутейший пистолет, пистолет-крюк, бутаранги, переносной суперкомпьютер, ключи от мазерати, 3 миллиарда долларов в кеше')
# print('\nЧто же носит с собой мужик в костюме летучей мыши? А вот что:', bruce.backpack)


# bruce.beat_up(peter)
# print(bruce.status)
# print(peter.status)
