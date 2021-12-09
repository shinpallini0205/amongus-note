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
    player_sorted = sorted(list(player_set))
    st.write('プレイヤー名一覧')
    st.write(player_sorted)
    st.write(f"登録人数: {len(player_sorted)}名")

    st.markdown("---")

# Clear dead player list

clear_flag = st.button("キル・追放情報をリセット")
if clear_flag:
    st.session_state['dead'] = []
    st.session_state['ejected'] = []

selected_player = st.radio("プレイヤーを１人選んでください", options=player_sorted)

# Create dead player list

col1_kill, col2_kill = st.columns(2)

with col1_kill:
    killed_flag = st.button("キルされた")

def player_validation(selected_player: str, key: str):
    """キル、追放されたプレイヤーを適切に登録するための検証を実行
    args:
        selected_player:ラジオボタンで選んだプレイヤー
        key:'dead'または'ejected'でどのセッション変数に保存するか指定
    
    example:
        player_validation(selected_player, 'dead')
    """
    success_messages = {
        'dead': f'{selected_player}をキルされたリストに追加しました',
        'ejected': f'{selected_player}を追放されたリストに追加しました'
    }
    if selected_player in st.session_state['dead']:
        return st.error(f"{selected_player}はすでにキルされたリストにいるため追加できません")
    elif selected_player in st.session_state['ejected']:
        return st.error(f"{selected_player}はすでに追放されたリストにいるため追加できません")
    else:
        st.session_state[key].append(selected_player)

with col2_kill:
    undo_flag = st.button("キルから1人戻す")

# Create ejected player list

col1_eject, col2_eject = st.columns(2)
with col1_eject:
    ejected_flag = st.button("追放された")

with col2_eject:
    undo_ejected_flag = st.button("追放から1人戻す")

# Check button flags

if killed_flag:
    player_validation(selected_player, 'dead')

if undo_flag:
    if len(st.session_state['dead']) == 0:
        st.error("キルされたプレイヤーがいないため実行できません")
    else:
        poped = st.session_state['dead'].pop(-1)

if ejected_flag:
    player_validation(selected_player, 'ejected')

if undo_ejected_flag:
    if len(st.session_state['ejected']) == 0:
        st.error("追放されたプレイヤーがいないため実行できません")
    else:
        poped = st.session_state['ejected'].pop(-1)

# Update player status(dead, ejected)
with st.sidebar:
    st.write("キルされたプレイヤー")
    st.write(st.session_state['dead'])

with st.sidebar:
    st.write("追放されたプレイヤー")
    st.write(st.session_state['ejected'])

# Create alive player list

alives = [player for player in player_sorted if not player in (st.session_state['dead'] + st.session_state['ejected'])]

with st.sidebar:
    st.write("生きているプレイヤー")
    st.write(alives)

# Infomation Expander

st.markdown("---")

st.header("キル情報整理スペース")

for index, killed_player in enumerate(st.session_state['dead']):
    st.markdown(f'**{index+1}キル目**')
    with st.expander(f"{killed_player}キルについて"):
        col1_deduce, _, col2_deduce = st.columns([5,1,5])
        for index, alive_player in enumerate(alives):
            if index % 2 == 0:
                with col1_deduce:
                    st.select_slider(
                    f"{alive_player}が{killed_player}の犯行に関われる可能性",
                    options=['確白', '少し白い', '不明', '少し怪しい','容疑者'],
                    value='不明'
                    )
            else:
                with col2_deduce:
                    st.select_slider(
                    f"{alive_player}が{killed_player}の犯行に関われる可能性",
                    options=['確白', '少し白い', '不明', '少し怪しい','容疑者'],
                    value='不明'
                    )