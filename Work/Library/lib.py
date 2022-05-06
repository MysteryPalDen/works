import os, sys
import tkinter as tki
from settings import *

def fetch(data, x):
    """
    Returns a list containing the attributes of an element with a given id
    By Скриплёнок М. С.
    """
    y = data.loc[data['laptop_ID'] == x]
    for i in y.iterrows():
        return list(list(i)[1])

def searchData(company,price,ram,weight,diagonal,filename):
    """
    Searches data based on the specified parameters
    By Скриплёнок М. С.
    """
    global data
    price = list(map(int,price))
    ram = list(map(int,ram))
    weight = list(map(int,weight))
    diagonal = list(map(int,diagonal))

    names = data.columns
    newData = pd.DataFrame(columns=names)
    for t in data.iterrows():
        x=t[1]
        if(x['Company']==company and
           x['Price_euros']>=price[0] and x['Price_euros']<=price[1] and
           int(x['Ram'].split('G')[0])>=ram[0] and int(x['Ram'].split('G')[0])<=ram[1] and
           float(x['Weight'].split('k')[0])>=weight[0] and float(x['Weight'].split('k')[0])<=weight[1] and
           x['Inches']>=diagonal[0] and x['Inches']<=diagonal[1]):
            newDict={}
            n=0
            for i in names:
                newDict[i]=x[n]
                n+=1
            newData=newData.append(newDict,ignore_index=True)

    newData.to_excel('../Output/' + filename + ".xlsx", index=False)


def openSearch():
    """
    Creates and opens the search settings window
    By Скриплёнок М. С.
    """
    ConfigWindow = tki.Toplevel()
    ConfigWindow.resizable(height = False, width = False)

    SearchLabel = tki.Label(ConfigWindow, text="Настройки поиска",font="Times 16 bold")
    SearchLabel.grid(row=0,column=0, columnspan=2)

    BrandLabel = tki.Label(ConfigWindow, text="Фирма:",width=9)
    BrandLabel.grid(row=1,column=0, padx=30, pady=10)

    BrandInput = ttk.Combobox(ConfigWindow, values=list(data['Company'].unique()), state="readonly", width=9)
    BrandInput.current(0)
    BrandInput.grid(row=1,column=1, pady=10, columnspan=2)

    PriceLabel = tki.Label(ConfigWindow, text="Цена:")
    PriceLabel.grid(row=2,column=0, pady=10)

    MinPriceInput =tki.Entry(ConfigWindow, width=5)
    MinPriceInput.grid(row=2,column=1, padx=5)
    MinPriceInput.insert(0, '0')

    MaxPriceInput = tki.Entry(ConfigWindow, text='6100', width=5)
    MaxPriceInput.grid(row=2,column=2,padx=5)
    MaxPriceInput.insert(0, '6100')

    RamLabel = tki.Label(ConfigWindow, text="Оперативная память:")
    RamLabel.grid(row=3,column=0, pady=10)

    MinRamInput =tki.Entry(ConfigWindow, width=5)
    MinRamInput.grid(row=3,column=1, padx=5)
    MinRamInput.insert(0, '0')

    MaxRamInput = tki.Entry(ConfigWindow, text='64', width=5)
    MaxRamInput.grid(row=3,column=2,padx=5)
    MaxRamInput.insert(0, '64')

    WeightLabel = tki.Label(ConfigWindow, text="Вес:")
    WeightLabel.grid(row=4,column=0, pady=10)

    MinWeightInput =tki.Entry(ConfigWindow, width=5)
    MinWeightInput.grid(row=4,column=1, padx=5)
    MinWeightInput.insert(0, '0')

    MaxWeightInput = tki.Entry(ConfigWindow, text='5', width=5)
    MaxWeightInput.grid(row=4,column=2,padx=5)
    MaxWeightInput.insert(0, '5')

    DiagonalLabel = tki.Label(ConfigWindow, text="Диагональ:")
    DiagonalLabel.grid(row=5,column=0, pady=10)

    MinDiagonalInput = tki.Entry(ConfigWindow, width=5)
    MinDiagonalInput.grid(row=5,column=1, padx=5)
    MinDiagonalInput.insert(0, '0')

    MaxDiagonalInput = tki.Entry(ConfigWindow, text='19', width=5)
    MaxDiagonalInput.grid(row=5,column=2,padx=5)
    MaxDiagonalInput.insert(0, '19')

    NameLabel = tki.Label(ConfigWindow, text="Вывод имени файла:")
    NameLabel.grid(row=6,column=0, pady=10)

    NameInput = tki.Entry(ConfigWindow, width=20)
    NameInput.grid(row=6,column=1, columnspan=3, padx=5)
    NameInput.insert(0, 'search')

    SearchButton_ = tki.Button(ConfigWindow,text="Search", fg="green",
                               command=lambda: searchData(BrandInput.get(),[MinPriceInput.get(),MaxPriceInput.get()],
                                                          [MinRamInput.get(),MaxRamInput.get()],
                                                          [MinWeightInput.get(),MaxWeightInput.get()],
                                                          [MinDiagonalInput.get(),MaxDiagonalInput.get()],
                                                          NameInput.get()))
    SearchButton_.grid(row=7,column=0,columnspan=3)

