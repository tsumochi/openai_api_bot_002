
import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "あなたは非常に優秀なAWS認定のソリューションアーキテクト -プロフェッショナル（Solutions Architect -Professional)です。"}
        ]

# チャットボットとやりとりする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    # model="gpt-3.5-turbo"
    # model="gpt-4-0613"
    
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages
    )  

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去


# ユーザーインターフェイスの構築
st.title("My AI Assistant For AWS")
st.write("ChatGPT 4 APIを使ったチャットボットです。")

#####
user_input_id = st.text_input("idを入力してください。", key="user_input_id")
if user_input_id = "tsumchi":
    user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)
else:
    st.write("idが正しくありません！")
####
    

# user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 直近のメッセージを上に
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🤖"

        st.write(speaker + ": " + message["content"])
st.title("usage")
st.write("URL: https://platform.openai.com/account/usage")
