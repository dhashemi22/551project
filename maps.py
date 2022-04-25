import pandas as pd
import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster
import math

data = pd.read_json("alldata.json")
data["percentageGoodDays"] = data["Good Days"] / data["Days with AQI"]

loca = pd.read_csv("uscounties.csv")
latlong = loca.loc[loca['state_name'] == "California"].reset_index(drop=True)

data=data.rename(columns = {'County':'county'})
new = pd.merge(data, latlong, on='county')

# 2017
m_17 = folium.Map(location=[36.7783,-119.4179], tiles='cartodbpositron', zoom_start=6, tooltip = 'This tooltip will appear on hover')

def color_producer(val):
    if val >= np.mean(new17['percentageGoodDays']):
        return 'forestgreen'
    else:
        return 'darkred'

# Add a bubble map to the base map
for i in range(0,len(new17)):
    Circle(
        location=[new17.iloc[i]['lat'], new17.iloc[i]['lng']],
        radius=10000,
        color=color_producer(new17.iloc[i]['percentageGoodDays']), tooltip = "Year: "+ str(new17.iloc[i]['Year'])+"<br> County: " + str(new17.iloc[i]['county'])+"<br> Percent of Good AQI Days/Year: " + str((int(new17.iloc[i]['percentageGoodDays']*100)))+"%").add_to(m_17)

# Display the map
m_17


# 2018
m_18 = folium.Map(location=[36.7783,-119.4179], tiles='cartodbpositron', zoom_start=6, tooltip = 'This tooltip will appear on hover')

def color_producer(val):
    if val >= np.mean(new18['percentageGoodDays']):
        return 'forestgreen'
    else:
        return 'darkred'

# Add a bubble map to the base map
for i in range(0,len(new18)):
    Circle(
        location=[new18.iloc[i]['lat'], new18.iloc[i]['lng']],
        radius=10000,
        color=color_producer(new18.iloc[i]['percentageGoodDays']), tooltip = "Year: "+ str(new18.iloc[i]['Year'])+"<br> County: " + str(new18.iloc[i]['county'])+"<br> Percentage Good AQI Days/Year: " + str((int(new18.iloc[i]['percentageGoodDays']*100)))+"%").add_to(m_18)

# Display the map
m_18



# 2019
m_19 = folium.Map(location=[36.7783,-119.4179], tiles='cartodbpositron', zoom_start=6, tooltip = 'This tooltip will appear on hover')

def color_producer(val):
    if val >= np.mean(new19['percentageGoodDays']):
        return 'forestgreen'
    else:
        return 'darkred'

# Add a bubble map to the base map
for i in range(0,len(new19)):
    Circle(
        location=[new19.iloc[i]['lat'], new19.iloc[i]['lng']],
        radius=10000,
        color=color_producer(new19.iloc[i]['percentageGoodDays']), tooltip = "Year: "+ str(new19.iloc[i]['Year'])+"<br> County: " + str(new19.iloc[i]['county'])+"<br> Percentage Good AQI Days/Year: " + str((int(new19.iloc[i]['percentageGoodDays']*100)))+"%").add_to(m_19)

# Display the map
m_19



# 2020
m_20 = folium.Map(location=[36.7783,-119.4179], tiles='cartodbpositron', zoom_start=6, tooltip = 'This tooltip will appear on hover')

def color_producer(val):
    if val >= np.mean(new20['percentageGoodDays']):
        return 'forestgreen'
    else:
        return 'darkred'

# Add a bubble map to the base map
for i in range(0,len(new20)):
    Circle(
        location=[new20.iloc[i]['lat'], new20.iloc[i]['lng']],
        radius=10000,
        color=color_producer(new20.iloc[i]['percentageGoodDays']), tooltip = "Year: "+ str(new20.iloc[i]['Year'])+"<br> County: " + str(new20.iloc[i]['county'])+"<br> Percentage Good AQI Days/Year: " + str((int(new20.iloc[i]['percentageGoodDays']*100)))+"%").add_to(m_20)

# Display the map
m_20







