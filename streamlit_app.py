import streamlit as st

# 첫 페이지 설정
def page_one():
    st.sidebar.title("메뉴")
    menu_items = ["홈", "보드", "분석", "설정", "로그아웃"]
    for item in menu_items:
        st.sidebar.button(item)
    
    with st.container():
        st.text_area("설명을 입력하세요", height=300)
        st.text_input("간단한 메모")

    with st.container():
        st.text_area("AI 간단평", height=100)

    st.button("저장")

# 두 번째 페이지 설정
def page_two():
    st.sidebar.checkbox("이주 간격")
    st.sidebar.text("다음 메모")
    
    with st.container():
        st.text_area("주요 내용", height=300)

    with st.container():
        st.text_area("AI 의견", height=100)

# 앱 실행
if __name__ == "__main__":
    page = st.sidebar.selectbox("페이지 선택", ["첫 페이지", "두 번째 페이지"])

    if page == "첫 페이지":
        page_one()
    elif page == "두 번째 페이지":
        page_two()