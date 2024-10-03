def Accumulation_Distribution(data,n=10):

    '''
        
        If a security’s price is in a downtrend while the A/D line is in an uptrend, then the indicator shows there may be buying pressure and the security’s price may reverse to the upside.
        Conversely, if a security’s price is in an uptrend while the A/D line is in a downtrend, then the indicator shows there may be selling pressure, or higher distribution. 
        This warns that the price may be due for a decline.
        
    '''
    data['MFM'] = ((data['Close']-data['Low'])-(data['High']-data['Close']))/(data['High']-data['Low'])

    data['MFV'] = (data['MFM']*data['Volume'])/100000

    data['A/D'] = data['MFV'].cumsum()

    data['Signals']=0

    def calculate_slope(n):
        x = np.arange(len(n))
        if len(n) < 2: 
            return np.nan
        return np.polyfit(x, n, 1)[0]
    window_size = 10  
    data['Slope_A/D'] = data['A/D'].rolling(window=window_size).apply(calculate_slope, raw=False)
    data['Slope_Close'] = data['Close'].rolling(window=window_size).apply(calculate_slope, raw=False)
    data['Slope_A/D'] = data['Slope_A/D'].fillna(0)
    data['Slope_Close']=data['Slope_Close'].fillna(0)

    for i in range(len(data)):
        if data.iloc[i]['Slope_A/D']>0 and data.iloc[i]['Slope_Close']<0:
            data.loc[i,'Signals']=1
        if data.iloc[i]['Slope_A/D']<0 and data.iloc[i]['Slope_Close']>0:
            data.loc[i,'Signals']=-1
            
            
    


    return data

