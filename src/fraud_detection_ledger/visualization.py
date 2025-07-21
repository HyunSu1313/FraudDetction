import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 글꼴 설정
sns.set_theme(style="whitegrid")
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def plot_box_by_model(df, pred_col, title):
    plot_df = df[df['amount'] > 1].copy()
    if plot_df.empty or plot_df['amount'].max() <= 0:
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, f"{title}\n(시각화할 데이터 없음)", ha='center', va='center')
        ax.axis('off')
        return fig

    fig, ax = plt.subplots(figsize=(6, 5))
    plot_df.boxplot(
        column='amount',
        by=pred_col,
        ax=ax,
        showfliers=True,
        patch_artist=True,
        boxprops=dict(facecolor='orange')
    )
    ax.set_yscale('log')
    ax.set_ylim(1e2, 1e8)
    ax.set_title(title)
    ax.set_ylabel("거래 금액 (로그 스케일)")
    ax.set_xlabel("이상 여부 (0: 정상, 1: 이상)")
    plt.suptitle("")
    plt.tight_layout()
    return fig

def plot_daynight_bar(df, pred_col, title, palette='Blues', ylim=None):
    df_copy = df.copy()
    df_copy['daynight'] = df_copy['hour'].apply(lambda h: '낮' if 9 <= h < 18 else '야간')
    plot_df = df_copy[df_copy[pred_col] == 1].groupby('daynight').size().reset_index(name='count')
    plot_df['ratio'] = plot_df['count'] / plot_df['count'].sum()

    fig, ax = plt.subplots(figsize=(4, 4))
    sns.barplot(data=plot_df, x='daynight', y='ratio', palette=palette, ax=ax)
    ax.set_title(title)
    ax.set_ylabel("비율")
    ax.set(xlabel=None)
    if ylim:
        ax.set_ylim(ylim)
    plt.tight_layout()
    return fig

def plot_hourly_anomaly_ratio(df):
    df_copy = df.copy()
    hourly_if = df_copy.groupby('hour')['is_anomaly'].mean().reset_index(name='IF')
    hourly_rf = df_copy.groupby('hour')['rf_pred'].mean().reset_index(name='RF')
    hourly = pd.merge(hourly_if, hourly_rf, on='hour', how='outer').sort_values('hour')

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(data=hourly, x='hour', y='IF', marker='o', ax=ax, label='IF 기준')
    sns.lineplot(data=hourly, x='hour', y='RF', marker='s', ax=ax, label='RF 기준')
    ax.set_title("시간대별 이상 거래 비율")
    ax.set_ylabel("이상 거래 비율")
    ax.set_xlabel("시간")
    ax.set_ylim(0, 1)
    ax.legend()
    plt.tight_layout()
    return fig
