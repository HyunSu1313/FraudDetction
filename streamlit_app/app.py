import streamlit as st

st.title('Fraud Detection Dashboard')

st.write('이 앱은 ERP 회계 전표 데이터를 기반으로 자금 횡령 및 부정 거래를 탐지하는 시스템입니다.')

if st.button('모델 실행'):
    st.write('모델을 실행하는 중...')
