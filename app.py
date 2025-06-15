import pickle 
import streamlit as st
import requests
import os

st.header('Video Game Recommendation System Using Machine Learning')
video_games = pickle.load(open('artifacts/video_game_list.pkl', 'rb'))
similarity_score = pickle.load(open('artifacts/similarity.pkl', 'rb'))

video_game_list = video_games['name'].values
selected_vg = st.selectbox(
    'Select A Video Game for Recommendations',
    video_game_list
)

def recommend(video_game):
    index = video_games[video_games['name'] == video_game].index[0]
    distances = sorted(list(enumerate(similarity_score[index])), reverse=True, key = lambda x:x[1])
    recommended_vg_name = []
    recommended_vg_url = []
    for i in distances[1:6]:
        recommended_vg_name.append(video_games.iloc[i[0]]['name'])
        recommended_vg_url.append(video_games.iloc[i[0]]['urls'])
    return recommended_vg_name, recommended_vg_url

if st.button('Show Recommendations'):
    recommended_vg_name, recommended_vg_url = recommend(selected_vg)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_vg_name[0])
        st.write("[Click To View The Game](%s)" % recommended_vg_url[0])
    with col2:
        st.text(recommended_vg_name[1])
        st.write("[Click To View The Game](%s)" % recommended_vg_url[1])
    with col3:
        st.text(recommended_vg_name[2])
        st.write("[Click To View The Game](%s)" % recommended_vg_url[2])
    with col4:
        st.text(recommended_vg_name[3])
        st.write("[Click To View The Game](%s)" % recommended_vg_url[3])
    with col5:
        st.text(recommended_vg_name[4])
        st.write("[Click To View The Game](%s)" % recommended_vg_url[4])
