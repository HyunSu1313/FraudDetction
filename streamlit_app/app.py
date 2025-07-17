import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
import holidays
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

def load_data():
    df = pd.read_csv(r"C:\Users\HyunSu\Desktop\Fraud Detection Ledger\data\fake_journal_entries_500.csv")
    return df

def add_time_features(df):
    df['date'] = pd.to_datetime(df['date'])
    df['time'] = pd.to_datetime(df['time'], format='%H:%M')
    df['hour'] = df['time'].dt.hour
    df['is_late_entry'] = (df['hour'] >= 18).astype(int)
    return df

def add_holiday_flag(df, year=2025):
    kr_holidays = holidays.KR(years=year)
    holiday_dates = pd.to_datetime(list(kr_holidays.keys()))
    df['is_holiday'] = df['date'].isin(holiday_dates).astype(int)
    return df

def detect_anomalies(df):
    X = df[['amount', 'hour', 'is_late_entry', 'is_holiday']]
    iso = IsolationForest(contamination=0.1, random_state=42)
    df['anomaly'] = iso.fit_predict(X)
    df['is_anomaly'] = df['anomaly'] == -1
    return df

st.title('Fraud Detection Ledger 대시보드')
st.write('이 앱은 ERP 회계 전표 데이터를 기반으로 자금 횡령 및 부정 거래를 탐지하는 시스템입니다.')


df = load_data()
df = add_time_features(df)
df = add_holiday_flag(df)
df = detect_anomalies(df)

st.subheader('데이터 샘플')
st.dataframe(df.head())

st.subheader('이상 거래 금액 분포')
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(df[df['is_anomaly'] == 1]['amount'], bins=30, kde=True, ax=ax, color='r', label='이상 거래')
sns.histplot(df[df['is_anomaly'] == 0]['amount'], bins=30, kde=True, ax=ax, color='b', label='정상 거래')
ax.set_title('이상 거래 금액 분포')
ax.set_xlabel('금액')
ax.set_ylabel('빈도')
ax.legend()
st.pyplot(fig)

st.subheader('시간대별 이상 거래 비율')
hourly = df.groupby(['hour', 'is_anomaly']).size().reset_index(name='count')
hourly_pivot = hourly.pivot(index='hour', columns='is_anomaly', values='count').fillna(0)
hourly_pivot.columns = ['정상', '이상']
hourly_pivot['이상비율'] = hourly_pivot['이상'] / (hourly_pivot['정상'] + hourly_pivot['이상'])

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=hourly_pivot, x=hourly_pivot.index, y='이상비율', marker='o', ax=ax)
ax.set_title('시간대별 이상 거래 비율')
ax.set_xlabel('시간대 (hour)')
ax.set_ylabel('이상 거래 비율')
st.pyplot(fig)

st.subheader('이상 거래 예시')
st.dataframe(df[df['is_anomaly'] == 1][['amount', 'hour', 'is_late_entry', 'is_holiday']].head())