def openAddScreen(tree):
    """
    Creates and opens the element addition screen
    By Скриплёнок М. С.
    """
    global data
    names = list(data.columns)[1:]

    AddWindow = tki.Toplevel()
    AddWindow.resizable(height = False, width = False)

    entries=[]
    labels=[]
    curRow=curColumn=0
    for i in range(len(names)):
        labels.append(tki.Label(AddWindow, text=names[i],font="Times 16"))
        labels[-1].grid(row=curRow,column=curColumn,pady=10,padx=40)
        entries.append(tki.Entry(AddWindow))
        entries[-1].grid(row=curRow+1,column=curColumn)

        curRow+=2
        if((i+1)%3==0):
            curRow=0
            curColumn+=1

    _AddButton=tki.Button(AddWindow,text="Добавить",width=15,height=2, font="Times 18 bold",command = lambda: [addElement([i.get() for i in entries]), updateTable(tree)])
    _AddButton.grid(row=10,column=1,columnspan=2,pady=30)

def setText(e, text):
    """
    Changes entry text
    By Скриплёнок М. С.
    """
    e.delete(0,tki.END)
    e.insert(0,text)

def fetchClick(entries,x,data):
    """
    Fills a list of entries with values from a list of values
    By Скриплёнок М. С.
    """
    values = fetch(data, x)[1:]
    n=0
    for i in entries:
        setText(i,values[n])
        n+=1


def editClick(x, newValues):
    """
    Edits data
    By Скриплёнок М. С.
    """
    global data
    newLst=[]
    newLst.append(x)
    for i in newValues:
        newLst.append(i)
    data.loc[data['laptop_ID'] == x] = newLst

def openEditScreen(tree):
    """
    Creates and opens the edit menu
    By Скриплёнок М. С.
    """
    global data
    names = list(data.columns)[1:]

    EditWindow = tki.Toplevel()
    EditWindow.resizable(height = False, width = False)

    entries=[]
    labels=[]
    curRow=1
    curColumn=0

    IdLabel = tki.Label(EditWindow, text="Id для изменения:", font="Times 18 bold")
    IdLabel.grid(row=0,column=0,pady=10,padx=40)

    IdEntry = tki.Entry(EditWindow, width=5, font="Times 18 bold")
    IdEntry.grid(row=0,column=1,sticky='W')


    for i in range(len(names)):
        labels.append(tki.Label(EditWindow, text=names[i],font="Times 16"))
        labels[-1].grid(row=curRow,column=curColumn,pady=10,padx=40)
        entries.append(tki.Entry(EditWindow))
        entries[-1].grid(row=curRow+1,column=curColumn)

        curRow+=2
        if((i+1)%3==0):
            curRow=1
            curColumn+=1
    FetchButton = tki.Button(EditWindow, text="Получить",command = lambda: fetchClick(entries,int(IdEntry.get()),data))
    FetchButton.grid(row=0,column=2,sticky='W')

    _EditButton=tki.Button(EditWindow,text="Подтвердить",width=15,height=2, font="Times 18 bold", fg="green",command=lambda:[ editClick(int(IdEntry.get()),[i.get() for i in entries]), updateTable(tree)])
    _EditButton.grid(row=10,column=1,columnspan=2,pady=30)

