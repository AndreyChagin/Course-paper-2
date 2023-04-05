import tkinter.messagebox
from tkinter import CENTER

import customtkinter
from customtkinter import CTk

from DataBase import Users


class NewUser:
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    def __init__(self):
        self.__app = CTk()
        self.__app.geometry('500x400')
        self.__app.resizable(0, 0)
        self.__app.title('Регистрация')
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
        self.__repitpassword = customtkinter.CTkEntry(
            master=self.__frame,
            placeholder_text='Password',
            placeholder_text_color='gray',
            corner_radius=5,
            show="*"
        )
        self.__newUsers = customtkinter.CTkButton(
            master=self.__frame,
            text='Регистрация',
            corner_radius=5,
            command=self.__newclient,
            font=('ISOCPEUR', 20)
        )
        self.__phone = customtkinter.CTkEntry(
            master=self.__frame,
            placeholder_text='Phone',
            placeholder_text_color='gray',
            corner_radius=5
        )

    def __newclient(self):
        login = self.__login.get()
        password = self.__password.get()
        phone = self.__phone.get()
        if len(password) == 0 or len(self.__repitpassword.get()) == 0 or len(password) == 0 or len(login) == 0 or \
                len(phone) == 0:
            tkinter.messagebox.showerror('Оповещение', 'Поля не заполнены!')
        elif login in (item[1] for item in Users().data):
            tkinter.messagebox.showerror('Оповещение', 'Такой пользователь уже есть!')
        elif password != self.__repitpassword.get():
            tkinter.messagebox.showerror('Оповещение', 'Пароли не совпадают!')
        else:
            Users().new_user(login, password, phone)
            tkinter.messagebox.showinfo('Оповещение', 'Успешно')
            self.__app.destroy()

    def loop(self):
        self.__login.place(x=85, y=30)
        self.__password.place(x=85, y=70)
        self.__repitpassword.place(x=85, y=110)
        self.__phone.place(x=85, y=150)
        self.__newUsers.place(x=85, y=190)
        self.__app.mainloop()
