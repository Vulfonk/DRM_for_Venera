from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd

import tkinter as tk
import time
import tkinter.ttk as ttk
import CreateDB
import hash_example

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Обработка табличных данных")

        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        txt = Text(frame1, width=15, height=15, bg="white")
        txt.pack(fill=BOTH, pady=5, padx=10, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=BOTH, expand=True)

        txt1 = Text(frame2, width=7, height=7, bg="white")
        txt1.configure(state=tk.DISABLED)
        txt1.pack(fill=BOTH, pady=5, padx=20, expand=False)

        global path1
        path1 = str()
        global path2
        path2 = str()

        # выбрать пути
        # выбрать пути

        def CFD1():
            global path1
            path1 = fd.askdirectory(title="Выбрать")
            if type(path1) != tuple and path1 != '':
                txt1.configure(state=tk.NORMAL)
                txt1.insert(1.0, 'Назначено расположение архивных трендов: ' + path1 + '\n')
                txt1.configure(state=tk.DISABLED)
            print(path1)
            return path1

        def CFD2():
            global path2
            path2 = fd.askdirectory(title="Выбрать")
            if type(path2) != tuple and path2 != '':
                txt1.configure(state=tk.NORMAL)
                txt1.insert(1.0, 'Назначено расположение архивных сообщений: ' + path2 + '\n')
                txt1.configure(state=tk.DISABLED)
            return path2

        def OFD1(path1):

                txt.insert(1.0, s)
                doc.close()

        def OFD2(path2):
            doc_name = fd.askopenfilename(title="Открыть", initialdir=path2)
            if type(doc_name) != tuple and doc_name != '':
                txt1.configure(state=tk.NORMAL)
                txt1.insert(1.0, 'Открыт файл архивного сообщения' + doc_name + '\n')
                txt1.configure(state=tk.DISABLED)
                doc = open(doc_name, encoding="utf-8")
                s = doc.read()
                txt.delete(1.0, tk.END)
                txt.insert(1.0, s)
                doc.close()

        # сохранить файл
        def SFD():
            # назначаем шаблон для названия документа
            DT = time.strftime("_%Y-%m-%d_%H-%M-%S", time.localtime())
            doc_name = fd.asksaveasfilename(title="Сохранить", initialfile=DT, defaultextension="*.txt",
                                            filetypes=(("Текстовый", "*.txt"), ("CSV ", "*.csv"), ("XML ", "*.xml")))
            doc = open(doc_name, 'w', encoding="utf-8")
            s = txt.get(1.0, tk.END)
            doc.write(s)
            doc.close()
            if type(doc_name) != tuple:
                txt1.configure(state=tk.NORMAL)
                txt1.insert(1.0, 'Файл сохранён.\n')
                txt1.configure(state=tk.DISABLED)

        # вывод информации о разработчиках
        def InterText():
            Window1().mainloop()

        class Window1(Tk):
            def __init__(self, *arg, **kwarg):
                super().__init__(*arg, **kwarg)
                frame4 = Frame(self)
                frame4.pack(fill=X)

                txt = Text(frame4, width=60, height=20, bg="white")
                txt.pack(fill=BOTH, pady=10, padx=10, expand=True)

                txt.configure(state=tk.NORMAL)
                txt.insert(1.0, ' ')
                txt.configure(state=tk.DISABLED)
                txt.delete(1.0, tk.END)

        def create_window():
            Window().mainloop()

        class Window(Tk):
            def __init__(self, *arg, **kwarg):
                super().__init__(*arg, **kwarg)
                frame3 = Frame(self)
                frame3.pack(fill=X)

                txt = Text(frame3, width=100, height=20, bg="white")
                txt.pack(fill=BOTH, pady=10, padx=10, expand=True)

                txt.configure(state=tk.NORMAL)
                txt.insert(1.0, 'Краткая   ')
                txt.configure(state=tk.DISABLED)
                txt.delete(1.0, tk.END)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        # Добавление всплывающего подменю "выбрать файл"
        submenu = Menu(fileMenu)
        # Добавление всплывающего подменю "Сохранить файл..."
        fileMenu.add_command(label='Сохранить', underline=1, command=SFD)
        fileMenu.add_cascade(label='Выбрать файл', menu=submenu, underline=0)
        submenu.add_command(label="Архивные тренды", command=lambda: OFD1(path1))
        submenu.add_command(label="Архивные сообщения", command=lambda: OFD2(path2))
        submenu.add_command(label="Что-то еще")

        helpMenu = Menu(menubar)
        referMenu = Menu(helpMenu)
        # fileMenu.add_separator()
        # Добавление всплывающего меню "Файл" и "старт"
        menubar.add_cascade(label="Файл", underline=0, menu=fileMenu)
        menubar.add_cascade(label="Старт", underline=1)
        # Добавление всплывающего меню "Справка"
        menubar.add_cascade(label="Справка", underline=2, menu=helpMenu)
        helpMenu.add_command(label='Руководство пользователя', underline=0)
        # Добавление всплывающего подменю О программе
        helpMenu.add_cascade(label='О программе', menu=referMenu, underline=1)
        referMenu.add_command(label='Как работает программа', underline=0, command=create_window)
        referMenu.add_command(label='Информация о разработчиках и их контакты', underline=1, command=InterText)

        settingMenu = Menu(menubar)
        setmenu = Menu(settingMenu)
        # Добавление всплывающего меню "Настройки"
        menubar.add_cascade(label="Настройки", menu=settingMenu, underline=3)
        settingMenu.add_cascade(label='Назначить пути', menu=setmenu, underline=0)
        settingMenu.add_command(label='Что-то еще', underline=1)
        setmenu.add_command(label="Выберите путь для архивных трендов", command=CFD1)
        setmenu.add_command(label="Выберите путь для архивных сообщений", command=CFD2)

        # Добавление  меню "Выйти"
        menubar.add_cascade(label="Выйти", underline=4, command=self.onExit)

    def onExit(self):
        self.quit()


