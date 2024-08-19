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
    st.title("정보 입력")
    st.write("")
else:
    st.title("AI 컨설팅")
    st.write("")


# 첫 번째 페이지 구성
def page_one():

    with st.container():
        student_info, grade = st.columns(2)

        with student_info:
            st.text_input("학생 정보")
            st.text_input("학번")
            st.text_input("학과")
            st.text_input("학년")
            st.text_input("희망직종")

        with grade:
            grad_info = st.text_area("이수 정보 입력", height=400) 

    with st.container():
        empty_col, save_toggle = st.columns(2)

        with empty_col:
            st.write("   ")

        with save_toggle:
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
    page = st.selectbox(
        "Menu",
        ["페이지1", "페이지2"]
    )

    if page == "첫 페이지":
        page_one()
    elif page == "두 번째 페이지":
        page_two()

if __name__ == "__main__":
    main()
