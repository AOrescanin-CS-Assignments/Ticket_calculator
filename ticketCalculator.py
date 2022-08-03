#****************************************************************************************************
#
#       Name:       Alex Orescanin
#       File:       ticketCalculator.py
#       Description:
#               This program calculates the number of tickets selected of a certain type
#               and displays the users total charges
#
#****************************************************************************************************

import tkinter.messagebox
import tkinter

#****************************************************************************************************

class TicketCalculatorGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.senior = tkinter.Radiobutton(self.top_frame,
                                          text='Senior (>65)',
                                          variable=self.radio_var,
                                          value=7)
        self.adult = tkinter.Radiobutton(self.top_frame,
                                         text='Adult (15-65)',
                                         variable=self.radio_var,
                                         value=12)
        self.child = tkinter.Radiobutton(self.top_frame,
                                         text='Child (5-15)',
                                         variable=self.radio_var,
                                         value=5)

        self.ticket_label = tkinter.Label(self.mid_frame,
                                          text='Enter the number of tickets: ')
        self.tickets = tkinter.StringVar('')
        self.tickets_entry = tkinter.Entry(self.mid_frame, text=self.tickets)

        self.display_button = tkinter.Button(self.bottom_frame,
                                             text='Display Charges',
                                             command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        self.senior.pack()
        self.adult.pack()
        self.child.pack()

        self.ticket_label.pack()
        self.tickets_entry.pack()

        self.display_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

# ****************************************************************************************************

    def show_choice(self):
        self.message = 'Your total charges = $'
        self.total = 0.0
        self.total += (float(self.radio_var.get()) * float(self.tickets_entry.get()))
        self.message += str(self.total)
        tkinter.messagebox.showinfo('Selection', self.message)

#****************************************************************************************************

if __name__ == '__main__':
    my_gui = TicketCalculatorGUI()

