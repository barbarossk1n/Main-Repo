''' 
==========================================================================================
ИМПОРТИРУЕМ ФАЙЛ С БИБЛИОТЕКАМИ
==========================================================================================
'''
import os           # <- работа с директорией
import sys          # <- работа с директорией
import json         # <- работа с файлами формата .json
import datetime     # <- работа с датами и временем
import platform     # <- работа с ОС (для проверки типа ОС)
import subprocess   # <- работа с процессами компьютера (в том числе установка новых библиотек)



''' 
==========================================================================================
КЛАСС РАБОТЫ С ДИРЕКТОРИЯМИ
==========================================================================================
'''
class JsonSimplification():
    
    # -----------------------------------------------------------------------------------
    ''' ОБЯЗАТЕЛЬНЫЕ ПАРАМЕТРЫ НА ВВОД '''
    def __init__(self):
        
        # Проверка на ОС для выбора формата поиска директорий
        if 'win' in platform.platform().lower():
            self.delimiter = '\\'
        else:
            self.delimiter = '/'
        
        # Директории расположения файлов
        self.directory = os.getcwd()
        if 'notebooks' in self.directory:
            self.notebooks = self.directory
            
            self.data = self.notebooks.replace('notebooks', 'data')
            self.source = self.notebooks.replace('notebooks', 'source')
            self.components = self.notebooks.replace('notebooks', 'components')
        elif 'source' in self.directory:
            self.source = self.directory
            
            self.data = self.source.replace('source', 'data')    
            self.components = self.source.replace('source', 'components')
            self.notebooks = self.source.replace('source', 'notebooks')
        else:
            raise ValueError('Похоже, структура директории нарушена...\n \
                              Пожалуйста, проверьте расположение файлов.')

    
    # -----------------------------------------------------------------------------------
    ''' ФУНКЦИЯ СОХРАНЕНИЯ СЛОВАРЯ В JSON-ФАЙЛ '''
    # На вход принимает словарь, состоящий из следующих параметров:
    # - filename_prefix: наименование параметра, по которому совершался запрос для парсинга;
    # - type_search: тип запроса на сайт;
    # - region: регион, для которого делался запрос;
    # - data: непосредственно словарь с данными, который нужно сохранить; 
    # - date: дата, на которую делался запрос;
    def _save_to_json(self, info_dictionary: dict):
        
        # Смена директории на ту, куда будет выгружаться созданный json-файл
        os.chdir(self.components)
        
        # Введение параметров из словаря
        filename_prefix = info_dictionary['filename_prefix']
        type_search = info_dictionary['type_search']
        region = info_dictionary['region']
        data = info_dictionary['data']
        date = info_dictionary['date']
        
        # Процесс формирования наименования файла
        timestamp = datetime.now().strftime('%y%m%d')
        filename = f'{filename_prefix}_{region}_{type_search}_td{date}_qd{timestamp}.json'
        
        # Сохранение файла
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    

    ''' ФУНКЦИЯ ВЫГРУЗКИ ДАННЫХ ИЗ JSON-ФАЙЛА'''
    # Аналогично с процедурой сохранения данных в формат json
    def _load_from_json(self, info_dictionary: dict) -> dict:
        
        # Смена директории на ту, куда будет выгружаться созданный json-файл
        os.chdir(self.components)
        
        # Введение параметров из словаря
        filename_prefix = info_dictionary['filename_prefix']
        type_search = info_dictionary['type_search']
        region = info_dictionary['region']
        date = info_dictionary['date']
        
        # Процесс формирования наименования файла
        timestamp = datetime.now().strftime('%y%m%d')
        filename = f'{filename_prefix}_{region}_{type_search}_td{date}_qd{timestamp}.json'
        
        # Выгрузка данных
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            print(f'Файл {filename} найден.')
            return data
        
        except FileNotFoundError:
            print(f'Файл {filename} не найден.')
            return {}
        