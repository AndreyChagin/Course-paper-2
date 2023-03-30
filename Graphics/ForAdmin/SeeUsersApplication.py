import customtkinter
from customtkinter import CTk
from tkinter import ttk
from Logic import FullUsersApp
from DataBase import Users, Application
from tkinter import messagebox


class SeeApplicationUsers:
    def __init__(self):
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')
        self.__app = CTk()
        self.__app.geometry('900x400')
        self.__app.resizable(0, 0)
        self.__app.title('Услуги')
        self.__lable_title = customtkinter.CTkLabel(
            master=self.__app,
            text='Услуги клиентов',
            text_color='green',
            font=('ISOCPEUR', 25)
        )
        self.__button_delete_app = customtkinter.CTkButton(
            master=self.__app,
            text='Выполнена',
            corner_radius=5,
            command=self.__delete_app,
            font=('ISOCPEUR', 20)
        )
        self.__update_view = customtkinter.CTkButton(
            master=self.__app,
            text='Обновить',
            corner_radius=5,
            command=self.__update_table,
            font=('ISOCPEUR', 20)
        )
        self.__button = customtkinter.CTkButton(
            master=self.__app,
            text='Ок',
            corner_radius=5,
            command=self.__destroy_window,
            font=('ISOCPEUR', 20)
        )
        __values = (item[1] for item in Users().data if item[3] is not None)
        self.__combobox = customtkinter.CTkComboBox(master=self.__app, values=list(__values),
                                                    font=('ISOCPEUR', 15), state='readonly', command=self.__check)
        self.__table = ttk.Treeview(master=self.__app, show='headings')
        self.__table.delete(*self.__table.get_children())
        self.__table.configure(columns=('id', 'Наименование', 'Цена', 'Категория'))
        self.__table.heading(0, text='id')
        self.__table.heading(1, text='Наименование')
        self.__table.heading(2, text='Цена')
        self.__table.heading(3, text='Категория')

    def __check(self, event):
        self.__table.delete(*self.__table.get_children())
        __output = FullUsersApp().search_full_application_users(event)
        for row in range(len(__output)):
            self.__table.insert(parent='', index=row, values=__output[row])

    def __delete_app(self):
        if self.__table.item(self.__table.selection())['values'] != '':
            Application().delete_application(
                id_app=int(self.__table.item(self.__table.selection())['values'][0]))
            messagebox.showinfo('Оповещение', 'Заявка выполнена!!!')
        else:
            messagebox.showerror('Ошибка', 'Вы ничего не выбрали!!!')

    def __update_table(self):
        self.__table.delete(*self.__table.get_children())
        __output = FullUsersApp().search_full_application_users(self.__combobox.get())
        for row in range(len(__output)):
            self.__table.insert(parent='', index=row, values=__output[row])

    def __destroy_window(self):
        self.__app.destroy()

    def loop(self):
        self.__lable_title.place(x=50, y=15)
        self.__combobox.place(x=250, y=15)
        self.__table.place(x=50, y=70)
        self.__button_delete_app.place(x=310, y=320)
        self.__update_view.place(x=510, y=320)
        self.__button.place(x=710, y=320)
        self.__app.mainloop()
