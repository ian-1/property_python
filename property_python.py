# ~~~~~~~~~~~~~~~~~~~~~~ import modules ~~~~~~~~~~~~~~~~~~~~~~

from tkinter import Tk, Toplevel, Menu, PhotoImage, Frame, Button, Label, LabelFrame, Checkbutton,\
    LEFT, RIGHT, TOP, BOTTOM, X, W, SUNKEN

# ~~~~~~~~~~~~~~~~~~~~~~ working functions ~~~~~~~~~~~~~~~~~~~~~~

def propertyDetails():
    tar = Tk()
    tar_target_dis = Label(tar, text="prop", font=(font, 18, 'bold'), bg="blue", fg="white")
    tar_target_dis.pack()
    property_list.append(Property("KEL05A", "Flat B", "5", "Kellett Road", "SW2 1DX"))
    tar.mainloop()

def fill_property_list():
    property_list.append(Property("DEN89A", "Flat H", "89", "Denmark Hill", "SE5 8AA"))
    property_list.append(Property("MEL13A", "Flat 3", "13", "Melrose Road", "SW18 1ND"))
    property_list.append(Property("ARN03A", "", "3", "Arnould Avenue", "SE5 8AU"))
    property_list.append(Property("SWE58A", "", "58", "Southwell Road", "SE5 9PG"))
    property_list.append(Property("COL76A", "", "76", "Coleman Road", "SE5 7TG"))
    property_list.append(Property("LIL22A", "Flat B", "22", "Lilford Road", "SE5 9HX"))
    property_list.append(Property("KIR29A", "Flat A", "29", "Kirkwood Road", "SE15 3XT"))
    property_list.append(Property("KIR31A", "", "31", "Kirkwood Road", "SE15 3XT"))

def fill_property_frame(property_frame):
    indexval = 0
    for i in range(len(property_list)):
        checkbutt = Checkbutton(property_frame)
        label_A = Button(property_frame, text=property_list[i].code, bg="White", font=(monospaced_font, 12), width = 10,
                         command=lambda index=i: fill_right_frame(index))
        label_A.grid(row=(i+1), column=0)
        label_B = Button(property_frame, text=property_list[i].name, bg="White", font=(font, 12), width = 10)
        label_B.grid(row=(i+1), column=1)
        label_C = Button(property_frame, text=property_list[i].number, bg="White", font=(font, 12), width = 8)
        label_C.grid(row=(i+1), column=2)
        label_D = Button(property_frame, text=property_list[i].road, bg="White", font=(font, 12), width = 15)
        label_D.grid(row=(i+1), column=3)
        label_E = Button(property_frame, text=property_list[i].postcode, bg="White", font=(font, 12), width = 12)
        label_E.grid(row=(i+1), column=4)
        indexval += 1

def fill_right_frame(i):
    frame = Frame(window, width=500, height=500, bg='powder blue', relief=SUNKEN).pack(side=RIGHT)
    label_A = Label(frame, text=property_list[i].code, bg="White", font=(monospaced_font, 12), width = 10)
    label_A.grid(row=0, column=0)
    label_B = Label(frame, text=property_list[i].name, bg="White", font=(font, 12), width = 10)
    label_B.grid(row=(1), column=0)
    label_C = Label(frame, text=property_list[i].number, bg="White", font=(font, 12), width = 8)
    label_C.grid(row=(2), column=0)
    label_D = Label(frame, text=property_list[i].road, bg="White", font=(font, 12), width = 15)
    label_D.grid(row=(2), column=1)
    label_E = Label(frame, text=property_list[i].postcode, bg="White", font=(font, 12), width = 12)
    label_E.grid(row=(3), column=0)

# ~~~~~~~~~~~~~~~~~~~~~~ display functions ~~~~~~~~~~~~~~~~~~~~~~

def standard_menubar(window):
    menubar = Menu(window)
    root.config(menu=menubar)
    # file menu
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    # edit menu
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)
    menubar.add_cascade(label="Edit", menu=editmenu)
    # help menu
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

def create_toolbar_frame(window):
    toolbar = Frame(window)
    toolbar.pack(side=TOP, fill=X)
    return toolbar

def fill_standard_toolbar(toolbar, logo_photo, property_frame):
    # buttons
    insertButt = Button(toolbar, text="New Property", font=("Helvetica", 16), fg="dark red", command=propertyDetails)
    insertButt.pack(side=LEFT, padx=2, pady=2)
    printButt = Button(toolbar, text="Refresh List", font=("Helvetica", 16), fg="dark red", command=lambda: fill_property_frame(property_frame))
    printButt.pack(side=LEFT, padx=2, pady=2)
    # logo
    logoPic = Label(toolbar, image=logo_photo, bg="white")
    logoPic.pack(side=RIGHT, padx=2, pady=2)
    propSet = Label(toolbar, text="Property Setter", font=("Helvetica", 24), fg="dark red")
    propSet.pack(side=RIGHT, padx=2, pady=2)

def create_property_frame(window):
    property_frame = LabelFrame(window, text="Properties")
    property_frame.pack(side=LEFT, fill="both", expand="yes")
    # column titles
    label_A = Label(property_frame, text="CODE", font=("Helvetica", 12, 'bold'))
    label_A.grid(row=0, column=0)
    label_B = Label(property_frame, text="FT/APPT", font=("Helvetica", 12, 'bold'))
    label_B.grid(row=0, column=1)
    label_C = Label(property_frame, text="NO.", font=("Helvetica", 12, 'bold'))
    label_C.grid(row=0, column=2)
    label_D = Label(property_frame, text="ROAD/STREET", font=("Helvetica", 12, 'bold'))
    label_D.grid(row=0, column=3)
    label_E = Label(property_frame, text="POSTCODE", font=("Helvetica", 12, 'bold'))
    label_E.grid(row=0, column=4)
    return property_frame

def create_right_frame(window):
    right_frame = Frame(window, width=500, height = 500, bg='powder blue', relief=SUNKEN).pack(side=RIGHT)
    return right_frame

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

def status_bar(status_message):
    status = Label(root, text=status_message, bd=1, relief=SUNKEN, anchor=W)
    status.pack(fill=X)

# ~~~~~~~~~~~~~~~~~~~~~~ define classes & variables ~~~~~~~~~~~~~~~~~~~~~~

class Property():
    def __init__(self, code, name, number, road, postcode):
        self.code = code
        self.name = name
        self.number = number
        self.road = road
        self.postcode = postcode

property_list = []

monospaced_font = 'Consolas' # ,Consolas,Menlo,Monaco,Lucida Console,Liberation Mono,
                                # DejaVu Sans Mono,Bitstream Vera Sans Mono,Courier, Courier New,monospace,serif
font = 'Helvetica'

# ~~~~~~~~~~~~~~~~~~~~~~ main programme ~~~~~~~~~~~~~~~~~~~~~~

root = Tk()

# ~~~ create images ~~~
logo_photo = PhotoImage(file="logo.gif")

# ~~~ main ~~~

standard_menubar(root)
toolbar = create_toolbar_frame(root)
property_frame = create_property_frame(root)
#right_frame = create_right_frame(root)
fill_standard_toolbar(toolbar, logo_photo, property_frame)
# properties list
fill_property_list()
fill_property_frame(property_frame)

# status
# status_message = "Doing stuff (or not)..."
# status_bar(status_message)

root.mainloop()