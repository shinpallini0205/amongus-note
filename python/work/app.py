import streamlit as st

if 'dead' not in st.session_state:
    st.session_state['dead'] = []

if 'alive' not in st.session_state:
    st.session_state['alive'] = []

st.title('Among usノート')

# Create player list from text_area.

st.header('プレイヤー名記入')
players = st.text_area(
    "ここに参加者の名前を入力してください",
    placeholder="プレイヤー1\nプレイヤー2\nプレイヤー3\n..."
)
player_list = players.split()
st.write('プレイヤーリスト')
st.write(player_list)

# Clear dead player list

clear_flag = st.button("キルされたプレイヤー情報をリセット")
if clear_flag:
    st.session_state['dead'] = []
    st.session_state['alive'] = []


# Create dead player list

killed = st.selectbox("今回キルされたのは...", options=player_list)
append_flag = st.button("送信")
if append_flag:
    st.session_state['dead'].append(killed)

undo_flag = st.button("１人戻す")
if undo_flag:
    st.session_state['dead'].pop(-1)

st.write(st.session_state['dead'])

# Create alive player list

st.session_state['alive'] = [player for player in player_list if not player in st.session_state['dead']]
st.write(st.session_state['alive'])

# Expander test

for killed_player in st.session_state['dead']:
    with st.expander(killed_player):
        for alive_player in st.session_state['alive']:
            st.select_slider(
                f"{alive_player}が{killed_player}の犯行に関われる可能性",
                options=['確白', '少し白い', '不明', '少し怪しい','容疑者'],
                value='不明'
            )