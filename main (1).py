from tkinter import *


class AddressEntry(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, width=500, height=210, bd=3, relief=SUNKEN)

        # Properties
        self.size = "500x500"
        self.parent = parent
        self.form_count = 0

        # Forms
        self.first_name_text = self.__create_form("First Name:")
        self.last_name_text = self.__create_form("Last Name:")
        self.address_line_one_text = self.__create_form("Address Line 1:")
        self.address_line_two_text = self.__create_form("Address Line 2:")
        self.city_text = self.__create_form("City:")
        self.district_text = self.__create_form("District:")
        self.postal_code_text = self.__create_form("Postal Code:")
        self.country_text = self.__create_form("Country:")

    def __create_form(self, question):
        label = Label(self, text=question, justify=RIGHT, anchor="e")
        text = Text(self, height=1, width=50)

        label.grid(column=0, row=self.form_count, pady=1, sticky=E)
        text.grid(column=1, row=self.form_count)

        self.form_count += 1
        return text


if __name__ == '__main__':
    # Parent frame
    parent = Tk()
    parent.title("Supplement 3 Address Entry Form")
    parent.geometry("640x430")

    # Address entry frame
    address_frame = AddressEntry(parent)
    address_frame.pack()

    # Buttons frame
    buttons_frame = Frame(parent)
    buttons_frame.pack(anchor="e")

    # Buttons
    clear_button = Button(buttons_frame, width=7, height=1, text="Clear")
    submit_button = Button(buttons_frame, width=7, height=1, text="Submit")

    clear_button.grid(column=0, row=0, padx=5, pady=10)
    submit_button.grid(column=1, row=0, padx=5)

    # Start
    mainloop()