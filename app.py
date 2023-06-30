
import streamlit as st
import openai

MODEL_3 = "gpt-3.5-turbo"
MODEL_4 = "gpt-4-0613"

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "あなたは非常に優秀なAWS認定のソリューションアーキテクト -プロフェッショナル（Solutions Architect -Professional)です。"}
        ]

# チャットボットとやりとりする関数
def communicate(Version):
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    model_selected = MODEL_3
    if Version == 4:
        model_selected = MODEL_4
    
    response = openai.ChatCompletion.create(
        model=model_selected,
        messages=messages
    )  

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去


# ユーザーインターフェイスの構築
st.title("My AI Assistant For AWS")
st.write("ChatGPT APIを使ったチャットボットです。")

version = st.radio('Version',('3.5','4'))
st.write(version)
#####
user_input_id = st.text_input("idを入力してください。", key="user_input_id")
if user_input_id in "tsumchi":
    user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate(version))
    if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 直近のメッセージを上に
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🤖"

        st.write(speaker + ": " + message["content"])
else:
    st.write("idが正しくありません！")
####
    

# user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)

# if st.session_state["messages"]:
#    messages = st.session_state["messages"]

#    for message in reversed(messages[1:]):  # 直近のメッセージを上に
#        speaker = "🙂"
#        if message["role"]=="assistant":
#            speaker="🤖"

#        st.write(speaker + ": " + message["content"])

st.title("usage")
st.write("URL: https://platform.openai.com/account/usage")
