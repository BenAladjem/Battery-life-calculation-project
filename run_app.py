import datetime
import json
import math
from tkinter import *
from tkinter.ttk import *

from calculations.calc import Calculations
from devices.tracker import Tracker
from enums import WM, TB, TC, T5, TR, TD, TOne

mode = ' '

window = Tk()
window.title("Battery Life Estimator ")
window.geometry("700x710")
window.configure(bg="gray")

sv1 = StringVar()
sv2 = StringVar()
sv3 = StringVar()
sv4 = StringVar()
sv5 = StringVar()
sv6 = StringVar()
sv7 = StringVar()
sv8 = StringVar()
sv9 = StringVar()
sv10 = StringVar()

sv1.trace('w', lambda nm, idx, mode, var=sv1: validate_float(var))
sv2.trace('w', lambda nm, idx, mode, var=sv2: validate_float(var))
sv3.trace('w', lambda nm, idx, mode, var=sv3: validate_float(var))
sv4.trace('w', lambda nm, idx, mode, var=sv4: validate_float(var))
sv5.trace('w', lambda nm, idx, mode, var=sv5: validate_float(var))
sv6.trace('w', lambda nm, idx, mode, var=sv6: validate_float(var))
sv7.trace('w', lambda nm, idx, mode, var=sv7: validate_float(var))
sv8.trace('w', lambda nm, idx, mode, var=sv8: validate_float(var))
sv9.trace('w', lambda nm, idx, mode, var=sv9: validate_float(var))
sv10.trace('w', lambda nm, idx, mode, var=sv10: validate_float(var))

txt_empty0 = Entry(window, width=0).grid(row=0, column=6)
txt_empty1 = Entry(window, width=0).grid(row=1, column=6)
txt_empty2 = Entry(window, width=1).grid(row=2, column=6)
txt_empty3 = Entry(window, width=1).grid(row=3, column=6)
txt_empty4 = Entry(window, width=1).grid(row=4, column=6)
txt_empty5 = Entry(window, width=1).grid(row=5, column=6)
txt_empty6 = Entry(window, width=1).grid(row=6, column=6)
txt_empty7 = Entry(window, width=1).grid(row=7, column=6)
txt_empty8 = Entry(window, width=1).grid(row=8, column=6)
txt_empty9 = Entry(window, width=1).grid(row=9, column=6)
txt_empty10 = Entry(window, width=1).grid(row=10, column=6)
txt_empty11 = Entry(window, width=1).grid(row=11, column=6)
txt_empty12 = Entry(window, width=1).grid(row=12, column=6)
txt_empty13 = Entry(window, width=1).grid(row=13, column=6)
txt_empty14 = Entry(window, width=1).grid(row=14, column=6)
txt_empty15 = Entry(window, width=1).grid(row=15, column=6)
txt_empty16 = Entry(window, width=1).grid(row=16, column=6)
txt_empty17 = Entry(window, width=1).grid(row=17, column=6)
txt_empty18 = Entry(window, width=1).grid(row=18, column=6)
txt_empty19 = Entry(window, width=1).grid(row=19, column=6)
txt_empty20 = Entry(window, width=1).grid(row=20, column=6)
txt_empty21 = Entry(window, width=1).grid(row=21, column=6)
txt_empty22 = Entry(window, width=1).grid(row=22, column=6)
txt_empty23 = Entry(window, width=1).grid(row=23, column=6)
txt_empty24 = Entry(window, width=1).grid(row=24, column=6)
txt_empty25 = Entry(window, width=1).grid(row=25, column=6)
txt_empty26 = Entry(window, width=1).grid(row=26, column=6)
txt_empty27 = Entry(window, width=1).grid(row=27, column=6)

