from tkinter import ttk, messagebox

import customtkinter
from customtkinter import CTk

from Logic import ServiceSearch
from DataBase import Application


class CheckService:
    def __init__(self):
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')
        self.__app = CTk()
        self.__app.geometry('1005x350')
        self.__app.resizable(0, 0)
        self.__app.title('Услуги')
        self.__lable_title = customtkinter.CTkLabel(
            master=self.__app,
            text='Услуги',
            text_color='green',
            font=('ISOCPEUR', 25)
        )
        self.__button = customtkinter.CTkButton(
            master=self.__app,
            text='Ок',
            corner_radius=5,
            command=self.__accept,
            font=('ISOCPEUR', 20)
        )
        self.__button_new = customtkinter.CTkButton(
            master=self.__app,
            text='Добавить',
            corner_radius=5,
            command=self.__new_application,
            font=('ISOCPEUR', 20)
        )
        self.__combobox = customtkinter.CTkComboBox(master=self.__app, values=['Кузов', 'Салон', 'Другие'],
                                                    font=('ISOCPEUR', 15), state='readonly', command=self.__checkcat)
        self.__table = ttk.Treeview(master=self.__app, show='headings')
        self.__table.delete(*self.__table.get_children())
        self.__table.configure(columns=('id', 'Наименование', 'Цена', 'Категория', 'Скидка'))
        self.__table.heading(0, text='id')
        self.__table.heading(1, text='Наименование')
        self.__table.heading(2, text='Цена')
        self.__table.heading(3, text='Категория')
        self.__table.heading(4, text='Скидка')
        self.__output = ServiceSearch().service_full()
        for row in range(len(self.__output)):
            self.__table.insert(parent='', index=row, values=self.__output[row])

    def __checkcat(self, event):
        self.__table.delete(*self.__table.get_children())
        output = ServiceSearch().service_one(event.lower())
        for row in range(len(output)):
            self.__table.insert(parent='', index=row, values=output[row])

    def __new_application(self):
        if self.__table.item(self.__table.selection())['values'] != '':
            Application().new_app(id_service=self.__table.item(self.__table.selection())['values'][0])
            messagebox.showinfo('Оповещение', 'Заявка успешно добавлена, обновите таблицу!')
        else:
            messagebox.showerror('Ошибка', 'Вы ничего не выбрали!!!')

    def __accept(self):
        self.__app.destroy()

    def check(self):
        self.__table.grid(row=2, column=1, pady=10, columnspan=5)
        self.__combobox.grid(row=1, column=5, sticky='E', pady=10)
        self.__button.grid(row=3, column=5, sticky='E')
        self.__button_new.grid(row=3, column=4, sticky='E')
        self.__lable_title.grid(row=1, column=1, sticky='W', pady=10)
        self.__app.mainloop()
