import os
import pickle
import time
from tkinter import*
import tkinter.messagebox
import tkinter.ttk
import math

FONT= ("Courier New")

#main function to make pages switch
class main(Tk):

    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage(Frame):

    def __init__(self, parent, controller):
        
        Frame.__init__(self,parent)
        Frame.configure(self,bg='lightblue')
        
        label = Label(self, text = "JACKY DE HOTEL", font = ("Courier New" , 20 , "bold"),bg = "blue" ,fg = 'white' )
        label.pack(pady = 10, padx = 10)
        label2 = Label(self, text = "Hello and Welcome to our hotel!!" , font = (FONT , 12),bg = "lightblue")
        label2.pack(pady = 10 , padx = 10)
        label3 = Label(self, text = "This is a hotel for dogs where they can feel like home ^^" , font = (FONT , 12),bg = "lightblue")
        label3.pack(pady = 10 , padx = 10)
        label4 = Label(self, text = "This is a program to calculate the price for every services from your choice \nand a Pet Calculator to calculate your dog's age to human's age." ,bg = "lightblue", font = (FONT , 12))
        label4.pack(pady = 10 , padx = 10)
        label5 = Label(self, text = "Please click these 2 buttons below to get started" , font = (FONT , 10),bg = "lightblue")
        label5.pack(pady = 10 , padx = 10)

        button = Button(self, text="Book a room and calculate the price",bg = "pink",
                            command=lambda: controller.show_frame(PageOne))
        button.pack(pady = 10 , padx = 10)
        button2 = Button(self, text="Pet Calculator",bg = "pink",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(pady = 5 , padx = 10)

class PageOne(Frame):

    def __init__(self, parent, controller):
        
        Frame.__init__(self, parent)
        Frame.configure(self,bg='lightgreen')
        label = Label(self, text = "Book a room and calculate the price", font = (FONT , 20 , "bold"), bg = "lightgreen")
        label.pack(pady=10,padx=10)
        label2 = Label(self, text = "Please enter your dog's information below" , font = (FONT , 10),bg = "lightgreen")
        label2.pack(pady = 10 , padx = 10)
        
        name = Label(self, text = "Name :", font = (FONT,12),bg = "lightgreen")
        name.place(x = 100, y = 100)
        Entry(self, justify = RIGHT).place(x = 250, y = 100)
        
        age = Label(self, text = "Age(years) :", font = (FONT,12),bg = "lightgreen")
        age.place(x = 100, y = 120)
        Entry(self, justify = RIGHT).place(x = 250, y = 120)

        breed = Label(self, text = "Breed :", font = (FONT,12),bg = "lightgreen")
        breed.place(x = 100, y = 140)
        Entry(self, justify = RIGHT).place(x = 250, y = 140)
        
        size = Label(self, text = "Size :", font = (FONT,12),bg = "lightgreen")
        size.place(x = 100, y = 160)
        strvar = StringVar(value = 0)
        radio1 = Radiobutton(self, text = "Small" , variable = strvar , value = 'Small',bg = "lightgreen")
        radio1.place(x = 250,y = 160)
        radio2 = Radiobutton(self, text = "Medium" , variable = strvar , value = 'Medium',bg = "lightgreen")
        radio2.place(x = 300,y = 160)
        radio3 = Radiobutton(self, text = "Large" , variable = strvar , value = 'Large',bg = "lightgreen")
        radio3.place(x = 370,y = 160)

        gender = Label(self, text = "Gender :", font = (FONT,12),bg = "lightgreen")
        gender.place(x = 100, y = 180)
        strvar2 = StringVar(value = 0)
        radio4 = Radiobutton(self, text = "Male" , variable = strvar2 , value = 'Male',bg = "lightgreen")
        radio4.place(x = 250,y = 180)
        radio5 = Radiobutton(self, text = "Female" , variable = strvar2 , value = 'Female',bg = "lightgreen")
        radio5.place(x = 300,y = 180)

        period = Label(self, text = "How long will your dog stay here?(days):", font = (FONT,12),bg = "lightgreen")
        period.place(x = 100, y = 200)
        self.money = StringVar()
        days = Entry(self, justify = RIGHT,textvariable = self.money).place(x = 550, y = 200)

        food = Label(self, text = "Will you bring food with? :", font = (FONT,12),bg = "lightgreen")
        food.place(x = 100, y = 220)
        strvar3 = StringVar(value = 0)
        radio6 = Radiobutton(self, text = "Yes" , variable = strvar3 , value = 'Yes',bg = "lightgreen")
        radio6.place(x = 550,y = 220)
        radio7 = Radiobutton(self, text = "No" , variable = strvar3 , value = 'No',bg = "lightgreen")
        radio7.place(x = 590,y = 220)

        spa = Label(self, text = "Any salon and spa(included shower)? :", font = (FONT,12),bg = "lightgreen")
        spa.place(x = 100, y = 240)
        strvar4 = StringVar(value = 0)
        radio8 = Radiobutton(self, text = "Yes" , variable = strvar4 , value = 'Yes',bg = "lightgreen")
        radio8.place(x = 550,y = 240)
        radio9 = Radiobutton(self, text = "No" , variable = strvar4 , value = 'No',bg = "lightgreen")
        radio9.place(x = 590,y = 240)

        swim = Label(self, text = "Any swimming? :", font = (FONT,12),bg = "lightgreen")
        swim.place(x = 100, y = 260)
        strvar5 = StringVar(value = 0)
        radio10 = Radiobutton(self, text = "Yes" , variable = strvar5 , value = 'Yes',bg = "lightgreen")
        radio10.place(x = 550,y = 260)
        radio11 = Radiobutton(self, text = "No" , variable = strvar5 , value = 'No',bg = "lightgreen")
        radio11.place(x = 590,y = 260)

        need = Label(self, text = "Do your dog need any special help? :", font = (FONT,12),bg = "lightgreen")
        need.place(x = 100, y = 280)
        Entry(self, justify = RIGHT).place(x = 550, y = 285)

        note = Label(self, text = "Note : Any special services are included in the price per each day", font = (FONT,12),bg = "lightgreen")
        note.place(x = 100, y = 310)
        
        confirm = Button(self, text = "Confirm", command = self.calculate , bg = "pink")
##        confirm.pack(pady = 280 , padx = 10)
        confirm.place(x = 400, y = 350)
        
        button1 = Button(self, text="Back to Main Menu",bg = "pink",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x = 400, y = 400)
        button2 = Button(self, text="Pet Calculator",bg = "pink",
                            command=lambda: controller.show_frame(PageTwo))
        button2.place(x = 400, y = 450)

    def calculate(self) :
        
        if self.money.get().isdigit() == True:
            total = int(self.money.get())
            show = "Thank you ,Successfully booked!!!\nTotal is " + str(format("%d" % (total * 300))) + " baht."
            tkinter.messagebox.showinfo("Confirm", show)
        else:
            self.inputError()
            
    def inputError(self):
        
        tkinter.messagebox.showinfo("Error","Please try again")

class PageTwo(Frame):

    def __init__(self, parent, controller):
        
        Frame.__init__(self, parent)
        Frame.configure(self,bg='lightyellow')
        label = Label(self, text="Pet Calculator", font = (FONT , 20 , "bold"),bg='lightyellow')
        label.pack(pady=10,padx=10)
        label2 = Label(self, text = "Please enter your dog's age below" , font = (FONT , 10),bg='lightyellow')
        label2.pack(pady = 10 , padx = 10)
        
        age = Label(self, text = "Age(years) :", font = (FONT,12),bg='lightyellow')
        age.place(x = 100, y = 100)
        self.years = StringVar()
        days = Entry(self, justify = RIGHT,textvariable = self.years).place(x = 250, y = 100)

        confirm = Button(self, text = "Confirm", command = self.calculate,bg = "pink")
        confirm.place(x = 400 , y = 150)

        button1 = Button(self, text="Back to Main Menu",bg = "pink",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x = 400 , y = 200)
        button2 = Button(self, text="Book a room and calculate the price",bg = "pink",
                            command=lambda: controller.show_frame(PageOne))
        button2.place(x = 400 , y = 250)

    def calculate(self) :
        
        if self.years.get().isdigit() == True:
            age = float(self.years.get())
            show = "Your dog is " + str(format("%.2f" % (16 * math.log(age) + 31))) + " years old."
            tkinter.messagebox.showinfo("Confirm", show)
        else:
            self.inputError()
            
    def inputError(self):
        
        tkinter.messagebox.showinfo("Error","Please enter only integer")
        

window = main()
window.title("Jacky de hotel")
window.geometry('900x500')
window.mainloop()
