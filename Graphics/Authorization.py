import tkinter.messagebox
from tkinter import CENTER

import customtkinter
from customtkinter import CTk

from Graphics.ForUsers import NewUser, User
from Graphics.ForAdmin.AdminMain import MainAdmin
from Logic import Autorization


class Autor:
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    def __init__(self):
        self.__app = CTk()
        self.__app.geometry('500x400')
        self.__app.resizable(0, 0)
        self.__app.resizable(0, 0)
        self.__app.title('Авторизация')
        self.__frame = customtkinter.CTkFrame(
            master=self.__app,
            width=300,
            height=250,
            corner_radius=15,
            border_color='gray',
            border_width=1
        )
        self.__frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.__login = customtkinter.CTkEntry(
            master=self.__frame,
            placeholder_text='Login',
            corner_radius=5,
            placeholder_text_color='gray',
        )
        self.__password = customtkinter.CTkEntry(
            master=self.__frame,
            placeholder_text='Password',
            placeholder_text_color='gray',
            corner_radius=5,
            show="*"
        )
        self.__buttton = customtkinter.CTkButton(
            master=self.__frame,
            text='Войти',
            corner_radius=5,
            command=self.__autoriz,
            font=('ISOCPEUR', 20)
        )
        self.__newUsers = customtkinter.CTkButton(
            master=self.__frame,
            text='Регистрация',
            corner_radius=5,
            command=self.__newclient,
            font=('ISOCPEUR', 20)
        )

    def __autoriz(self):
        if Autorization().proverka(self.__login.get(), self.__password.get()) == 'Users':
            tkinter.messagebox.showinfo('Оповещение', 'Вы авторизованы как юзер')
            self.__app.destroy()
            User().loop()
        elif Autorization().proverka(self.__login.get(), self.__password.get()) == 'Manager':
            tkinter.messagebox.showinfo('Оповещение', 'Вы авторизованы как админ')
            self.__app.destroy()
            MainAdmin().loop()
        else:
            tkinter.messagebox.showinfo('Оповещение', 'Ooops... Что то пошло не так')

    @staticmethod
    def __newclient():
        NewUser().loop()

    def loop(self):
        self.__login.place(x=85, y=50)
        self.__password.place(x=85, y=90)
        self.__buttton.place(x=85, y=130)
        self.__newUsers.place(x=85, y=170)
        self.__app.mainloop()
