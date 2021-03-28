from tkinter import Tk, Button, Frame, Menu, Entry, Label
from datetime import date, sys

class Calculator:

    def __init__(self, master):
        self.master = master
        self.numframe = Frame(master=self.master, bg='dark red')
        self.rframe = Frame(master=self.master, bg='light green')
        self.lframe = Frame(master=self.master, bg='light blue')
        # self.scrframe = Frame(master=self.master, bg='navy blue')
        self.entry = Entry(master=self.master, font=('Times New Roman', 16, 'bold'), bg='silver',
                           fg='black', relief='sunken', bd=5)

        self.del_all = Button(self.lframe, text='ON', width=5, height=3, command=self.reset_scr)
        self.del_one = Button(self.lframe, text='DEL', width=5, height=3, command=self.bspace)

        self.num0 = Button(self.numframe, text='0', bg='black', fg='white', width=5, height=3, command=lambda: self.numpress('0'))
        self.num1 = Button(self.numframe, text='1', bg='black', fg='white', width=5, height=3, command=lambda: self.numpress('1'))
        self.num2 = Button(self.numframe, text='2', bg='black', fg='white', width=5, height=3, command=lambda: self.numpress('2'))
        self.num3 = Button(self.numframe, text='3', bg='black', fg='white', width=5, height=3, command=lambda: self.numpress('3'))
        self.num4 = Button(self.numframe, text='4', bg='black', fg='white', width=5, height=3, command=lambda: self.numpress('4'))
        self.num5 = Button(self.numframe, text='5', bg='black', fg='white', width=5, height=3, command=lambda: self.numpress('5'))
        self.num6 = Button(self.numframe, text='6', bg='black', fg='white', width=5, height=3, command=lambda: self.numpress('6'))
        self.num7 = Button(self.numframe, text='7', bg='black', fg='white', width=5, height=3, command=lambda: self.numpress('7'))
        self.num8 = Button(self.numframe, text='8', bg='black', fg='white', width=5, height=3, command=lambda: self.numpress('8'))
        self.num9 = Button(self.numframe, text='9', bg='black', fg='white', width=5, height=3, command=lambda: self.numpress('9'))

        self.point = Button(self.numframe, text='.', bg='black', fg='white', width=5, height=3, command=lambda: self.numpress('.'))
        self.eq = Button(self.numframe, text='=', bg='black', fg='white', width=5, height=3, command=self.evaluate )
        self.open_paren = Button(self.lframe, text='(', width=5, height=3, command=lambda: self.numpress('('))
        self.close_paren = Button(self.lframe, text=')', width=5, height=3, command=lambda: self.numpress(')'))

        self.minus = Button(self.rframe, text='-', width=5, height=3, command=lambda: self.numpress('-'))
        self.plus = Button(self.rframe, text='+', width=5, height=3, command=lambda: self.numpress('+'))
        self.mult = Button(self.rframe, text='*', width=5, height=3, command=lambda: self.numpress('*'))
        self.div = Button(self.rframe, text='/', width=5, height=3, command=lambda: self.numpress('/'))

    def place_frames(self):
        # frames (invisible containers) for screen and buttons
        self.numframe.grid(row=2, column=1, rowspan=4, columnspan=3, sticky='NSEW', padx=2, pady=2)
        # self.scrframe.grid(row=0, column=0, columnspan=5, sticky='NSEW', padx=2, pady=2)
        self.rframe.grid(row=2, rowspan=4, column=4, sticky='NSEW', padx=2, pady=2)
        self.lframe.grid(row=2, rowspan=4, column=0, sticky='NSEW', padx=2, pady=2)

    def place_entry(self):
        self.entry.grid(row=0, column=0, columnspan=5, sticky='NSEW', padx=2, pady=2)

    def place_buttons(self):
        self.num7.grid(row=2, column=1, pady=2, padx=2)
        self.num8.grid(row=2, column=2, pady=2, padx=2)
        self.num9.grid(row=2, column=3, pady=2, padx=2)
        self.num4.grid(row=3, column=1, pady=2, padx=2)
        self.num5.grid(row=3, column=2, pady=2, padx=2)
        self.num6.grid(row=3, column=3, pady=2, padx=2)
        self.num1.grid(row=4, column=1, pady=2, padx=2)
        self.num2.grid(row=4, column=2, pady=2, padx=2)
        self.num3.grid(row=4, column=3, pady=2, padx=2)
        self.num0.grid(row=5, column=2, pady=2, padx=2)

        self.point.grid(row=5, column=3, pady=2, padx=2)
        self.eq.grid(row=5, column=1, pady=2, padx=2)

        self.plus.grid(row=0, pady=2, padx=2)
        self.minus.grid(row=1, pady=2, padx=2)
        self.mult.grid(row=2, pady=2, padx=2)
        self.div.grid(row=3, pady=2, padx=2)

        self.del_all.grid(row=0, pady=2, padx=2)
        self.del_one.grid(row=1, pady=2, padx=2)
        self.open_paren.grid(row=2, pady=2, padx=2)
        self.close_paren.grid(row=3, pady=2, padx=2)

    def numpress(self, button_entry):
        # if open parenthesis was pressed
        # if len(self.entry.get()) > 0:
        #     # display last input
        #     print(self.entry.get()[len(self.entry.get()) - 1])
        if (button_entry == '(') and (self.entry.get()[len(self.entry.get()) - 1] == '('):
            # print('Check')
            return None
        elif button_entry == '(' and self.entry.get()[len(self.entry.get()) - 1] not in ['*', '/', '+', ')', '-']:
            return self.entry.insert(len(self.entry.get()), f"* {button_entry}")

        self.entry.insert(len(self.entry.get()), button_entry)

    def evaluate(self):
        result = eval(self.entry.get())
        self.entry.delete(first=0, last='end')
        self.entry.insert(0, result)

    def bspace(self):
        print(len(self.entry.get()))
        self.entry.delete(first=len(self.entry.get())-1, last='end')

    def reset_scr(self):
        self.entry.delete(first=0, last='end')


win1 = Tk()
win1.title("Calculator")

calc = Calculator(master=win1)
calc.place_frames()
calc.place_entry()
calc.place_buttons()


def new_win():
    win2 = Tk()
    win2.title("Calculator")
    calc2 = Calculator(win2)
    calc2.place_frames()
    calc2.place_entry()
    calc2.place_buttons()

    menu_bar = Menu(master=win2, tearoff=0)
    win2.config(menu=menu_bar)

    menu = Menu(menu_bar, tearoff=0)
    menu.add_command(command=new_win, label='New Window')

    menu_bar.add_cascade(menu=menu, label='MENU')
    menu_bar.add_command(label="Osagie Aib 28-03-2021")
    menu_bar.add_command(label=date.today())

    win2.mainloop()

menu_bar = Menu(master=win1, tearoff=0)
win1.config(menu=menu_bar)

menu = Menu(menu_bar, tearoff=0)
menu.add_command(command=new_win, label='New Window')

menu_bar.add_cascade(menu=menu, label='MENU')
menu_bar.add_command(label="Osagie Aib 28-03-2021")
menu_bar.add_command(label=date.today())

win1.mainloop()