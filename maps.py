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
import requests

st.set_page_config(layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)


url = "https://dsci551-7ef30-default-rtdb.firebaseio.com/.json"
response = requests.get(url)
d = response.json()
data = pd.DataFrame.from_dict(d)


data["percentageGoodDays"] = data["Good Days"] / data["Days with AQI"]

new=data.rename(columns = {'County':'county'})

new['UH Days'] = new['Unhealthy Days'] + new['Very Unhealthy Days']

new17=new.loc[new['Year'] == 2017]
new18=new.loc[new['Year'] == 2018]
new19=new.loc[new['Year'] == 2019]
new20=new.loc[new['Year'] == 2020]
new21=new.loc[new['Year'] == 2021]


st.title("Air Quality in California Counties")
st.text("Please select a year.")
st.text("This map shows the percentage of Good Air Quality Index Days per year in each county.")
st.text("The green dots are counties with above average AQI days per year, while the red dots are counties below average.")
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




import plotly.graph_objects as go

fig = go.Figure(data=[
    go.Bar(name='2017', x=new17['county'], y=new17['percentageGoodDays']),
    go.Bar(name='2018', x=new18['county'], y=new18['percentageGoodDays']),
    go.Bar(name='2019', x=new19['county'], y=new19['percentageGoodDays']),
    go.Bar(name='2020', x=new20['county'], y=new20['percentageGoodDays']),
])
# Change the bar mode
fig.update_layout(barmode='group',
    title="Percentage of Good AQI Days by County per Year",
    xaxis_title="County",
    yaxis_title="Percentage of Good AQI Days",
    legend_title="Year")
st.plotly_chart(fig, use_container_width=True)


option = st.selectbox("AQI Level of Concern", ("Moderate", "Unhealthy for Sensitive Groups", "Unhealthy"))

if option == "Moderate":
    fig = go.Figure(data=[
    go.Bar(name='2017', x=new17['county'], y=new17['Moderate Days']),
    go.Bar(name='2018', x=new18['county'], y=new18['Moderate Days']),
    go.Bar(name='2019', x=new19['county'], y=new19['Moderate Days']),
    go.Bar(name='2020', x=new20['county'], y=new20['Moderate Days']),
    ])
# Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()

    fig.update_layout(barmode='group',
    title="Moderate AQI Days by County per Year",
    xaxis_title="County",
    yaxis_title="Number of Moderate AQI Days",
    legend_title="Year")
    st.plotly_chart(fig, use_container_width=True)


elif option == "Unhealthy for Sensitive Groups":
    fig = go.Figure(data=[
    go.Bar(name='2017', x=new17['county'], y=new17['Unhealthy for Sensitive Groups Days']),
    go.Bar(name='2018', x=new18['county'], y=new18['Unhealthy for Sensitive Groups Days']),
    go.Bar(name='2019', x=new19['county'], y=new19['Unhealthy for Sensitive Groups Days']),
    go.Bar(name='2020', x=new20['county'], y=new20['Unhealthy for Sensitive Groups Days']),
    ])
# Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()

    fig.update_layout(barmode='group',
    title="Unhealthy for Sensitive Groups AQI Days by County per Year",
    xaxis_title="County",
    yaxis_title="Number of Unhealthy for Sensitive Groups AQI Days",
    legend_title="Year")
    st.plotly_chart(fig, use_container_width=True)


elif option == "Unhealthy":
    fig = go.Figure(data=[
    go.Bar(name='2017', x=new17['county'], y=new17['UH Days']),
    go.Bar(name='2018', x=new18['county'], y=new18['UH Days']),
    go.Bar(name='2019', x=new19['county'], y=new19['UH Days']),
    go.Bar(name='2020', x=new20['county'], y=new20['UH Days']),
    ])
# Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()

    fig.update_layout(barmode='group',
    title="Unhealthy AQI Days by County per Year",
    xaxis_title="County",
    yaxis_title="Number of Unhealthy AQI Days",
    legend_title="Year")
    st.plotly_chart(fig, use_container_width=True)



option2 = st.selectbox("Specific Toxins", ("Carbon Dioxide (CO2)", "Nitrogen Dioxide (NO2)", "Ozone", "PM10", "PM2.5", "Sulfur Dioxide (SO2)"))



