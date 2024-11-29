#На основе ранее созданного класса Restaurant из прошлого задания создайте разновидность ресторана – «Кафе-мороженое». Напишите класс IceCreamStand,
# наследующий от класса Restaurant. Добавьте атрибут с именем flavors для хранения списка сортов мороженого. Напишите метод, который выводит этот список.
# Создайте экземпляр IceCreamStand и вызовите этот метод.
from modules import Restaurant
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name, cuisine_type='мороженое')
        self.flavors = flavors

    def show_flavors(self):
        print("Сорта мороженого в наличии:")
        for flavor in self.flavors:
            print(f"- {flavor}")


flavor_list = ['Базилик', 'Шоколад', 'Клубника']
ice_cream_stand = IceCreamStand('Белоснежка', flavor_list)

print(f"Название ресторана: {ice_cream_stand.restaurant_name}")
print(f"Тип кухни: {ice_cream_stand.cuisine_type}")

ice_cream_stand.show_flavors()
print(f'Добро пожаловать в кафе {ice_cream_stand.restaurant_name}!\n')