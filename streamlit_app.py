import streamlit as st
import json
#from langchain.chains import OpenAIChain  # LangChain에서 OpenAI 모듈 사용 예시
from langchain.chat_models import OpenAIChain

# 스트림릿 페이지 설정
st.title("JSON 파일 처리")

# 파일 업로더 생성
uploaded_file = st.file_uploader("JSON 파일을 업로드하세요", type=['json'])

# 파일이 업로드되면 내용을 처리
if uploaded_file is not None:
    # JSON 파일 읽기
    data = json.load(uploaded_file)
    
    # LangChain 설정 및 사용 예시
    lc = OpenAIChain()  # 예시로 OpenAI 모델을 사용하는 LangChain 인스턴스 생성
    result = lc.complete_prompt("Here is a sample prompt")  # 간단한 프롬프트로 완성 시도
    
    # 결과 출력
    st.write("처리된 데이터:", data)
    st.write("LangChain 결과:", result)

# 스트림릿 실행을 위해 터미널에서 `streamlit run your_script.py` 실행
