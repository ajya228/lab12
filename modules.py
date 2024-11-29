#Задача «Ресторан»: создайте класс с именем Restaurant. Метод __init__() класса Restaurant должен содержать два атрибута: restaurant_name
# (название ресторана) и cuisine_type (тип кухни).
# Создайте метод describe_restaurant(), который выводит два атрибута, и метод open_restaurant(), который выводит сообщение о том, что ресторан открыт.
# Создайте на основе своего класса экземпляр с именем newRestaurant. Выведите два атрибута по отдельности, затем вызовите оба метода.

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant (self):
        print(f"Название ресторана: {self.restaurant_name}\n"
              f"Тип кухни:    {self.cuisine_type}\n")
    def open_restaurant (self):
        print (f"Ресторан {self.restaurant_name} открыт!")


#newRestaurant.update_rating(4.9)
