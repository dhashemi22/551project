import streamlit as st
from streamlit_folium import folium_static
import pandas as pd
import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)

data = pd.read_json("alldata.json")
data["percentageGoodDays"] = data["Good Days"] / data["Days with AQI"]

loca = pd.read_csv("uscounties.csv")
latlong = loca.loc[loca['state_name'] == "California"].reset_index(drop=True)

data=data.rename(columns = {'County':'county'})
new = pd.merge(data, latlong, on='county')


new17=new.loc[new['Year'] == 2017]
new18=new.loc[new['Year'] == 2018]
new19=new.loc[new['Year'] == 2019]
new20=new.loc[new['Year'] == 2020]
new21=new.loc[new['Year'] == 2021]


st.title("Air Quality in California Counties")
yr = st.slider("Select Year", 2017, 2020)


if yr == 2017:
    import streamlit as st
    from streamlit_folium import folium_static
    import folium

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
            color=color_producer(new17.iloc[i]['percentageGoodDays']), tooltip = "Year: "+ str(new17.iloc[i]['Year'])+"<br> County: " + str(new17.iloc[i]['county'])+"<br> Percent of Good AQI Days/Year: " + str((int(new17.iloc[i]['percentageGoodDays']*100)))+"%", popup = new17.iloc[i]).add_to(m_17)

# Display the map
    folium_static(m_17)

elif yr == 2018:
   
# 2018
    import streamlit as st
    from streamlit_folium import folium_static
    import folium


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
            color=color_producer(new18.iloc[i]['percentageGoodDays']), tooltip = "Year: "+ str(new18.iloc[i]['Year'])+"<br> County: " + str(new18.iloc[i]['county'])+"<br> Percentage Good AQI Days/Year: " + str((int(new18.iloc[i]['percentageGoodDays']*100)))+"%", popup = new18.iloc[i]).add_to(m_18)

# Display the map
    folium_static(m_18)



elif yr == 2019:
    

# 2019
    import streamlit as st
    from streamlit_folium import folium_static
    import folium


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
            color=color_producer(new19.iloc[i]['percentageGoodDays']), tooltip = "Year: "+ str(new19.iloc[i]['Year'])+"<br> County: " + str(new19.iloc[i]['county'])+"<br> Percentage Good AQI Days/Year: " + str((int(new19.iloc[i]['percentageGoodDays']*100)))+"%", popup = new19.iloc[i]).add_to(m_19)

# Display the map
    folium_static(m_19)

elif yr == 2020:

# 2020
    import streamlit as st
    from streamlit_folium import folium_static
    import folium

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
            color=color_producer(new20.iloc[i]['percentageGoodDays']), tooltip = "Year: "+ str(new20.iloc[i]['Year'])+"<br> County: " + str(new20.iloc[i]['county'])+"<br> Percentage Good AQI Days/Year: " + str((int(new20.iloc[i]['percentageGoodDays']*100)))+"%", popup = new20.iloc[i]).add_to(m_20)

# Display the map
    folium_static(m_20)


new = new[new['Year'] != 2021]


width = st.sidebar.slider("plot width", 1, 100, 3)
height = st.sidebar.slider("plot height", 1, 40, 1)


import plotly.graph_objects as go

fig = go.Figure(data=[
    go.Bar(name='2017', x=new17['county'], y=new17['percentageGoodDays']),
    go.Bar(name='2018', x=new18['county'], y=new18['percentageGoodDays']),
    go.Bar(name='2019', x=new19['county'], y=new19['percentageGoodDays']),
    go.Bar(name='2020', x=new20['county'], y=new20['percentageGoodDays']),
])
# Change the bar mode
fig.update_layout(barmode='group')
st.plotly_chart(fig, use_container_width=True)



plt.figure(figsize=(5,5))
ax=sns.barplot(x='Year',y='Good Days',data=new)
ax.set(xlabel='Year', ylabel='Avg Good AQI Days')
st.pyplot()