lbl1 = Label(window, text="Battery capacity", font=("Arial Bold", 15))
lbl1.grid(column=0, row=0)
lbl3 = Label(window, text="Capacity *", font=("Arial Bold", 13))
lbl3.grid(column=0, row=2)
lbl5 = Label(window, text="Device", font=("Arial Bold", 15))
lbl5.grid(column=0, row=4)
lbl8 = Label(window, text="Search time ", font=("Arial Bold", 13))
lbl8.grid(column=0, row=8)
lbl9 = Label(window, text="Work time *", font=("Arial Bold", 13))
lbl9.grid(column=0, row=10)
lbl10 = Label(window, text="Sleep time *", font=("Arial Bold", 13))
lbl10.grid(column=0, row=12)
lbl13 = Label(window, text="Battery self discharge", font=("Arial Bold", 15))
lbl13.grid(column=0, row=14)
lbl15 = Label(window, text="self discharge", font=("Arial Bold", 13))
lbl15.grid(column=0, row=16)
lbl19 = Label(window, text="Cyclic mode *", font=("Arial Bold", 15))
lbl19.grid(column=0, row=18)
lbl21 = Label(window, text="Estimated battery lifetime", font=("Arial Bold", 15))
lbl21.grid(column=0, row=20)
lbl23 = Label(window, width=10, text="Lifetime", font=("Arial Bold", 13))
lbl23.grid(column=0, row=22)
lbl24 = Label(window, width=10, text="Iterations", font=("Arial Bold", 13))
lbl24.grid(column=0, row=23)

lbl_lifetime = Label(window, width=10, text=" ", font=("Arial Bold", 13))
lbl_lifetime.grid(column=1, row=22)
lbl_iterations = Label(window, width=10, text=" ", font=("Arial Bold", 13))
lbl_iterations.grid(column=1, row=23)

lbl61 = Label(window, text="mAh", font=("Arial Bold", 13))
lbl61.grid(column=3, row=2)
lbl62 = Label(window, width=10, text="Search cap", font=("Arial Bold", 13))
lbl62.grid(column=3, row=8)
lbl63 = Label(window, text="s", font=("Arial Bold", 13))
lbl63.grid(column=2, row=8)
lbl63 = Label(window, text="s", font=("Arial Bold", 13))
lbl63.grid(column=3, row=10)
lbl64 = Label(window, text="s", font=("Arial Bold", 13))
lbl64.grid(column=3, row=12)
lbl65 = Label(window, text="%", font=("Arial Bold", 13))
lbl65.grid(column=3, row=16)

lbl100 = Label(window, text="      ", width=12, font=("Arial Bold", 13))
lbl100.grid(column=2, row=18)

lbl101 = Label(window, text="mA", width=3, font=("Arial Bold", 13))
lbl101.grid(column=5, row=8)
lbl_wrc_cap = Label(window, text="work cap ", width=12, font=("Arial Bold", 13))
lbl_wrc_cap.grid(column=4, row=10)
lbl102 = Label(window, text="mA", width=3, font=("Arial Bold", 13))
lbl102.grid(column=5, row=10)
lbl_slp_cap = Label(window, text="sleep cap ", width=12, font=("Arial Bold", 13))
lbl_slp_cap.grid(column=4, row=12)
lbl103 = Label(window, text="mA", width=3, font=("Arial Bold", 13))
lbl103.grid(column=5, row=12)
lbl_ws_cycles = Label(window, width=13, text="WS Cycles", font=("Arial Bold", 13))
lbl_ws_cycles.grid(column=4, row=18)

txt_batt_cap = Entry(window, validate='key', textvariable=sv1, width=10)
txt_batt_cap.grid(column=2, row=2)
txt_src_time = Entry(window, validate='key', textvariable=sv2, width=10)
txt_src_time.grid(column=1, row=8)
txt_wrk_time = Entry(window, validate='key', textvariable=sv3, width=10)
txt_wrk_time.grid(column=2, row=10)
txt_slp_time = Entry(window, validate='key', textvariable=sv4, width=10)
txt_slp_time.grid(column=2, row=12)
txt_bsd = Entry(window, validate='key', textvariable=sv5, width=10)
txt_bsd.grid(column=2, row=16)
txt_rep_freq = Entry(window, validate='key', textvariable=sv9, width=10)
txt_rep_freq.grid(row=19, column=4)

txt_src_cap = Entry(window, validate='key', textvariable=sv10, width=10)
txt_src_cap.grid(column=4, row=8)

combo = Combobox(window)
combo['values'] = ("Tracker Bike", "Tracker Car", "Tracker LoRa", "Tracker Pet", "Water Meter", "Tracker One", "Test Device")
combo.current(0)
combo.grid(column=0, row=6)

flag = False  # flag_test_device
flag1 = False  # Check Enter Valid data

kind_of_device = ''
global batt_capacity
global report_time
global sleep_time
global work_time
global type_report
global batt_self_discharge
global class_device


