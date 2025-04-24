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
        pass

    '''Функція створення таблиці на головному екрані та виведення в ній списку контактів із бази даних'''
    def DisplayRecords(self):
        pass

    '''Функція вводу контактної інформації для пошуку контактів'''
    def GetContact_to_Search(self):
        pass

    '''Функція очищення екрану при натисканні кнопки Головний екран'''
    def ClearScreen(self):
        pass

    '''Функція виходу з ПЗ'''
    def Exit(self):
        pass

if __name__ == "__main__":
    root = Tk()
    obj = Management(root)
    root.mainloop()