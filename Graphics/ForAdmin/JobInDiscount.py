from DataBase import Discount
from customtkinter import CTk
import customtkinter
from tkinter import ttk, messagebox, END
from Graphics.ForAdmin.WorkingDataBase import NewDiscount
from Logic import ServiceSearch


class DiscountFull:
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    def __init__(self):
        self.__app = CTk()
        self.__app.geometry(
            f'{int(self.__app.winfo_screenwidth() * 0.54)}x{int(self.__app.winfo_screenheight() * 0.45)}')
        self.__app.resizable(0, 0)
        self.__app.title("Услуги")
        self.__frame = customtkinter.CTkFrame(
            master=self.__app,
            border_width=1,
            border_color='gray',
            width=int(self.__app.winfo_screenwidth() * 0.5)-40,
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
        self.__button_new_discount = customtkinter.CTkButton(
            master=self.__frame,
            text='Добавить',
            font=('ISOCPEUR', 15),
            command=self.__new_discount
        )
        self.__button_delete = customtkinter.CTkButton(
            master=self.__frame,
            text='Удалить',
            font=('ISOCPEUR', 15),
            command=self.__delete_discount
        )

        self.__button_change = customtkinter.CTkButton(
            master=self.__frame,
            text='Изменить',
            font=('ISOCPEUR', 15),
            command=self.__update_discount
        )

        self.__entry_new_discount = customtkinter.CTkEntry(
            master=self.__frame,
            placeholder_text='Новая скидка в %',
            placeholder_text_color='gray',
            corner_radius=5,
            font=('ISOCPEUR', 15)
        )

        self.__table = ttk.Treeview(
            master=self.__app,
            show='headings',
            columns=('id', 'Наименование', 'Скидка'),
        )
        self.__table.heading(0, text='id')
        self.__table.heading(1, text='Наименование')
        self.__table.heading(2, text='Скидка')

        for items in range(len(Discount().data)):
            self.__table.insert(parent='', index=items,
                                values=(Discount().data[items][0],
                                        ServiceSearch().return_name_service(Discount().data[items][1]),
                                        Discount().data[items][2]))

    def __table_view(self):
        self.__table.delete(*self.__table.get_children())
        for items in range(len(Discount().data)):
            self.__table.insert(parent='', index=items,
                                values=(Discount().data[items][0],
                                        ServiceSearch().return_name_service(Discount().data[items][1]),
                                        Discount().data[items][2]))

    def __update_discount(self):
        if self.__table.item(self.__table.selection()) != '' and self.__entry_new_discount.get() != '':
            Discount().update_discount(
                id_discount=self.__table.item(self.__table.selection())['values'][0],
                discount=str(self.__entry_new_discount.get())
            )
            self.__entry_new_discount.delete(0, END)
            messagebox.showinfo('Оповещение', 'Обновите таблицу для просмотра результата!!!')
        else:
            messagebox.showerror('Ошибка', 'Вы ничего не выбрали!!!')

    def __delete_discount(self):
        if self.__table.item(self.__table.selection()) != '':
            Discount().delete_discount(
                id_discount=self.__table.item(self.__table.selection())['values'][0]
            )
            messagebox.showinfo('Оповещение', 'Обновите таблицу для просмотра результата!!!')
        else:
            messagebox.showerror('Ошибка', 'Вы ничего не выбрали!!!')

    @staticmethod
    def __new_discount():
        NewDiscount().loop()

    def loop(self):
        self.__frame.grid(row=1, column=1, columnspan=5, padx=50, pady=10)
        self.__button_update.place(x=10, y=40)
        self.__button_new_discount.place(x=160, y=40)
        self.__button_delete.place(x=310, y=40)
        self.__button_change.place(x=460, y=40)
        self.__entry_new_discount.place(x=610, y=40)
        self.__table.grid(row=5, column=1, columnspan=4, padx=50, pady=25)
        self.__app.mainloop()
