class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it." )

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message+= " miles on a full charge"
        print(message)

class EletricCar(Car):
    def __init__(self, make, model, year):

        super().__init__(make, model, year)
        self.battery = Battery()


    def fill_gas_tank():
        print("This car doesn't have a gas tank!")


my_tesla = EletricCar('tesla', 'model s', 2016)
print(my_tesla.get_description_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
