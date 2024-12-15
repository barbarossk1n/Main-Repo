
# Дефолтные библиотеки (в том числе для установки остальных)
from datetime import datetime   # <- работа с датами
import datetime as dt
from time import sleep          # <- работа со временем (если нужно сделать временную остановку во время выполнения кода)

# Библиотеки для работы с данными
import pandas as pd

# Библиотеки для визуализации
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
import seaborn as sns

# Библиотеки для парсинга (без открытия браузера)
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests

# Библиотеки для парсинга (с открытием браузера)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options                         # <- для настройки параметров браузера 
from selenium.webdriver.chrome.service import Service as ChromeService        # <- для настройки параметров браузера 
from selenium.webdriver.common.by import By                                   # <- для поиска элемента по условию (кнопки прогрузки)
from selenium.webdriver.support.ui import WebDriverWait                       # <- таймер для браузера
from selenium.webdriver.support import expected_conditions as EC              # <- для ожидания определенных условий на странице
from selenium.common.exceptions import TimeoutException, WebDriverException   # <- чтобы избежать ошибки в случае истечения времени

# Библиотека для автоматического обновления/скачивания/удаления драйвера
from webdriver_manager.chrome import ChromeDriverManager
