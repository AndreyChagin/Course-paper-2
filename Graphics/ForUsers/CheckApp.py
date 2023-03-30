from tkinter import ttk, messagebox

import customtkinter
from customtkinter import CTk

from Logic import SearchAppUser
from DataBase import Application


class CheckMyApp:
    def __init__(self):
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')
        self.__app = CTk()
        self.__app.geometry('900x350')
        self.__app.resizable(0, 0)
        self.__app.title('Заявки')
        self.__lable_title = customtkinter.CTkLabel(
            master=self.__app,
            text='Заявки',
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
        self.__button_delete = customtkinter.CTkButton(
            master=self.__app,
            text='Удалить',
            corner_radius=5,
            command=self.__delete_application,
            font=('ISOCPEUR', 20)
        )
        self.__button_update = customtkinter.CTkButton(
            master=self.__app,
            text='Обновить',
            corner_radius=5,
            command=self.__update_table_view,
            font=('ISOCPEUR', 20)
        )

        self.__table = ttk.Treeview(master=self.__app, show='headings')
        self.__table.configure(columns=('id', 'Наименование', 'Цена', 'Категория'))
        self.__table.heading(0, text='id')
        self.__table.heading(1, text='Наименование')
        self.__table.heading(2, text='Цена')
        self.__table.heading(3, text='Категория')
        self.__table.delete(*self.__table.get_children())
        self.__summ = 0
        self.__output_list = SearchAppUser().search_app()
        for row in range(len(self.__output_list)):
            self.__table.insert(parent='', index=row, values=self.__output_list[row])
            self.__summ += self.__output_list[row][2]
        self.__label = customtkinter.CTkLabel(master=self.__app, text_color='white',
                                              text=f"Итоговая стоимость: {self.__summ}", font=('ISOCPEUR', 15))

    def __delete_application(self):
        if self.__table.item(self.__table.selection())['values'] != '':
            Application().delete_application(id_app=self.__table.item(self.__table.selection())['values'][0])
            messagebox.showinfo('Оповещение', 'Заявка удалена!!!')
        else:
            messagebox.showerror('Ошибка', 'Вы ничего не выбрали!!!')

    def __update_table_view(self):
        self.__table.delete(*self.__table.get_children())
        self.__output_list = SearchAppUser().search_app()
        self.__summ = 0
        for row in range(len(self.__output_list)):
            self.__table.insert(parent='', index=row, values=self.__output_list[row])
            self.__summ += self.__output_list[row][2]
        self.__label.configure(text=f'Итоговая стоимость: {self.__summ}')

    def __accept(self):
        self.__app.destroy()

    def check(self):
        self.__table.place(x=50, y=50)
        self.__button.place(x=710, y=280)
        self.__button_delete.place(x=510, y=280)
        self.__button_update.place(x=310, y=280)
        self.__label.place(x=50, y=275)
        self.__lable_title.place(x=50, y=15)
        self.__app.mainloop()
