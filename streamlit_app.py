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

if toggle:
    st.session_state.show = not st.session_state.show

# 상태에 따라 정보 표시
if st.session_state.show:
    st.title("정보 입력")
    st.write("")
else:
    st.title("AI 컨설팅")
    st.write("")

# 스트림릿 사이드바 메뉴 설정
def main():
    st.sidebar.title("Navigation")
    menu = ["정보 입력", "AI 컨설팅"]
    choice = st.sidebar.radio("메뉴를 선택하세요:", menu)
    
    if choice == "정보 입력":
        page_one()
    elif choice == "AI 컨설팅":
        page_two()

def page_one():
    global general_credits, major_credits

    with st.form("my_form"):
        st.text_input("학번", value=ID)
        st.text_input("학과", value=Major)
        st.text_input("학년", value=str(Grade))
        career_choice = st.selectbox("희망직종 선택", Career, index=Career.index(Student_Career))
        grad_info = st.text_area("이수 정보 입력(예: 과목명, 구분, 학점)", height=375)

        # 입력된 데이터를 줄별로 분리
        lines = grad_info.split('\n')

        general_credits = 0
        major_credits = 0

        # 각 줄을 처리
        for line in lines:
            if line.strip():  # 공백이 아닌 줄만 처리
                parts = line.split(',')  # 쉼표로 데이터 분리
                if len(parts) == 3:  # 정확히 세 부분으로 나뉘는지 확인
                    category = parts[1].strip()  # 구분 (교양 혹은 전공)
                    credits = int(parts[2].strip())  # 학점

                    if category == "교양":
                        general_credits += credits
                    elif category == "전공":
                        major_credits += credits

        submitted = st.form_submit_button("저장")
        if submitted:
            st.session_state.page = "AI 컨설팅"
            st.experimental_rerun()

def page_two():
    st.write("희망 직종 : " + Student_Career)
    st.write("교양 : " + str(general_credits))
    st.write("전공 : " + str(major_credits))
    st.text_area("추천 강좌", height=200)
    st.text_area("AI의견", height=200)

if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state.page = "정보 입력"
    main()
