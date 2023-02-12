import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Survey Results')
st.header('heyooo here is shining statisitics of our placements')
st.subheader('hope we are helpful to you :)')

### --- LOAD DATAFRAME
excel_file = 'Survey_Results.xlsx'
sheet_name = 'DATA'

df = pd.read_excel(excel_file,sheet_name=sheet_name,usecols='B:D',header=3)

df_participants = pd.read_excel(excel_file,sheet_name= sheet_name,usecols='F:G',header=3)
df_participants.dropna(inplace=True)

# --- STREAMLIT SELECTION
company = df['Company'].unique().tolist()
ages = df['Year'].unique().tolist()

age_selection = st.slider('Year:', min_value= min(ages), max_value= max(ages), value=(min(ages),max(ages)))

company_selection = st.multiselect('Company:', company,default=company)

# --- FILTER DATAFRAME BASED ON SELECTION
mask = (df['Year'].between(*age_selection)) & (df['Company'].isin(company_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['Job_Role']).count()[['Year']]
df_grouped = df_grouped.rename(columns={'Year': 'Placed_Students'})
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped, x='Job_Role', y='Placed_Students', text='Placed_Students', color_discrete_sequence = ['#F63366']*len(df_grouped), template= 'plotly_white')
st.plotly_chart(bar_chart)
  