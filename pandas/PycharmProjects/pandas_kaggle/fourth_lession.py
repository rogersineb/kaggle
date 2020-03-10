import pandas as pd
import numpy as np

hotel_bookings = pd.read_csv("~/Documents/kaggle/Datasets/hotel_bookings.csv")

# Columns in Dataset
print("Columns(Series) in hoteal booking Dataset:\n")
for column in hotel_bookings.columns:
    print(column)

# Groupwise analysis (groupby, agg)

# -- replicate value-counts function with (groupby)
print("\n\n", hotel_bookings.groupby('company').company.count())

# -- Using (value_counts) function
print("\n\n", hotel_bookings.company.value_counts())

# -- get the cheapest company
print("\n\nMin whit groupby():\n", type(hotel_bookings.groupby('company').is_canceled.count().index))

# -- make operation over set of data in dataset
print(hotel_bookings.groupby('is_canceled').apply(lambda ic: ic.is_canceled % 2))

# -- pick out more than one column with groupby
print("\n\n", type(hotel_bookings.groupby(['country', 'hotel', 'arrival_date_month']).lead_time.mean()))

# -- groupby method worth mentioning is (agg)
print("\n\n", hotel_bookings.groupby(['days_in_waiting_list', 'is_canceled']).days_in_waiting_list.agg([len]))

# Multi-indexes

print("\n\n", type(hotel_bookings.groupby(['country', 'hotel', 'company']).lead_time.agg([len]).index))

# -- (reset_idex)
multi_index_dataset = hotel_bookings.groupby(['country', 'hotel', 'company']).lead_time.agg([len])

# -- dataset with multi-index
print("\n\nTipo de index: {}\nDataset:\n{}".format(type(multi_index_dataset.index), multi_index_dataset))

# -- dataset with reset multi-index
print("\n\nTipo de index: {}\nDataset:\n{}".format(type(multi_index_dataset.reset_index()), multi_index_dataset.reset_index()))

# Sorting

# -- sorting by (sort_values)
multi_index_dataset = multi_index_dataset.reset_index()
print("\n\n", multi_index_dataset.sort_values(by='len', ascending=False))

# -- sorting by (sort_index)
print("\n\n", multi_index_dataset.sort_index())

# -- sorting by more than one column at a time
print(multi_index_dataset.sort_values(by=['country', 'company']))

# companion of exercises from kaggle

print('\n\nQuantas vezes cada país aparece no dataset?\n', hotel_bookings.groupby('country').size().sort_values(ascending=False))

print('\n\nQual o tempo máximo de espera para cada hotel no dataset:\n', hotel_bookings.groupby('hotel')['lead_time'].max().sort_index())

print('\n\nQual o tempo médio e o tempo máximo de espera para cada hotel no dataset?\n',
      hotel_bookings.groupby('hotel').lead_time.agg([np.nanmedian, max]))

print('\n\nQual a combinação que mais aparece quando analisamos o número de cancelamentos anteriores por hotel e por '
      'clientes que já estiveram no hotel:\n',
      hotel_bookings.groupby(['hotel', 'is_repeated_guest'])['previous_cancellations'].size())

print('\n\nQual a quntidade de reservas feitas por cada categoria de cliente, entre os novos e aqueles que já fizeram reservas anteriores, por mês:\n',
      hotel_bookings.groupby(['hotel', 'is_repeated_guest', 'arrival_date_month', 'customer_type'])['arrival_date_month'].count().head(10))

print('\n\n', hotel_bookings.iloc[0])
