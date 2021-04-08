from tkinter import Tk, Frame, Text, Menu, BOTH, X,Button
from tkinter import filedialog as fd
import tkinter as tk
import time


class Example(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("��������� ��������� ������")

        self.pack(fill=BOTH, expand=True)
        
        frame1 = Frame(self)
        frame1.pack(fill=X)
        
        txt = Text(frame1,width=15, height=15, bg = "white")
        txt.pack(fill=BOTH, pady=5, padx=10, expand=True )   
        
        frame2 = Frame(self)
        frame2.pack(fill=BOTH, expand=True)     
 
        txt1 = Text(frame2,width=7, height=7, bg = "white")
        txt1.configure(state=tk.DISABLED)
        txt1.pack(fill=BOTH, pady=5, padx=20, expand=False)            
        
        global path1 
        path1 = str()
        global path2 
        path2 = str()
        #������� ����
        #������� ����
        
 
        def CFD1():
            global path1 
            path1 = fd.askdirectory(title = "�������")
            if type(path1) != tuple and path1 != '':
                txt1.configure(state=tk.NORMAL)
                txt1.insert(1.0, '��������� ������������ �������� �������: ' + path1 + '\n')
                txt1.configure(state=tk.DISABLED)
            print (path1)
            return path1


        def CFD2():
            global path2
            path2 = fd.askdirectory(title = "�������")
            if type(path2) != tuple and path2 != '':
                txt1.configure(state=tk.NORMAL)
                txt1.insert(1.0, '��������� ������������ �������� ���������: ' + path2 + '\n')
                txt1.configure(state=tk.DISABLED)
            return path2

   
        def OFD1(path1):
            doc_name = fd.askopenfilename(title = "�������", initialdir = path1)
            print (path1)
            if type(doc_name) != tuple and doc_name != '':
                txt1.configure(state=tk.NORMAL)
                txt1.insert(1.0, '������ ���� ��������� ������' + doc_name + '\n')
                txt1.configure(state=tk.DISABLED)
                doc = open(doc_name, encoding="utf-8")
                s = doc.read()
                txt.delete(1.0, tk.END)
                txt.insert(1.0, s)
                doc.close()



        def OFD2(path2):
            doc_name = fd.askopenfilename(title = "�������", initialdir = path2)
            if type(doc_name) != tuple and doc_name != '':
                txt1.configure(state=tk.NORMAL)
                txt1.insert(1.0, '������ ���� ��������� ���������' + doc_name + '\n')
                txt1.configure(state=tk.DISABLED)
                doc = open(doc_name, encoding="utf-8")
                s = doc.read()
                txt.delete(1.0, tk.END)
                txt.insert(1.0, s)
                doc.close()
     

        #��������� ����
        def SFD():
            #��������� ������ ��� �������� ���������
            DT = time.strftime("_%Y-%m-%d_%H-%M-%S", time.localtime())
            doc_name = fd.asksaveasfilename(title = "���������", initialfile = DT, defaultextension="*.txt", filetypes = (("���������", "*.txt"), ("CSV ", "*.csv"), ("XML ", "*.xml")))
            doc = open(doc_name, 'w', encoding="utf-8")
            s = txt.get(1.0, tk.END)
            doc.write(s)
            doc.close()
            if type(doc_name) != tuple:
                txt1.configure(state=tk.NORMAL)
                txt1.insert(1.0, '���� �������.\n')
                txt1.configure(state=tk.DISABLED)
                
         #����� ���������� � ������������� 
        def InterText():
            Window1().mainloop()

        class Window1(Tk):
            def __init__(self, *arg, **kwarg):
                super().__init__(*arg, **kwarg)
                frame4 = Frame(self)
                frame4.pack(fill=X)
                
                txt = Text(frame4,width=60, height=20, bg = "white")
                txt.pack(fill=BOTH, pady=10, padx=10, expand=True ) 
                
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
        
                txt = Text(frame3,width=100, height=20, bg = "white")
                txt.pack(fill=BOTH, pady=10, padx=10, expand=True ) 
                
                txt.configure(state=tk.NORMAL)
                txt.insert(1.0, '�������   ')
                txt.configure(state=tk.DISABLED) 
                txt.delete(1.0, tk.END) 

                       
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        fileMenu = Menu(menubar)       
        #���������� ������������ ������� "������� ����"  
        submenu = Menu(fileMenu)
        #���������� ������������ ������� "��������� ����..."  
        fileMenu.add_command(label='���������',  underline=1, command = SFD)
        fileMenu.add_cascade(label='������� ����', menu=submenu, underline=0)
        submenu.add_command(label="�������� ������", command = lambda: OFD1(path1))
        submenu.add_command(label="�������� ���������", command = lambda: OFD2(path2))
        submenu.add_command(label="���-�� ���")
        
        helpMenu = Menu(menubar)       
        referMenu = Menu(helpMenu)
        #fileMenu.add_separator()
        #���������� ������������ ���� "����" � "�����"  
        menubar.add_cascade(label="����", underline=0, menu=fileMenu)   
        menubar.add_cascade(label="�����", underline=1)
        #���������� ������������ ���� "�������"     
        menubar.add_cascade(label="�������", underline=2, menu=helpMenu)   
        helpMenu.add_command(label='����������� ������������', underline=0)
        #���������� ������������ ������� � ���������
        helpMenu.add_cascade(label='� ���������',menu=referMenu,underline=1)
        referMenu.add_command(label='��� �������� ���������',underline=0,command=create_window )
        referMenu.add_command(label='���������� � ������������� � �� ��������',underline=1,command=InterText )
        
        
        settingMenu = Menu(menubar)
        setmenu = Menu(settingMenu)
        #���������� ������������ ���� "���������"
        menubar.add_cascade(label="���������", menu=settingMenu, underline=3)
        settingMenu.add_cascade(label='��������� ����',menu=setmenu, underline=0)
        settingMenu.add_command(label='���-�� ���', underline=1)
        setmenu.add_command(label="�������� ���� ��� �������� �������",command = CFD1)
        setmenu.add_command(label="�������� ���� ��� �������� ���������",command = CFD2)
        
         #����������  ���� "�����"   
        menubar.add_cascade(label="�����", underline=4, command=self.onExit)
        
    def onExit(self):
        self.quit()
        
def main():
    root = Tk()
    root.geometry("700x400+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()