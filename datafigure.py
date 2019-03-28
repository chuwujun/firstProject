import json
import pandas as pd
import sys
from matplotlib import pyplot as plt

def data_plot():
    file="user_study.json"
    df=pd.read_json(file)
    seta=sorted(set(list(df['user_id'])))    
    lista=[]
    listb=[]
    for one in seta:
        minutes=0
        lista.append(one)
        minutes=df[df['user_id']==one]['minutes'].sum()
        listb.append(minutes)
    
    
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.set_title("StudyData")
    ax.set_xlabel("User ID")
    ax.set_ylabel("Study Time")
    ax.plot(lista,listb)
    plt.show()
    #print(lista[0:11])
    #print(listb[0:11])

    return ax

data_plot()
