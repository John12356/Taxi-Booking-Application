from . import Taxi
from app import Db_Manager

class Booking:
    
    taxi_travel_det = {}
    scheduled_taxies = {}

    def __init__(self, taxi_id, pick_loc, drop_loc, pick_time, drop_time, cus_id):
        self.taxi_id = taxi_id
        self.pick_loc = pick_loc
        self.drop_loc = drop_loc
        self.pick_time = pick_time
        self.drop_time = drop_time
        self.cus_id = cus_id

    @staticmethod
    def book_ticket(c):
        paths = ["A", "B", "C", "D", "E", "F"]
        new_path = Booking.find_nearby_loc(paths, c.pick_up)
        free_taxi = []

        for i in new_path:
            for taxi in Taxi.Taxi.all_taxies:
                if taxi.taxi_id in Booking.scheduled_taxies:
                    last_schedule = Booking.scheduled_taxies[taxi.taxi_id][-1]
                    first_schedule = Booking.scheduled_taxies[taxi.taxi_id][0]
                    if abs(last_schedule[4] - c.end_time) >= abs(
                            ord(last_schedule[2]) - ord(c.drop)
                    ) and abs(c.end_time - first_schedule[4]) >= abs(
                        ord(c.drop) - ord(first_schedule[2])
                    ):
                        if (
                                last_schedule[1] != c.pick_up
                                and last_schedule[2] != c.drop
                                and last_schedule[3] != c.pick_time
                        ):
                            Booking.add_to_schedule(taxi, c)
                            return

                elif c.end_time < taxi.drop_time and taxi.pick_time - c.end_time >= abs(
                        ord(taxi.pick_loc) - ord(c.drop)
                ):
                    Booking.add_to_schedule(taxi, c)
                    return

                elif (
                        taxi.cur_loc == i and taxi.cur_loc == c.pick_up
                ) or taxi.drop_time <= c.pick_time:
                    short_dis = Booking.find_shorter_dis(c.pick_up, taxi.cur_loc)
                    taxi.short_dis = short_dis
                    free_taxi.append(taxi)

            if free_taxi:
                break

        if free_taxi:
            free_taxi.sort(
                key=lambda each_taxi: (
                    each_taxi.short_dis,
                    each_taxi.cur_loc,
                    Taxi.Taxi.taxi.get(taxi.taxi_id),
                )
            )
            Booking.confirm_ticket(free_taxi[0], c)
            return
        print("Sorry!, No taxi is  available at the moment!!..")
        
    @staticmethod
    def find_shorter_dis(pick_up, cur_loc):
        return abs(ord(pick_up) - ord(cur_loc))
        
    @staticmethod
    def find_nearby_loc(paths, pick_up):
        req_index = paths.index(pick_up)
        result = [pick_up]
        left_index = req_index - 1
        right_index = req_index + 1

        while left_index >= 0 or right_index < len(paths):
            if left_index >= 0:
                result.append(paths[left_index])
                left_index -= 1
            if right_index < len(paths):
                result.append(paths[right_index])
                right_index += 1
            if len(paths) == len(result):
                break
        return result
    
    @staticmethod
    def find_amount(c):
        dis = abs(ord(c.drop) - ord(c.pick_up))
        dis = (dis * 15) - 5
        return 100 + (dis * 10)

    @staticmethod
    def add_amount(amount, cur_taxi):
        if cur_taxi in Taxi.Taxi.taxi:
            Taxi.Taxi.taxi[cur_taxi] += amount
            new_amount = Taxi.Taxi.taxi.get(int(cur_taxi))
            Db_Manager.update_income(new_amount, cur_taxi)

        else:
            Taxi.Taxi.taxi[cur_taxi] = amount
            Db_Manager.set_income(cur_taxi, amount)

    @staticmethod
    def confirm_ticket(taxi, c):
        Db_Manager.update_taxi(taxi.cur_loc, c.drop, c.pick_up, c.pick_time, c.end_time, taxi.taxi_id)
        amount = Booking.find_amount(c)
        Booking.add_amount(amount, taxi.taxi_id)
        Booking.update_details(c, taxi.taxi_id)
    
    @staticmethod
    def add_to_schedule(taxi, c):
        Db_Manager.add_schedule(taxi.taxi_id, c.pick_up, c.drop, c.pick_time, c.end_time)
        amount = Booking.find_amount(c)
        Booking.add_amount(amount, taxi.taxi_id)
        Booking.update_details(c, taxi.taxi_id)

    @staticmethod
    def update_details(c, taxi_id):
        Db_Manager.add_booking_details(taxi_id, c.pick_up, c.drop, c.pick_time, c.end_time, c.cus_id)
        print("Taxi " + str(taxi_id) + " booked successfully!!!...")
        
    @staticmethod
    def print_taxi():
        for key, value in Booking.taxi_travel_det.items():
            print("Taxi No : " + str(key) + ", Income = " + str(Taxi.Taxi.taxi.get(key)))
            print("---------------------------------")
            print("Customer Id  Pickup At  Drop At  Pickup Time  Reach Time")
            print("-----------  ---------  -------  -----------  ----------")
            for i in value:
                print(
                    f"{i.cus_id: <13}{i.pick_loc: <11}{i.drop_loc: <9}{i.pick_time: <13}{i.drop_time: <12}"
                )
            print()