from gettext import npgettext
import streamlit as st
import numpy as np
import pandas as pd
import time 
from PIL import Image

st.title('Streamlit 入門')
#st.write('DataFrame')
#st.write('Interactive Widgets')
st.write('プログレスバーの表示')
'start!!'

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

left_column, right_column=st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

text=st.text_input('あなたの趣味を教えてください。')
condition=st.slider('あなたの今の調子は?',0,100,50) #最小、最大、初期値

expand=st.expander('問い合わせ')
expand.write('問い合わせ内容を書く')

'あなたの趣味.',text
'コンディション:',condition

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)

'あなたの好きな数字は', option, 'です'

#if st.checkbox('Show Image'):
#    img = Image.open('sample.jpg')
#    st.image(img, caption='a', use_column_width=True)

#乱数生成から緯度、経度を50で割る。割った値を足す。
df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69, 139.70],
    columns=['lat','lon']
)
#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)
#st.map(df)

#st.table(df.style.highlight_max(axis=0))

#st.dataframe 表の描画 (引数あり)
#st.write 表の描画 (引数なし)
#st.table 表の描画 (静的)

