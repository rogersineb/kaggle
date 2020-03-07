import pandas as pd

hotel_bookings = pd.read_csv("~/Documents/kaggle/Datasets/hotel_bookings.csv")

# Columns of dataset
columns = []
for i in range(len(hotel_bookings.columns)):
    columns.append(hotel_bookings.columns[i])
    if i % 3 == 0:
        print(columns, "\n")
        columns = []

# Summary functions

# Different ways the describe function shows the summary of dataset
# Simple summary for no numerical data (String in this case)
print("\n", hotel_bookings.country.describe())

# Simple summary for numerical data
print("\n", hotel_bookings.is_canceled.describe())

# (mean function)
print("\nMédia dos dias em espera:", hotel_bookings.days_in_waiting_list.mean())

# (unique function)
print("\nNomes distintos de hoteis:", hotel_bookings.hotel.unique())

# (value_counts function)
print("\nValores únicos e quantas vezes esses aparecem no dataset:\n{}".format(hotel_bookings.hotel.value_counts()))

# Maps (There are two mapping methods used often)
# (map function)
hotel_bookings_days_in_waiting_list = hotel_bookings.days_in_waiting_list.mean()


# print("\n", hotel_bookings.days_in_waiting_list.map(lambda p: p - hotel_bookings_days_in_waiting_list))


# (apply function) it's equivalent to map function
def remain_days_in_waiting_list(row):
    row.days_in_waiting_list = row.days_in_waiting_list - hotel_bookings_days_in_waiting_list
    return row


print("\n Result of the apply function over dataset: {}\n"
      .format(hotel_bookings.apply(remain_days_in_waiting_list, axis='columns').days_in_waiting_list))
