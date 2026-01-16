
from tkinter import *
def miles_to_km():
    miles= float(mile_input.get())
    km = round(miles *1.609)
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("MILESTONE COVERTOR")
window.config(padx=20,pady=20)
mile_input= Entry()
mile_input.grid(column=1,row=0)
mile_input.grid(column=1,row=0)
mile_label = Label(text="miles")
mile_label.grid(column=2,row=0)
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0,row=1)
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1,row=1)
kilometer_label = Label(text="km")
kilometer_label.grid(column=2,row=1)
calculate_button = Button(text="calculate",command=miles_to_km)
calculate_button.grid(column=1,row=2)
window.mainloop()
