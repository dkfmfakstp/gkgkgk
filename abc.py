import pandas as pd

# Google Drive 링크에서 CSV 파일 다운로드
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
data = pd.read_csv(url)

# 데이터 확인
print(data.head())
import plotly.express as px

# 예시: 'x_column'과 'y_column'을 사용하여 산점도 생성
fig = px.scatter(data, x='x_column', y='y_column', title='산점도 예시')

# 그래프 표시
fig.show()
import streamlit as st

# 앱 제목
st.title('데이터 시각화 웹앱')

# 데이터 업로드 기능
uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head())

    # 시각화 옵션 선택
    x_axis = st.selectbox('X축 선택', options=data.columns)
    y_axis = st.selectbox('Y축 선택', options=data.columns)

    # 선택된 열로 산점도 생성
    fig = px.scatter(data, x=x_axis, y=y_axis, title=f'{x_axis} vs {y_axis}')
    st.plotly_chart(fig)
streamlit run app.py
