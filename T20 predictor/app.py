import streamlit as st
import pickle
import numpy as np
import pandas as pd
pipe = pickle.load(open('pipe.pkl','rb'))
teams = ['Afghanistan', 'Australia', 'Bangladesh', 'England', 'India','New Zealand', 'Pakistan', 'South Africa', 'Sri Lanka', 'West Indies']
cities=['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'Cape Town',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Manchester',
 'Abu Dhabi',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Cardiff',
 'Christchurch',
 'Trinidad']
st.title('T20 Match Predictor')
col1, col2 = st.columns(2)
with col1:
    battinn_team=st.selectbox('Select Batting Team',sorted(teams))
    with col2:
        bowling_team=st.selectbox('Select Bowling Team',sorted(teams))

city = st.selectbox('Select City',sorted(cities))
col3, col4, col5 = st.columns(3)
with col3:
    current_score = st.number_input('Current Score')
with col4:
    over_done = st.number_input('Overs Done(works for over>5)')
with col5:
    wickets=st.number_input('Wickets Out')  
last_five=st.number_input('Runs Scored in Last 5 Overs')
if st.button('Predict Score'):
    balls_left = 120 - (over_done*6)
    wickets_left = 10 -wickets
    crr = current_score/over_done

    input_df = pd.DataFrame(
     {'batting_team': [battinn_team], 'bowling_team': [bowling_team],'city':city, 'current_score': [current_score],'balls_left': [balls_left], 'wickets_left': [wickets], 'crr': [crr], 'last_five': [last_five]})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))


