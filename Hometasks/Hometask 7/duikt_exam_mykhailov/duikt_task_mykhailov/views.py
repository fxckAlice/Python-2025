from django.http import HttpResponse
from .models import CarsBrand
from django.shortcuts import render
from .models import CarsInfo

def cars_list_view(request):
    cars = CarsInfo.objects.select_related('CAR_BRAND').all()
    return render(request, "cars_list.html", {"cars": cars})


def install_demo_data(request):
    output = []

    brands_data = [
        {"BRAND_NAME": "Toyota", "BRAND_COUNTRY": "Japan", "BRAND_RATING": 9},
        {"BRAND_NAME": "Ford", "BRAND_COUNTRY": "USA", "BRAND_RATING": 8},
        {"BRAND_NAME": "BMW", "BRAND_COUNTRY": "Germany", "BRAND_RATING": 9},
    ]

    brand_objects = {}

    for data in brands_data:
        obj, created = CarsBrand.objects.get_or_create(
            BRAND_NAME=data["BRAND_NAME"],
            defaults={
                "BRAND_COUNTRY": data["BRAND_COUNTRY"],
                "BRAND_RATING": data["BRAND_RATING"],
            },
        )

        if created:
            output.append(f"Added: {obj.BRAND_NAME}")
        else:
            output.append(f"Not Created: {obj.BRAND_NAME}")

        brand_objects[obj.BRAND_NAME] = obj

    cars_data = [
        {"CAR_NAME": "Corolla", "CAR_MODEL": "2023", "CAR_PRICE": 20000, "CAR_BRAND": "Toyota"},
        {"CAR_NAME": "Mustang", "CAR_MODEL": "2022", "CAR_PRICE": 35000, "CAR_BRAND": "Ford"},
        {"CAR_NAME": "X5", "CAR_MODEL": "2023", "CAR_PRICE": 60000, "CAR_BRAND": "BMW"},
    ]

    for data in cars_data:
        brand_obj = brand_objects[data["CAR_BRAND"]]

        obj, created = CarsInfo.objects.get_or_create(
            CAR_NAME=data["CAR_NAME"],
            CAR_MODEL=data["CAR_MODEL"],
            defaults={
                "CAR_PRICE": data["CAR_PRICE"],
                "CAR_BRAND": brand_obj,
            },
        )

        if created:
            output.append(f"Added: {obj.CAR_NAME} {obj.CAR_MODEL}")
        else:
            output.append(f"Not created: {obj.CAR_NAME} {obj.CAR_MODEL}")

    return HttpResponse("<br>".join(output))