class All_devices(Tracker):

    def __init__(self, bat_cap, src_time, src_cap, slp_time, wrk_time, type_rep, bsd, cd):
        super().__init__(bat_cap, src_time, src_cap, slp_time, wrk_time, type_rep, bsd)

        self.cd = cd
        self.AVG_CURRENT_TIME_REPORT = self.cd.AVG_CURRENT_TIME_REPORT.value
        self.AVG_CURRENT_CONSUMPTION_REPORT = self.cd.AVG_CURRENT_CONSUMPTION_REPORT.value
        self.AVG_CURRENT_CONSUMPTION_SLEEP = self.cd.AVG_CURRENT_CONSUMPTION_SLEEP.value
        self.AVG_CURRENT_CONSUMPTION_WORK = self.cd.AVG_CURRENT_CONSUMPTION_WORK.value


        self.rep_energy = self.AVG_CURRENT_CONSUMPTION_REPORT * self.AVG_CURRENT_TIME_REPORT
        self.slp_energy = self.AVG_CURRENT_CONSUMPTION_SLEEP * self.slp_time
        self.wrk_energy = self.AVG_CURRENT_CONSUMPTION_WORK * self.wrk_time
        self.iter_time = Calculations.one_iteration_time(self.type_rep, self.AVG_CURRENT_TIME_REPORT, self.slp_time,
                                                         self.wrk_time, src_time)
        self.iter_cap = Calculations.one_iteration_capacity(self.type_rep, self.rep_energy, self.slp_energy,
                                                            self.wrk_energy, self.src_energy)
        self.batt_life = Calculations.calculate_time(self.bat_cap, self.iter_cap, self.iter_time, self.bsd)
        self.batt_life_time = Calculations.time_convert(
            Calculations.calculate_time(self.bat_cap, self.iter_cap, self.iter_time, self.bsd))
        self.num_iterations = math.floor(self.batt_life / self.iter_time)


class TestDevice(Tracker):
    def __init__(self, bat_cap, src_time, src_cap, slp_time, slp_cap, wrk_time, wrk_cap, type_rep, bsd):
        super().__init__(bat_cap, src_time, src_cap, slp_time, wrk_time, type_rep, bsd)
        self.wrk_cap = wrk_cap
        self.slp_cap = slp_cap

        self.TD = TD
        self.rep_time = self.TD.report_time.value
        self.rep_cap = self.TD.report_capacity.value

        self.src_energy = self.src_cap * self.src_time
        self.slp_energy = self.slp_cap * self.slp_time
        self.wrk_energy = self.wrk_cap * self.wrk_time
        self.rep_energy = self.rep_cap * self.rep_time

        self.iter_time = Calculations.one_iteration_time(self.type_rep, self.rep_time, self.slp_time, self.wrk_time,
                                                         self.src_time)
        self.iter_cap = Calculations.one_iteration_capacity(self.type_rep, self.rep_energy, self.slp_energy,
                                                            self.wrk_energy, self.src_energy)
        self.batt_life = Calculations.calculate_time(self.bat_cap, self.iter_cap, self.iter_time, self.bsd)
        self.batt_life_time = Calculations.time_convert(
            Calculations.calculate_time(self.bat_cap, self.iter_cap, self.iter_time, self.bsd))
        self.num_iterations = math.floor(self.batt_life / self.iter_time)


def type_of_device(device):
    if device == "Tracker Bike":
        class_device = TB
    elif device == "Tracker Car":
        class_device = TC
    elif device == "Tracker Pet":
        class_device = T5
    elif device == "Tracker LoRa":
        class_device = TR
    elif device == "Water Meter":
        class_device = WM
    elif device == "Tracker One":
        class_device = TOne
    else:
        class_device = TestDevice
    return class_device


def clicked_get_device():
    kind_of_device = combo.get()
    global class_device, txt_rep_cap, txt_wrk_cap, txt_slp_cap, flag
    if kind_of_device == "Test Device":
        flag = True
    if kind_of_device == "Test Device":
        txt_wrk_cap = Entry(window, validate='key', textvariable=sv7, width=10)
        txt_wrk_cap.grid(column=4, row=11)
        txt_slp_cap = Entry(window, validate='key', textvariable=sv8, width=10)
        txt_slp_cap.grid(column=4, row=13)

        lbl_wrc_cap.configure(text="work cap")
        lbl_slp_cap.configure(text="sleep cap")
    else:
        if flag:
            txt_wrk_cap.delete(0, END)
            txt_slp_cap.delete(0, END)

        device = combo.get()
        class_device = type_of_device(device)

        lbl_wrc_cap.configure(text=class_device.AVG_CURRENT_CONSUMPTION_WORK.value)
        lbl_slp_cap.configure(text=class_device.AVG_CURRENT_CONSUMPTION_SLEEP.value)