def openDeleteScreen():
    """
    Creates and opens the edit menu
    By Палуха Д. В.
    """

    DeleteWindow = tki.Toplevel()
    DeleteWindow.resizable(height = False, width = False)

    DeleteLabel = tki.Label(DeleteWindow, text="Удалить по ID", font="Times 18 bold")
    DeleteLabel.grid(row=0,column=0,columnspan=2)

    IdLabel = tki.Label(DeleteWindow, text="ID:", font="Times 18")
    IdLabel.grid(row=1,column=0,pady=20)

    IdEntry=tki.Entry(DeleteWindow, font="Times 18", width=5)
    IdEntry.grid(row=1,column=1,padx=20)

    DeleteButton=tki.Button(DeleteWindow,text="Delete", font="Times 18",fg='red',command=lambda: IdEntry.delete(0,tki.END))
    DeleteButton.grid(row=2,column=0,columnspan=2,pady=10);


def sortData(data, key):
    """
    Sorts data using smart algorithms
    By Скриплёнок М. С.
    """
    if (key in ['laptop_ID', 'Company', 'Product', 'TypeName', 'Inches', 'Gpu', 'OpSys', 'Price_euros']):
        newData = data.sort_values(by=[key])
    elif (key=='ScreenResolution'):
        newData = data.sort_values(by=['ScreenResolution'], key = lambda x: x.apply(convertResolution))
    elif (key=='Cpu'):
        newData = data.sort_values(by=['Cpu'], key = lambda x: x.apply(convertCPU))
    elif (key=='Ram'):
        newData = data.sort_values(by=['Ram'], key = lambda x: x.apply(convertWeightRam))
    elif (key=='Weight'):
        newData = data.sort_values(by=['Weight'], key = lambda x: x.apply(convertWeightRam))
    elif (key=='Memory'):
        newData = data.sort_values(by=['Memory'], key = lambda x: x.apply(convertMemory))
    return newData


def removeElement(x):
    """
    Removes entry from a table
    By Скриплёнок М. С.
    """
    global data
    data.drop(data.index[(data["laptop_ID"] == x)],axis=0,inplace=True)

def addElement(attributes):
    """
    Adds entry to a table
    By Скриплёнок М. С.
    """
    global data
    names = data.columns[1:]
    newDict={}
    newDict['laptop_ID']=getNextId(data)
    n=0
    for i in names:
        newDict[i]=attributes[n]
        n+=1
    data.append(newDict,ignore_index=True,inplace=True)


def createTable(tree):
    """
    Fills treeview with data from the dataframe
    By Скриплёнок М. С.
    """
    global data
    names = data.columns
    tree['show'] = 'headings'
    tree["columns"] = tuple(names)

    for i in names:
        tree.column(i, width=100)
        tree.heading(i, text=i)

    for i in data.iterrows():
        tree.insert("", tki.END, values=(list(i[1])))

def updateTable(tree):
    """
    Fills treeview with new data
    By Скриплёнок М. С.
    """
    global data
    names = data.columns
    for item in tree.get_children():
        tree.delete(item)

    for i in names:
        tree.column(i, width=100)
        tree.heading(i, text=i)

    for i in data.iterrows():
        tree.insert("", tki.END, values=(list(i[1])))

def sortTable(tree, key):
    """
    Sorts data by the given key and puts it in a treeview
    By Скриплёнок М. С.
    """
    global data
    data = sortData(data,key)
    updateTable(tree)
    return data


def convertWeightRam(s):
    """
    Parses weight and ram data
    By Асташов С. Д.
    """
    return float(s[:-2])

def convertCPU(s):
    """
    Returns the frequency of a CPU using the CPU data
    By Палуха Д. В.
    """
    a = s.split(' ')
    for i in a:
        if('GHz' in i):
            return float(i[:-3])

def convertResolution(s):
    """
    Parses resolution data
    By Скриплёнок М. С.
    """
    a = s.split(' ')
    for i in a:
        if('x' in i):
            l = i.split('x')
            return int(l[0])*int(l[1])

