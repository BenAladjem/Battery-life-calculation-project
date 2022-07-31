class Calculations():
    @staticmethod
    def one_iteration_time(typ, rep, slp, wrk, src):
        iter_time = 0
        for ch in typ:
            if ch == 'R':
                iter_time += rep
            elif ch == 'W':
                iter_time += wrk
            elif ch == 'S':
                iter_time += slp
            elif ch == 'C':
                iter_time += src
        return iter_time

    @staticmethod
    def one_iteration_capacity(typ, rep, slp, wrk, src):
        iter_cap = 0
        for ch in typ:
            if ch == 'R':
                iter_cap += rep
            elif ch == 'W':
                iter_cap += wrk
            elif ch == 'S':
                iter_cap += slp
            elif ch == 'C':
                iter_cap += src
        return iter_cap

    @staticmethod
    def time_convert(t):
        if t > 24 * 30 * 12:
            years = t // (24 * 30 * 12)
            months = (t - years * 24 * 30 * 12) // (24 * 30)
            return f"{int(years)}y {int(months)}m"
        elif t > 24 * 30:
            months = t // (24 * 30)
            days = (t - (months * 24 * 30)) // 24
            return f"{int(months)}m {int(days)}d "
        elif t > 24:
            days = t // 24
            hours = t - (days * 24)
            return f"{int(days)}d {int(hours)}h"
        else:
            return f"{int(t)}h"

    @staticmethod
    def calculate_time(bat, iter_cap, iter_time, discharge):
        # 1 year = 365d* 24h = 8760h,   730h = 1 month
        time = 0
        time_batt = 0
        while bat >= 0:
            bat -= iter_cap
            time += iter_time
            time_batt += iter_time
            if time_batt >= 730:
                bat *= (100 - discharge / 12) / 100
                time_batt = 0
        return time
