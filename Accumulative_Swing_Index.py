
def Accumulative_Swing_Index(data):

    '''Generally, when the ASI is positive, it supports that the long-term trend will be higher, and when the ASI is negative, it suggests that the long-term trend will be lower.'''

    if len(data) < 3:
        raise ValueError("There must be atlest 3 rows of data")

    data['SI'] = 0

    for i in range(2, len(data)):

        k = max((data.iloc[i-1]['High'] - data.iloc[i]['Close']),
                 (data.iloc[i-1]['Low'] - data.iloc[i]['Close']))


        if max((data.iloc[i]['High'] - data.iloc[i-1]['Close']),
                (data.iloc[i]['Low'] - data.iloc[i-1]['Close']),
                (data.iloc[i]['High'] - data.iloc[i]['Low'])) == (data.iloc[i]['High'] - data.iloc[i-1]['Close']):
            r = (data.iloc[i]['High'] - data.iloc[i-1]['Close'] - 
                 0.5 * (data.iloc[i]['Low'] - data.iloc[i-1]['Close']) +
                 0.25 * (data.iloc[i-1]['Close'] - data.iloc[i-1]['Open']))
        elif max((data.iloc[i]['High'] - data.iloc[i-1]['Close']),
                  (data.iloc[i]['Low'] - data.iloc[i-1]['Close']),
                  (data.iloc[i]['High'] - data.iloc[i]['Low'])) == (data.iloc[i]['Low'] - data.iloc[i-1]['Close']):
            r = (data.iloc[i]['Low'] - data.iloc[i-1]['Close'] - 
                 0.5 * (data.iloc[i]['High'] - data.iloc[i-1]['Close']) +
                 0.25 * (data.iloc[i-1]['Close'] - data.iloc[i-1]['Open']))
        elif max((data.iloc[i]['High'] - data.iloc[i-1]['Close']),
                  (data.iloc[i]['Low'] - data.iloc[i-1]['Close']),
                  (data.iloc[i]['High'] - data.iloc[i]['Low'])) == (data.iloc[i]['High'] - data.iloc[i]['Low']):
            r = (data.iloc[i]['High'] - data.iloc[i-1]['Low'] + 
                 0.25 * (data.iloc[i-1]['Close'] - data.iloc[i-1]['Open']))
        else:
            r = 1e-10 

        t = data.iloc[i]['High'] - data.iloc[i]['Low']

        if t == 0:
            t = 1e-10

        data.loc[i,'SI'] = (50 * ((data.iloc[i-1]['Close'] - data.iloc[i]['Close']) +
                                     0.5 * (data.iloc[i-1]['Close'] - data.iloc[i-1]['Open']) +
                                     0.25 * (data.iloc[i]['Close'] - data.iloc[i]['Open'])) / r) * (k / t)

    return data
