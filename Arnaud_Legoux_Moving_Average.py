def ALMA(data, window=9, sigma=6, offset=0.85):

    '''The Arnaud Legoux Moving Average (ALMA) is a technical analysis indicator used to smooth price movements and identify trends in the market'''

    alma = pd.Series(index=data.index)
    

    for i in range(window - 1, len(data)):

        prices = data[i - window + 1:i + 1]
        

        weights = np.array([np.exp(-0.5 * ((j - (window - 1) * offset) / sigma) ** 2) for j in range(window)])
        weights /= weights.sum() 
        

        alma.iloc[i] = np.dot(weights, prices)
    
    
    return alma
