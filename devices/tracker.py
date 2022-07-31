class Tracker:
    def __init__(self, bat_cap, src_time, src_cap, slp_time, wrk_time, type_rep, bsd):
        self.src_cap = src_cap
        self.type_rep = type_rep
        self.wrk_time = wrk_time
        # work time
        self.src_time = src_time
        # search time
        self.slp_time = slp_time
        # sleep time
        self.bat_cap = bat_cap
        self.bsd = bsd
        self.src_energy = self.src_cap * self.src_time