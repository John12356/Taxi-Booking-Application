from taxi_booking.Booking import Booking
from taxi_booking.Taxi import Taxi
from app import Db_Manager


def bookTaxi(c):
    if c.pick_time > 24:
        print("Enter correct time to pickup!!..")
        return
    Booking.book_ticket(c)


def getdata():
    Taxi.all_taxies.clear()
    db_taxi_det = Db_Manager.get_all_taxi_data()
    for taxi in db_taxi_det:
        each_taxi = Taxi(
            taxi.get("taxino"),
            taxi.get("cur_loc"),
            taxi.get("drop_time"),
            taxi.get("short_dis"),
            taxi.get("prev_loc"),
            taxi.get("pick_time"),
            taxi.get("pick_loc"),
        )
        Taxi.all_taxies.append(each_taxi)

    # Booking.taxi_travel_det.clear()
    # taxi_details = Db_Manager.get_taxi_traveled_details()
    # for taxi in taxi_details:
    #     taxi_det = Booking(
    #         taxi.get("taxino"),
    #         taxi.get("pick_loc"),
    #         taxi.get("drop_loc"),
    #         taxi.get("pick_time"),
    #         taxi.get("drop_time"),
    #         taxi.get("cus_id"),
    #     )
    #     if taxi.get("taxino") not in Booking.taxi_travel_det:
    #         Booking.taxi_travel_det[taxi.get("taxino")] = []
    #     Booking.taxi_travel_det[taxi.get("taxino")].append(taxi_det)

    Taxi.taxi.clear()
    db_incomes = Db_Manager.get_income_data()
    for each in db_incomes:
        Taxi.taxi[each.get("taxino")] = each.get("amount")

    Booking.scheduled_taxies.clear()
    db_scheduled_taxies = Db_Manager.get_scheduled_data()
    for data in db_scheduled_taxies:
        if data.get("taxi_id") not in Booking.scheduled_taxies:
            Booking.scheduled_taxies[data.get("taxi_id")] = []
        temp = (
            data.get("taxi_id"),
            data.get("pick_loc"),
            data.get("drop_loc"),
            data.get("pick_time"),
            data.get("drop_time"),
        )
        Booking.scheduled_taxies[data.get("taxi_id")].append(temp)


def initialize_taxi(count):
    for i in range(1, count + 1):
        Db_Manager.initialixe_taxi(i)
