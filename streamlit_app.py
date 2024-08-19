import streamlit as st

# 학생 정보 초기화
if 'student_info' not in st.session_state:
    st.session_state.student_info = {
        'grade': 1,
        'major': "컴퓨터공학과",
        'student_id': "20001234",
        'student_career': "미정",
        'general_credits': 0,
        'major_credits': 0
    }

# 페이지 1: 정보 입력
def page_one():
    st.subheader("학생 정보")
    with st.container():
        student_info_col, grade_col = st.columns(2)

        with student_info_col:
            st.session_state.student_info['student_id'] = st.text_input("학번", value=st.session_state.student_info['student_id'])
            st.session_state.student_info['major'] = st.text_input("학과", value=st.session_state.student_info['major'])
            st.session_state.student_info['grade'] = st.number_input("학년", value=st.session_state.student_info['grade'], format="%d")
            st.session_state.student_info['student_career'] = st.selectbox("희망 직종 선택", ["미정", "프론트엔드", "백엔드", "임베디드", "보안", "인공지능"], index=["미정", "프론트엔드", "백엔드", "임베디드", "보안", "인공지능"].index(st.session_state.student_info['student_career']))

        with grade_col:
            grad_info = st.text_area("이수 정보 입력(입력방법: 과목명, 구분, 학점)", height=375)  # 이수한 과목 및 학점 입력

            # 입력된 데이터를 줄별로 분리
            lines = grad_info.split('\n')
            general_credits, major_credits = 0, 0

            # 각 줄을 처리
            for line in lines:
                if line.strip():  # 공백이 아닌 줄만 처리
                    parts = line.split(',')  # 쉼표로 데이터 분리
                    if len(parts) == 3:  # 정확히 세 부분으로 나뉘는지 확인
                        category = parts[1].strip()  # 구분 (교양 혹은 전공)
                        credits = int(parts[2].strip())  # 학점

                        # 교양과 전공 학점 합산
                        if category == "교양":
                            general_credits += credits
                        elif category == "전공":
                            major_credits += credits

            st.session_state.student_info['general_credits'] = general_credits
            st.session_state.student_info['major_credits'] = major_credits

        if st.button("저장"):
            st.session_state.page = "AI 컨설팅"

# 페이지 2: AI 컨설팅
def page_two():
    st.subheader("AI 컨설팅")

    student_id = int(st.session_state.student_info['student_id'])
    if student_id >= 20160000:
        required_general_credits = "/46"
        required_major_credits = "/42"
    else:
        required_general_credits = "/40"
        required_major_credits = "/46"

    
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.write("희망 직종 : ", st.session_state.student_info['student_career'])
        
        with col2:
            st.write("교양 학점 : ", st.session_state.student_info['general_credits'], required_general_credits)
            st.write("전공 학점 : ", st.session_state.student_info['major_credits'], required_major_credits)

    st.write("---")

    with st.container():
        col2_1, col2_2 = st.columns(2)

        with col2_1:
            st.text_area("추천 강좌", "프롬프트 값 출력", height=200)
        
        with col2_2:
            st.text_area("AI의견", "프롬프트 값 출력", height=200)

    

# 메인 함수
def main():
    if 'page' not in st.session_state:
        st.session_state.page = "정보 입력"

    page = st.sidebar.radio("MENU", ["정보 입력", "AI 컨설팅"], index=["정보 입력", "AI 컨설팅"].index(st.session_state.page))

    if page == "정보 입력":
        page_one()
    elif page == "AI 컨설팅":
        page_two()

if __name__ == "__main__":
    main()
