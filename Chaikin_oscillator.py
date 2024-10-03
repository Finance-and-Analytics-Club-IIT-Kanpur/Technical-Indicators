def calculate_chaikin_oscillator(data):

    '''
       The Chaikin oscillator utilizes two primary buy and sell signals.
       First, a positive divergence is confirmed with a center-line crossover above the accumulation-distribution line, signaling a potential buying opportunity.
       Second, a negative divergence is confirmed with a center-line crossover below the accumulation-distribution line, signaling a potential selling opportunity.
    
    '''


    data['Money Flow Multiplier'] = ((data['Close'] - data['Low']) - (data['High'] - data['Close'])) / (data['High'] - data['Low'])
    

    data['Money Flow Volume'] = data['Money Flow Multiplier'] * data['Volume']
    

    data['CMF'] = data['Money Flow Volume'].rolling(window=21).sum() / data['Volume'].rolling(window=21).sum()


    data['EMA_3'] = data['CMF'].ewm(span=3, adjust=False).mean()
    data['EMA_10'] = data['CMF'].ewm(span=10, adjust=False).mean()

    data['CHO'] = data['EMA_3'] - data['EMA_10']

    data['Signals']=0
    for i in range(len(data)):
        if data.iloc[i]['CMF']>0 and data.iloc[i-1]['CMF']<0:
            data.loc[i,'Signals']=1
        if data.iloc[i]['CMF']<0 and data.iloc[i-1]['CMF']>0:
            data.loc[i,'Signals']=-1

    return data
