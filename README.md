# Andela Labs

[![Build Status](https://travis-ci.org/mattgathu/andelabs.svg?branch=master)](https://travis-ci.org/mattgathu/andelabs)

This repository contains [Andela code labs exercises](http://labs.andela.com)

## Overview

### Data type Lab


**LAB** : Define a function called data_type, to take one argument. 
Compare and return results, based on the argument supplied to the function. 
Complete the test to produce the perfect function that accounts for all expectations.

**file** : `datatype.py`

**code snippet**

```python
def data_type(input_value):
    """Data type lab function

    """
    # check if input is None
    if input_value is None:
        return 'no value'

    # check if input is str
    elif isinstance(input_value, str):
        return len(input_value)

    # check if input is boolean
    elif isinstance(input_value, bool):
        return input_value

    # check if input is integer
    elif isinstance(input_value, int):
        if input_value < 100:
            return 'less than 100'
        elif input_value > 100:
            return 'more than 100'
        else:
            return 'equal to 100'

    # check if input is a list
    elif isinstance(input_value, list):
        if len(input_value) >= 3:
            return input_value[2]
        else:
            return None
```


### Fizz Buzz Lab

**LAB** : Create a function fizz_buzz to return 'Fizz', 'Buzz', 'FizzBuzz', 
or the argument it receives, all depending on the argument of the function, 
a number that is divisible by, 3, 5, or both 3 and 5, respectively.
When the number is not divisible by 3 or 5, the number itself should be returned.

**file** : `fizzbuzz.py`

**code snippet**

```python
def fizz_buzz(num):
    """fizz buzz function

     return 'Fizz', 'Buzz', 'FizzBuzz', or the argument it receives,
     all depending on the argument
    """
    # if number divisible by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    # if number divisible by 3 only
    elif num % 3 == 0:
        return 'Fizz'
    # if number divisible by 5 only
    elif num % 5 == 0:
        return 'Buzz'
    # if number indivisible by both 3 and 5
    else:
        return num
```

### Car CLass Lab

**LAB** : You are to create a Car class that can be used to instantiate 
various vehicles. It takes in arguments that depict the type, model, 
and name of the vehicle, provided they are set.

**file** : `carclass.py`

**code snippet**

```python
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
```

## Getting started

These instructions will get you a copy of the project up and running on 
your local machine for development and testing purposes.

```
git clone https://github.com/mattgathu/andelabs.git
```

### Prerequisites

You need to have [Python](https://www.python.org/downloads/) installed.

## Running the tests

To run the automated tests for this project

### Using [nose](http://nose.readthedocs.io/en/latest/)

Installing nose

```
pip install nose
```

Running tests

```
nosetests
```

### Using Python

You can run tests using Python by executing `python tests_module.py` e.g.

```
python carclass_tests.py
```

## Authors

* **[Matt Gathu](https://github.com/mattgathu)** 

## License

This project is licensed under the MIT License.

## Acknowledgments

* Andela Bootcamp 14 Cohort