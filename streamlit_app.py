import streamlit as st


# 학생 정보
Grade = 1               # 학년
Major = "컴퓨터공학과"   # 학과
ID = "20001234"         # 학번
Student_Career = "미정"              # 희망직종
general_credits = 0     # 교양학점
major_credits = 0       # 전공학점


# 희망 직종
Career = ["미정", "프론트엔드", "백엔드", "임베디드", "보안", "인공지능"]

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
            st.text_input("학번", value=ID)
            st.text_input("학과", value = Major)
            st.text_input("학년", value = Grade)
            st.selectbox("희망직종 선택", Career, index=Career.index(Student_Career))
            #Student_Career = st.selectbox("희망직종", Career)

        with grade_col:
            grad_info = st.text_area("이수 정보 입력( EX: 과목명, 구분, 학점)", height=375)  # 이수한 과목 및 학점 입력

            # 교양과 전공 학점을 저장할 변수 초기화
            general_credits = 0
            major_credits = 0

            # 입력된 데이터를 줄별로 분리
            lines = grad_info.split('\n')

            # 각 줄을 처리
            for line in lines:
                if line.strip():  # 공백이 아닌 줄만 처리
                    parts = line.split(',')  # 쉼표로 데이터 분리
                    if len(parts) == 3:  # 정확히 세 부분으로 나뉘는지 확인
                        ##course_name = parts[0].strip()  # 과목명
                        category = parts[1].strip()  # 구분 (교양 혹은 전공)
                        credits = int(parts[2].strip())  # 학점

                        # 교양과 전공 학점 합산
                        if category == "교양":
                            general_credits += credits
                        elif category == "전공":
                            major_credits += credits

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
            process = st.button("저 장")
        
    if process : print("저장 완료")



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
                    text = "교양 : " + str(general_credits)
                    st.write(text)
                    
                with major:
                    text = "전공 : " + str(major_credits)
                    st.write(text)

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
