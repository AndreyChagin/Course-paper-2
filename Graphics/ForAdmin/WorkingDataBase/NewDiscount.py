from DataBase import Service, Discount
from customtkinter import CTk
import customtkinter
from tkinter import messagebox
from Logic import ServiceSearch


class NewDiscount:
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    def __init__(self):
        self.__app = CTk()
        self.__app.geometry("300x300")
        self.__app.resizable(0, 0)
        self.__app.title("Скидки")
        self.__frame = customtkinter.CTkFrame(
            master=self.__app,
            border_width=1,
            border_color='gray',
        )
        self.__combobox = customtkinter.CTkComboBox(
            master=self.__frame,
            state='readonly',
            values=[item[1] for item in Service().data],
            font=('ISOCPEUR', 15)
        )

        self.__entry_new_discount = customtkinter.CTkEntry(
            master=self.__frame,
            placeholder_text='Скидка',
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
        if (self.__entry_new_discount.get() and self.__combobox.get()) != '':
            Discount().new_discount(id_service=ServiceSearch().return_id_service(self.__combobox.get()),
                                    discount=int(self.__entry_new_discount.get()))
            messagebox.showinfo('Успешно', 'Для просмотра обновите таблицу!')
        else:
            messagebox.showerror('Ошибка', 'Введите все поля!!!')

    def loop(self):
        self.__frame.place(x=50, y=50)
        self.__combobox.place(x=28, y=40)
        self.__entry_new_discount.place(x=28, y=100)
        self.__button_update.place(x=28, y=160)
        self.__app.mainloop()
