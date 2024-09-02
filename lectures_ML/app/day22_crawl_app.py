import streamlit as st
import crawl

st.sidebar.title('Side Bar')
st.sidebar.header('로그인 정보')
user_id = st.sidebar.text_input('아이디 입력 : ', value='streamlit', max_chars=15)
user_pw = st.sidebar.text_input('비밀번호 입력 : ', value='1234', max_chars=15)

st.sidebar.header('크롤링 사이트 선택')
news_list = ['NY Times', '동아일보']
selected = st.sidebar.selectbox('크롤링 대상을 선택해주세요 : ', news_list)
st.sidebar.write('대상 : ', selected)

st.title('Main Window')
select_idx = news_list.index(selected)
st.write('대상 : ', select_idx)

if st.button('Get News Title'):
    if select_idx==0:
        title = crawl.getNewsTitle('ny')
    elif select_idx==1:
        title = crawl.getNewsTitle('donga')
    st.write(title)