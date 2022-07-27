import tkinter as tk


class Validator:
    def __init__(self, master1):
        # self.t4 = t4
        self.panel2 = tk.Frame(master1)
        self.panel2.grid()

        # self.button2 = tk.Button(self.panel2, text="Quit", command=self.panel2.quit)
        # self.button2.grid()
        vcmd = (master1.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.text1 = tk.Entry(self.panel2, validate='key', validatecommand=vcmd)
        self.text1.grid()
        self.text1.focus()

        self.text2 = tk.Entry(self.panel2, validate='key', validatecommand=vcmd, width=10)
        self.text2.grid(column=2, row=2)
        self.text2.focus()

        self.text3 = tk.Entry(self.panel2, validate='key', validatecommand=vcmd)
        self.text3.grid()
        self.text3.focus()

        # self.t4 = tk.Entry(self.panel2, validate='key', validatecommand=vcmd)
        # self.t4.grid()
        # self.t4.focus()

    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False


window = tk.Tk()
window.title('My test window')
window.geometry('600x200')

vcmd = ('%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

# text4 = tk.Entry(root1, text = "Text", width=5, validate='key', validatecommand=vcmd)
# text4.grid(column=1, row=6)
Validator(window)
window.mainloop()