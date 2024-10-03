def Acclerator_Oscillator(data):
    '''If the value is positive it indicates bullish signs thus you should buy and if the value is negative it shows bearish sign thus you should only sell'''\
    
    
    data['Signals']=0
    data['Median']= (data['High']+data['Low'])/2
    data['AO']= data['Median'].rolling(window=5).mean()-data['Median'].rolling(window=34).mean()
    data['AO']= data['AO'].fillna(0)
    for i in range(len(data)):
        if data.iloc[i]['AO'] >=0:
            data.loc[i,'Signals']=1
        if data.iloc[i]['AO']<=0:
            data.loc[i,'Signals']=-1
    
    indices = np.arange(len(data))
    colors= ['green' if value>0 else 'red' for value in data['AO']]
    plt.bar(indices,data['AO'],color=colors)
    plt.axhline(0,color='black',linestyle='--',linewidth=1.5,label= 'Zero Line')

    plt.title('Acclerator Oscillator')
    plt.xlabel('Date')
    plt.ylabel('Median')

    plt.legend()
    plt.show()

    return data
