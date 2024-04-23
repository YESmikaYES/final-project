from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from core.models import Car
from django.template import loader


# Create your views here.
def load_charts(request):
    all_cars = Car.objects.all().values()
    manufacturers_data = {}
    clutch_data = {}
    car_type_data = {}

    manufacturers_data_copy = {}
    car_type_data_copy = {}

    # get all values for manufacturers, clutches and car types
    for car in all_cars:
        if car["manufacturer"].replace(" ", "_") not in manufacturers_data.keys():
            manufacturers_data.update({car["manufacturer"].replace(" ", "_") : 0})
            # manufacturers_data_copy.update({car["manufacturer"] : 0})


        if car["clutch"] not in clutch_data.keys():
            clutch_data.update({car["clutch"] : 0})

        if car["car_type"].replace(" ", "_") not in car_type_data.keys():
            car_type_data.update({car["car_type"].replace(" ", "_") : 0})
            # car_type_data_copy.update({car["car_type"] : 0})


    # get rid of spaces in manufacturer and car type names
    # for manufacturer in manufacturers_data_copy.keys():
    #     if " " in manufacturer:
    #         manufacturers_data[manufacturer.replace(" ", "_")] = manufacturers_data[manufacturer]
    #         manufacturers_data.pop(manufacturer)
            
    # for car_type in car_type_data_copy.keys():
    #     if " " in car_type:
    #         car_type_data[car_type.replace(" ", "_")] = car_type_data[car_type]
    #         car_type_data.pop(car_type)
    

    # count all occurences of previously gathered data only in borrowed cars
    for car in all_cars:
        if car["current_user_id"] != None:
            manufacturers_data[car["manufacturer"].replace(" ", "_")] = manufacturers_data[car["manufacturer"].replace(" ", "_")] + 1
            clutch_data[car["clutch"]] = clutch_data[car["clutch"]] + 1
            car_type_data[car["car_type"].replace(" ", "_")] = car_type_data[car["car_type"].replace(" ", "_")] + 1

    context = {
        "manufacturers_data" : manufacturers_data,
        "clutch_data": clutch_data,
        "car_type_data": car_type_data
    }

    template = loader.get_template("charts.html")
    return HttpResponse(template.render(request=request, context=context))
