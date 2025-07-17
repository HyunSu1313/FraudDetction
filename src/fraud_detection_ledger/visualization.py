import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def plot_cv_accuracy(cv_scores: list) -> plt.Figure:
    """
    교차 검증 정확도 선 그래프 반환.
    cv_scores: fold별 정확도 리스트
    """
    folds = np.arange(1, len(cv_scores) + 1)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(folds, cv_scores, marker='o', linestyle='-')
    mean, std = np.mean(cv_scores), np.std(cv_scores)
    ax.fill_between(folds, mean - std, mean + std, alpha=0.2)
    ax.axhline(mean, linestyle='--', color='r', 
               label=f'평균 정확도: {mean:.4f}')
    ax.set(title='교차 검증 정확도', xlabel='Fold 번호', ylabel='정확도')
    ax.legend()
    ax.grid(True)
    return fig

def plot_amount_distribution(amount_series: pd.Series) -> plt.Figure:
    """
    금액 분포 히스토그램 반환.
    amount_series: 거래 금액 시리즈
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(amount_series, bins=30, kde=True, ax=ax)
    ax.set(title='금액 분포', xlabel='금액', ylabel='빈도')
    return fig
