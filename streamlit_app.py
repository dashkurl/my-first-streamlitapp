# Standard imports
import pandas as pd

# matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
#import seaborn as sns
#plotly
import plotly.express as px
import plotly.graph_objects as go

import streamlit as st
from copy import deepcopy
st.title("Internet usage compared")

#df = pd.read_csv("./data/mpg.csv")

@st.cache_data
def load_data(path):
    df=pd.read_csv(path)
    return df


internet_access=load_data(path="./share-of-individuals.csv")
internet_access_df=deepcopy(internet_access)

countries=[]
year_recent=[]
for i,year in internet_access_df.groupby("Code"):
    countries.append(i)
    year_recent.append(year["Year"].max())
    


#Combine both the names of the countries and the most recent year.
years_index=pd.DataFrame({"Code":countries,"most_recent":year_recent})

recent_df = pd.merge(years_index,internet_access)
#print(recent_df)
recent_df1=recent_df[recent_df["Year"]==2017]
old_df=recent_df[recent_df["Year"]==2000]
#recent_df=recent_df[recent_df["Year"]]
#recent_df = recent_p[recent_perc["Year"]==recent_perc["most_recent_year"]]

#recent_df1
#old_df
year=st.selectbox("Choose a year",[2000,2017])

if year == 2000:
    
    st.title("Internet usage 2000")
    fig=px.choropleth(
    old_df,
    locations="Code",
    color="Individuals using the Internet (% of population)",
    
    width=800,
    height=400,
    labels={"Individuals using the Internet (% of population)":"% of Population",
           "most_recent_year":"Year"},
    hover_name="Entity",
    hover_data={"Code": False,
                "most_recent":False,
                "Individuals using the Internet (% of population)":':.1f'},
    title="<b>Percentage of Population on the Internet</b>",
    color_continuous_scale="Earth",
    )

    fig.update_traces(marker={"opacity":0.7})

    fig.update_layout(margin={"r":25,"t":35,"l":0,"b":0},
                  font_family="Rockwell",
                  hoverlabel={"bgcolor":"white", 
                              "font_size":12,
                             "font_family":"Rockwell"},
                  title={"font_size":20,
                        "xanchor":"left", "x":0,
                        "yanchor":"top"},
                  geo={"resolution":50,
                      "showlakes":True, "lakecolor":"lightblue", 
                       "showocean":True, "oceancolor":"aliceblue"
                      }
                 )

    st.plotly_chart(fig)
    

elif year== 2017: 
    st.title("Internet usage :2017")
    fig=px.choropleth(
    recent_df1,
    locations="Code",
    color="Individuals using the Internet (% of population)",
    
    width=800,
    height=400,
    labels={"Individuals using the Internet (% of population)":"% of Population",
           "most_recent_year":"Year"},
    hover_name="Entity",
    hover_data={"Code": False,
                "most_recent":False,
                "Individuals using the Internet (% of population)":':.1f'},
    title="<b>Percentage of Population on the Internet</b>",
    color_continuous_scale="Earth",
    )

    fig.update_traces(marker={"opacity":0.5})

    fig.update_layout(margin={"r":25,"t":35,"l":0,"b":0},
                  font_family="Rockwell",
                  hoverlabel={"bgcolor":"white", 
                              "font_size":12,
                             "font_family":"Rockwell"},
                  title={"font_size":20,
                        "xanchor":"left", "x":0,
                        "yanchor":"top"},
                  geo={"resolution":50,
                      "showlakes":True, "lakecolor":"lightblue", 
                       "showocean":True, "oceancolor":"aliceblue"
                      }
                 )

    st.plotly_chart(fig)
    
    
