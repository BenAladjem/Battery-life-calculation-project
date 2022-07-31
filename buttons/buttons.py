class Buttons():
    pass


mode = ' '


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