def check_valid_data():
    global flag1

    if len(txt_batt_cap.get()) == 0:
        lbl_iterations.configure(text="batt cap")
    elif len(txt_wrk_time.get()) == 0:
        lbl_iterations.configure(text="work time")
    elif len(txt_slp_time.get()) == 0:
        lbl_iterations.configure(text="sleep time")
    elif mode == '' or mode == ' ':
        lbl_iterations.configure(text="")
        lbl_iterations.configure(text="mode")
    else:
        flag1 = True
    if not combo.get() == "Test Device":
        if flag1:
            print_result()
    else:
        clicked_get_device()
        if flag1:
            if len(txt_wrk_cap.get()) == 0:
                lbl_lifetime.configure(text="Enter")
                lbl_iterations.configure(text="work cap")
            elif len(txt_slp_cap.get()) == 0:
                lbl_lifetime.configure(text="Enter")
                lbl_iterations.configure(text="sleep cap")
            else:
                print_result()
    if flag1 == False:
        lbl_lifetime.configure(text="Enter")


def print_result():
    result_dict = {}
    clicked_get_device()

    global class_device, class_device
    batt_capacity = float(txt_batt_cap.get())
    work_time = float(txt_wrk_time.get()) / 3600
    sleep_time = float(txt_slp_time.get()) / 3600

    if len(txt_bsd.get()) == 0:
        batt_self_discharge = 0
    else:
        batt_self_discharge = float(txt_bsd.get())

    if len(txt_src_time.get()) == 0:
        search_time = 0
    else:
        search_time = float(txt_src_time.get())

    if len(txt_src_cap.get()) == 0:
        search_cap = 0
    else:
        search_cap = float(txt_src_cap.get())

    device = combo.get()
    type_report = ws_cycles()
    class_device = type_of_device(device)

    if class_device == TestDevice:
        work_cap = float(txt_wrk_cap.get())
        sleep_cap = float(txt_slp_cap.get())

        dev = class_device(batt_capacity, search_time / 3600, search_cap, sleep_time,
                           sleep_cap, work_time, work_cap, type_report, batt_self_discharge)

        result_dict["work cap"] = work_cap
        result_dict["sleep cap"] = sleep_cap
        result_dict["report cap"] = dev.rep_cap
        result_dict["report time"] = 0
        result_dict["report cap"] = 0
    else:
        dev = All_devices(batt_capacity, search_time / 3600, search_cap, sleep_time, work_time, type_report,
                          batt_self_discharge, class_device)

        result_dict["work cap"] = dev.AVG_CURRENT_CONSUMPTION_WORK
        result_dict["sleep cap"] = dev.AVG_CURRENT_CONSUMPTION_SLEEP
        result_dict["report time"] = dev.AVG_CURRENT_TIME_REPORT * 3600
        result_dict["report cap"] = dev.AVG_CURRENT_CONSUMPTION_REPORT
    lbl_lifetime.configure(text=dev.batt_life_time)
    lbl_iterations.configure(text=dev.num_iterations)

    if len(txt_rep_freq.get()) == 0:
        result_dict["WS cycles"] = "default"
    else:
        result_dict["WS cycles"] = txt_rep_freq.get()
    result_dict["batt self discharge"] = batt_self_discharge
    result_dict["cycling mode"] = type_report
    result_dict["device"] = device
    result_dict["batt capacity"] = batt_capacity
    result_dict["work time"] = txt_wrk_time.get()
    result_dict["sleep time"] = txt_slp_time.get()
    result_dict["search time"] = search_time
    result_dict["search cap"] = search_cap
    result_dict["lifetime"] = dev.batt_life_time
    result_dict["iterations"] = dev.num_iterations

    return result_dict


def print_r():
    global mode
    if len(mode) < 10 and not mode[-1] == "R":
        mode += "R"
    lbl100.configure(text=mode)


def print_s():
    global mode
    if len(mode) < 10 and not mode[-1] == "S":
        mode += "S"
    lbl100.configure(text=mode)


def print_w():
    global mode
    if len(mode) < 10 and not mode[-1] == "W":
        mode += "W"
    lbl100.configure(text=mode)


