import customtkinter
from customtkinter import CTk
from .CheckApp import CheckMyApp
from .CheckService import CheckService


class User:
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    def __init__(self):
        self.__app = CTk()
        self.__app.geometry('300x225')
        self.__app.resizable(0, 0)
        self.__app.title('Выбор')

        self.__frame = customtkinter.CTkFrame(master=self.__app, height=175, corner_radius=15, border_color='gray',
                                              border_width=1)
        self.__button_app = customtkinter.CTkButton(
            master=self.__frame,
            corner_radius=5,
            text='Мои заявки',
            command=self.__check_app,
            font=('ISOCPEUR', 20)
        )
        self.__button_service = customtkinter.CTkButton(
            master=self.__frame,
            corner_radius=5,
            text='Услуги',
            command=self.__check_service,
            font=('ISOCPEUR', 20)
        )

    @staticmethod
    def __check_app():
        CheckMyApp().check()

    @staticmethod
    def __check_service():
        CheckService().check()

    def loop(self):
        self.__frame.place(x=50, y=20)
        self.__button_app.place(x=30, y=50)
        self.__button_service.place(x=30, y=100)
        self.__app.mainloop()