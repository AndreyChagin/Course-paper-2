from DataBase import Service
from customtkinter import CTk
import customtkinter
from tkinter import messagebox


class NewService:
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    def __init__(self):
        self.__app = CTk()
        self.__app.geometry("300x300")
        self.__app.resizable(0, 0)
        self.__app.title("Услуги")
        self.__frame = customtkinter.CTkFrame(
            master=self.__app,
            border_width=1,
            border_color='gray',
        )
        self.__combobox = customtkinter.CTkComboBox(
            master=self.__frame,
            state='readonly',
            values=['кузов', 'салон', 'другие'],
            font=('ISOCPEUR', 15)
        )
        self.__entry_new_name = customtkinter.CTkEntry(
            master=self.__frame,
            placeholder_text='Название',
            placeholder_text_color='gray',
            corner_radius=5,
        )
        self.__entry_new_price = customtkinter.CTkEntry(
            master=self.__frame,
            placeholder_text='Цена',
            placeholder_text_color='gray',
            corner_radius=5,
        )
        self.__button_update = customtkinter.CTkButton(
            master=self.__frame,
            text='Добавить',
            font=('ISOCPEUR', 15),
            command=self.__new_row
        )

    def __new_row(self):
        if (self.__entry_new_price.get() and self.__entry_new_name.get() and self.__combobox.get()) != '':
            Service().new_service(
                name=self.__entry_new_name.get(),
                price=int(self.__entry_new_price.get()),
                category=self.__combobox.get()
            )
            messagebox.showinfo('Успешно', 'Для просмотра обновите таблицу!')
        else:
            messagebox.showerror('Ошибка', 'Введите все поля!!!')

    def loop(self):
        self.__frame.place(x=50, y=50)
        self.__combobox.place(x=28, y=100)
        self.__entry_new_name.place(x=28, y=20)
        self.__entry_new_price.place(x=28, y=60)
        self.__button_update.place(x=28, y=140)
        self.__app.mainloop()
