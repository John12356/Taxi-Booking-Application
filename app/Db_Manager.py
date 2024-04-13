from . models import ALL_TAXIES, SCHEDULED_TAXIES, TAXI_DETAILS, TAXI_INCOME


def get_all_taxi_data():
    return ALL_TAXIES.objects.all().values()


def get_taxi_traveled_details():
    return TAXI_DETAILS.objects.all().values()


def get_income_data():
    return TAXI_INCOME.objects.all().values()


def get_scheduled_data():
    return SCHEDULED_TAXIES.objects.all().values()


def reset_db():
    ALL_TAXIES.objects.all().delete()
    TAXI_DETAILS.objects.all().delete()
    TAXI_INCOME.objects.all().delete()
    SCHEDULED_TAXIES.objects.all().delete()


def initialixe_taxi(taxi_id):
    ALL_TAXIES.objects.create(
        taxino=taxi_id,
        cur_loc="A",
        drop_time=0,
        short_dis=0,
        prev_loc=" ",
        pick_time=0,
        pick_loc="A",
    )


def update_income(amount, taxi):
    row = TAXI_INCOME.objects.get(pk=taxi)
    row.amount = amount
    row.save()


def set_income(taxi, amount):
    TAXI_INCOME.objects.create(taxino=taxi, amount=amount)


def update_taxi(cur_loc, drop_loc, pick_up, pick_time, drop_time, taxi_id):
    row = ALL_TAXIES.objects.get(taxino=taxi_id)
    row.prev_loc = cur_loc
    row.cur_loc = drop_loc
    row.pick_loc = pick_up
    row.pick_time = pick_time
    row.drop_time = drop_time
    row.save()


def add_schedule(taxi_id, pick_loc, drop_loc, pick_time, drop_time):
    SCHEDULED_TAXIES.objects.create(
        taxi_id=taxi_id,
        pick_loc=pick_loc,
        drop_loc=drop_loc,
        pick_time=pick_time,
        drop_time=drop_time,
    )

    row = ALL_TAXIES.objects.get(taxino=taxi_id)
    row.pick_loc = pick_loc
    row.save()


def add_booking_details(taxi_id, pick_loc, drop_loc, pick_time, drop_time, cus_id):
    TAXI_DETAILS.objects.create(
        taxino=taxi_id,
        pick_loc=pick_loc,
        drop_loc=drop_loc,
        pick_time=pick_time,
        drop_time=drop_time,
        cus_id=cus_id,
    )
    

