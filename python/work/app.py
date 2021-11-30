import streamlit as st

if 'dead' not in st.session_state:
    st.session_state['dead'] = []

if 'alive' not in st.session_state:
    st.session_state['alive'] = []

st.title('Among us Note')

"""Create player list from text_area.
"""
st.header('Player list')
players = st.text_area("Please write player name.")
player_list = players.split()
st.write('Player list')
st.write(player_list)


"""Clear dead player list
"""
clear_flag = st.button("Clear")
if clear_flag:
    st.session_state['dead'] = []
    st.session_state['alive'] = []


"""Create dead player list
"""

killed = st.selectbox("Select killed player...", options=player_list)
append_flag = st.button("Click me")
if append_flag:
    st.session_state['dead'].append(killed)

st.write(st.session_state['dead'])

"""Create alive player list
"""

st.session_state['alive'] = [player for player in player_list if not player in st.session_state['dead']]
st.write(st.session_state['alive'])

"""Expander test
"""

for killed_player in st.session_state['dead']:
    with st.expander(killed_player):
        for alive_player in st.session_state['alive']:
            st.slider(f"Possibility that {alive_player} killed {killed_player}")
