from functools import partial
from tkinter import *
from tkinter import ttk, messagebox
from turtle import width
import pymysql
import custom as cs
import credentials as cr
import validemail as vl

class Management:
    '''Функція ініціалізації нового вікна бібліотекою TKinter'''
    def __init__(self, root):
        self.window = root
        self.window.title("ContactManager")
        self.window.geometry("940x480")
        self.window.config(bg = "white")
     
        # Кастомізація
        self.color_1 = cs.color_1
        self.color_2 = cs.color_2
        self.color_3 = cs.color_3
        self.color_4 = cs.color_4
        self.font_1 = cs.font_1
        self.font_2 = cs.font_2
        self.columns = cs.columns

        # Облікові дані користувача бази даних
        self.host = cr.host
        self.user = cr.user
        self.password = cr.password
        self.database = cr.database

        # Лівий фрейм
        self.frame_1 = Frame(self.window, bg=cs.color_1)
        self.frame_1.place(x=0, y=0, width=740, relheight = 1)

        # Правий фрейм
        self.frame_2 = Frame(self.window, bg = cs.color_2)
        self.frame_2.place(x=740,y=0,relwidth=1, relheight=1)

        # Створення меню для розмішення кнопок
        getMenu = Label(self.frame_2, text="Меню", font=(self.font_2, 18, "bold"), bg=self.color_2).place(x=63,y=5)
        # Створення кнопок
        self.add_new_bt = Button(self.frame_2, text='Додати контакт', font=(cs.font_1, 12), bd=2, command=self.AddRecord,cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=30,y=45,width=140,height=40)
        self.display_bt = Button(self.frame_2, text='Список контактів', font=(cs.font_1, 12), bd=2, command=self.DisplayRecords, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=30,y=105,width=140,height=40)
        self.search_bt = Button(self.frame_2, text='Пошук контактів', font=(cs.font_1, 12), bd=2, command=self.GetContact_to_Search,cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=30,y=165,width=140,height=40)
        self.clear_bt = Button(self.frame_2, text='Головний екран', font=(cs.font_1, 12), bd=2, command=self.ClearScreen,cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=30,y=345,width=140,height=40)
        self.exit_bt = Button(self.frame_2, text='Вихід', font=(cs.font_1, 12), bd=2, command=self.Exit, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=30,y=405,width=140,height=40)
        
    '''Функція створення текстових полів введення контакної інформації для додавання нових контактів'''
    def AddRecord(self):
        self.ClearScreen()

        self.name = Label(self.frame_1, text="Ім'я", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=220,y=30)
        self.name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.name_entry.place(x=220,y=60, width=300)

        self.surname = Label(self.frame_1, text="Прізвище", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=220,y=100)
        self.surname_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.surname_entry.place(x=220,y=130, width=300)

        self.addr = Label(self.frame_1, text="Адреса", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=220,y=170)
        self.addr_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.addr_entry.place(x=220,y=200, width=300)

        self.contact = Label(self.frame_1, text="Номер телефону", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=220,y=240)
        self.contact_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.contact_entry.place(x=220,y=270, width=300)

        self.email = Label(self.frame_1, text="Email", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=220,y=310)
        self.email_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.email_entry.place(x=220,y=340, width=300)

        self.submit_bt_1 = Button(self.frame_1, text='Зберегти', font=(self.font_1, 12), bd=2, command=self.Submit, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=310,y=389,width=100)

    '''Функція додавання нового контакту в базу даних'''
    def Submit(self):
        if self.name_entry.get() == "" or self.surname_entry.get() == "" or self.addr_entry.get() == "" or self.contact_entry.get() == "" or self.email_entry.get() == "":
            messagebox.showerror("Помилка!","Пробачте, усі поля повинні бути заповнені",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from contact_register where contact=%s", self.contact_entry.get())
                row=curs.fetchone()

                if row!=None:
                    messagebox.showerror("Error!","The contact number is already exists, please try again with another number",parent=self.window)
                else:
                    if vl.IsValidEmail(self.email_entry.get()):
                        curs.execute("insert into contact_register (f_name,l_name,address,contact,email) values(%s,%s,%s,%s,%s)",
                                            (
                                                self.name_entry.get(),
                                                self.surname_entry.get(),
                                                self.addr_entry.get(),
                                                self.contact_entry.get(),
                                                self.email_entry.get()  
                                            ))
                        connection.commit()
                        connection.close()
                        messagebox.showinfo('Готово!', "Дані успішно збережено!")
                        self.reset_fields()
                    else:
                        messagebox.showerror("Помилка!", "Перевірте формат введеної Вами електронної пошти")
            except Exception as e:
                messagebox.showerror("Помилка!",f"Причина помилки: {str(e)}",parent=self.window)

    '''Функція створення текстових полів вводу контактної інформації для пошуку контактів'''
    def GetContact_to_Search(self):
        self.ClearScreen()
        getName = Label(self.frame_1, text="Ім'я", font=(self.font_2, 18, "bold"), bg=self.color_1).place(x=160,y=70)
        self.name_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.name_entry.place(x=160, y=110, width=200, height=30)

        getSurname = Label(self.frame_1, text="Прізвище", font=(self.font_2, 18, "bold"), bg=self.color_1).place(x=420,y=70)
        self.surname_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.surname_entry.place(x=420, y=110, width=200, height=30)

        submit_bt_2 = Button(self.frame_1, text='Знайти', font=(self.font_1, 14), bd=2, command=self.CheckContact_to_Search, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=340,y=180,width=100)

    '''Функція перевірки правильності введення контактної інформації та наявності шуканого контакту'''
    def CheckContact_to_Search(self):
        if self.name_entry.get() == "" and self.surname_entry.get() == "":
            messagebox.showerror("Помилка!", "Заповніть, будь ласка, поля Ім'я або Прізвище",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from contact_register where f_name=%s or l_name=%s", (self.name_entry.get(), self.surname_entry.get()))
                rows=curs.fetchall()
                if len(rows) == 0:
                    messagebox.showerror("Помилка!","Введеного Вами контакту не існує!",parent=self.window)
                    connection.close()
                    self.name_entry.delete(0, END)
                    self.surname_entry.delete(0, END)
                else:
                    self.ShowRecords(rows)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Помилка!",f"Причина помилки: {str(e)}",parent=self.window)

    '''Функція виводу шуканих контактів'''
    def ShowRecords(self, rows):
        self.ClearScreen()
        scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_1, columns=self.columns, height=400, selectmode="extended", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        scroll_x.pack(side=BOTTOM, fill=X)

        # Стовпці таблиці бази даних
        self.tree.heading('first_name', text="Ім'я", anchor=W)
        self.tree.heading('last_name', text='Прізвище', anchor=W)
        self.tree.heading('contact', text='Номер телефону', anchor=W)
        self.tree.heading('address', text='Адрес', anchor=W)
        self.tree.heading('email', text='Email', anchor=W)
        self.tree.pack()
        self.tree.bind('<Button-1>', self.Selected)
        # Внесення даних до таблиць
        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list)+1), values=(list[0], list[1], list[2], list[3], list[4]))

    '''Функція створення таблиці на головному екрані та виведення в ній списку контактів із бази даних'''
    def DisplayRecords(self):
        self.ClearScreen()

        scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_1, columns=self.columns, height=400, selectmode="extended", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)

        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)

        scroll_x.pack(side=BOTTOM, fill=X)

        # Заголовки таблиці
        self.tree.heading('first_name', text="Ім'я", anchor=W)
        self.tree.heading('last_name', text='Прізвище', anchor=W)
        self.tree.heading('contact', text='Номер телефону', anchor=W)
        self.tree.heading('address', text='Адрес', anchor=W)
        self.tree.heading('email', text='Email', anchor=W)
        self.tree.pack()

        self.tree.bind('<Button-1>', self.Selected)

        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            curs = connection.cursor()
            curs.execute("select * from contact_register")
            rows=curs.fetchall()
            if rows == None:
                messagebox.showinfo("База даних пуста!","Немає даних для виведення!",parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Помилка!",f"Причина помилки: {str(e)}",parent=self.window)
        # Формування рядків
        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list)+1), values=(list[0], list[1], list[2], list[3], list[4]))

    '''Функція появи кнопок редагування та видалення контактів при виборі будь-якого контакту'''
    def Selected(self, a):
        pass

    '''Функція скидання введеної інформації в текстові поля після їх застосування'''
    def reset_fields(self):
        self.name_entry.delete(0, END)
        self.surname_entry.delete(0, END)
        self.addr_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.email_entry.delete(0, END)

    '''Функція очищення екрану при натисканні кнопки Головний екран'''
    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

    '''Функція виходу з ПЗ'''
    def Exit(self):
        pass

if __name__ == "__main__":
    root = Tk()
    obj = Management(root)
    root.mainloop()