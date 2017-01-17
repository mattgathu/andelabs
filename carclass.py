"""
File      : carclass.py
Date      : January, 2017
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : car class lab module
"""


# ============================================================================
# Car class implementation
# ============================================================================
class Car(object):
    """Car class

    attributes:
        - name (str): car name
        - model (str): car model
        - car_type (str): car type
        _ speed (int): car speed
        _ num_of_doors (int): number of car doors
        _ num_of_wheels (int): number of car wheels
    """
    def __init__(self, name='General', model='GM', car_type='saloon'):
        """class constructor method"""
        self.name = name
        self.model = model
        self.car_type = car_type
        self.speed = 0
        self.num_of_doors = self.get_num_of_doors()
        self.num_of_wheels = self.get_num_of_wheels()

    def get_num_of_doors(self):
        """Determine car's number of doors

        Uses the car name to determine the correct number of doors.

        """
        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            return 2
        else:
            return 4

    def get_num_of_wheels(self):
        """Determine car's number of wheels

        Uses the car type to determine the correct number of wheels.

        """
        if self.car_type == 'trailer':
            return 8
        else:
            return 4

    def is_saloon(self):
        """check if car is of type saloon

        """
        return self.car_type == 'saloon'

    def drive(self, num):
        """drive car by altering speed

        this method as returns the updated car object.
        """
        if self.car_type == 'saloon':
            self.speed = 10 ** num
        else:
            self.speed = 77

        return self

# ============================================================================
# EOF
# ============================================================================
