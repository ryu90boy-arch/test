# 스트림릿 예제
import streamlit as st
import pandas as pd

# 제목
st.title("간단한 Streamlit 예제")

# 설명
st.write("첫 번째 Streamlit 앱입니다!")

# 사용자 입력
name = st.text_input("이름을 입력하세요")

# 버튼
if st.button("인사하기"):
    if name:
        st.success(f"안녕하세요, {name}님!")
    else:
        st.warning("이름을 입력해주세요.")

# 샘플 데이터
data = pd.DataFrame({
    "이름": ["철수", "영희", "민수"],
    "점수": [85, 92, 78]
})

# 테이블 표시
st.subheader("점수 테이블")
st.dataframe(data)

# 차트 표시
st.subheader("점수 차트")
st.bar_chart(data.set_index("이름"))