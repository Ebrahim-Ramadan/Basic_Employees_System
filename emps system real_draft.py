# This is the first Tkinter-used project I've ever worked on with py, So alot of issues of reduced performance is gonna be there
# and, I'd extremely like to hear your feedbacks of any weekness points
# Ebrahim Ramadan Diab 320220029 section02


import tkinter as tk
from tkinter import *
from abc import ABC, abstractmethod
# import numpy as np
# from numpy import *
# I thought it'd be better in handling-wise to store in no arrays


class AbstractClass(ABC):

    def __init__(self, name, age, salary, fees):
        self.name = name
        self.age = age
        self.salary = salary
        self.fees = fees
        self.List_Names = []
        self.List_Ages = []
        self.List_Fees = []


class Employees(AbstractClass):

    def Adding(self, name, age, fees):
        self.List_Names.append(name)
        self.List_Ages.append(age)
        self.List_Fees.append(fees)
        return self.List_Names, self.List_Ages, self.List_Fees

    def Displaying(self):
        return self.List_Names, self.List_Ages, self.List_Fees

    def delete_employee(self, name):
        if name in self.List_Names:
            index = self.List_Names.index(name)
            self.List_Names.pop(index)
            self.List_Ages.pop(index)
            self.List_Fees.pop(index)
            return True
        else:
            return False

    def Update_info(self, name, new_name, new_age, new_fees):
        if name in self.List_Names:
            index = self.List_Names.index(name)
            self.List_Names[index] = new_name
            self.List_Ages[index] = new_age
            self.List_Fees[index] = new_fees
            return True
        else:
            return False


E1 = Employees(5, 6, 8, 500)

root = tk.Tk()
root.title('Employees system')
root.geometry("400x200")
root.resizable(True, True)


def open_add_windows():
    new_add_window = tk.Toplevel(root)
    new_add_window.title("Adding window")
    new_add_window.geometry("400x200")
    #################
    label = Label(new_add_window, text='This is a new windows')
    label.pack()
    ##################
    name_label = Label(new_add_window, text="name ")
    name_label.pack()
    name_entry = Entry(new_add_window)
    name_entry.pack()
    age_label = Label(new_add_window, text="age ")
    age_label.pack()
    age_entry = Entry(new_add_window)
    age_entry.pack()
    fees_label = Label(new_add_window, text='fees?')
    fees_label.pack()
    fees_entry = Entry(new_add_window)
    fees_entry.pack()

    def add_employeebtn():
        name = name_entry.get()
        age = age_entry.get()
        fees = fees_entry.get()
        E1.Adding(name, age, fees)
        name_entry.delete(0, END)
        age_entry.delete(0, END)
        fees_entry.delete(0, END)

    The_final_Addbtn = tk.Button(
        new_add_window, text='Add', command=add_employeebtn)
    The_final_Addbtn.pack()


def Update_an_exsiting_emp():
    new_update_window = tk.Toplevel(root)
    new_update_window.title("Updating window")
    new_update_window.geometry("400x300")
    new_update_window.resizable(True, True)
    label = Label(new_update_window, text='This is a new windows')
    label.pack()

    name_label = Label(new_update_window, text="existing name to update ")
    name_label.pack()
    name_entry = Entry(new_update_window)
    name_entry.pack()
    new_name_label = Label(new_update_window, text="name ")
    new_name_label.pack()
    new_name_entry = Entry(new_update_window)
    new_name_entry.pack()

    new_age_label = Label(new_update_window, text="age ")
    new_age_label.pack()
    new_age_entry = Entry(new_update_window)
    new_age_entry.pack()
    new_fees_label = Label(new_update_window, text="fees ")
    new_fees_label.pack()
    new_fees_entry = Entry(new_update_window)
    new_fees_entry.pack()

    def update_employee_btn():
        existing_name = name_entry.get()
        new_name = new_name_entry.get()
        new_age = new_age_entry.get()
        new_fees = new_fees_entry.get()
        updated = E1.Update_info(
            existing_name, new_name, new_age, new_fees)
        if updated:
            name_entry.delete(0, END)
            new_name_entry.delete(0, END)
            new_age_entry.delete(0, END)
            new_fees_entry.delete(0, END)

    The_final_updbtn = tk.Button(
        new_update_window, text='update', command=update_employee_btn)
    The_final_updbtn.pack()


def Delete_emplo():
    new_del_window = Toplevel(root)
    new_del_window.title("Deleting employees")
    new_del_window.geometry("200x200")
    Name_Label = Label(new_del_window, text="name to delete ")
    Name_Label.pack()
    Name_entry = Entry(new_del_window)
    Name_entry.pack()

    def To_Delete():
        Del_Name = Name_entry.get()
        E1.delete_employee(Del_Name)
        Name_entry.delete(0, END)
    DEL_BTN = tk.Button(new_del_window, text="Delete", command=To_Delete)
    DEL_BTN.pack()


def display_employees():
    employees = E1.Displaying()
    employee_strings = [
        f"{name} ({age} yrs, {fees} egp)" for name, age, fees in zip(*employees)]
    # a list complehension that iterates over the employees var list using zip func() to group the name, age, and fees of each employee
    # and * operator is unpacking the employees list (because it's returned as tuple i think) into arguments for the zip funciton

    employee_strings_as_a_list = '\n'.join(employee_strings)
    with open("Employees list.txt", 'w') as file:
        file.write(employee_strings_as_a_list)
    # this way we store  & show the info in a txt file, file auto closes when the open function (in write mode parameter'w') ends (because I used with statement)

    display_window = tk.Toplevel(root)
    display_window.title("Display Employees")
    display_window.geometry("400x400")
    display_label = Label(
        display_window, text=employee_strings_as_a_list, justify=LEFT)
    display_label.pack()
    return employee_strings
    # this way we store & show the info in the window


init_add_btn = tk.Button(
    root, text='Add a new employee', command=open_add_windows, padx=10, pady=10)
# make it have the full width whatever the widget
init_add_btn.pack(fill=tk.BOTH, expand=True)
# with open('Employees list', 'w') as file:
#     file.write(open_add_windows.__getattribute__)

init_update_btn = tk.Button(
    root, text='Update an existing employee', command=Update_an_exsiting_emp, padx=10, pady=10)
init_update_btn.pack(fill=tk.BOTH, expand=True)

init_delete_btn = tk.Button(
    root, text="Delete an existing employee", command=Delete_emplo, padx=10, pady=10)
init_delete_btn.pack(fill=tk.BOTH, expand=True)

init_display_btn = tk.Button(
    root, text='Display all employees', command=display_employees, padx=10, pady=10)
init_display_btn.pack(fill=tk.BOTH, expand=True)

root.mainloop()