def search():
    global mode
    if len(txt_src_time.get()) > 0 and len(txt_src_cap.get()) > 0:
        if len(mode) < 10 and not mode[-1] == "C":
            mode += "C"
    lbl100.configure(text=mode)


def clean():
    global mode
    if len(mode) > 1:
        mode = mode[:-1]
    lbl100.configure(text=mode)


def save():
    if flag1:
        generate_report()


def validate_float(var):
    new_value = var.get()
    try:
        new_value == '' or float(new_value)
        validate_float.old_value = new_value
    except:
        var.set(validate_float.old_value)


def nums_protocol():
    try:
        open('my.nums')
    except:
        data = '1'
        with open('my.nums', 'w') as file:
            file.writelines(data)

    with open('my.nums', 'r') as f:
        x = f.read()
    x += '1'
    with open('my.nums', 'w') as file:
        file.writelines(x)
    return len(x)


def generate_report():
    info = {}
    info = print_result()
    window2 = Tk()
    window2.title("Saved data")
    window2.geometry("400x600")

    info["number protocol"] = nums_protocol()
    date = datetime.datetime.now()
    date_format = date.strftime("%Y-%m-%d %H:%M:%S")
    info["date"] = date_format

    num_protocol = info["number protocol"]
    data = info["date"]
    device = info["device"]
    batt_capacity = info["batt capacity"]
    report_time = info["report time"]
    report_cap = info["report cap"]
    work_time = info["work time"]
    work_cap = info["work cap"]
    sleep_time = info["sleep time"]
    sleep_cap = info["sleep cap"]
    search_time = info["search time"]
    search_cap = info["search cap"]
    batt_self_discharge = info["batt self discharge"]
    cycling_mode = info["cycling mode"]
    ws_cyc = info["WS cycles"]
    batt_life_time = info["lifetime"]
    iterations = info["iterations"]

    lbl_protocol = Label(window2, text=f"Num Protocol:{num_protocol}"
                                       f"\n\n Data: {data}"
                                       f"\n\n Device: {device}"
                                       f"\n\n Batt Capacity: {batt_capacity} mA"
                                       f"\n\n Report Time: {report_time}s"
                                       f"\n\n AVG report cap: {report_cap}mA"
                                       f"\n\n Work Time: {work_time}s"
                                       f"\n\n AVG work cap: {work_cap}mA"
                                       f"\n\n Sleep Time: {sleep_time}s "
                                       f"\n\n AVG sleep cap: {sleep_cap}mA"
                                       f"\n\n Search time: {search_time}s"
                                       f"\n\n AVG search cap: {search_cap}mA"
                                       f"\n\n Batt Self Discharge: {batt_self_discharge} %"
                                       f"\n\n Cycling Mode: {cycling_mode}"
                                       f"\n\n WS cycles: {ws_cyc}"
                                       f"\n\n Batt Life Time: {batt_life_time}"
                                       f"\n\n Iterations: {iterations}").pack()

    try:
        data = json.load(open('my.protocol'))
    except:
        data = []
    data.append(info)
    with open('my.protocol', 'w') as file:
        json.dump(data, file, indent=3)


def ws_cycles():
    global new_mode
    if len(txt_rep_freq.get()) > 0:
        report_frequency = int(txt_rep_freq.get())
        if "WS" in mode and not report_frequency == 0:
            pos = mode.index("WS")
            new_mode = mode[:pos] + ("WS" * report_frequency) + mode[pos + 2:]
        else:
            new_mode = mode
    else:
        new_mode = mode
    return new_mode


btn_device = Button(window, width=14, text="Device consumption", command=clicked_get_device)
btn_device.grid(column=4, row=6)
btn_calculate = Button(window, width=14, text=" Calculate       ", command=check_valid_data)
btn_calculate.grid(column=4, row=22)
btn_save = Button(window, width=6, text="Save", command=save).grid(column=4, row=25)
btn_report = Button(window, text="Report", command=print_r).grid(column=1, row=19)
btn_work = Button(window, text="Work", command=print_w).grid(column=2, row=19)
btn_sleep = Button(window, text="Sleep", command=print_s).grid(column=3, row=19)
btn_clean = Button(window, text="X", command=clean).grid(column=3, row=18)
btn_src = Button(window, text="Search", command=search).grid(column=1, row=18)

validate_float.old_value = ''
window.mainloop()
