# Technical Assignment for Hex Trust

> Name: Liu Wei\
> Email: u3555658@connect.hku.hku

This repository is for Task2 and Task3. 

## For Task 2

- For the orderbook question,  I use the depth difference data from binance, for constructing the orderbook, i use the priorityQueue,in this case, it can remove the best bid/ask in O(1)time.  

    - please run the code:
    ```
    python ./Task2/orderbook.py
    ```

- For the problem: "**Find the AWS instance that has the lowest latency with the server where the exchange’s matching engine resides**", 
    - I use the Dijkstra Algorithm, all the servers in AWS would in the graph structure.
    - the weight in each edge would be the response time for the adjancent node. 
    - To get the reponse time, we should use the `ping` method to get the time
    - please run the code :
    ```
    python ./Task2/dijkstra.py


## Task 3
- `Question1.py` is the implementation of calculating the funding rate
- `Question2.py` is the implementation of the implied funding rate

- `Question3.ipynb` is the data exploratory and trade idea.