class Result(tk.Tk):
    def __init__(self, selected_item, data_base, extends):
        super().__init__()
        self.title("Result")

        self.frame_result_table = Frame(self, width=200, height=100)
        self.frame_result_table.place(x=10, y=10)

        columns = ("#1", "#2", "#3", "#4")
        self.frame_result_table.tree = ttk.Treeview(self.frame_result_table,
                                                    show="headings", columns=columns, height=27)
        tree_table = self.frame_result_table.tree

        tree_table.heading("#1", text="Путь каталога")
        tree_table.heading("#2", text="Хэш")
        tree_table.heading("#3", text="Дата проверки")
        tree_table.heading("#4", text="Результат")
        ysb_table = ttk.Scrollbar(self.frame_result_table, orient=tk.VERTICAL, command=tree_table.yview)
        tree_table.configure(yscroll=ysb_table.set)

        tree_table.grid(row=0, column=0)
        ysb_table.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.frame_result_table.rowconfigure(0, weight=1)
        self.frame_result_table.columnconfigure(0, weight=1)

        tree_table.column("#1", minwidth=40, width=650, stretch=0)
        tree_table.column("#2", minwidth=40, width=400, stretch=0)
        tree_table.column("#3", minwidth=40, width=200, stretch=0)
        tree_table.column("#4", minwidth=40, width=120, stretch=0)

        for i in tree_table.get_children():
            tree_table.delete(i)
        dir_path = fd.askdirectory(parent=self, title="")

        lis = hash_example.Equal(data_base.view_etalon_hashes(selected_item),
                                 hash_example.DictHashesClass(dir_path, extends))

        for files in lis:
            tree_table.insert("", tk.END, values=files)

