def calculate_bop(data):

    '''
       Balance of Power = (Close price - Open price) / (High price - Low price)
       Consider buying when the BOP becomes positive (crossing above the zero line) as it may imply that bulls are taking control.
       Consider selling when BOP becomes negative (crosses below the zero line) as it may imply that bears are taking control. 
    '''

    data['BOP'] = (data['Close'] - data['Open']) / (data['High'] - data['Low'])
    data['Signals']=0
    for i in range(len(data)):
        if data.iloc[i]['BOP']>0 and data.iloc[i-1]['BOP']<0:
            data.loc[i,'Signals']=1
        if data.iloc[i]['BOP']<0 and data.iloc[i-1]['BOP']>0:
            data.loc[i,'Signals']=-1
    

    return data
