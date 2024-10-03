def calculate_52_week_high_low(data,x=252):
    
    high_x_week=  data['High'].rolling(window=x, min_periods=1).max().iloc[-1]
    low_x_week = data['Low'].rolling(window=x, min_periods=1).min().iloc[-1] 

    return high_x_week,low_x_week
