''' 
==========================================================================================
ПРЕДОБРАБОТКА
==========================================================================================
'''
# Импорт библиотек
from data.load_data import *
from utils.libraries_apply import *

# Класс для работы директории
json_work = JsonSimplification()




''' 
==========================================================================================
КЛАСС ИНСТРУМЕНТОВ ДЛЯ ПАРСИНГА
==========================================================================================
'''
class Parsing():
    
    # -----------------------------------------------------------------------------------
    # ''' ИНИЦИАЛИЗИРУЕТ ДРАЙВЕР SELENIUM В HEADLESS РЕЖИМЕ '''
    ''' ПРЕДВАРИТЕЛЬНАЯ ПОДГОТОВКА '''
    def __init__(self, headless = True):
        
        # Инициируем настройки для хрома
        chrome_options = Options()
            
        if headless:
            chrome_options.add_argument("--headless=new")  # <-- Фоновый режим
            chrome_options.add_argument("--disable-gpu")   # <-- Отключение GPU (для headless)
            chrome_options.add_argument("--no-sandbox")    # <-- Отключение sandbox (для некоторых систем)
        
        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service = service, options = chrome_options)
    
    
    ''' ФУНКЦИЯ ОТКРЫТИЯ ВЕБ-СТРАНИЦЫ ДЛЯ ПАРСИНГА (БЕЗ ОТКРЫТИЯ) '''
    def _link_get(self, link: str) -> object:
        
        # Отправляем запрос на запуск функции
        req = Request(
                    url=link,
                    headers={'User-Agent': 'Mozilla/5.0'}
                    )
        webpage = urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(webpage, 'html.parser')
        
        return soup
    
    
    ''' ФУНКЦИЯ НЕСКОЛЬКИХ ПОПЫТОК И ОБРАБОТКИ ОШИБОК '''
    def _process_retry(self, func, *args, retries = 3, **kwargs):
        
        # Запуск цикла попытки реализации функции (парсинга)
        for attempt in range(1, retries + 1):
            try:
                return func(*args, **kwargs)
            
            except (TimeoutException, WebDriverException) as e:
                print(f'Ошибка при загрузке данных: {e}')
                print(f'Попытка {attempt} из {retries}...')
                
                if attempt < retries:
                    sleep(2 ** attempt) # <-- Экспоненциальная задержка между попытками
                else:
                    raise               # <-- Поднимаем исключение, если все попытки неудачны 
