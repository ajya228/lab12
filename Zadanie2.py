#Добавить атрибуты для описания локации и времени работы кафе-мороженого.
#Реализовать методы для добавления и удаления сортов мороженого из списка flavors.
#Реализовать метод для проверки наличия определенного сорта мороженого в списке flavors.
#Добавить методы для разных типов мороженого (например, мороженое на палочке, мягкое мороженое, и т.д.) и реализовать методы для работы с каждым типом.
from modules import Restaurant
from Zadanie1 import IceCreamStand
from Zadanie1 import ice_cream_stand,flavor_list
setattr(IceCreamStand, 'location', 'Сосновый бор') #добавляет новые атрибуты и методы
setattr(IceCreamStand, 'working_hours', '11-18')
setattr(IceCreamStand, 'types_of_icecream', ['В рожке', 'В пиалочке', 'Фруктовый лёд','На палочке'])

def flavor_add(self, flavor):
    if flavor not in self.flavors:
        self.flavors.append(flavor)
        print(f"Вкус '{flavor}' добавлен в меню.")
    else:
        print(f"Вкус '{flavor}' уже есть в меню.")

def delete_flavor(self, flavor):
    if flavor in self.flavors:
        self.flavors.remove(flavor)
        print(f"Вкус мороженого '{flavor}' удален из меню.")
    else:
        print(f"Вкус мороженого '{flavor}' не найден в меню.")

def check_flavor(self, flavor):
    if flavor in self.flavors:
        print(f"Вкус мороженого '{flavor}' доступен.")
    else:
        print(f"Вкус мороженого '{flavor}' недоступен.")

IceCreamStand.flavor_add = flavor_add
IceCreamStand.delete_flavor = delete_flavor
IceCreamStand.check_flavor = check_flavor

ice_cream_stand.show_flavors()
ice_cream_stand.flavor_add('Ваниль')
ice_cream_stand.show_flavors()

ice_cream_stand.check_flavor('Шоколад')
ice_cream_stand.check_flavor('Мятный')

ice_cream_stand.delete_flavor('Клубника')
ice_cream_stand.show_flavors()