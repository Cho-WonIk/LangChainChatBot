import streamlit as st
import json
from langchain_openai import ChatOpenAI

# 스트림릿 페이지 설정
st.title("LangChain을 이용한 JSON 파일 내 텍스트 처리")

# API 키 입력
api_key = st.text_input("OpenAI API 키를 입력하세요:", type="password")

# 파일 업로더 생성
uploaded_file = st.file_uploader("JSON 파일을 업로드하세요", type=['json'])

# API 키와 파일이 모두 제공된 경우 처리 진행
if api_key and uploaded_file:
    # ChatOpenAI 모델 초기화
    llm = ChatOpenAI(api_key=api_key, model="gpt-4o-mini")

    # JSON 파일 읽기
    data = json.load(uploaded_file)
    
    # JSON에서 텍스트 프롬프트 추출 (JSON 구조에 따라 수정이 필요할 수 있음)
    if "prompt" in data:
        prompt_text = data["prompt"]
        st.write("처리할 프롬프트:", prompt_text)
        
        # 프롬프트 처리 버튼
        if st.button("프롬프트 처리"):
            # ChatOpenAI를 이용하여 프롬프트 처리
            result = llm.complete(prompt_text)
            # 결과 출력
            st.write("결과:", result)
    else:
        st.error("JSON 파일에 'prompt' 키가 없습니다.")
