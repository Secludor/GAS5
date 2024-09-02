import streamlit as st

st.title('title : Hello World!')
st.header('header : Hello World!')
st.subheader('subheader : Hello World!')
st.text('text : Hello World!')

st.markdown('<style>h1 {font-size: 50px;}</style>', unsafe_allow_html=True)
st.markdown('# 파이썬 코드를 출력할 수 있습니다.', unsafe_allow_html=False)
st.markdown('## 파이썬 코드를 출력할 수 있습니다.', unsafe_allow_html=False)
st.markdown('### 파이썬 코드를 출력할 수 있습니다.', unsafe_allow_html=False)

st. markdown('''```python
def say_hello():
    print('Hello, World!')
    ```''')

my_code = '''
def say_hello():
    print('Hello, World!')
'''

st.code(my_code)

st. markdown(f'''```python
{my_code}```
    ''')

st.markdown(f'<div style="font-size: 18px; font-family: monospace; '
f'background-color: green; padding: 10px; border-radius: 5px;">'
f'```{my_code}```</div>', unsafe_allow_html=True) 

import pandas as pd

path = 'D:\\elice_python\\GAS_5\\pytest\\'
data_path = path + 'iris.csv'

df = pd.read_csv(data_path)

st.title('Streamlit Data')
st.subheader('st.dataframe() 사용하기')
st.dataframe(df)

df1 = df.iloc[:,[1,2]] # 행 전체, 1,2열

st.subheader('line, area, bar chart')
st.line_chart(df1)
st.area_chart(df1)
st.bar_chart(df1)

import matplotlib

st.markdown('## 한글 폰트 설정')
#한글 폰트 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False
month = range(1, 13) # range(include:exclude)
amount = [100, 110, 130, 150, 120, 140, 170, 180, 150, 160, 200, 210]
df = pd.DataFrame(amount, index=month)
ax = df.plot(grid=True, figsize=(10, 5))
ax.legend(['월별 생산량'], fontsize=10)
ax.set_title('생산 현황', fontsize=20)
ax.set_xlabel('월', fontsize=15)
ax.set_ylabel('생산량', fontsize=15)
fig = ax.get_figure()
st.subheader('월별 생산량 그래프')
st.pyplot(fig)

st.subheader('st.write()')

# st.write('# 하나')
# st.markdown('# 하나')
st.write('## 두울')
st.markdown('## 두울')
st.write('### 세엣')
st.markdown('### 세엣')
# st.write('#### 네엣')
# st.markdown('#### 네엣')
# st.write('##### 다섯')
# st.markdown('##### 다섯')
# st.write('###### 여섯')
# st.markdown('###### 여섯')

st.write('### st.write()는 여러 데이터 타입을 출력할 수 있다.')
st.write("#### 월별 생산량 그래프", fig) 

from PIL import Image

st.title('이미지 띄우기')

img_path = 'D:\elice_python\GAS_5\pytest_img\images\Abyssinian_2.jpg'

img = Image.open(img_path)

st.image(img, width=300, caption='고양이')


st.title('입력 도구')
st.header('버튼')

clicked1 = st.button('버튼 1')
st.write('버튼 1 상태 : ', clicked1)

if clicked1:
    st.write('버튼 1을 클릭했습니다.')
else:
    st.write('버튼 1을 클릭하지 않았습니다.')
    
clicked2 = st.button('버튼 2')
st.write('버튼 2 상태 : ', clicked2)

if clicked2:
    st.write('버튼 2를 클릭했습니다.')
else:
    st.write('버튼 2를 클릭하지 않았습니다.')
    
    
st.header('체크박스')

checked1 = st.checkbox('체크박스 1')
st.write('체크박스 1 상태 : ', checked1)

if checked1:
    st.write('체크박스 1을 클릭했습니다.')
else:
    st.write('체크박스 1을 클릭하지 않았습니다.')
    
checked2 = st.checkbox('체크박스 2')
st.write('체크박스 2 상태 : ', checked2)

if checked2:
    st.write('체크박스 2를 클릭했습니다.')
else:
    st.write('체크박스 2를 클릭하지 않았습니다.')
    
    
st.header('라디오 버튼')

radio1_options = [10,20,30,'40']
selected1 = st.radio('(1) 당신의 연령대는? ', radio1_options)
st.write('선택 연령대 : ', selected1)

