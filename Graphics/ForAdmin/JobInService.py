from DataBase import Service
from customtkinter import CTk
import customtkinter
from tkinter import ttk
from Graphics.ForAdmin.WorkingDataBase import UpdateService, NewService


class ServiceFull:
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    def __init__(self):
        self.__app = CTk()
        self.__app.geometry(f'{int(self.__app.winfo_screenwidth()*0.43)}x{int(self.__app.winfo_screenheight()*0.4)}')
        self.__app.resizable(0, 0)
        self.__app.title("Услуги")
        self.__frame = customtkinter.CTkFrame(
            master=self.__app,
            border_width=1,
            border_color='gray',
            width=600,
            height=100
        )
        self.__label_title = customtkinter.CTkLabel(
            master=self.__app,
            text='Услуги',
            font=('ISOCPEUR', 15)
        )

        self.__button_update = customtkinter.CTkButton(
            master=self.__frame,
            text='Обновить',
            font=('ISOCPEUR', 15),
            command=self.__table_view
        )
        self.__button_new_service = customtkinter.CTkButton(
            master=self.__frame,
            text='Добавить',
            font=('ISOCPEUR', 15),
            command=self.__new_service
        )
        self.__button_change = customtkinter.CTkButton(
            master=self.__frame,
            text='Изменить',
            font=('ISOCPEUR', 15),
            command=self.__update_service
        )

        self.__table = ttk.Treeview(
            master=self.__app,
            show='headings',
            columns=('Наименование', 'Цена', 'Категория'),
        )
        self.__table.heading(0, text='Наименование')
        self.__table.heading(1, text='Цена')
        self.__table.heading(0, text='Категория')

        for items in range(len(Service().data)):
            self.__table.insert(parent='', index=items,
                                values=Service().data[items][1:])

    def __table_view(self):
        self.__table.delete(*self.__table.get_children())
        for items in range(len(Service().data)):
            self.__table.insert(parent='', index=items,
                                values=Service().data[items][1:])

    @staticmethod
    def __update_service():
        UpdateService().loop()

    @staticmethod
    def __new_service():
        NewService().loop()

    def loop(self):
        self.__frame.grid(row=1, column=1, columnspan=3, padx=50, pady=10)
        self.__button_update.place(x=10, y=40)
        self.__button_new_service.place(x=230, y=40)
        self.__button_change.place(x=445, y=40)
        self.__table.grid(row=2, column=1, columnspan=3, padx=50, pady=10)
        self.__app.mainloop()
