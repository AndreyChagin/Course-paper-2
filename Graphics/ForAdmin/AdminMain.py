import customtkinter
from customtkinter import CTk
from Graphics.ForAdmin.SeeUsersApplication import SeeApplicationUsers
from Graphics.ForAdmin.SeeUsers import SeeUsers
from Graphics.ForAdmin.JobInService import ServiceFull
from Graphics.ForAdmin.JobInDiscount import DiscountFull


class MainAdmin:
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    def __init__(self):
        self.__app = CTk()
        self.__app.geometry('240x185')
        self.__app.resizable(0, 0)
        self.__app.title('Выбор')

        self.__frame = customtkinter.CTkFrame(
            master=self.__app,
            border_width=1,
            border_color='gray',
            width=220,
            height=165
        )
        self.__button_users = customtkinter.CTkButton(
            master=self.__frame,
            text='Посмотреть клиентов',
            font=('ISOCPUER', 20),
            command=self.__check_users
        )
        self.__button_application = customtkinter.CTkButton(
            master=self.__frame,
            text='Посмотреть заявки',
            font=('ISOCPUER', 20),
            command=self.__check_application
        )

        self.__button_service = customtkinter.CTkButton(
            master=self.__frame,
            text='Услуги',
            font=('ISOCPUER', 20),
            command=self.__check_service
        )

        self.__button_coupon = customtkinter.CTkButton(
            master=self.__frame,
            text='Скидки',
            font=('ISOCPUER', 20),
            command=self.__check_discounts
        )

    @staticmethod
    def __check_users():
        SeeUsers().loop()

    @staticmethod
    def __check_application():
        SeeApplicationUsers().loop()

    @staticmethod
    def __check_service():
        ServiceFull().loop()

    @staticmethod
    def __check_discounts():
        DiscountFull().loop()

    def loop(self):
        self.__frame.place(x=10, y=10)
        self.__button_users.place(x=5, y=10)
        self.__button_application.place(x=15, y=50)
        self.__button_service.place(x=40, y=90)
        self.__button_coupon.place(x=40, y=130)
        self.__app.mainloop()