radio2_options = ['학생', '교사', '회사원', '자영업', '무직']
selected2 = st.radio('(2) 당신의 직업은? ', radio2_options)
st.write('선택 직업군 : ', selected2)

    
st.header('셀렉트 박스')

select1_options = [10,'20',30,'40']
selected1 = st.selectbox('(1) 당신의 연령대는? ', select1_options)
st.write('선택 연령대 : ', selected1)

select2_options = ['학생', '교사', '회사원', '자영업', '무직']
selected2 = st.selectbox('(2) 당신의 직업은? ', select2_options)
st.write('선택 직업군 : ', selected2)


st.header('로그인')

user_id = st.text_input('아이디 입력 : ', value='streamlit', max_chars=15)
user_pw = st.text_input('아이디 입력 : ', value='???????', type='password')

if user_id == 'streamlit':
    if user_pw == '1234':
        st.write('로그인 되었습니다.')
    else:
        st.write('ID나 PW를 확인하세요')
else:
    st.write('ID나 PW를 확인하세요')
    
    
st.header('숫자 입력')

num1 = st.number_input('나이를 입력하세요 : ', min_value=1, max_value=120, value=10)
st.write('입력받은 나이 : ', num1)

height = st.number_input('키(cm)를 입력하세요', min_value=10.0, max_value=250.0, value=160.0, step=0.1)
weight = st.number_input('몸무게(kg)를 입력하세요', min_value=1.0, value=60.0, step=0.1)
BMI = round(weight / ((height/100)**2), 2)
st.write('신체질량지수(BMI):', BMI)


st.header('날짜 입력')
import datetime

birthday = st.date_input('생일을 입력하세요 : ', value=datetime.date(2000,1,1))
st.write('당신의 생일 : ', birthday)

date_range = st.date_input('프로젝트의 기간을 입력하세요.',
                           value=[datetime.date(2024,1,1), datetime.date(2024,12,31)],
                           min_value=datetime.date(2024,1,1),
                           max_value=datetime.date(2024,12,31))


st.header('시간 입력')

start_time = st.time_input('시작 시각을 입력하세요 : ', value=datetime.time(8,30))
st.write('시작 시각 : ', start_time)

end_time = st.time_input('종료 시각을 입력하세요 : ', value=datetime.time(15))
st.write('종료 시각 : ', end_time)



st.title('화면 나누기')
st.header('영역 구분')

col1, col2, col3 = st. columns([2,3,0.5])

with col1:
    st.title('here is column1')

with col2:
    st.title('here is column2')
    st.checkbox('this is checkboc1 in col2')
    
with col3:
    st.title('here is column3')



st.header('영역 구분 사용 예시')
import streamlit as st
from PIL import Image
import pandas as pd

path = 'D:\\elice_python\\GAS_5\\pytest\\'
data_path = path + 'iris.csv'
df = pd.read_csv(data_path)

col1, col2 = st.columns(2)
with col1:
    st.subheader('iris 데이터')
    st.dataframe(df.iloc[:5,2:5])
with col2:
    st.subheader('Petal Info.')
    st.line_chart(df.iloc[:10,2:4])
    
    
st.header('Tab 구분')
tab1, tab2 = st.tabs(['Tab A','Tab B'])

with tab1:
    st.write('hello')
with tab2:
    st.write('hi')
    

st.header('Sidebar')
    
st.sidebar.title('this is sidebar')
st.sidebar.checkbox('체크박스에 표시될 문구')


st.sidebar.title('Side Bar')
st.sidebar.header('텍스트 사용 입력 예')
user_id = st.sidebar.text_input('아이디 입력', value='streamlit', max_chars=15)
user_passwd = st.sidebar.text_input('패스워드 입력', value='1234', type='password')
st.sidebar.header('SelectBox 사용 예')
option = ['아메리카노', '카페라떼', '카푸치노', '딸기주스']
selected = st.sidebar.selectbox('원하시는 메뉴는?', option)
st.sidebar.write('주문하신 메뉴는:', selected)
st.title('Main Window')

path = "D:\\Users\\Caelu\\Downloads\\menu_pics\\"
images = ['카페 아메리카노.jpg', '카페 라떼.jpg', '카푸치노.jpg', '딸기주스 190ML.jpg']
# Side Bar의 SelectBox 선택 내용에 따라 Main Window의 이미지 교체
select_idx = option.index(selected)
selected_img = images[select_idx]
img = Image.open(path+selected_img)
st.image(img, caption=selected)