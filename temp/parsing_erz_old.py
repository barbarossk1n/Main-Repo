# ''' 
# ==========================================================================================
# ИМПОРТИРУЕМ ФАЙЛЫ С БИБЛИОТЕКАМИ И КОНСТАНТАМИ 
# ==========================================================================================
# '''
# ---
# ---
# ---
# ---


# ''' 
# ==========================================================================================
# КЛАСС ОБРАБОТКИ ДАННЫХ И СОЗДАНИЯ ТАБЛИЦ
# ==========================================================================================
# '''
# class Data_Transform():
    
#     def __init__(self):
        
#         # Предобработка директорий
#         self.directory = os.getcwd()
#         self.components = self.directory + '/components' if 'source' not in self.directory else self.directory

    
#     ''' ФУНКЦИЯ ИМПОРТА ФАЙЛА JSON ''' 
#     def _import_json(self, filename: str):
#         filepath = os.path.join(self.components, f'{filename}.json')
#         try:
#             with open(filepath, 'r', encoding='utf-8') as f:
#                 data = json.load(f)
#             return data
#         except FileNotFoundError:
#             print(f'Файл {filename}.json не найден в папке components.')
#             return None
    
    
#     ''' МЕТОД ИЗВЛЕЧЕНИЯ ПАРАМЕТРОВ ИЗ ВСЕХ СЛОВАРЕЙ ''' 
#     def extract_data(self, developers: dict, estates: dict, complexes: dict):
        
#         # Выгрузка словарей
#         self.developers = self._import_json(developers)
#         self.estates = self._import_json(estates)
#         self.complexes = self._import_json(complexes)
        
#         # Создание пустого списка для хранения данных таблицы
#         table_data = []
        
#         # Находим максимальное количество значений в списках параметров продаж
#         max_sales_params = 1 
#         for group_name, dev_dict in self.developers.items():
#             for dev_name, _ in dev_dict.items():
#                 for est_name in self.estates.get(dev_name, {}).keys() - {'id СЗ'}:
#                     est_data = self.complexes.get(est_name, {})
#                     sales_data = est_data.get('Общее', {}).get('Продажи', {})
                    
#                     for param_name, param_values in sales_data.items():
#                         if isinstance(param_values, list):
#                             max_sales_params = max(max_sales_params, len(param_values))
        
#         # Итерация по группам
#         for group_name, dev_dict in self.developers.items():
            
#             # Итерация по СЗ внутри группы
#             for dev_name, _ in dev_dict.items():
                
#                 # Получение информации по СЗ
#                 dev_id = self.estates.get(dev_name, {}).get('id')
                
#                 for est_name in self.estates.get(dev_name, {}).keys() - {'id'}:
#                     est_data = self.complexes.get(est_name, {})
#                     row_data = {
#                                 'Название ГК': group_name,
#                                 'Название СЗ': dev_name,
#                                 'ID': dev_id,
#                                 'ЖК': est_name
#                                 }
                
#                     # Обработка данных из "Общее" и "Продажи"
#                     for key, value in est_data.get('Общее', {}).items():
#                         if key != 'Продажи':
#                             row_data[key] = value
                            
#                     sales_data = est_data.get('Общее', {}).get('Продажи', {})
#                     for i in range(max_sales_params):
#                         for param_name, param_values in sales_data.items():
#                             if param_name == 'Квартиры на дату':
#                                 date_str = self._get_value(sales_data, 'Квартиры на дату')
#                                 if date_str:
#                                     try:
#                                         date_obj = pd.to_datetime(date_str, format='%d.%m.%Y')
#                                         row_data['Квартиры на дату'] = date_obj.strftime('%m.%Y')
                                    
#                                     except ValueError:
#                                         row_data['Квартиры на дату'] = date_str

#                             else:
#                                 row_data[param_name] = param_values
                        
#                     # Обработка данных корпусов
#                     for complex_name, complex_data in est_data.items():
#                         if complex_name not in ['Общее', 'Продажи']:
#                             row_data['Корпус'] = complex_name
#                             for key, value in complex_data.items():
#                                 row_data[key] = value
                            
#                             table_data.append(row_data.copy()) 
                            
#                     if not any(k for k in est_data.keys() if k not in ['Общее', 'Продажи']):
#                         table_data.append(row_data.copy())

#         df = pd.DataFrame(table_data)
#         df.to_csv('test.csv', index=False)
                
                
                
                

# '''
# ==========================================================================================
# ЗАПУСКАЕМ КЛАСС ИЗВЛЕЧЕНИЯ СЛОВАРЕЙ
# ==========================================================================================
# '''
# name_groups = 'grps_moskva_vol_now_bld_td240901_qd240911'
# name_developers = 'dvls_moskva_vol_now_bld_td240901_qd240911'
# name_estates = 'ests_moskva_vol_now_bld_td240901_qd240912'
# name_complexes = 'crps_moskva_vol_now_bld_td240901_qd240912'

# data_import = Data_Transform()
# data_import.extract_data(name_developers, name_estates, name_complexes)
        