class App(tk.Tk):
    def __init__(self):
        self.database = CreateDB.HashesDataBase("TestingDataBase2")

        super().__init__()
        self.title("DRM")

        # кнопка
        # "Сравнить"
        def b_select_click(event):
            selected_item = self.frame_list_etalons.tree.item(self.frame_list_etalons.tree.focus())["values"][0]
            extens = self.tbox_extensions.get().split()
            res = Result(selected_item, self.database, extens)
            res.geometry('1400x800+200+100')
            res.resizable(width=False, height=False)
            res.mainloop()

        self.button_directory_dialog = Button(self, text="Сравнить")
        self.button_directory_dialog.place(x=590, y=550)
        self.button_directory_dialog.bind("<Button-1>", b_select_click)

        # кнопка
        # "Добавить эталон"

        def b_etalon_select_click(event):
            dir = fd.askdirectory(parent=self, title="")
            extens = self.tbox_extensions.get().split()
            hash_obj = hash_example.DictHashesClass(dir, extens)
            self.database.add_etalon(hash_obj)
            for i in self.frame_list_etalons.tree.get_children():
                self.frame_list_etalons.tree.delete(i)
            for etalons in self.database.view_etalons_list(is_absolute_path=False):
                self.frame_list_etalons.tree.insert("", tk.END, values=etalons[1:2])


        self.button_add_dialog = Button(self, text="Добавить эталон")
        self.button_add_dialog.place(x=480, y=550)
        self.button_add_dialog.bind("<Button-1>", b_etalon_select_click)

        # кнопка
        # "Удалить эталон"

        def b_dir_dialog_click(event):
            for selection in self.frame_list_etalons.tree.selection():
                dir = self.frame_list_etalons.tree.item(selection)['values'][0]

            self.database.del_etalon(dir)
            for i in self.frame_list_etalons.tree.get_children():
                self.frame_list_etalons.tree.delete(i)

            for etalons in self.database.view_etalons_list(is_absolute_path=False):
                self.frame_list_etalons.tree.insert("", tk.END, values=etalons[1:2])

            tree_table = self.frame_result_table.tree
            for i in tree_table.get_children():
                tree_table.delete(i)

        self.button_select_dialog = Button(self, text="Удалить эталон")
        self.button_select_dialog.place(x=380, y=550)
        self.button_select_dialog.bind("<Button-1>", b_dir_dialog_click)

        # список
        # эталонов

        self.frame_list_etalons = Frame(self, width=200, height=100)
        self.frame_list_etalons.place(x=10,y=10)

        columns = ("#1")
        self.frame_list_etalons.tree = ttk.Treeview(self.frame_list_etalons,
                                                    show="headings", columns=columns, height=27)
        etalon_list = self.frame_list_etalons.tree
        etalon_list.heading("#1", text="Etalons")
        etalon_list.column("#1", minwidth=330, width=330, stretch=0)

        ysb_list = ttk.Scrollbar(self.frame_list_etalons, orient=tk.VERTICAL, command=etalon_list.yview)
        etalon_list.configure(yscroll=ysb_list.set)

        etalon_list.grid(row=0, column=0)
        ysb_list.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.frame_list_etalons.rowconfigure(0, weight=1)
        self.frame_list_etalons.columnconfigure(0, weight=1)

        for etalons in self.database.view_etalons_list(is_absolute_path=False):
            etalon_list.insert("", tk.END, values=etalons[1:2])
            print(etalons[1])
            print(type(etalons[1]))

        # таблица
        # результатов
        # сравнения

        self.frame_result_table = Frame(self, width=200, height=100)
        self.frame_result_table.place(x=380, y=10)

        columns = ("#1", "#2")
        self.frame_result_table.tree = ttk.Treeview(self.frame_result_table,
                                                    show="headings", columns=columns, height=24)
        tree_table = self.frame_result_table.tree

        tree_table.heading("#1", text="Путь каталога")
        tree_table.heading("#2", text="Хэш")
        ysb_table = ttk.Scrollbar(self.frame_result_table, orient=tk.VERTICAL, command=tree_table.yview)
        tree_table.configure(yscroll=ysb_table.set)

        etalon_list.bind("<<TreeviewSelect>>", self.print_selection)

        tree_table.grid(row=0, column=0)
        ysb_table.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.frame_result_table.rowconfigure(0, weight=1)
        self.frame_result_table.columnconfigure(0, weight=1)

        tree_table.column("#1", minwidth=350, width=350, stretch=0)
        tree_table.column("#2", minwidth=300, width=400, stretch=0)

        # текстовое
        # поле ввода
        # для расширений
        self.tbox_extensions = Entry(self, width=75)
        self.tbox_extensions.place(x=680, y=551)

    def print_selection(self, event):
        tree_table = self.frame_result_table.tree
        for i in tree_table.get_children():
            tree_table.delete(i)
        for selection in self.frame_list_etalons.tree.selection():
            path = self.frame_list_etalons.tree.item(selection)['values'][0]
            for item in self.database.view_etalon_hashes(path):
                self.frame_result_table.tree.insert("", tk.END, values=item[1:3])

if __name__ == "__main__":
    app = App()
    app.geometry('1200x600+200+100')
    app.resizable(width=False, height=False)
    app.mainloop()

