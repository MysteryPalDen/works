import tkinter as tki
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt

"""
Конфигурационный файл
By Асташов С.Д.
"""
HD_RES = "1280x720"
MAIN_WIN_TITLE = "Анализ ноутбуков"

path = ""
data=pd.read_csv("../Data/laptop_price.csv",encoding="ISO-8859-1")
data['laptop_ID'] = data['laptop_ID'].astype(int)
data['Inches'] = data['Inches'].astype(float)
data['Price_euros'] = data['Price_euros'].astype(float)
