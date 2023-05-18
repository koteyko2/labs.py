import tkinter as tk


def zad12_12():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, work_time, location):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.work_time = work_time
            self.location = location

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
            print(f'Время работы: {self.work_time}')
            print(f'Локация: {self.location}')

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, work_time, location, flavors):
            super().__init__(restaurant_name, cuisine_type, work_time, location)
            self.flavors = flavors

        def show_flavors(self):
            print("Список доступных вкусов:")
            for flavor in self.flavors:
                print(f"- {flavor}")

        def add_flavor(self, flavor):
            self.flavors.append(flavor)
            print(f"Вкус {flavor} добавлен")

        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"Вкус {flavor} удален")
            else:
                print(f"Вкус {flavor} не найден")

        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"Вкус {flavor} есть")
            else:
                print(f"Вкус {flavor} отсутствует")

    class StickIceCream(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, work_time, location, flavors, stick_type):
            super().__init__(restaurant_name, cuisine_type, work_time, location, flavors)
            self.stick_type = stick_type

        def describe_stick_type(self):
            print(f"Тип палочки: {self.stick_type}")

    class SoftIceCream(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, work_time, location, flavors, cone_type):
            super().__init__(restaurant_name, cuisine_type, work_time, location, flavors)
            self.cone_type = cone_type

        def describe_cone_type(self):
            print(f"Тип рожка: {self.cone_type}")


    myIceCreamStand = IceCreamStand('Баскин-Роббинс', "Кафе-мороженое", 'Пн-Пт, 10:00-22:00', 'Saint-P', ['банан', 'вишня', 'ваниль'])


    myIceCreamStand.describe_restaurant()
    myIceCreamStand.show_flavors()
    myIceCreamStand.add_flavor(input('Введите вкус, чтобы добавить: '))
    myIceCreamStand.remove_flavor(input('Введите вкус, чтобы удалить: '))
    myIceCreamStand.check_flavor(input('Введите вкус, чтобы проверить: '))


    myStickIceCream = StickIceCream('Мороженое на палочке', 'Кафе-мороженое', 'Пн-Пт, 10:00-22:00', 'Moscow',
                                    ['chocolate', 'vanilla'], 'wooden')
    myStickIceCream.show_flavors()
    myStickIceCream.describe_stick_type()

    mySoftIceCream = SoftIceCream('Мягкое мороженое', 'Кафе-мороженое', 'Пн-Пт, 10:00-22:00', 'Kazan',
                                  ['strawberry', 'blueberry'], 'waffle')
    mySoftIceCream.show_flavors()
    mySoftIceCream.describe_cone_type()



def zad12_3():
    class IceCreamStand:
        def __init__(self, flavors):
            self.flavors = flavors
            self.root = tk.Tk()
            self.root.title("Приложенька")
            self.flavors_label = tk.Label(self.root, text="Доступные вкусы:")
            self.flavors_label.grid(row=1)
            self.flavors_listbox = tk.Listbox(self.root)
            for flavor in self.flavors:
                self.flavors_listbox.insert(tk.END, flavor)
            self.flavors_listbox.grid(row=2)
            self.root.mainloop()


    if __name__ == "__main__":
        flavors = ["Ваниль", "Банан", "Вишня"]
        ice_cream_stand = IceCreamStand(flavors)
