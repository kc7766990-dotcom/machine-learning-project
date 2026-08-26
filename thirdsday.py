import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = [
    ['semester 1','mathmetics',45],
    ['semester 1','physics',35],
    ['semester 1','chemistry',45],
    ['semester 1','evs',45],
    ['semester 1','ml',45],


    ['semester 2','electronic',52],
    ['semester 2','electrical',45],
    ['semester 2','python',45],
    ['semester 2','electronic',35],
    ['semester 2','electrical',45],

    ['semester 3','coa',46],
    ['semester 3','data structure',45],
    ['semester 3','python',55],
    ['semester 3','electronic',54],
    ['semester 3','electrical',45],

    ['semester 4','operating system',42],
    ['semester 4','math4',45],
    ['semester 4','python',55],
    ['semester 4','java',50],
    ['semester 4','autometa',39],

    ['semester 5','coa',46],
    ['semester 5','data structure',45],
    ['semester 5','python',52],
    ['semester 5','electronic',54],
    ['semester 5','electrical',45],
    
    ['semester 6','software engineering',42],
    ['semester 6','cn',45],
    ['semester 6','blockchain',55],
    ['semester 6','java',50],
    ['semester 6','data analysis',45],     

]

df = pd.DataFrame(data,columns = ["semester","subject","marks"])


print(df)

# total_marks = np.sum(data,asix=1)
# print("total marks", total_marks)
# x = ['sem1','sem2','sem3']
# y = [500, 600]
plt.subplot(2,2,1)
plt.bar(df['subject'],df['marks'],color = 'red',width=.3)
plt.title("result1")
plt.grid()

plt.subplot(2,2,2)
plt.plot(df['subject'],df['marks'],color = 'green',marker="*")
plt.title("result")
plt.grid()

plt.show()



