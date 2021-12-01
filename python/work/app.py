import streamlit as st

# Set session_state dictonary.

if 'dead' not in st.session_state:
    st.session_state['dead'] = []

if 'ejected' not in st.session_state:
    st.session_state['ejected'] = []


st.caption("Created by shinpallini0205")
st.title('Among usノート')

# Create player list from text_area.
with st.sidebar:
    st.header('プレイヤー名記入')
    players = st.text_area(
        "ここに参加者の名前を入力してください",
        placeholder="プレイヤー1\t\nプレイヤー2\t\nプレイヤー3\t\n..."
    )
    player_set = frozenset(players.split())
    st.write('プレイヤー名一覧')
    st.write(player_set)

# Clear dead player list

clear_flag = st.button("キル・追放情報をリセット")
if clear_flag:
    st.session_state['dead'] = []
    st.session_state['ejected'] = []

selected_player = st.radio("プレイヤーを１人選んでください", options=player_set)

# Create dead player list

col1_kill, col2_kill = st.columns(2)

with col1_kill:
    killed_flag = st.button("キルされた")
    if killed_flag:
        st.session_state['dead'].append(selected_player)

with col2_kill:
    undo_flag = st.button("キルから1人戻す")
if undo_flag:
    if len(st.session_state['dead']) == 0:
        st.error("キルされたプレイヤーがいないため実行できません")
    else:
        st.session_state['dead'].pop(-1)

with st.sidebar:
    st.write("キルされたプレイヤー")
    st.write(st.session_state['dead'])

# Create ejected player list

col1_eject, col2_eject = st.columns(2)
with col1_eject:
    ejected_flag = st.button("追放された")
    if ejected_flag:
        st.session_state['ejected'].append(selected_player)

with col2_eject:
    undo_ejected_flag = st.button("追放から1人戻す")
if undo_ejected_flag:
    if len(st.session_state['ejected']) == 0:
        st.error("追放されたプレイヤーがいないため実行できません")
    else:
        st.session_state['ejected'].pop(-1)

with st.sidebar:
    st.write("追放されたプレイヤー")
    st.write(st.session_state['ejected'])

# Create alive player list

alives = [player for player in player_set if not player in (st.session_state['dead'] + st.session_state['ejected'])]

with st.sidebar:
    st.write("生きているプレイヤー")
    st.write(alives)

# Infomation Expander

st.header("キル情報整理スペース")

for killed_player in st.session_state['dead']:
    with st.expander(killed_player):
        for alive_player in alives:
            st.select_slider(
                f"{alive_player}が{killed_player}の犯行に関われる可能性",
                options=['確白', '少し白い', '不明', '少し怪しい','容疑者'],
                value='不明'
            )