from tkinter import Menu
import win.window as Window
from win.property import PropertyWin
from win.landlord import LandlordWin
from win.task import TaskWin
from win.action import ActionWin
# Test
from win.contact import ContactWin

class MainPage:
    # view items used on main window

    def donothing():
        print('do nothing')

    def standard_menubar(user):
        menubar = Menu(user.root)
        user.root.config(menu=menubar)
        # file menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Change User", command=MainPage.donothing)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=user.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        # properties menu
        property_menu = Menu(menubar, tearoff=0)
        property_menu.add_command(label="View Properties", command=lambda: Window.show_window(user, 'property'))
        property_menu.add_command(label="Add Property", command=lambda: Window.add_window(user, 'property'))
        property_menu.add_separator()
        property_menu.add_command(label="View Tenancies", command=MainPage.donothing)
        property_menu.add_command(label="Add Tenancy", command=MainPage.donothing)
        menubar.add_cascade(label="Properties", menu=property_menu)
        # People menu
        people_menu = Menu(menubar, tearoff=0)
        people_menu.add_command(label="View Landlords", command=lambda: Window.show_window(user, 'landlord'))
        people_menu.add_command(label="Add Landlord", command=lambda: Window.add_window(user, 'landlord'))
        people_menu.add_separator()
        people_menu.add_command(label="View Additional Contacts", command=MainPage.donothing)
        people_menu.add_command(label="Add Additional Contact", command=MainPage.donothing)
        people_menu.add_separator()
        people_menu.add_command(label="View Tenants", command=MainPage.donothing)
        people_menu.add_command(label="Add Tenant", command=MainPage.donothing)
        people_menu.add_separator()
        people_menu.add_command(label="View Contractors", command=MainPage.donothing)
        people_menu.add_command(label="Add Contractor", command=MainPage.donothing)
        menubar.add_cascade(label="People", menu=people_menu)
        # Objects menu
        object_menu = Menu(menubar, tearoff=0)
        object_menu.add_command(label="View Key Tags", command=MainPage.donothing)
        object_menu.add_command(label="Add Key Tag", command=MainPage.donothing)
        object_menu.add_separator()
        object_menu.add_command(label="View Keys/Fobs", command=MainPage.donothing)
        object_menu.add_command(label="Add Key/Fob", command=MainPage.donothing)
        menubar.add_cascade(label="Objects", menu=object_menu)
        # Tasks menu
        task_menu = Menu(menubar, tearoff=0)
        task_menu.add_command(label="View All Tasks", command=lambda: Window.show_window(user, 'task'))
        task_menu.add_command(label="Add General Task", command=lambda: Window.add_window(user, 'task'))
        task_menu.add_separator()
        task_menu.add_command(label="View Maintenance Jobs", command=MainPage.donothing)
        task_menu.add_command(label="Add Maintenance Job", command=MainPage.donothing)
        task_menu.add_separator()
        task_menu.add_command(label="View Tenancy Tasks", command=MainPage.donothing)
        task_menu.add_command(label="Add Tenancy Task", command=MainPage.donothing)
        task_menu.add_separator()
        task_menu.add_command(label="View Certificates", command=MainPage.donothing)
        task_menu.add_command(label="Add Certificate", command=MainPage.donothing)
        task_menu.add_separator()
        task_menu.add_command(label="View Inspections", command=MainPage.donothing)
        task_menu.add_command(label="Add Inspection", command=MainPage.donothing)
        task_menu.add_separator()
        task_menu.add_command(label="View Templates", command=MainPage.donothing)
        menubar.add_cascade(label="Tasks", menu=task_menu)
        # actions menu
        action_menu = Menu(menubar, tearoff=0)
        action_menu.add_command(label="View Actions", command=lambda: Window.show_window(user, 'action'))
        action_menu.add_command(label="Add Action", command=lambda: Window.add_window(user, 'action'))
        menubar.add_cascade(label="Actions", menu=action_menu)
        # test menu
        test_menu = Menu(menubar, tearoff=0)
        test_menu.add_command(label="View Contacts", command=lambda: Window.show_window(user, 'contact'))
        test_menu.add_command(label="Add Contact", command=lambda: Window.add_window(user, 'contact'))
        menubar.add_cascade(label="Test", menu=test_menu)
