#записуємо шаблони відповідей
class Pediatr:

    def to_pediatr(self):
        print("Ви ще дитина, зверніться до педіатра")


class Simeyniy:

    def to_simeyniy(self):
        print("Ви вже дорослий, зверніться до сімйного лікаря")


class Greeting:

    def goodbye(self):
        print("Дякую за звернення")


class TheMenFacade:
    #ініціалізуємо поля в констуркторі класу
    def __init__(self):
        self._pediatr = Pediatr()
        self._simeyniy = Simeyniy()
        self._greeting = Greeting()
    #звертаємось до методу кожного з класів
    def for_child(self):
        self._pediatr.to_pediatr()

    def for_adult(self):
        self._simeyniy.to_simeyniy()

    def for_everyone(self):
        self._greeting.goodbye()


if __name__ == '__main__':
    facade = TheMenFacade() #викликаємо метод Фасаду
    age = int(input("Вкажіть скільки вам років"))
    if age < 18:
        facade.for_child()
    else:
        facade.for_adult()
    facade.for_everyone()