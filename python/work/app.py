import streamlit as st

if 'dead' not in st.session_state:
    st.session_state['dead'] = []

if 'alive' not in st.session_state:
    st.session_state['alive'] = []

if 'ejected' not in st.session_state:
    st.session_state['ejected'] = []

if 'selected_player' not in st.session_state:
    st.session_state['selected_player'] = ""

st.title('Among usノート')

# Create player list from text_area.

st.header('プレイヤー名記入')
players = st.text_area(
    "ここに参加者の名前を入力してください",
    placeholder="プレイヤー1\nプレイヤー2\nプレイヤー3\n..."
)
player_set = frozenset(players.split())
st.write('プレイヤー名一覧')
st.write(player_set)

# Clear dead player list

clear_flag = st.button("キル・追放情報をリセット")
if clear_flag:
    st.session_state['dead'] = []
    st.session_state['alive'] = []
    st.session_state['ejected'] = []

# Create dead player list

st.selectbox("プレイヤーを１人選んでください", options=player_set, key="selected_player")

col1_kill, col2_kill = st.columns(2)

with col1_kill:
    killed_flag = st.button("キル")
    if killed_flag:
        st.session_state['dead'].append(st.session_state["selected_player"])

with col2_kill:
    undo_flag = st.button("キルから1人戻す")
if undo_flag:
    if len(st.session_state['dead']) == 0:
        st.error("キルされたプレイヤーがいないため実行できません")
    else:
        st.session_state['dead'].pop(-1)

st.write(st.session_state['dead'])

# Create ejected player list

col1_eject, col2_eject = st.columns(2)
with col1_eject:
    ejected_flag = st.button("追放")
    if ejected_flag:
        st.session_state['ejected'].append(st.session_state["selected_player"])

with col2_eject:
    undo_ejected_flag = st.button("追放から1人戻す")
if undo_ejected_flag:
    if len(st.session_state['ejected']) == 0:
        st.error("追放されたプレイヤーがいないため実行できません")
    else:
        st.session_state['ejected'].pop(-1)

st.write(st.session_state['ejected'])

# Create alive player list

st.session_state['alive'] = [player for player in player_set if not player in (st.session_state['dead'] + st.session_state['ejected'])]
st.write(st.session_state['alive'])

# Infomation Expander

st.header("キル情報整理スペース")

for killed_player in st.session_state['dead']:
    with st.expander(killed_player):
        for alive_player in st.session_state['alive']:
            st.select_slider(
                f"{alive_player}が{killed_player}の犯行に関われる可能性",
                options=['確白', '少し白い', '不明', '少し怪しい','容疑者'],
                value='不明'
            )