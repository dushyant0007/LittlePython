from tkinter import *

window = Tk()
window.title("Unit Convertor")
window.minsize(width=310, height=120)
window.config(padx=20, pady=20)

miles_input = Entry(width=5)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)


def miles_to_km(g):
    result = float(miles_input.get()) * 1.609
    kilometer_result_label["text"] = str(result)
    print(g)
    print("ok")

miles_to_km(12)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to ")
is_equal_to_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=3)

window.mainloop()
