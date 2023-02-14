# "Calculator of Photographer"

from tkinter import *
import math

root = Tk()
root["bg"] = '#707070'
root.title("Rasuldjan Jalalov")
root.geometry("520x460")
root.resizable(False, False)

# Frames:
frame = LabelFrame(root, text=" Angle of Movement ", font='Times 22 bold', fg="WHITE", bg="#707070")
frame.grid(row=1, column=0)
frame.pack(padx=3, pady=3)

frame1 = LabelFrame(frame, text=" Note: ", font='Times 18 bold', fg="#F8C729", bg="#707070")
frame1.pack(padx=5, pady=5)

frame2 = LabelFrame(frame, text=" First Entries: ", font='Times 18 bold', fg="#F8C729", bg="#707070")
frame2.pack(padx=5, pady=5)

frame3 = LabelFrame(frame, text=" Second Entries: ", font='Times 18 bold', fg="#F8C729", bg="#707070")
frame3.pack(padx=5, pady=5)

frame4 = LabelFrame(frame, text=" Calculations: ", font='Times 18 bold', fg="#F8C729", bg="#707070")
frame4.pack(padx=5, pady=5)


def angle():
    altitude_1 = float(e2.get())
    altitude_2 = float(e5.get())
    azimuth_1 = float(e3.get())
    azimuth_2 = float(e6.get())
    distance_1 = float(e4.get())
    distance_2 = float(e7.get())

    if altitude_1 == altitude_2:
        result = 0
        a["text"] = f"{round(result, 4)}° (flat)"

    if altitude_1 < altitude_2:

        if azimuth_1 > azimuth_2:
            alfa = azimuth_1 - azimuth_2
            beta = altitude_2 - altitude_1
            side1 = math.sqrt(
                distance_1 ** 2 + distance_2 ** 2 - 2 * distance_1 * distance_2 * (math.cos(math.radians(alfa))))
            side2 = math.sqrt(
                distance_2 ** 2 + distance_2 ** 2 - 2 * distance_2 * distance_2 * (math.cos(math.radians(beta))))
            movement_angle = math.degrees(math.atan(side2 / side1))

            result = movement_angle
            a["text"] = f"{round(result, 4)}° (ascends)"

        if azimuth_1 < azimuth_2:
            alfa = azimuth_2 - azimuth_1
            beta = altitude_2 - altitude_1
            side1 = math.sqrt(
                distance_1 ** 2 + distance_2 ** 2 - 2 * distance_1 * distance_2 * (math.cos(math.radians(alfa))))
            side2 = math.sqrt(
                distance_2 ** 2 + distance_2 ** 2 - 2 * distance_2 * distance_2 * (math.cos(math.radians(beta))))
            movement_angle = math.degrees(math.atan(side2 / side1))

            result = movement_angle
            a["text"] = f"{round(result, 4)}° (ascends)"

    if altitude_1 > altitude_2:

        if azimuth_1 > azimuth_2:
            alfa = azimuth_1 - azimuth_2
            beta = altitude_1 - altitude_2
            side1 = math.sqrt(
                distance_1 ** 2 + distance_2 ** 2 - 2 * distance_2 * distance_1 * (math.cos(math.radians(alfa))))
            side2 = math.sqrt(
                distance_1 ** 2 + distance_1 ** 2 - 2 * distance_1 * distance_1 * (math.cos(math.radians(beta))))
            movement_angle = math.degrees(math.atan(side2 / side1))

            result = movement_angle
            a["text"] = f"{round(result, 4)}° (descends)"

        if azimuth_1 < azimuth_2:
            alfa = azimuth_2 - azimuth_1
            beta = altitude_1 - altitude_2
            side1 = math.sqrt(
                distance_2 ** 2 + distance_1 ** 2 - 2 * distance_2 * distance_1 * (math.cos(math.radians(alfa))))
            side2 = math.sqrt(
                distance_1 ** 2 + distance_1 ** 2 - 2 * distance_1 * distance_1 * (math.cos(math.radians(beta))))
            movement_angle = math.degrees(math.atan(side2 / side1))

            result = movement_angle
            a["text"] = f"{round(result, 4)}° (descends)"

# Frame-1 == By Default:

note = Label(frame1, text="Angle of movement of celestial objects - Moon / Sun / Stars", font='Times 18 bold',
             width=52, pady=10, fg="white", bg="#454545")
note.grid(row=0, column=0)


# Frame-2 == First Observer:

l2 = Label(frame2, text='Altitude of Space_Object  -  degrees:', width=32, pady=5, fg="white", bg="#454545")
l2.grid(row=0, column=0)

e2 = Entry(frame2, width=19, borderwidth=2, justify=CENTER)
e2.get()
e2.insert(0, '')
e2.grid(row=0, column=1)

l3 = Label(frame2, text='Azimuth of Space_Object  -  degrees:', width=32, pady=5, fg="white", bg="#454545")
l3.grid(row=1, column=0)

e3 = Entry(frame2, width=19, borderwidth=2, justify=CENTER)
e3.get()
e3.insert(0, '')
e3.grid(row=1, column=1)

l4 = Label(frame2, text='Distance to Space_Object  -  kilometers:', width=32, pady=5, fg="white", bg="#454545")
l4.grid(row=2, column=0)

e4 = Entry(frame2, width=19, borderwidth=2, justify=CENTER)
e4.get()
e4.insert(0, '')
e4.grid(row=2, column=1)


# Frame-3 == Second Observer:

l5 = Label(frame3, text='Altitude of Space_Object  -  degrees:', width=32, pady=5, fg="white", bg="#454545")
l5.grid(row=0, column=0)

e5 = Entry(frame3, width=19, borderwidth=2, justify=CENTER)
e5.get()
e5.insert(0, '')
e5.grid(row=0, column=1)

l6 = Label(frame3, text='Azimuth of Space_Object  -  degrees:', width=32, pady=5, fg="white", bg="#454545")
l6.grid(row=1, column=0)

e6 = Entry(frame3, width=19, borderwidth=2, justify=CENTER)
e6.get()
e6.insert(0, '')
e6.grid(row=1, column=1)

l7 = Label(frame3, text='Distance to Space_Object  -  kilometers:', width=32, pady=5, fg="white", bg="#454545")
l7.grid(row=2, column=0)

e7 = Entry(frame3, width=19, borderwidth=2, justify=CENTER)
e7.get()
e7.insert(0, '')
e7.grid(row=2, column=1)


# Frame-4 == Calculations of Azimuths Between Observers:

c = Button(frame4, text="Angle of Movement = degrees:", font='Times 16 bold', width=32, pady=6, borderwidth=2,
             fg="#850000", command=angle)
c.grid(row=0, column=0)

a = Label(frame4, width=20, pady=10, bg="#F8C729")
a.grid(row=0, column=1)
a.bind("<Button>", angle)


root.mainloop()
