import customtkinter
from customtkinter import CTk
from tkinter import ttk
from DataBase import Users


class SeeUsers:
    def __init__(self):
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')
        self.__app = CTk()
        self.__app.geometry('500x350')
        self.__app.resizable(0, 0)
        self.__app.title('Клиенты')
        self.__lable_title = customtkinter.CTkLabel(
            master=self.__app,
            text='Услуги клиентов',
            text_color='green',
            font=('ISOCPEUR', 25)
        )
        self.__button = customtkinter.CTkButton(
            master=self.__app,
            text='Ок',
            corner_radius=5,
            command=self.__destroy_window,
            font=('ISOCPEUR', 20)
        )
        self.__table = ttk.Treeview(master=self.__app, show='headings', columns=('Login', 'Телефон'))
        self.__table.delete(*self.__table.get_children())
        self.__table.heading(0, text='Login')
        self.__table.heading(1, text='Телефон')
        __output = [item[1] for item in Users().data if item[3] is not None]
        for row in range(len(__output)):
            self.__table.insert(parent='', index=row, values=__output[row])

    def __destroy_window(self):
        self.__app.destroy()

    def loop(self):
        self.__lable_title.place(x=50, y=15)
        self.__table.place(x=50, y=50)
        self.__button.place(x=310, y=280)
        self.__app.mainloop()

