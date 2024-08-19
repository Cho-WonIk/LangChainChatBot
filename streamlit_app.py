import streamlit as st

# 첫 번째 페이지 구성
def page_one():
    with st.container():
        st.subheader("첫 번째 페이지")
        st.text_area("설명을 입력하세요", height=300)
        st.text_input("간단한 메모")
        st.text_area("AI 간단평", height=100)
        st.button("저장")

# 두 번째 페이지 구성
def page_two():
    with st.container():
        st.subheader("두 번째 페이지")
        st.checkbox("이주 간격")
        st.text("다음 메모")
        st.text_area("주요 내용", height=300)
        st.text_area("AI 의견", height=100)

# 스트림릿 앱 메인 실행 함수
def main():
    st.title("스트림릿 애플리케이션")
    page_one()
    st.write("---")  # 페이지 구분자
    page_two()

if __name__ == "__main__":
    main()
