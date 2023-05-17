def zad11_1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"название ресторана: {self.restaurant_name}")
            print(f"тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print("ресторан открыт")

    newRestaurant = Restaurant(input(), "Многонациональная")

    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()



def zad11_2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"название ресторана: {self.restaurant_name}")
            print(f"тип кухни: {self.cuisine_type}")

    res_1 = Restaurant(input('Введите ресторан: '), "Итальянская")
    res_2 = Restaurant("Токио_сити", "Азиатская")
    res_3 = Restaurant("KFC", "Фаст-фуд")

    res_1.describe_restaurant()
    res_2.describe_restaurant()
    res_3.describe_restaurant()


def zad11_3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"название ресторана: {self.restaurant_name}")
            print(f"тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"ресторан открыт!")

        def old_rating(self, rating):
            self.rating = rating
            print(f"рейтинг: {self.rating}")

        def new_rating(new_rat):
            new_rat.rating = float(input('новый рейтинг: '))
            print()
            newRestaurant = Restaurant("Баклажан", "Многонациональная")
            newRestaurant.describe_restaurant()
            newRestaurant.open_restaurant()
            print(f"рейтинг обновлён: {new_rat.rating}")

    newRestaurant = Restaurant("Баклажан", "Многонациональная")
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
    newRestaurant.old_rating(4.7)
    print()
    newRestaurant.new_rating()