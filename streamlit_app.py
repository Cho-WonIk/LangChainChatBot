import streamlit as st

##openai_api_key = st.secrets["openai_api_key"]

#prompt = ""

def call_openai_api(text):
    # st.secrets를 통해 API 키를 가져옵니다.
    openai_api_key = st.secrets["openai_api_key"]
    # OpenAI API 호출
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # 사용할 모델, 필요에 따라 다른 모델로 변경 가능
        prompt=text,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# 학생 정보
Grade = 1               # 학년
Major = "컴퓨터공학과"   # 학과
ID = "20001234"         # 학번
Student_Career = "미정"              # 희망직종

# 희망 직종
Career = ["미정", "프론트엔드", "백엔드", "자바", "c언어", "인공지능"]

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
        student_info_col, grade_col = st.columns(2)

        with student_info_col:
            st.text_input("학생 정보")
            ID = st.text_input("학번")
            Major = st.text_input("학과")
            Grade = st.text_input("학년")
            Student_Career = st.selectbox("희망직종", Career)

        with grade_col:
            grad_info = st.text_area("이수 정보 입력", height=375) 

    with st.container():
        empty_col1, empty_col2, empty_col3, empty_col4, empty_col5, empty_col6, empty_col7, save_toggle_col = st.columns(8)

        with empty_col1:
            st.write("")
        
        with empty_col2:
            st.write("")
        
        with empty_col3:
            st.write("")

        with empty_col4:
            st.write("")

        with empty_col5:
            st.write("")
        
        with empty_col6:
            st.write("")

        with empty_col7:
            st.write("")

        with save_toggle_col:
            st.button("저 장")



# 두 번째 페이지 구성
def page_two():
    with st.container():
        Career_info_col, requirements_col = st.columns(2)

        with Career_info_col:
            text = "희망 직종 : " + Student_Career
            st.write(text)

        with requirements_col:
            st.write("이수 조건")
            with st.container():
                general, major = st.columns(2)

                with general:
                    st.text("교양 : ")
                    
                with major:
                    st.text("전공 : ")

    st.write("---")

    with st.container():
        Career_recommended_col, ai_result_col = st.columns(2)
        with Career_recommended_col:
            st.text_area("추천 강좌", height=200)
        
        with ai_result_col:
            st.text_area("AI의견", height=200)


# 스트림릿 사이드바 메뉴 설정
def main():
    page = st.sidebar.radio("MENU", ["정보 입력", "AI 컨설팅"])

    if page == "정보 입력":
        page_one()
    elif page == "AI 컨설팅":
        page_two()

if __name__ == "__main__":
    main()
