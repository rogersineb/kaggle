import pandas as pd

airbnb_neighbourhood = pd.read_csv('~/Downloads/berlin-airbnb-data/neighbourhoods.csv')
airbnb_reviews = pd.read_csv('~/Downloads/berlin-airbnb-data/reviews.csv')
airbnb_reviews_summary = pd.read_csv('~/Downloads/berlin-airbnb-data/reviews_summary.csv')
airbnb_listings = pd.read_csv('~/Downloads/berlin-airbnb-data/listings.csv')
airbnb_listings_summary = pd.read_csv('~/Downloads/berlin-airbnb-data/listings_summary.csv')

#  Dataset columns
print('\n{}//{}\n'.format('-' * 35, '-' * 35))
print('Colunas do dataset listings:\n', airbnb_listings.columns)
print('\n{}//{}'.format('-' * 35, '-' * 35))
# print('\nColunas do dataset listings summary:\n', airbnb_listings_summary.columns)
# print('\n{}//{}'.format('-' * 35, '-' * 35))
# print('\nColunas do dataset reviews:\n', airbnb_reviews.columns)
# print('\n{}//{}'.format('-' * 35, '-' * 35))
print('\nColunas do dataset reviews summary:\n', airbnb_reviews_summary.columns)
print('\n{}//{}'.format('-' * 35, '-' * 35))

# print('\nColunas do dataset neighbourhood:\n', airbnb_neighbourhood.columns)
# print('{}'.format('*' * 70))

# RENAMING

# (rename) function change the [index names] and the [column names]
print('\n\nRenomeação da coluna \'neighbourhood_group\' para ngbhood_group:\n',
      airbnb_neighbourhood.rename(columns={'neighbourhood_group': 'ngbhood_group'}))

# -- change index is very rarely and for that, (set_index) method may be used.
print('\nRenomeação dos indexes de \'0\' a \'4\' para \'firstEntry\' até \'fifthEntry\':\n',
     airbnb_neighbourhood.rename(index={0: 'firstEntry', 1: 'secondEntry', 2: 'thirdEntry', 3: 'fourthEntry', 4: 'fifthEntry'}))

# Both the row index and column index can have their own name attribute. For that, the (rename_axis) method may be used.
print('\n\nRenomeando os eixos x e y do dataset:\n', airbnb_neighbourhood.rename_axis('Entry', axis='rows').rename_axis('Fields', axis='columns'), sep='')

# COMBINING

# -- Pandas has three method for combine different DataFrames and/or Series.
# In order of increasing complexity, these are (concat), (join) and (merge).

# -- (concat) Pandas method
print('\n\nConcatenação dos Datasets listing_summary e listing:\n', pd.concat([airbnb_listings_summary, airbnb_listings]).columns)

# -- (join) Pandas method
left = airbnb_listings.rename(columns={'id': 'listing_id'}).set_index('listing_id')
rigth = airbnb_reviews_summary.set_index('listing_id')

print('\n\nCombinação dos Datasetes \'listing\' e \'reviews_summary\' utilizando o método \'join()\':\n',
      left.join(rigth, lsuffix='_LIS', rsuffix='_RVW').columns)

print('\n\n5 linhas do dataset reviews_summary:\n', airbnb_reviews_summary.iloc[:5, -5:])
print('\n\n5 linhas do dataset listing:\n', airbnb_listings.iloc[:5, :])
