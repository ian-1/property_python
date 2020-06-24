# ~~~~~~~~~~~~~~~~~~~~~~ import modules ~~~~~~~~~~~~~~~~~~~~~~

from tkinter import Menu
from views.action import Action

# ~~~~~~~~~~~~~~~~~~~~~~ class ~~~~~~~~~~~~~~~~~~~~~~

class MainPage:
    # view items used on main window

    def donothing():
        print('do nothing')

    def standard_menubar(window, user):
        menubar = Menu(window)
        window.config(menu=menubar)
        # file menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Change User", command=MainPage.donothing)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=window.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        # property menu
        property_menu = Menu(menubar, tearoff=0)
        property_menu.add_command(label="View Property", command=MainPage.donothing)
        property_menu.add_command(label="Add Property", command=MainPage.donothing)
        property_menu.add_command(label="Remove property", command=MainPage.donothing)
        menubar.add_cascade(label="Property", menu=property_menu)
        # maintenace menu
        maintenance_menu = Menu(menubar, tearoff=0)
        maintenance_menu.add_command(label="View Repair Jobs", command=MainPage.donothing)
        maintenance_menu.add_separator()
        maintenance_menu.add_command(label="Open Repair Job", command=MainPage.donothing)
        maintenance_menu.add_command(label="Add Repair Job", command=MainPage.donothing)
        menubar.add_cascade(label="Maintenance", menu=maintenance_menu)
        # template menu
        template_menu = Menu(menubar, tearoff=0)
        template_menu.add_command(label="View Templates", command=MainPage.donothing)
        template_menu.add_separator()
        template_menu.add_command(label="Open Template", command=MainPage.donothing)
        menubar.add_cascade(label="Template", menu=template_menu)
        # action menu
        action_menu = Menu(menubar, tearoff=0)
        action_menu.add_command(label="View Actions", command=lambda: Action.show_window(window, user))
        action_menu.add_separator()
        action_menu.add_command(label="Add Action", command=lambda: Action.add_window(window, user))
        menubar.add_cascade(label="Action", menu=action_menu)
        # landlord menu
        landlord_menu = Menu(menubar, tearoff=0)
        landlord_menu.add_command(label="View Landlords", command=MainPage.donothing)
        landlord_menu.add_separator()
        landlord_menu.add_command(label="Open Landlord", command=MainPage.donothing)
        landlord_menu.add_command(label="Add Landlord", command=MainPage.donothing)
        menubar.add_cascade(label="Landlords", menu=landlord_menu)
        # tenant menu
        tenant_menu = Menu(menubar, tearoff=0)
        tenant_menu.add_command(label="View Tenants", command=MainPage.donothing)
        tenant_menu.add_separator()
        tenant_menu.add_command(label="Open Tenant", command=MainPage.donothing)
        tenant_menu.add_command(label="Add Tenant", command=MainPage.donothing)
        menubar.add_cascade(label="Tenants", menu=tenant_menu)
        # contractor menu
        contractor_menu = Menu(menubar, tearoff=0)
        contractor_menu.add_command(label="View Contractors", command=MainPage.donothing)
        contractor_menu.add_separator()
        contractor_menu.add_command(label="Open Contractor", command=MainPage.donothing)
        contractor_menu.add_command(label="Add Contractor", command=MainPage.donothing)
        menubar.add_cascade(label="Contractors", menu=contractor_menu)
