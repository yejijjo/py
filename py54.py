import matplotlib.pyplot as plt

def 원형그래프():
    figure = plt.figure()
    axes = figure.add_subplot(111)
    data = [1,2,3]
    label = ['Good','Bad','Normal']
    axes.pie(data, labels=label, autopct='%d%%')
    plt.axis('equal')
    plt.legend(label, loc='center left')
    plt.show()

# data = [0.18, 0.3, 3.33, 3.75, 0.38, 25, 0.25, 2.75, 0.1]
# label = ['비타민A','비타민B1','비타민B2','나이아신','비타민B6','비타민C','비타민D','비타민E','엽산']
# 원형그래프(data, label)

원형그래프()