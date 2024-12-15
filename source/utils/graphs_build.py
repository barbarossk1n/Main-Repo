
from utils.libraries_apply import *


''' Функция построения боксплотов в конкретном стиле '''
def plot_boxplot(data: object, data_x: object, data_y: object, 
                 title: str, x_label: str, y_label: str, 
                 figsize=(12, 8), order=None) -> None:
    
    # Размер графика
    plt.figure(figsize=figsize) 
    
    # График самого боксплота 
    sns.boxplot(x=data_x, y=data_y, data=data, palette='Blues', showfliers=False, order=order)
    
    # Подпись графика/осей
    plt.title(title, fontsize=20, pad=20)
    plt.xlabel(x_label, fontsize=14, labelpad=15)
    plt.ylabel(y_label, fontsize=16, labelpad=15)
    
    # Доп. настройка
    plt.xticks(rotation=90)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.2)
    plt.tight_layout()
    
    # Построение
    plt.show()


''' Функция построения пайчартов в конкретном стиле '''
def pie_plot(data: object, title: str, figsize=(12, 8), 
             colors=[], save_img=False) -> None:

    # Настройка цветов для пайчарта
    if colors == []:
        colors = plt.cm.Blues(range(0, 256, 25)) 

    # Функция для отображения процентов и значений
    def func(percentage, allvalues):
        absolute = int(percentage / 100. * sum(allvalues))
        return f'{absolute} м²\n({percentage:.1f}%)'

    # Размер графика
    plt.figure(figsize=figsize)

    # График самого пайчарта
    plt.pie(data, 
            labels=data.index, 
            colors=colors,
            autopct=lambda pct: func(pct, data), 
            startangle=140,
            textprops={'size': 8})
    
    plt.title(title, fontsize =20)
    plt.axis('equal')           # <-- для равных осей (круглая форма)
    
    if save_img:
        # Сохранение графика в высоком качестве
        plt.savefig('save_img.png', dpi=300, bbox_inches='tight')
        
    plt.show()
    
    
''' Функция построения барплотов в конкретном стиле '''
def bar_plot(data: object, chosen_column:str, n: int, criteria: str, 
             title: str, x_label: str, y_label: str,
             figsize=(12, 6)) -> None:
    
    # Выбираем топ-n элементов (по какому-то критерию, указанному в "title")
    top_n = data.nlargest(n, criteria)
    
    # Строим график
    plt.figure(figsize=figsize)
    
    # Построение бар-плота
    plt.bar(top_n[chosen_column], top_n[criteria], color='skyblue')
    
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    