class Taxi:
    all_taxies = []
    taxi = {}

    def __init__(
        self, taxi_id, cur_loc, drop_time, short_dis, prev_loc, pick_time, pick_loc
    ):
        self.taxi_id = taxi_id
        self.cur_loc = cur_loc
        self.drop_time = drop_time
        self.short_dis = short_dis
        self.prev_loc = prev_loc
        self.pick_time = pick_time
        self.pick_loc = pick_loc
