import tkinter as tki
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
from settings import *
sys.path.append(os.path.abspath('../Library'))
from lib import *

MainWindow = tki.Tk()
MainWindow.title(MAIN_WIN_TITLE)
MainWindow.geometry(HD_RES)
MainWindow.resizable(False, False)

tree = ttk.Treeview(MainWindow)
createTable(tree)
tree.grid(row=22,column=8, columnspan=70)

scrl = ttk.Scrollbar(MainWindow, orient="vertical", command=tree.yview)
scrl.grid(row=22,column=80, rowspan=1, sticky='ns')

scrlX = ttk.Scrollbar(MainWindow, orient="horizontal", command=tree.xview)
scrlX.grid(row=23,column=8, sticky='ew', columnspan=100)

tree.configure(yscrollcommand=scrl.set, xscrollcommand=scrlX.set)

sortOptions = list(data.columns)
SortCombo = ttk.Combobox(values=sortOptions, state="readonly")
SortCombo.current(0)
SortCombo.grid(row=24,column=30)

sortButton = tki.Button(text="Сортировать", command = lambda: sortTable(tree,SortCombo.get()))
sortButton.grid(row=25,column=30)

idEntry = tki.Entry()
idEntry.grid(row=24,column=31)

delButton = tki.Button(text="Удалить", command = lambda: [removeElement(int(idEntry.get())), updateTable(tree)])
delButton.grid(row=25,column=31)

for i in range (0, 19):
    JustLabel = tki.Label(MainWindow, text = "  ")
    JustLabel.grid(row=0,column=i)

SearchLabel = tki.Label(MainWindow, text="База данных ноутбуков",font="Times 16 bold")
SearchLabel.grid(row=0,column=30, columnspan=2)


SearchButton = tki.Button(MainWindow,text="Поиск",width=20,height=3,command=openSearch)
SearchButton.grid(row=2,column=32, padx=2,pady=20)

EditButton = tki.Button(MainWindow,text="Редактирование",width=20,height=3,command=lambda: openEditScreen(tree))
EditButton.grid(row=2,column=30, padx=2,pady=20, columnspan=2)


AddButton = tki.Button(MainWindow,text="Добавить",width=20,height=3,command= lambda: openAddScreen(tree))
AddButton.grid(row=2,column=29, padx=2,pady=20)

SaveButton = tki.Button(MainWindow,text="Сохранить",width=20,height=3,command= lambda: save())
SaveButton.grid(row=26,column=30, padx=2,pady=20, columnspan=2)

QB = tki.Button(MainWindow,text="Количественный отчёт",width=20,height=3, command= lambda : openQuant(tree))
QB.grid(row=20,column=31, padx=30,pady=20)

GB = tki.Button(MainWindow,text="Качественный отчёт",width=25,height=3, command= lambda : openQual(tree))
GB.grid(row=20,column=32, padx=32,pady=20)

PivotButton = tki.Button(MainWindow,text="Сводная таблица",width=20,height=3, command= lambda: open_pivottable(tree))
PivotButton.grid(row=20,column=30, padx=2,pady=20)

GraphButton = tki.Button(MainWindow, text="Построить график", width=25, height=3, command=lambda:openGraphMenu(tree))
GraphButton.grid(row=20,column=29, padx=2,pady=20)

MainWindow.mainloop()