def convertMemory(s):
    """
    Converts a string with memory data into an integer representing the total memory
    By Скриплёнок М. С.
    """
    ans = 0
    l = s.split(' ')
    for i in l:
        if(i[-2:]=='GB'):
            ans+=float(i[:-2])
        if(i[-2:]=='TB'):
            ans+=1024*float(i[:-2])
    return ans

def removeElement(x):
    """
    Removes entry from a table
    By Скриплёнок М. С.
    """
    global data
    data.drop(data.index[(data["laptop_ID"] == x)],axis=0,inplace=True)

def addElement(attributes):
    """
    Adds entry to a table
    By Скриплёнок М. С.
    """
    global data
    names = data.columns[1:]
    newDict={}
    newDict['laptop_ID']=getNextId(data)
    n=0
    for i in names:
        newDict[i]=attributes[n]
        n+=1
    data = data.append(newDict,ignore_index=True)


def createTable(tree):
    """
    Fills treeview with data from the dataframe
    By Скриплёнок М. С.
    """
    global data
    names = data.columns
    tree['show'] = 'headings'
    tree["columns"] = tuple(names)

    for i in names:
        tree.column(i, width=80)
        tree.heading(i, text=i)

    for i in data.iterrows():
        tree.insert("", tki.END, values=(list(i[1])))

def updateTable(tree):
    """
    Fills treeview with new data
    By Скриплёнок М. С.
    """
    global data
    names = data.columns
    for item in tree.get_children():
        tree.delete(item)

    for i in names:
        tree.column(i, width=100)
        tree.heading(i, text=i)

    for i in data.iterrows():
        tree.insert("", tki.END, values=(list(i[1])))

def sortTable(tree, key):
    """
    Sorts data by the given key and puts it in a treeview
    By Скриплёнок М. С.
    """
    global data
    data = sortData(data,key)
    updateTable(tree)
    return data

def getNextId(data):
    """
    Finds the smallest unoccupied id
    By Палуха Д. В.
    """
    newData=sortData(data, 'laptop_ID')
    n=0
    for i in newData.iterrows():
        n+=1
        x = i[1]
        if(int(x['laptop_ID']) != n):
              return n
    return n+1

def notify_send(msg):
    """
    Функция для создания уведомлений
    Автор Асташов С.Д.
    """
    global data
    ConfigWindow = tki.Toplevel()
    ConfigWindow.resizable(height = False, width = False)
    #ConfigWindow.geometry("800x600")
    SearchLabel = tki.Label(ConfigWindow, text=msg, font="Times 16 bold")
    SearchLabel.grid(row=0,column=0, columnspan=2)

    ApplyButton = tki.Button(ConfigWindow, text='Ок', command=lambda:ConfigWindow.destroy())
    ApplyButton.grid(row=2, column=0,padx=10,pady=10)

def open_pivottable(tree):
    """
    Функция для создания сводной таблицы
    Автор Асташов С.Д.
    """
    global data
    ConfigWindow = tki.Toplevel()
    ConfigWindow.resizable(height = False, width = False)
    ConfigWindow.geometry("800x600")

    SearchLabel = tki.Label(ConfigWindow, text="Параметры сводной таблицы", font="Times 16 bold")
    SearchLabel.grid(row=0,column=0, columnspan=2)

    qualityVars = ['Company','Product','TypeName','ScreenResolution','Cpu','Ram','Gpu','OpSys']

    BrandInput = ttk.Combobox(ConfigWindow, values=qualityVars, state="readonly", width=60)
    BrandInput.current(0)
    BrandInput.grid(row=3,column=3, pady=10, columnspan=20)

    BrandInput2 = ttk.Combobox(ConfigWindow, values=qualityVars, state="readonly", width=60)
    BrandInput2.current(0)
    BrandInput2.grid(row=10,column=3, pady=10, columnspan=20)

    functions = ['max', 'min', 'sum']

    Func= ttk.Combobox(ConfigWindow, values=functions, state="readonly", width=60)
    Func.current(0)
    Func.grid(row=17,column=3, pady=10, columnspan=20)

    ApplyButton = tki.Button(ConfigWindow, text='Подтвердить', command=lambda:generate_pivot_table(data,BrandInput.get(), BrandInput2.get(), Func.get()))
    ApplyButton.grid(row=2, column=0,padx=10,pady=10)

