from matplotlib import font_manager
from matplotlib.lines import _LineStyle
import pandas as pd
from openpyxl.workbook import workbook
import matplotlib.pyplot as plt


def 표만들기():
    번호 = [1,2,3]
    data = {
        '이름':['홍길동','아무게','김철수'],
        '키':[175.5,166.3,180.0],
        '몸무게':[66.8,50.7,80.8]
    }

    df = pd.DataFrame(data, index=번호)
    print(df)

    df.to_csv('my Table.txt', sep='\t')

    df.to_excel('my Table.wlsx', index=False)

    df2 = pd.read_excel('my Table.wlsx')
    print(df2)

from matplotlib import font_manager, rc
def 꺾은선():
    font_name = font_manager.FontProperties(fname='HMFMMUEX.TTC').get_name()
    plt.rc('font',family=font_name)

    figure = plt.figure()
    axes = figure.add_subplot(111)
    x = ['1월','2월','3월','4월','5월','6월']
    y = [1200,800,500,400,700,800]
    axes.plot(x,y, linestyle='--', marker='^')
    plt.title('상반기 실적')
    plt.show()

def 원형그래프():
    font_name = font_manager.FontProperties(fname='HMFMMUEX.TTC').get_name()
    plt.rc('font',family=font_name)
    figure = plt.figure()
    axes = figure.add_subplot(111)
    data = [1,2,3]
    label = ['Good','Bad','Normal']
    axes.pie(data, labels=label, autopct='%d%%')
    plt.axis('equal')
    plt.legend(label, loc='center left')
    plt.show()

data = [0.18, 0.3, 3.33, 3.75, 0.38, 25, 0.25, 2.75, 0.1]
label = ['비타민A','비타민B1','비타민B2','나이아신','비타민B6','비타민C','비타민D','비타민E','엽산']
원형그래프(data, label)