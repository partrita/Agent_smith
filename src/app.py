import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Streamlit 앱 설정
st.set_page_config(page_title="Agent Smith", page_icon=":robot:")

# 제목 표시
st.title("Agent Smith")


# Gemma3 모델 및 토크나이저 로드
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("google/gemma-3-1b-it")
    model = AutoModelForCausalLM.from_pretrained(
        "google/gemma-3-1b-it", device_map="auto", torch_dtype=torch.float16
    )
    return tokenizer, model


tokenizer, model = load_model()


def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=200)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response


# 채팅 입력 및 출력
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gemma3 모델 응답 생성
    response = generate_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
