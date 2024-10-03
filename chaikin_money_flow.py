
def calculate_chaikin_money_flow(data, period=20):

    '''
       Bullish crosses occur when the CMF crosses the zero line from below, and stock prices continue on an upward trend. 
       Bearish crosses occur when the CMF crosses the zero line from above, and prices continue to fall.
    
    '''
    data['Money Flow Multiplier'] = ((data['Close'] - data['Low']) - (data['High'] - data['Close'])) / (data['High'] - data['Low'])

    data['Money Flow Volume'] = data['Money Flow Multiplier'] * data['Volume']


    data['CMF'] = data['Money Flow Volume'].rolling(window=period).sum() / data['Volume'].rolling(window=period).sum()

    data['Signals']=0
    for i in range(len(data)):
        if data.iloc[i]['CMF']>0 and data.iloc[i-1]['CMF']<0:
            data.loc[i,'Signals']=1
        if data.iloc[i]['CMF']<0 and data.iloc[i-1]['CMF']>0:
            data.loc[i,'Signals']=-1

    return data
