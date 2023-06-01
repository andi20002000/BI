import pandas as pd
from scipy.spatial.distance import cdist

# Load the ski resort and snow observation data into pandas dataframes
resorts = pd.read_csv('resorts.csv')
snow = pd.read_csv('snow.csv')

# Convert the latitude and longitude columns to radians
resorts['Latitude'] = resorts['Latitude'].apply(lambda x: x * (3.14159 / 180))
resorts['Longitude'] = resorts['Longitude'].apply(lambda x: x * (3.14159 / 180))
snow['Latitude'] = snow['Latitude'].apply(lambda x: x * (3.14159 / 180))
snow['Longitude'] = snow['Longitude'].apply(lambda x: x * (3.14159 / 180))

# Calculate the distance between each ski resort and snow observation point
distances = cdist(resorts[['Latitude', 'Longitude']], snow[['Latitude', 'Longitude']], 'euclidean')

# Find the minimum distance for each ski resort
min_distances = distances.min(axis=1)

# Find the index of the closest snow observation point for each ski resort
closest_snow_index = distances.argmin(axis=1)

# Get the latitude and longitude of the closest snow observation point for each ski resort
closest_snow_lat = snow.loc[closest_snow_index, 'Latitude'].reset_index(drop=True)
closest_snow_lon = snow.loc[closest_snow_index, 'Longitude'].reset_index(drop=True)

# Add the minimum distance and closest snow observation point location to the resorts dataframe
resorts['Minimum_distance'] = min_distances
resorts['Closest_snow_lat'] = closest_snow_lat.apply(lambda x: x * (180 / 3.14159))
resorts['Closest_snow_lon'] = closest_snow_lon.apply(lambda x: x * (180 / 3.14159))

resorts['Closest_snow_lat_degrees'] = resorts['Closest_snow_lat'].apply(lambda x: x * (180 / 3.14159))



# store the result in a csv file
resorts.to_csv('resorts_with_snow.csv', index=False)
