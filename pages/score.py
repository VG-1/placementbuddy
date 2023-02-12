import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image


st.set_page_config(page_title='Score Analysis')
st.header('hey! here you can see the score analysis of your test')
st.subheader('hope we are helpful to you :)')
st.subheader('Adarsh score is 69')


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
                                   company,
                                    default=company)

# --- FILTER DATAFRAME BASED ON SELECTION
mask = (df['Average_Score'].between(*age_selection)) & (df['Job_Role'].isin(company_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['Company']).count()[['Average_Score']]
df_grouped = df_grouped.rename(columns={'Average_Score': 'Average_Score'})
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped,
                   x='Company',
                   y='Average_Score',
                   text='Average_Score',
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)

# --- DISPLAY IMAGE & DATAFRAME
col1, col2 = st.columns(2)
image = Image.open('images/survey.jpg')
col1.image(image,
        caption='Designed by slidesgo / Freepik',
        use_column_width=True)
col2.dataframe(df[mask])

# --- PLOT PIE CHART
pie_chart = px.pie(df_participants,
                title='Total No. of Participants',
                values='Participants',
                names='Companies')

st.plotly_chart(pie_chart)
