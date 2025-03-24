import pandas as pd
import numpy as np

df = pd.read_csv("reatail_ecommerce_sales_dataset.csv")

products = {
    'Clothing': [
        'T-Shirt', 'Jeans', 'Jacket', 'Sweater', 'Dress', 
        'Shorts', 'Skirt', 'Hoodie', 'Blouse', 'Socks'
    ],
    'Beauty': [
        'Shampoo', 'Conditioner', 'Body Lotion', 'Face Cream', 'Lip Balm', 
        'Facial Cleanser', 'Hair Oil', 'Perfume', 'Deodorant', 'Makeup Kit'
    ],
    'Electronics': [
        'Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch', 
        'Camera', 'Keyboard', 'Mouse', 'USB Drive', 'Bluetooth Speaker'
    ]
}


df['Product Name'] = df['Product Category'].apply(lambda x: np.random.choice(products[x]))

np.random.seed(0)
df['Product Stock'] = np.random.randint(50, 501, size=len(df))

print(df[['Customer ID', 'Product Name', 'Product Stock']])

df.to_csv("retail_sales_dataset.csv")