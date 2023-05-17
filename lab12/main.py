def zad12_1():
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

        def showing_flavors(self):
            print("Список доступных вкусов:")
            for flavor in self.flavors:
                print(f"- {flavor}")




    myIceCreamStand = IceCreamStand('Баскин-Роббинс', "Кафе-мороженое", 'Пн-Пт, 10:00-22:00', 'Saint-P', ['banana', 'cherry', 'vanilla'])
    myIceCreamStand.describe_restaurant()
    myIceCreamStand.showing_flavors()