def generate_pivot_table(data, index_, values_, aggfunc_):
    """
    Функция создания сводной таблицы
    By Асташов С.Д.
    """
    if index_ == values_:
        #tki.messagebox.showinfo("Неверный набор параметров")
        notify_send("Неверный набор параметров")
    else:
        table = pd.pivot_table(data, index = index_, values = values_, aggfunc = aggfunc_)
        table.to_excel('../Output/pivottable_' +str(index_) + "_" + str(values_) + '_' + str(aggfunc_)+  '.xlsx')

def save():
    """
    Saves table
    By Палуха Д. В.
    """
    global data
    data.to_csv('../Data/laptop_price.csv', index=False)

def createReport(param):
    """
    Creates a report table given a parameter
    By Скриплёнок М.С.
    """
    global data
    qualityVars = ['Company','Product','TypeName','ScreenResolution','Cpu','Ram','Gpu','OpSys']
    quantityVars=['Inches','Weight','Price_euros']
    if param in qualityVars:
        count = data[param].value_counts()
        total = count.sum()
        percentage = []
        for  i in count:
            percentage.append(100*i/total)
        outputData={ param: list(data[param].unique()),
                    'Count': count.tolist(),
                    '%': percentage}
        outputTable = pd.DataFrame(outputData)
        #outputTable.to_excel('../Output/pivottable.xlsx',index=False)
        outputTable.to_excel('../Output/' +  param + '.xlsx',index=False)

def quantReport(holder):
    """
    createReport для количественных данных
    Принимает список
    By Асташов С.Д.
    """
    global data
    newdata = data.copy()
    newdata['Weight'] = newdata['Weight'].apply(lambda x :convertWeightRam(x))
    print("kek")
    qualityVars = ['Company','Product','TypeName','ScreenResolution','Cpu','Ram','Gpu','OpSys']
    quantityVars=['Inches','Weight','Price_euros']
    name, one, two, three, four, five = [list() for i in range(6)]
    for param in holder:
        if param in quantityVars:
            _max = newdata[param].max()
            _min = newdata[param].min()
            _mean = newdata[param].mean()
            pillar = newdata[param].value_counts()
            _sum = 0
            for i in pillar:
                _sum += ( i - _mean ) ** 2
            _bias = (1/(len(pillar)-1) * _sum)**0.5
            _disp = _bias ** 2
            name.append(param)
            one.append(_max)
            two.append(_min)
            three.append(_mean)
            four.append(_disp)
            five.append(_bias)
    outdata = {
        'name' : name,
        'max' : one,
        'min' : two,
        'mean' : three,
        'dispersion' : four,
        'bias' : five
    }
    outtable = pd.DataFrame(outdata)
    outtable.to_excel('../Output/' + "quantitative" + '.xlsx', index=False)

def openQuant(tree):
    """
    Открывает страницу выбора количественных параметров
    Автор Асташов С.Д.
    """
    global data
    quantityVars=['Inches','Weight','Price_euros']
    window = tki.Toplevel()
    window.resizable(False, False)
    aa, bb, cc = tki.IntVar(), tki.IntVar(), tki.IntVar()
    arr = [aa, bb, cc]
    a = tki.Checkbutton(window, text="Inches", variable=aa)
    a.pack()
    b = tki.Checkbutton(window, text="Weight", variable=bb)
    b.pack()
    c = tki.Checkbutton(window, text='Price_euros', variable=cc)
    c.pack()
    d = tki.Button(window, text="Построить", command=lambda : [getQuant(aa, bb, cc), window.destroy(), window.update()])
    d.pack()

def getQuant(aa, bb, cc):
    """
    Обрабатывает кнопки openQuant
    Автор Асташов С.Д.

    """
    quantityVars=['Inches','Weight','Price_euros']
    holder = list()
    if aa.get() == 1:
        holder.append("Inches")
    if bb.get() == 1:
        holder.append("Weight")
    if cc.get() == 1:
        holder.append("Price_euros")
    quantReport(holder)