if option2 == "Carbon Dioxide (CO2)":
    fig = go.Figure(data=[
    go.Bar(name='2017', x=new17['county'], y=new17['Days CO']),
    go.Bar(name='2018', x=new18['county'], y=new18['Days CO']),
    go.Bar(name='2019', x=new19['county'], y=new19['Days CO']),
    go.Bar(name='2020', x=new20['county'], y=new20['Days CO']),
    ])
# Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()

    fig.update_layout(barmode='group',
    title="Days Carbon Dioxide Present by County per Year",
    xaxis_title="County",
    yaxis_title="Number of Carbon Dioxide Present Days",
    legend_title="Year")
    st.plotly_chart(fig, use_container_width=True)


elif option2 == "Nitrogen Dioxide (NO2)":
    fig = go.Figure(data=[
    go.Bar(name='2017', x=new17['county'], y=new17['Days NO2']),
    go.Bar(name='2018', x=new18['county'], y=new18['Days NO2']),
    go.Bar(name='2019', x=new19['county'], y=new19['Days NO2']),
    go.Bar(name='2020', x=new20['county'], y=new20['Days NO2']),
    ])
# Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()

    fig.update_layout(barmode='group',
    title="Days Nitrogen Dioxide Present by County per Year",
    xaxis_title="County",
    yaxis_title="Number Nitrogen Dioxide Present Days",
    legend_title="Year")
    st.plotly_chart(fig, use_container_width=True)


elif option2 == "Ozone":
    fig = go.Figure(data=[
    go.Bar(name='2017', x=new17['county'], y=new17['Days Ozone']),
    go.Bar(name='2018', x=new18['county'], y=new18['Days Ozone']),
    go.Bar(name='2019', x=new19['county'], y=new19['Days Ozone']),
    go.Bar(name='2020', x=new20['county'], y=new20['Days Ozone']),
    ])
# Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()

    fig.update_layout(barmode='group',
    title="Ozone Days Present by County per Year",
    xaxis_title="County",
    yaxis_title="Number of Ozone Days",
    legend_title="Year")
    st.plotly_chart(fig, use_container_width=True)


elif option2 == "PM10":
    fig = go.Figure(data=[
    go.Bar(name='2017', x=new17['county'], y=new17['Days PM10']),
    go.Bar(name='2018', x=new18['county'], y=new18['Days PM10']),
    go.Bar(name='2019', x=new19['county'], y=new19['Days PM10']),
    go.Bar(name='2020', x=new20['county'], y=new20['Days PM10']),
    ])
# Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()

    fig.update_layout(barmode='group',
    title="Days PM10 Present by County per Year",
    xaxis_title="County",
    yaxis_title="Number of PM10 Present Days",
    legend_title="Year")
    st.plotly_chart(fig, use_container_width=True)


elif option2 == "PM2.5":
    fig = go.Figure(data=[
    go.Bar(name='2017', x=new17['county'], y=new17['Days PM2andhalf']),
    go.Bar(name='2018', x=new18['county'], y=new18['Days PM2andhalf']),
    go.Bar(name='2019', x=new19['county'], y=new19['Days PM2andhalf']),
    go.Bar(name='2020', x=new20['county'], y=new20['Days PM2andhalf']),
    ])
# Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()

    fig.update_layout(barmode='group',
    title="Days PM2.5 Present by County per Year",
    xaxis_title="County",
    yaxis_title="Number PM2.5 Present Days",
    legend_title="Year")
    st.plotly_chart(fig, use_container_width=True)


elif option2 == "Sulfur Dioxide (SO2)":
    fig = go.Figure(data=[
    go.Bar(name='2017', x=new17['county'], y=new17['Days SO2]),
    go.Bar(name='2018', x=new18['county'], y=new18['Days SO2']),
    go.Bar(name='2019', x=new19['county'], y=new19['Days SO2']),
    go.Bar(name='2020', x=new20['county'], y=new20['Days SO2']),
    ])
# Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()

    fig.update_layout(barmode='group',
    title="Days Sulfur Dioxide Present by County per Year",
    xaxis_title="County",
    yaxis_title="Number of Sulfur Dioxide Present Days",
    legend_title="Year")
    st.plotly_chart(fig, use_container_width=True)



















