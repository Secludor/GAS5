import streamlit as st
import crawl

st.sidebar.title('Side Bar')
st.sidebar.header('로그인 정보')

forcast_list = ['단기 예보', '중기 예보']
kind = st. sidebar.radio('예보 종류를 선택해주세요 : ', forcast_list)
st.sidebar.write('종류 : ',kind)

location_list = ['전국', '서울/경기','강원','충청','전라','경상', '제주']
location = st.sidebar.selectbox('대상 지역을 선택해주세요 : ', location_list)
st.sidebar.write('대상 : ', location)

url, validate, content = crawl.searchWeather(kind, location)
st.write(url)
st.markdown(validate.prettify(),unsafe_allow_html=True)
st.markdown(content.prettify(),unsafe_allow_html=True)