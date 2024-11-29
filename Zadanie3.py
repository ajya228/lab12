#Создать класс IceCreamStand для кафе-мороженого и используя библиотеку tkinter построить простой графический интерфейс,
# показанный на рисунке, приложенном к задаче.
from Zadanie2 import IceCreamStand
from tkinter import Tk, Label, ttk, PhotoImage
from datetime import datetime

setattr(IceCreamStand, 'hours_is_open', (11, 18))

def is_open(self):
	now = datetime.now()
	open_hour, close_hour = self.hours_is_open
	open_time = open_hour <= now.hour < close_hour
	return 'открыто' if open_time else 'закрыто'


setattr(IceCreamStand, 'is_open', is_open)


def __str__(self):
	return (
		f'Название: {self.restaurant_name}\n'
		f'Часы работы: {self.working_hours} ({self.is_open()})\n'
		f'Расположение: {self.location}\n'
		f'Виды мороженого: {", ".join(self.types_of_icecream)}\n'
		f'Вкусы: {", ".join(self.flavors)}\n')


setattr(IceCreamStand, '__str__', __str__)

my_icecream_stand = IceCreamStand(restaurant_name='Белоснежка',flavors=['Базилик', 'Шоколад', 'Ваниль'])

main_window = Tk()

main_window.title(my_icecream_stand.restaurant_name.upper())

main_window.geometry('500x800')
main_window.resizable(width=False, height=False)

main_window.iconbitmap('icecream.ico')
main_window.attributes('-alpha', 0.9)

welcome_msg = ttk.Label(main_window, text=f'Добро пожаловать в кафе «{my_icecream_stand.restaurant_name}»', font=("Klein", 12))
welcome_msg.pack()

my_logo = PhotoImage(file='icecream.png')

logo_label = ttk.Label(main_window, image=my_logo)

logo_label.pack()
info_msg = ttk.Label(main_window, text=my_icecream_stand.__str__(), font=("Arial", 10))

info_msg.pack()
close_button = ttk.Button(main_window, text='Close', command=main_window.destroy)
close_button.pack(expand=True, anchor='s')



print(my_icecream_stand)
main_window.mainloop()










#setattr(IceCreamStand, 'working_hours', '11-18')
# #def __init__(self,restaurant_name,flavors,hours_is_open,location,types_of_icecream):
#     self.restaurant_name = restaurant_name
#     self.flavors = flavors
#     self.hours_is_open = hours_is_open
#     self.location = location
#     self.types_of_icecream = types_of_icecream
#
#
# def is_open(self):
#     now = datetime.now()
#     open_hour, close_hour = self.hours_is_open
#     open_time = open_hour <= now.hour < close_hour
#     return 'открыто' if open_time else 'закрыто'
#
# setattr(IceCreamStand, 'is_open', is_open)
#
# def __str__(self):
#     return (
#         f'Название: {self.restaurant_name}\n'
#         f'Часы работы: {self.working_hours} (сейчас {self.is_open()})\n'
#         f'Расположение: {self.location}\n'
#         f'Виды мороженого: {", ".join(self.types_of_icecream)}\n'
#         f'Вкусы: {", ".join(self.flavors)}\n'
#     )
#class IceStandIceCream:
 #   def __init__(self, restaurant_name, flavors, working_hours, location, types_of_icecream):
  #      self.restaurant_name = restaurant_name
   #     self.flavors = flavors
    #    self.hours_is_open = working_hours
     #   self.location = location
      #  self.types_of_icecream = types_of_icecream
#
 #   def is_open(self):
  #      now = datetime.now()
   #     open_hour, close_hour = self.hours_is_open
    #    open_time = open_hour <= now.hour < close_hour
     #   return 'открыто' if open_time else 'закрыто'
#
 #   def __str__(self):
  #      return (
   #         f'Название: {self.restaurant_name}\n'
    #        f'Часы работы: {self.hours_is_open} (сейчас {self.is_open()})\n'
     #       f'Расположение: {self.location}\n'
      #      f'Виды мороженого: {", ".join(self.types_of_icecream)}\n'
       #     f'Вкусы: {", ".join(self.flavors)}\n'
        #)


