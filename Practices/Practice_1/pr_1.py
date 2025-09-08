import datetime
price_for_new = 50000
car_obj = {
    "year_of_manufacture": 0,
    "age_of_car": 0,
    "initial_price": 0,
    "current_mileage": 0,
    "avg_annual_mileage": 0,
    "current_price": 0
}
def get_new_car():
    new_car = car_obj.copy()
    new_car["initial_price"] = price_for_new
    new_car["year_of_manufacture"] = int(input("Enter the year of manufacture: "))
    new_car["current_mileage"] = int(input("Enter the current mileage: "))
    new_car["age_of_car"] = calculate_age(new_car["year_of_manufacture"])
    new_car["avg_annual_mileage"] = calculate_avg_annual_mileage(new_car["current_mileage"])
    new_car["current_price"] = calculate_current_price(price_for_new, new_car["age_of_car"])
    return new_car

def calculate_current_price(price_for_new, age):
    return int(price_for_new * (1 - age * 0.1))

def calculate_age(year_of_manufacture):
    return datetime.datetime.now().year - year_of_manufacture

def calculate_avg_annual_mileage(current_mileage):
    return current_mileage / datetime.datetime.now().year

def display_car_details(car_obj):
    print(f"Year of manufacture: {car_obj['year_of_manufacture']}")
    print(f"Age of car: {calculate_age(car_obj['year_of_manufacture'])}")
    print(f"Initial price: {car_obj['initial_price']}")
    print(f"Current mileage: {car_obj['current_mileage']}")
    print(f"Average annual mileage: {car_obj['avg_annual_mileage']}")
    print(f"Current price: {car_obj['current_price']}")

def main():
    new_car = get_new_car()
    display_car_details(new_car)

main()