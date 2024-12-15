
# ======================================================================================================
# ОБЩИЕ ПАРАМЕТРЫ ДЛЯ ССЫЛОК
DOMEN_ERZ = 'https://erzrf.ru'
DEFAULT_LINK_DEVELOPER = 'https://erzrf.ru/top-zastroyshchikov/{0}?topType={1}&date={2}'
DEFAULT_LINK_ZHK = 'https://erzrf.ru/top-novostroek/{0}?regionKey={1}&version=v2024&topType={2}&datePublication={3}&dateVersion=3&region={0}'

# ======================================================================================================
# СЛОВАРИ ДЛЯ СОХРАНЕНИЯ ЗНАЧЕНИЙ
TOP_TYPE_DEVELOPERS = {
                    '0': 'volume_ongoing_realestate',        # <- По объёму текущего строительства
                    '1': 'volume_commission_realestate',     # <- По объёму ввода жилья
                    '2': 'volume_quality_realestate',        # <- По потребительским качествам ЖК
                    '3': 'speed_build_realestate',           # <- По скорости строительства
                    '4': 'accumulate_commission_realestate'  # <- По накопленному вводу жилья (с 2016 г.)
                    }
TOP_TYPE_ZHK = {
                '0': 'consumer_quality',    # <- По потребительским качествам
                '1': 'project_scale'        # <- По масштабу проекта
                }

REGIONS_KEYS = {
                'moskva': '143443001'
                }

# ======================================================================================================
# ПАРАМЕТРЫ ДЛЯ ПОИСКА КОЛИЧЕСТВА ГК И СТРАНИЦ С ИХ ПЕРЕЧИСЛЕНИЕМ
TYPE_PAG_GK = 'p'
CLASS_PAG_GK = 'pagination__hint'
NUMBER_GROUPS = 20

TYPE_PAG_ZHK = 'p'
CLASS_PAG_ZHK = 'pagination__hint'
NUMBER_ZHK = 20

# ======================================================================================================
# ПАРАМЕТРЫ ДЛЯ ВЫГРУЗКИ НАЗВАНИЯ ГК И ЕЁ ССЫЛКИ
GC_HR_CL = 'span'
GC_CLASS = 'developer-td-3'                                 # <- наименование группы
GC_AREA = 'developer-td-4 ng-star-inserted'                 # <- площадь введённая/текущая, зависит от таблицы
GC_AREA_OTHER_DATE = 'developer-td-5 ng-star-inserted'      # <- площадь введённая/текущая с переносом даты РНВ, зависит от таблицы
GC_AREA_OD_PERCENT = 'developer-td-6 ng-star-inserted'      # <- для предыдущего параметра % от общей введённой/текущей, зависит от таблицы
GC_CLASS_SPD = 'developer-speed-td developer-speed-td-3'    # <- наименование группы в таблице скорости стройки
GC_BUILD_SPD = 'developer-speed-td developer-speed-td-4'    # <- скорость строительства
GC_VVOD_3YR = 'developer-speed-td developer-speed-td-5'     # <- введено МКД по ДДУ за 3 года
GC_AVG_AREA = 'developer-speed-td developer-speed-td-6'     # <- средняя S дома
GC_AVG_STAGE = 'developer-speed-td developer-speed-td-7'    # <- средняя этажность
GC_PARAMS = 'a'                                             # <- конкретный числовой показатель

# ======================================================================================================
# ПАРАМЕТРЫ ДЛЯ ВЫГРУЗКИ НАЗВАНИЯ ЖК И ЕГО ССЫЛКИ
ZHK_HR_CL = 'div'
ZHK_CLASS = 'td-3 p-10 ng-star-inserted'
# ZHK_PARAMS = 'a'

# ======================================================================================================
# ПАРАМЕТРЫ ДЛЯ ПОИСКА ПО ВЕБ-СТРАНИЦЕ ГК (ПОИСК СЗ)
BUTTON_GC_CLASS = "//a[@class='accordion__head collapsed']"
LIST_DEVELOPERS = "//div[@class='cmn_clmns text']//p[@class='ng-star-inserted']/a"

# ======================================================================================================
# ПАРАМЕТРЫ ДЛЯ ПОИСКА ЖК
# ------------------------------------------------------------------------------------------------------
# Поиск кнопок для раскрытия списка ЖК
ZHK_BLD = ""

# ------------------------------------------------------------------------------------------------------
# Поиск ID СЗ
ID_DVLPR = "//div[@class='__title_inf']/div[@class='ng-star-inserted']"

# ------------------------------------------------------------------------------------------------------
# Поиск кнопок для раскрытия списка ЖК
# ZHK_BLD = "//app-org-stage-of-construction[@id='org-stage-of-construction-build']//a"
# ZHK_BLT = "//app-org-stage-of-construction[@id='org-stage-of-construction-finish']//a"

# ------------------------------------------------------------------------------------------------------
# Элементы списка ЖК
# ZHK_BLD_NAMES = "//app-org-stage-of-construction[@id='org-stage-of-construction-build']//a[@class='ng-star-inserted']"
# ZHK_BLT_NAMES = "//app-org-stage-of-construction[@id='org-stage-of-construction-finish']//a[@class='ng-star-inserted']"

# ======================================================================================================
# ПАРАМЕТРЫ ДЛЯ ПОИСКА КОРПУСОВ
# ------------------------------------------------------------------------------------------------------
# Список названия корпусов
HDR_SCRL = "//div[@class='headers scroll']/tab-header"

# ------------------------------------------------------------------------------------------------------
# Общая информация по ЖК
GNRL_HDR = 'Общее'
GNRL_INFO = [
            'Вид группы объектов застройки',
            'Регион',
            'Населенный пункт',
            'Округ',
            'Район',
            'Улица',
            'Начало строительства ЖК',
            'Окончание строительства ЖК',
            'Жилая площадь объектов',
            'Всего квартир в ЖК'
            ]
GNRL_BTTN = "//td[@class='td flex gk-params-button closed']"
GNRL_DESCRIPT = [
                "//tr[@class='ng-star-inserted']",
                "//tr[@class='tr ng-star-inserted']"
                ]

# ------------------------------------------------------------------------------------------------------
# Информация по продажам (таблица)
SELL_INFO = "//table[@class='table--light table--natural']"
SELL_HDRS = '//th'
SELL_ROWS = "//tr[@class='ng-star-inserted']"
ROW_NAME = 'td'
ROW_EXCLUDE = 'visible-mobile ng-star-inserted'

# ------------------------------------------------------------------------------------------------------
# Информация по конкретному корпусу
CRPS_INFO = [
            'Вид объекта', 
            'Стадия строительства',
            'Срок сдачи', 
            'Класс объекта',
            'Всего квартир',
            'Отделка',
            'Количество этажей',
            'Жилая площадь объекта',
            'Материал наружных стен'
            ]
LIST_DESCRIPT = [
                "//tr[@class='tr tr--edge ng-star-inserted']",
                "//tr[@class='tr tr--edge ng-star-inserted']",
                "//tr[@class='ng-star-inserted']",
                "//tr[@class='tr ng-star-inserted']"
                ]
