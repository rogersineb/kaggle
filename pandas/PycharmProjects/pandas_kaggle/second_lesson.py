import pandas as pd

hotel_bookings = pd.read_csv("~/Documents/kaggle/Datasets/hotel_bookings.csv")
pd.set_option("display.max_rows", 6)

print("\n", hotel_bookings.columns)

print("\n", hotel_bookings.head())
print("\n", hotel_bookings['arrival_date_year'])

# Index-based selection (iloc operator)
print("\n", hotel_bookings.iloc[0])

print("\n", hotel_bookings.iloc[:3, 1])

print("\n", hotel_bookings.iloc[0:10, 1])

print("\n", hotel_bookings.iloc[-5:, -3:])

# Label-based selection (loc operator)
print("\n", hotel_bookings.loc[0:10, 'is_canceled'])

print("\n", hotel_bookings.loc[[1, 2, 5, 7, 10], ['arrival_date_week_number', \
 'arrival_date_day_of_month', 'stays_in_weekend_nights']])

print(hotel_bookings.set_index("reservation_status"))

print("\n", hotel_bookings.loc[(hotel_bookings.hotel == 'City Hotel') & (hotel_bookings.is_canceled == 1) \
 | (hotel_bookings.lead_time >= 90), "hotel": "lead_time"])

# build-in conditional (isin)
print("\n", hotel_bookings.loc[hotel_bookings.hotel.isin(["Resort Hotel", "City Hotel"])])

# build-in conditional (isnull) or its companion
print("\n", hotel_bookings.loc[hotel_bookings.days_in_waiting_list.notnull()])

# Verify type of result
print("\n", type(hotel_bookings.loc[(hotel_bookings.is_canceled == 1)]))
