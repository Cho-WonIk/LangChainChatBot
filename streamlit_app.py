import streamlit as st

# 첫 번째 페이지 구성
def page_one():
    with st.container():
        st.text_area("설명을 입력하세요", height=300)
        st.text_input("간단한 메모")

    with st.container():
        st.text_area("AI 간단평", height=100)

    st.button("저장")

# 두 번째 페이지 구성
def page_two():
    with st.container():
        st.checkbox("이주 간격")
        st.text("다음 메모")
    
    with st.container():
        st.text_area("주요 내용", height=300)

    with st.container():
        st.text_area("AI 의견", height=100)

# 스트림릿 사이드바 메뉴 설정
def main():
    page = st.sidebar.selectbox("페이지 선택", ["첫 페이지", "두 번째 페이지"])

    if page == "첫 페이지":
        page_one()
    elif page == "두 번째 페이지":
        page_two()

if __name__ == "__main__":
    main()
