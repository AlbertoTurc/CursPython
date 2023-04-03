import csv
import json
import os


def read_data():
    with open("input.csv") as f:
        dict_reader = csv.DictReader(f)
        cars = list(dict_reader)
        return cars


def get_slow_cars(cars):
    slow_cars = []
    for car in cars:
        for key, value in car.items():
            if key == "hp":
                if int(value) < 120:
                    slow_cars.append(car)
    return slow_cars


def get_fast_cars(cars):
    fast_cars = []
    for car in cars:
        for key, value in car.items():
            if key == "hp":
                if 120 <= int(value) < 180:
                    fast_cars.append(car)
    return fast_cars


def get_sport_cars(cars):
    sport_cars = []
    for car in cars:
        for key, value in car.items():
            if key == "hp":
                if int(value) >= 180:
                    sport_cars.append(car)
    return sport_cars


def get_cheap_cars(cars):
    cheap_cars = []
    for car in cars:
        for key, value in car.items():
            if key == "price":
                if int(value) < 1000:
                    cheap_cars.append(car)
    return cheap_cars


def get_medium_cars(cars):
    medium_cars = []
    for car in cars:
        for key, value in car.items():
            if key == "price":
                if 1000 <= int(value) < 5000:
                    medium_cars.append(car)
    return medium_cars


def get_expensive_cars(cars):
    expensive_cars = []
    for car in cars:
        for key, value in car.items():
            if key == "price":
                if int(value) >= 5000:
                    expensive_cars.append(car)
    return expensive_cars


def write_json(cars, filename):
    folder = r"Output"
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = filename + ".json"
    directory = folder + "/" + filename
    with open(directory, "w") as output_file:
        json.dump(cars, output_file, indent=4)


def write_brand_json(cars):
    brands = set()
    tmp_car = []
    for car in cars:
        for key, value in car.items():
            if key == "brand":
                brands.add(value)
    for brand in brands:
        tmp_car.clear()
        for car in cars:
            for key, value in car.items():
                if key == "brand" and value == brand:
                    tmp_car.append(car)
        write_json(tmp_car, brand)


def exec_lesson_4():
    cars = read_data()
    slow_cars = get_slow_cars(cars)
    fast_cars = get_fast_cars(cars)
    sport_cars = get_sport_cars(cars)
    cheap_cars = get_cheap_cars(cars)
    medium_cars = get_medium_cars(cars)
    expensive_cars = get_expensive_cars(cars)
    write_json(slow_cars, "slow_cars")
    write_json(fast_cars, "fast_cars")
    write_json(sport_cars, "sport_cars")
    write_json(cheap_cars, "cheap_cars")
    write_json(medium_cars, "medium_cars")
    write_json(expensive_cars, "expensive_cars")
    write_brand_json(cars)
