import pandas as pd
import numpy as np

hotel_bookings = pd.read_csv("~/Documents/kaggle/Datasets/hotel_bookings.csv")

airbnb = pd.read_csv('~/Documents/kaggle/Datasets/berlin-airbnb-data/neighbourhoods.csv')

# Dtypes
print('O tipo de dado (dtype) da coluna \'is_canceled\' é:', hotel_bookings.is_canceled.dtype)

print('\nO tipo de dado (dtype) da coluna \'hotel\' é:', hotel_bookings.hotel.dtype)

print('\nO tipo de dado (dtype) da coluna \'adults\' é:', hotel_bookings.adults.dtype)

print('\nTipo de dados das Series do Dataset Hotel Booking:\n', hotel_bookings.dtypes)

# -- Change dtype columns with (astype) function
print('\nTroca do tipo \'{}\' por \'{}\' na coluna \'is_canceled\'.'.format(hotel_bookings.is_canceled.dtype,
                                                                    hotel_bookings.is_canceled.astype('float64').dtype))

# Missing data (NaN)
print('\n', hotel_bookings.sort_index(ascending=False))

# -- Replace a missing values (fillna) method
# (
# Another Strategy is Backfill Strategy (Substituir os valores nulos do dataset
# com o primeiro valor não nulo que aparecer, algumas vezes após um dado registro na base de dados)
# )
print('\nSubstituindo o NaN por um valor padrão (Unknown):\n', airbnb.neighbourhood.fillna('Unknown'))

# -- Replace non-null value with (replace) method
print('\n', airbnb.neighbourhood.replace('Grunewald', 'Alguma cidade na alemanhã'))


# companion of exercises from kaggle





