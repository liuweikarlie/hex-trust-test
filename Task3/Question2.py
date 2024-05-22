import math

from datetime import datetime

# def implile_interest_Rate(F, S, current_time,future_time):
#     # current_time = datetime.fromtimestamp(current_time)  
#     # future_time = datetime.fromtimestamp(future_time)  
#     T = ((future_time - current_time).days)/365
#     r=0.003

#     F_0 = S * math.exp(r * T)

#     IFR = (F - F_0) / (F_0 * T)
#     return round(IFR, 10)

    # rate = IFR * 365
   
def implile_interest_Rate(F, S, current_time,future_time):
    T= (future_time - current_time).days/365
    return round((math.pow(F/S, 1/T) - 1)/100,10)


    


# testing the function
# Test the function with the following inputs
current_future_price = 3991
current_spot_price = 3989
current_time = datetime(2023, 3, 15)
future_time = datetime(2023, 4, 15)
print(implile_interest_Rate(current_future_price, current_spot_price, current_time, future_time))  # Expected output: 0.0005