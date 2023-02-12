import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image


st.set_page_config(page_title='Score Analysis')
st.header('Here you can see the score analysis of your test')
st.write(' ')
st.write(' ')
# col1, col2, col3 = st.columns(3)
# with col1:
st.image("understanding-your-cibil-score.jpg",width=550)

st.subheader('Adarsh\'s score is 69')


### --- LOAD DATAFRAME
excel_file = 'Score.xlsx'
sheet_name = 'Score_Data'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='B:D',
                   header=3)

df_participants = pd.read_excel(excel_file,
                                sheet_name= sheet_name,
                                usecols='F:G',
                                header=3)
df_participants.dropna(inplace=True)

# --- STREAMLIT SELECTION
company = df['Job_Role'].unique().tolist()
ages = df['Average_Score'].unique().tolist()
company1 = df['Company'].unique().tolist()

age_selection = st.slider('Average_Score:',
                        min_value= min(ages),
                        max_value= max(ages),
                        value=(min(ages),max(ages)))

company_selection = st.multiselect('Job_Role:',
                                   company,default=company)

st.title('Average scored required for given company')
mask = (df['Average_Score'].between(*age_selection)) & (df['Job_Role'].isin(company_selection))
number_of_result = df[mask].shape[0]
# st.markdown(f'*Available Results: {number_of_result}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['Company']).count()[['Average_Score']]
df_grouped = df_grouped.rename(columns={'Average_Score': 'Average_Score'})
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped,
                   x='Company',y='Average_Score',text='Average_Score',color_discrete_sequence = ['#F63366']*len(df_grouped),template= 'plotly_white')
st.plotly_chart(bar_chart)

# --- DISPLAY IMAGE & DATAFRAME

st.title('Cut-off for given companies')
st.dataframe(df[mask])


