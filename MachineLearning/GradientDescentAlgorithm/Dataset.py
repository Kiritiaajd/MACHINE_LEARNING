import numpy as np 
import pandas as pd 

np.random.seed(42)

Area = np.random.randint(500, 3000 , 50)
No_of_rooms = np.random.randint(1 , 6, 50)

price = 5000 * No_of_rooms + 200 * Area + np.random.randint(1000, 50000 , 50)

data  = pd.DataFrame({
    "Area of house (sq ft)" : Area , 
    "Number of rooms" : No_of_rooms , 
    "Price(in (INR))" : price
})

data.to_csv("house_price_dataset.csv" , index= False)