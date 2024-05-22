
# Task 3 - Question 1
def calculate_imn_usds(max_lev):
    
    initial_margin_rate = 0.05  

    imn = max_lev / initial_margin_rate
    
    return int(imn)




def get_impact_prices(bid_orderbook, ask_orderbook, imn):

  bid_orderbook['Accumulated'] = bid_orderbook['Price'] * bid_orderbook['Quantity'].cumsum()  

  bid_idx = bid_orderbook['Accumulated'].gt(imn).idxmax()

  impact_bid_price = bid_orderbook.loc[bid_idx, 'Price']

  
  ask_orderbook['Accumulated'] = ask_orderbook['Price'] * ask_orderbook['Quantity'].cumsum()

  ask_idx = ask_orderbook['Accumulated'].gt(imn).idxmax()  

  impact_ask_price = ask_orderbook.loc[ask_idx, 'Price']

  return impact_bid_price, impact_ask_price




def calculate_funding_rate(impact_bid_price, impact_ask_price, index_price):
    
    premium_index = (max(0, impact_bid_price - index_price) - 
                    max(0, index_price - impact_ask_price)) / index_price
    
    interest_rate = 0.0003
    
    clamped_premium_index = max(-0.0005, min(premium_index, 0.0005)) 
    
    funding_rate = clamped_premium_index + interest_rate - clamped_premium_index
    
    return funding_rate



