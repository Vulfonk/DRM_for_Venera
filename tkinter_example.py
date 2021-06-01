from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd

import tkinter as tk
import time
import tkinter.ttk as ttk
import CreateDB
import hash_example

import xlwt

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

        def b_import_click(event):
            wb = xlwt.Workbook()
            xl_file = fd.asksaveasfilename(defaultextension=".xls", filetypes=(("xls file", "*.xls"),))
            ws = wb.add_sheet('Отчет')
            i, j = 0, 0
            for turp in lis:
                for item in turp:

                    ws.write(r=i, c=j, label=str(item))
                    j += 1
                i += 1
                j = 0

            wb.save(xl_file)

        self.button_exel_import = Button(self, text="Сохранить отчет")
        self.button_exel_import.place(x=590, y=590)
        self.button_exel_import.bind("<Button-1>", b_import_click)

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
            res.geometry('1400x700+200+100')



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

