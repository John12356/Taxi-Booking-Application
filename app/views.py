from django.shortcuts import render
from taxi_booking import main
from . import Db_Manager
from taxi_booking.Customer import Customer
from taxi_booking.Booking import Booking
from taxi_booking.Taxi import Taxi


def taxi_admin(request):
    main.getdata()
    if Taxi.all_taxies:
        data = Db_Manager.get_taxi_traveled_details()
        return render(request, "data.html", {"taxies": data})
    elif request.method == "POST":
        taxi_count = int(request.POST["taxi-count"])
        print(taxi_count)
        main.initialize_taxi(taxi_count)
    return render(request, "admin.html")


def index(request):
    main.getdata()
    if request.method == "POST": 
        cus_id = int(request.POST["cus_id"])
        pick_loc = request.POST["pick_loc"]
        drop_loc = request.POST["drop_loc"]
        pick_time = int(request.POST["pick_time"])
        end_time = abs(ord(drop_loc) - ord(pick_loc)) + pick_time

        c = Customer(cus_id, pick_loc, drop_loc, pick_time, end_time)
        main.bookTaxi(c)

    return render(request, "index.html")


def reset(request):
    Db_Manager.reset_db()
    return render(request, "admin.html")