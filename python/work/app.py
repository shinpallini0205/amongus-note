import streamlit as st

if 'status' not in st.session_state:
    st.session_state['status'] = {}

st.title('Among us Note')

"""Create player list from text_area.
"""
st.header('Player list')
players = st.text_area("Please write player name.")
player_list = players.split()
st.write('Player list')
st.write(player_list)

"""Create player status dictionaly.
"""
st.session_state['status'] = {k: v for k, v in zip(player_list, [1]*len(player_list))}
st.write(st.session_state['status'])

"""Expander test
"""
for k, v in st.session_state['status'].items():
    with st.expander(k):
        st.write(f'Player name: {k}, Player_status: {v}')
        st.slider(f'{k}')
