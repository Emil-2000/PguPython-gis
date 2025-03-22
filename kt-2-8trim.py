#В этой работе мы привели пример использовании основных трех методов ООП на примере транспорта
# Родительский класс Vehicle
class Vehicle:
    def __init__(self,  brand, model, year):
        # Приватный атрибут марка производителя
        self.__make =  brand
        # Приватны атрибут модель
        self.__model = model
        # Год выпуска
        self.year = year
        #Приватный атрибут статуса (двигается или нет), по умолчанию нет
        self.__is_moving = False

    #Проверяем статус, двигается ли транспорт или нет
    def move(self):
        self.__is_moving = True
        return f"{self.year} {self.__make} {self.__model} Выехал."

    def stop(self):
        self.__is_moving = False
        return f"{self.year} {self.__make} {self.__model} Припаркован."

    def check_status(self):
        if self.__is_moving:
            return f"{self.year} {self.__make} {self.__model} Сейчас в движении."
        else:
            return f"{self.year} {self.__make} {self.__model} Сейчас не двигается."

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

# Родительский класс ElectricalVehicle - электрический транспорт
class ElectricalVehicle:
    def __init__(self, battery_capacity):
        # Приватный атрибут емкость батареи
        self.__battery_capacity = battery_capacity

    def charge_battery(self):
        return f"Батарея емкостью {self.__battery_capacity} киловатт заряжается."

    def check_battery_status(self):
        return f"Состояние батареи, осталось: {self.__battery_capacity} киловатт."

# Класс Car, наследующий от Vehicle
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def open_trunk(self):
        return f"{self.year} {self.get_make()} {self.get_model()} багажник открыт."

# Класс Motorcycle, наследующий от Vehicle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_kickstand):
        super().__init__(make, model, year)
        #Добавляем уникальный атрибут - боковая подножка
        self.has_kickstand = has_kickstand

    def use_kickstand(self):
        if self.has_kickstand:
            return f"Боковая подножка {self.year} {self.get_make()} {self.get_model()} использована."
        else:
            return f"У {self.year} {self.get_make()} {self.get_model()} нет боковой подножки."

# Класс Truck, наследующий от Vehicle
class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        #добавляем уникальный атрибут - вес груза
        self.cargo_capacity = cargo_capacity

    def load_cargo(self):
        return f"{self.year} {self.get_make()} {self.get_model()} загружен груз емкостью {self.cargo_capacity} тонн."

# Класс ElectricalCar, наследующий от Car и ElectricalVehicle (двойное наследование от родительских классов)
class ElectricalCar(Car, ElectricalVehicle):
    def __init__(self, make, model, year, num_doors, battery_capacity):
        Car.__init__(self, make, model, year, num_doors)
        ElectricalVehicle.__init__(self, battery_capacity)

# создаение экзепляров
vehicles = [
    Car("Toyota", "Camry", 2019, 4),
    Motorcycle("Yamaha", "Dragstar", 2006, True),
    Truck("Kamaz", "Самосвал", 2010, 2.5),
    ElectricalCar("Tesla", "Model S", 2021, 4, 75)
]

for vehicle in vehicles:
    print(vehicle.move())
    print(vehicle.check_status())
    print(vehicle.stop())
    print(vehicle.check_status())
    #if isinstance(vehicle, Car):
    #если транспорт остановлен
    if isinstance(vehicle, Car) and not isinstance(vehicle, ElectricalCar):
        print(vehicle.open_trunk()) #открываем багажник у машины
    elif isinstance(vehicle, Motorcycle):
        print(vehicle.use_kickstand()) #опускаем подножку у мотоцикла
    elif isinstance(vehicle, Truck):
        print(vehicle.load_cargo()) #загружаем груз в грузовик
    elif isinstance(vehicle, ElectricalCar):
        print(vehicle.charge_battery()) #заряжаем теслу
        print(vehicle.check_battery_status())