def qualityReport(params):
    """
    Creates a report table given a parameter
    By Скриплёнок М.С.
    """
    global data
    qualityVars = ['Company','Product','TypeName','ScreenResolution','Cpu','Ram','Gpu','OpSys']
    for param in params:
        count = data[param].value_counts()
        total = count.sum()
        percentage = []
        for  i in count:
            percentage.append(100*i/total)
        outputData={ param: list(data[param].unique()),
                    'Count': count.tolist(),
                    '%': percentage}
        outputTable = pd.DataFrame(outputData)
        #outputTable.to_excel('../Output/pivottable.xlsx',index=False)
        outputTable.to_excel('../Output/report' +  param + '.xlsx',index=False)

def openQual(tree):
    """
    Открывает страницу выбора качественных переменных
    Автор Асташов С.Д.
    """
    global data
    window = tki.Toplevel()
    window.resizable(False, False)
    aa, bb, cc, dd, ee, ff, gg, hh = tki.IntVar(), tki.IntVar(), tki.IntVar(), tki.IntVar(), tki.IntVar(), tki.IntVar(), tki.IntVar(), tki.IntVar()
    a = tki.Checkbutton(window, text="Company", variable=aa)
    a.pack()
    b = tki.Checkbutton(window, text="Product", variable=bb)
    b.pack()
    c = tki.Checkbutton(window, text='TypeName', variable=cc)
    c.pack()
    d = tki.Checkbutton(window, text='ScreenResolution', variable=dd)
    d.pack()
    e = tki.Checkbutton(window, text='Cpu', variable=ee)
    e.pack()
    f = tki.Checkbutton(window, text='Ram', variable=ff)
    f.pack()
    g = tki.Checkbutton(window, text='Gpu', variable=gg)
    g.pack()
    h = tki.Checkbutton(window, text='OpSys', variable=hh)
    h.pack()

    x = tki.Button(window, text="Построить", command=lambda : [getQual(aa, bb, cc, dd, ee, ff, gg, hh), window.destroy(), window.update()])
    x.pack()

def getQual(aa, bb, cc, dd, ee, ff, gg, hh):
    """
    Обрабатывает кнопки для количественных переменных
    Автор Асташов С.Д.

    """
    holder = list()
    if aa.get() == 1:
        holder.append("Company")
    if bb.get() == 1:
        holder.append("Product")
    if cc.get() == 1:
        holder.append("TypeName")
    if dd.get() == 1:
        holder.append("ScreenResolution")
    if ee.get() == 1:
        holder.append("Cpu")
    if ff.get() == 1:
        holder.append("Ram")
    if gg.get() == 1:
        holder.append("Gpu")
    if hh.get() == 1:
        holder.append("OpSys")

    qualityReport(holder)

def openGraphMenu(tree):
    """
    Автор Асташов С.Д.
    """
    ConfigWindow = tki.Toplevel()
    ConfigWindow.resizable(height = False, width = False)
    ConfigWindow.geometry("800x600")

    SearchLabel = tki.Label(ConfigWindow, text="Выбор типа графика", font="Times 16 bold")
    SearchLabel.grid(row=0,column=0, columnspan=2)

    #BrandLabel = tki.Label(ConfigWindow, text=":",width=9)
    #BrandLabel.grid(row=1,column=0, padx=10, pady=10)

    values_holder = ['Количественный-качественный с категоризированной гистограммой', 'Количественный-качественный Бокса-Вискера','2 количественных и один качественный с диаграммой рассеивания']
    BrandInput = ttk.Combobox(ConfigWindow, values=values_holder, state="readonly", width=60)
    BrandInput.current(0)
    BrandInput.grid(row=3,column=3, pady=10, columnspan=20)
    ApplyButton = tki.Button(ConfigWindow, text='Подтвердить', command=lambda:getGraphType(BrandInput.get()))
    ApplyButton.grid(row=2, column=0,padx=10,pady=10)

def getGraphType(value):
    """
    Автор Асташов С.Д.
    """
    print(value)
    if value == 'Количественный-качественный с категоризированной гистограммой':
        openltMenu()
    if value == 'Количественный-качественный Бокса-Вискера':
        openltboxMenu()
    if value == '2 количественных и один качественный с диаграммой рассеивания':
        open2tlMenu()

