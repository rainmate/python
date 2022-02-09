import numpy as np
import pandas as pd
import  requests
import urllib

def print_Series():
    arr = np.array([12,34,45.56,55])
    s3 = pd.Series(arr,index=['white','blue','green','yellow'])

    print(s3)

def print_dict():
    mydict = { 'red': 2000,'blue': 1000,'yellow' : 500,'orange' : 1000}
    myseries = pd.Series(mydict)
    print(myseries)
    colors = [ 'red' ,'yellow' , 'orange' , 'blue' ,'green']
    myseries = pd. Series(mydict,index=colors)
    
    print(myseries)

def print_pd_DataFrame():
    data = {'color': ['blue' , 'green ' ,'yellow' , ' red', 'white'],
            'object':[ 'bali' ,' pen ' ,' pencii ' , ' paper ', 'mug' ],
            'price': [1.2,1.0,0.6,0.9,1.7]}
    frame = pd. DataFrame(data)

    print(frame)

    frame3 = pd.DataFrame(np.arange(16).reshape((4,4)),
                index=[ 'red' , 'blue ' , 'yellow ' , ' white'],
                columns=[ 'ball' ,'pen', 'pencil' , ' paper'])

    print(frame3.columns)


if __name__ == '__main__':
    print_pd_DataFrame()

