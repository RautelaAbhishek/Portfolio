from tkinter import *

FONT = ("Arial",12)

def calculate():
    miles = float(miles_input.get())
    km = round((miles * 1.609),2)
    kilometer_calculated["text"] = km
    

window = Tk()

window.title("Miles to Kilometer conversion")


miles_input = Entry(width=10,font=FONT)
miles_input.grid(column=1,row=0)

miles_notation = Label(text="Miles",font=FONT)
miles_notation.grid(column=2,row=0)


main_text = Label(text="is equal to ",font=FONT)
main_text.grid(column=0,row=1)

kilometer_calculated = Label(text="0",font=FONT)
kilometer_calculated.grid(column=1,row=1)

kilometer_notation = Label(text="Km",font=FONT)
kilometer_notation.grid(column=2,row=1)


calculate_button = Button(text="Calculate",font=FONT,command=calculate)
calculate_button.grid(column=1,row=2)



window.mainloop()