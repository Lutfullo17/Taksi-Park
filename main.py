# class Student:
#     def __init__(self,name, phone, seria_id, group_id):
#         self.name = name
#         self.phone = phone
#         self.__seria_id = seria_id
#         self.group = group_id
#     @property
#     def get_seria(self):
#         return self.__seria_id
#     @get_seria.setter
#     def set_seria(self,new_seria):
#         if type(new_seria) == int:
#             self.__seria_id=new_seria
#         else:
#             print("Butun son kiriting ")
#
#
# p1 = Student('name', 6445,545454,554)
# # print(p1.get_seria())
# # p1.set_seria(999)
#
# print(p1.get_seria)
# p1.set_seria = 1000
# print(p1.get_seria)


class Car:
    def __init__(self,model, brand, seria, year ):
        self.model = model
        self.brand = brand
        self.seria = seria
        self.year = year
        self.is_active = True

class User:
    def __init__(self,name,phone,seria, password, age, is_admin=False):
        self.username = name
        self.phone = phone
        self.seria = seria
        self.password = str(password)
        self.age = age
        self.is_active = True
        self.is_admin = is_admin

    def edit(self):
        field = input("1. Username \n 2. phone \n 3. age \n 4. Password : ")
        new_field = input("New: ")
        if field == "1":
            self.username = new_field
            print("Username Tahrirlandi")
        elif field == '2':
            self.phone = new_field
            print("Phone Tahrirlandi")
        elif field == '3':
            self.age = new_field
            print("Age Tahrirlandi")
        elif field == '4':
            self.password = str(new_field)
            print("Password Tahrirlandi")
        else:
            print("Break")
            return


class Order:
    def __init__(self,user_id,car_id,data_start,data_end):
        self.user_id = user_id
        self.car_id = car_id
        self.data_start = data_start
        self.data_end = data_end
        self.is_active = True

class Park:
    def __init__(self,title):
        self.title = title
        self.username = "admin"
        self.password = "1234"
        self.users = []
        self.orders = []
        self.cars = []

    def public_cars(self):
        count = 0
        for item in self.cars:
            if item.is_active:
                count += 1
                print(f"{count}, model: {item.model}, brand: {item.brand} ")

    def add_car(self):
        print("Add Car")
        model = input("Car Model: ")
        brand = input("Car Brand: ")
        seria = input("Car Seria: ")
        year = input("Car Year: ")
        car2 = Car(model,brand,seria,year)
        self.cars.append(car2)
        print("Muvaffaqiyatli Car Qo'shidi")

    def view_cars(self):
        if not self.cars:
            print("Car Mavjud emas")
            return

        count = 0
        for item in self.cars:
            print("Car View")
            count += 1
            print(f"{count}, Model: {item.model}, Brand: {item.brand}, Seria: {item.seria}, Year: {item.year}")

    def add_user(self):
        print("Add User")
        name = input("User Name: ")
        phone = input("User Phone: ")
        seria = input("User Seria: ")
        password = input("User Password: ")
        age = input("User Age: ")

        user2 = User(name,phone,seria,password,age)
        self.users.append(user2)
        print("Muvaffaqiyatli User Qo'shildi")

    def delete_user(self):
        if not self.users:
            print("Users Mavjud emas")
            return
        print("User Delete")
        name = input("Name Kiriting: ")
        for item in self.users:
            if item.username == name:
                print("Topildi")
                print(f"Name: {item.username}, Seria: {item.seria}, Phone: {item.phone}, Age: {item.age}")
                ha = input("Malumot o'chilsinmi: (Ha/Yo'q)  ").lower()
                if ha == "ha":
                    self.users.remove(item)
                    print("Muvaffaqiyatli O'chirildi")
                return
        print("Bunday user Mavjud emas")

    def view_users(self):
        if not self.users:
            print("User Mavjud emas")
            return

        count = 0
        for item in self.users:
            print("User View")
            count += 1
            print(f"{count}, Name: {item.username}, Seria: {item.seria}, Phone: {item.phone}, Age: {item.age}")

    def get_user(self,seria):
        for item in self.users:
            if item.seria == seria and item.is_active:
                return item

        print("Malumot Topilmadi")
        return None

    def get_car(self,seria):
        for item in self.cars:
            if item.seria == seria and item.is_active:
                return item

        print("Malumot Topilmadi")
        return None

    def rent_car(self):
        print("Ijaraga oling")

        user_seria = input("User Seria Kiritng: ")
        car_seria = input("Car Seria Kiritng: ")

        user = self.get_user(user_seria)
        if not user:
            print("Bunday User Topilmadi")
            return

        car = self.get_car(car_seria)
        if not car:
            print("Bunday car Topilmadi")
            return

        date_start = input("Date Start kiriting: ")
        date_end = input("Date End kiriting: ")

        order = Order(user_seria,car_seria,date_start,date_end)
        self.orders.append(order)
        car.is_active = False

        print("Car Ijaraga olindi")

    def login(self):
        name = input("Username: ")
        password = input("Password: ")

        password = str(password)

        for item in self.users:
            if item.username == name and item.password == password:
                return item, True

        return 0, False


    def orders_view(self):
        if not self.orders:
            print("Order Mavjud emas")
            return

        count = 0
        for item in self.orders:
            print("Order View")
            count += 1
            print(f"{count}, User id: {item.user_id}, Car id: {item.car_id}, Data start: {item.data_start}, Data end: {item.data_end}")

    def end1_car(self,user_seria):
        for item in self.orders:
            if item.user_seria == user_seria and item.is_active:
                return item

        print("Malumot Topilmadi")
        return None

    def end_car(self):
        print("End Car")

        user_seria = input("User Seria Kiritng: ")

        user = self.end1_car(user_seria)
        if not user:
            print("Bunday User Topilmadi")
            return


park = Park('fddhj')
admin = User("admin",456456,4566,4564,54)
park.users.append(admin)
u1 = User("User", 12545,45655,5544,554)
park.users.append(u1)


def taxi_manager(p:Park, u:User):
    while True:
        kod = input("1. Edit \n 2. Public car \n 3. Break : ")
        if kod == '1':
            u.edit()
        elif kod == '2':
            p.public_cars()
        else:
            break

def admin_manager(p:Park, u:User):
    while True:
        kod = input("1. Car add\n 2. Car view \n 3. User add \n 4. user view \n 5. Car rent \n 6. Exit \n : ")
        if kod == "1":
            p.add_car()
        elif kod == "2":
            p.view_cars()
        elif kod == "3":
            p.add_user()
        elif kod == "4":
            p.view_users()
        elif kod == "5":
            p.rent_car()
        elif kod == "6":
            print("Tizimdan Chiqdingiz")
            break
        else:
            print("Faqat (1-6) Tanlang ")

def park_manager(p: Park):
    item = p.login()
    if item[1]:
        if item[0].is_admin:
            admin_manager(p,item[0])
        else:
            taxi_manager(p,item[0])
    else:
        print("xato")


park_manager(park)
