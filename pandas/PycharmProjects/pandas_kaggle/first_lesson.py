import pandas as pd

data_frame = pd.DataFrame({'Yes': [50, 21, 4], 'No': [131, 2, 12], 'Maybe': [-55, 32, -20]}, index=['New York boys age', 'San Francisco boys age', 'Texas boys age'])

data_frame2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])

s_pd = pd.Series([1, 2, 3, 4, 5], index=['number 2000', 'number 2001', 'number 2002', 'number 2003', 'number 2004'], name='Good years')

print(data_frame)

print()
print(data_frame2)

print()
print(s_pd)

hotel_bookings = pd.read_csv('~/Documents/kaggle/Datasets/hotel_bookings.csv')

print("\n",  hotel_bookings.shape)

print("\n", hotel_bookings.head())

print("\n", hotel_bookings.describe())