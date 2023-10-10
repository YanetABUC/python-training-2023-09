class NotEnoughFuelException(Exception):
    def __init__(self, message = "Not enough fuel for this operation") -> None:
        self.message = message
        super().__init__(message)

class InvalidFuelValueException(Exception):
    def __init__(self, message = "The value of the fuel is not valid") -> None:
        self.message = message
        super().__init__(message)

class Rocket:

    FUEL_TO_TAKE_OFF = 10 # Default amount of fuel, in liters, to take off successfully 

    def __init__(self, fuel_total:float) -> None:
        if(fuel_total < 0):
            raise InvalidFuelValueException()
        
        self.__fuel_total = fuel_total

    @property
    def fuel_total(self):
        return self.__fuel_total

    def take_off(self):
        if(self.__fuel_total <= self.FUEL_TO_TAKE_OFF):
            raise NotEnoughFuelException(f"This rocket requires  {self.FUEL_TO_TAKE_OFF} liters of fuel to take off. It has {self.__fuel_total} liters of fuel")
        
        self.__fuel_total -= self.FUEL_TO_TAKE_OFF
        print("The rocket took off")
        print(f"There are {self.__fuel_total} liters of fuel left")

    def recharge_fuel(self, total_of_litters:int):
        self.__fuel_total += total_of_litters
        print("Recharging fuel...")
        print(f"There are {self.__fuel_total} liters of fuel now")
    

try:
    initial_amout_fuel = float(input("Enter the amount of fuel in liters for your rocket: "))
    rocket = Rocket(initial_amout_fuel)
    rocket.take_off()
except NotEnoughFuelException as e:
    print(e)    
    rocket.recharge_fuel(rocket.FUEL_TO_TAKE_OFF )
except InvalidFuelValueException as e:
    print(e)