def openltMenu():
    """
    Функция для создания графика первого типа
    Автор Асташов С.Д.
    """
    global data
    ConfigWindow = tki.Toplevel()
    ConfigWindow.resizable(height = False, width = False)
    ConfigWindow.geometry("800x600")

    SearchLabel = tki.Label(ConfigWindow, text="Параметры графика", font="Times 16 bold")
    SearchLabel.grid(row=0,column=0, columnspan=2)

    qualityVars = ['Company','Product','TypeName','ScreenResolution','Cpu','Ram','Gpu','OpSys']
    quantityVars=['Inches','Weight','Price_euros']

    BrandInput = ttk.Combobox(ConfigWindow, values=qualityVars, state="readonly", width=60)
    BrandInput.current(0)
    BrandInput.grid(row=3,column=3, pady=10, columnspan=20)

    BrandInput2 = ttk.Combobox(ConfigWindow, values=quantityVars, state="readonly", width=60)
    BrandInput2.current(0)
    BrandInput2.grid(row=10,column=3, pady=10, columnspan=20)

    ApplyButton = tki.Button(ConfigWindow, text='Подтвердить', command=lambda:qualQuantGraph([BrandInput.get(), BrandInput2.get()]))
    ApplyButton.grid(row=2, column=0,padx=10,pady=10)
    
def open2tlMenu():
    """
    Функция для создания графика первого типа
    Автор Палуха Д.В.
    """
    global data
    ConfigWindow = tki.Toplevel()
    ConfigWindow.resizable(height = False, width = False)
    ConfigWindow.geometry("800x600")

    SearchLabel = tki.Label(ConfigWindow, text="Параметры графика", font="Times 16 bold")
    SearchLabel.grid(row=0,column=0, columnspan=2)

    qualityVars = ['Company','Product','TypeName','ScreenResolution','Cpu','Ram','Gpu','OpSys']
    quantityVars=['Inches','Weight','Price_euros']

    BrandInput = ttk.Combobox(ConfigWindow, values=qualityVars, state="readonly", width=60)
    BrandInput.current(0)
    BrandInput.grid(row=3,column=3, pady=10, columnspan=20)

    BrandInput2 = ttk.Combobox(ConfigWindow, values=quantityVars, state="readonly", width=60)
    BrandInput2.current(0)
    BrandInput2.grid(row=10,column=3, pady=10, columnspan=20)
    
    BrandInput3 = ttk.Combobox(ConfigWindow, values=quantityVars, state="readonly", width=60)
    BrandInput3.current(0)
    BrandInput3.grid(row=11,column=3, pady=10, columnspan=20)

    ApplyButton = tki.Button(ConfigWindow, text='Подтвердить', command=lambda:twoqualQuantGraph([BrandInput.get(), BrandInput2.get(), BrandInput3.get()]))
    ApplyButton.grid(row=2, column=0,padx=10,pady=10)

def twoqualQuantGraph(params):
    """
    Creates a bar diagram for quality-quantity types of data
    By Палуха Д.В.
    """
    if params[1] == params[2]:
        notify_send("2 одинаковых параметра")
    else:
        global data
        newData = data.copy()
        newData['Weight'] = newData['Weight'].apply(lambda x :convertWeightRam(x))
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(x = newData[str(params[1])], y = newData[str(params[2])])
        plt.xlabel(str(params[1]))
        plt.ylabel(str(params[2]))
        plt.savefig("../Graphics/"+ str(params[0]) + '_' + str(params[1]) +  '_' + str(params[2]) +".png")
        notify_send("График пострен")

def qualQuantGraph(params):
    """
    Creates a bar diagram for quality-quantity types of data
    By Скриплёнок М.С.
    """
    global data
    newData = data.copy()
    newData['Weight'] = newData['Weight'].apply(lambda x :convertWeightRam(x))
    means = newData.groupby(params[0])[params[1]].mean()
    fig = means.plot(kind='bar', color='blue')
    fig.set_ylabel(params[1])
    plt.savefig("../Graphics/"+ str(params[0]) + '_' + str(params[1]) + ".png")
