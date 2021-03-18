from car import*
from battery import*
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):

		"""Initialize attributes of the parent class."""


		super().__init__(make, model, year)
		self.battery= Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

my_tesla.update_odometer(23_500)
my_tesla.read_odometer()