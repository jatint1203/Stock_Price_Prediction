import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO


def prediction(request):
    key='FH07SZXZ2ONHNOOO'
    df= pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_daily&symbol=REliance.BSE&datatype=csv&apikey=key')
    print(df)
    plt.figure(figsize=(16,8))
    plt.plot(df['close'])
    plt.title("Stock Data Analysis")
    plt.xlabel("Time  Period", fontsize=23)
    plt.ylabel('Close  History', fontsize=23)
    print("Called Function")
    graph=prediction_image()
    return graph
    
    
    
def prediction_image():
    print('Enterecsd sdfsdf')
    buffer=BytesIO()
    plt.savefig(buffer, foramt='png')
    buffer.seek(0)
    image_png = buffer.getvalue()        
    grph=base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

