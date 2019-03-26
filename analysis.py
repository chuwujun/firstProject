import json
import pandas as pd
import sys


def analysis(file,user_id):
    times=0
    minutes=0

    user_id=int(user_id)
    df=pd.read_json(file)
    df2=df[df['user_id']==user_id]
    times=len(df2)
    minutes=df2['minutes'].sum()

    return times,minutes


if __name__ == "__main__":
    s=analysis(sys.argv[1],sys.argv[2])
    print(s)
