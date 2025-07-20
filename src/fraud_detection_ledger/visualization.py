import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_hourly_anomaly_ratio(df: pd.DataFrame) -> plt.Figure:
    iso_hour = df.groupby(['hour', 'is_anomaly']).size().unstack(fill_value=0)
    iso_hour['isolation_비율'] = iso_hour.get(True, 0) / iso_hour.sum(axis=1)

    rf_hour = df.groupby(['hour', 'rf_pred']).size().unstack(fill_value=0)
    rf_hour['rf_비율'] = rf_hour.get(1, 0) / rf_hour.sum(axis=1)

    fig, ax = plt.subplots(figsize=(10, 4))
    sns.lineplot(x=iso_hour.index, y=iso_hour['isolation_비율'], marker='o', label='Isolation Forest', ax=ax)
    sns.lineplot(x=rf_hour.index, y=rf_hour['rf_비율'], marker='s', label='Random Forest', ax=ax)
    ax.set(title='시간대별 이상 거래 비율', xlabel='시간대 (hour)', ylabel='이상 거래 비율')
    ax.grid(True)
    ax.legend()
    return fig

def plot_box_by_model(df: pd.DataFrame, model_column: str, title: str) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(
        data=df,
        x=model_column,
        y='amount',
        hue=model_column,
        palette=['C0', 'C1'],
        legend=False,
        ax=ax
    )
    ax.set_yscale('log')
    ax.set_ylim(1e3, 1e8)
    ax.set_xlabel('이상 여부 (0: 정상, 1: 이상)')
    ax.set_ylabel('거래 금액 (로그 스케일)')
    ax.set_title(title)
    ax.grid(True)
    return fig

def plot_daynight_bar(df: pd.DataFrame, label_column: str, title: str, palette: str) -> plt.Figure:
    weekday_df = df[df['is_holiday'] == 0]
    pivot = weekday_df.groupby('is_late_entry')[label_column].mean().reset_index()
    pivot['입력 시간대'] = pivot['is_late_entry'].map({0: '평일 낮', 1: '평일 야간'})

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(
        data=pivot,
        x='입력 시간대',
        y=label_column,
        hue='입력 시간대',
        palette=palette,
        legend=False,
        ax=ax
    )
    ax.set_title(title)
    ax.set_ylabel('이상 거래 비율')
    ax.set_xlabel('입력 시간대')
    ax.grid(True, axis='y')
    return fig
