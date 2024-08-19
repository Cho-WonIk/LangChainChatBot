import streamlit as st

# 사이드바에 토글 버튼 생성
toggle = st.sidebar

# 세션 상태 관리를 위해 스트림릿의 세션 상태 API 사용
if 'show' not in st.session_state:
    st.session_state.show = False

# 버튼이 눌렸을 때 상태 토글
if toggle:
    st.session_state.show = not st.session_state.show

# 상태에 따라 정보 표시
if st.session_state.show:
    st.write("학생 개인정보")
else:
    st.write("AI 컨설팅")


# 첫 번째 페이지 구성
def page_one():

    with st.container():
        col1, col2 = st.colums(2)

        with col1:
            st.write("첫 번째 박스")
            for i in range(10):  # 예제를 위한 반복 내용
                st.write(f"항목 {i + 1}")

        with col2:
            st.write("두 번째 박스")
            for i in range(10):  # 예제를 위한 반복 내용
                st.write(f"정보 {i + 1}")  

    with st.container():
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
    page = st.sidebar.radio("", ["첫 페이지", "두 번째 페이지"])

    if page == "첫 페이지":
        page_one()
    elif page == "두 번째 페이지":
        page_two()

if __name__ == "__main__":
    main()
