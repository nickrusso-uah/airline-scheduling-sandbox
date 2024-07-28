
import os
import sys
import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Add the directory containing the 'utils' folder to the Python path
utils_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(utils_dir)


from utils.math.earth_utils import wrap_to_360


# Load in data
file_path = "C:/Users/nicks/Desktop/repos/airline-scheduling-sandbox/data/geographic/cb_2018_us_state_20m/cb_2018_us_state_20m.shp"
data = gpd.read_file(file_path)

# List of FIPS codes for the 48 contiguous states
contiguous_states_fips = [
    '01', '02', '04', '05', '06', '08', '09', '10', '11', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '44', '45', '46', '47', '48', '49', '50', '51', '53', '54', '55', '56'
]

# Filter the data to include only the 48 contiguous states
data_contiguous = data[data['STATEFP'].isin(contiguous_states_fips)]

print(data)

#print(multi_polygon.bounds())
# Wrap latitudes to 360 degrees
#data['geometry'] = data['geometry'].apply(lambda geom: translate(geom, xoff=0, yoff=wrap_to_360(geom.y)))

fig, ax = plt.subplots(figsize=(15, 10))

data_contiguous.plot(edgecolor='black', figsize=(15, 10))

plt.show()