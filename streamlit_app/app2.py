import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

from fraud_detection_ledger.data import load_data
from fraud_detection_ledger.features import (
    add_time_features,
    add_holiday_flag,
    add_transaction_features,
    add_label
)
from fraud_detection_ledger.models import train_models
from fraud_detection_ledger.visualization import (
    plot_hourly_anomaly_ratio,
    plot_box_by_model,
    plot_daynight_bar
)

# 한글 폰트 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

@st.cache_data
def load_and_prepare():
    df = load_data("data/fake_journal_entries_500_final.csv")
    df = add_time_features(df)
    df = add_holiday_flag(df)
    df = add_transaction_features(df)
    df = add_label(df)
    df['time_str'] = df['time'].dt.strftime('%H:%M')
    return df

st.title("회계 전표 이상 거래 분석 시스템")

try:
    df = load_and_prepare()
    df = train_models(df)

    st.subheader("데이터 미리보기")
    preview_cols = ['date', 'time_str', 'amount', 'entered_by', 'vendor', 'description', 'is_holiday']
    st.dataframe(df[preview_cols].head())

    st.subheader("시간대별 이상 거래 비율")
    st.pyplot(plot_hourly_anomaly_ratio(df))

    st.subheader("금액 분포 비교")
    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(plot_box_by_model(df, 'rf_pred', 'RF 기준 금액 분포'))
    with col2:
        st.pyplot(plot_box_by_model(df, 'is_anomaly', 'IF 기준 금액 분포'))

    st.subheader("평일 낮/야간 이상 거래 비율")
    col3, col4 = st.columns(2)
    with col3:
        st.pyplot(plot_daynight_bar(df, 'rf_pred', 'RF 기준 낮/야간 비율', palette='Blues', ylim=(0, 1)))
    with col4:
        st.pyplot(plot_daynight_bar(df, 'is_anomaly', 'IF 기준 낮/야간 비율', palette='Oranges', ylim=(0, 1)))

except Exception as e:
    st.error(f"❌ 오류 발생: {e}")
