import pandas as pd
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score

def train_models(df: pd.DataFrame) -> pd.DataFrame:
    """
    Isolation Forest 및 Random Forest 모델을 학습하고 예측 결과를 df에 추가합니다.
    """
    # Isolation Forest (비지도 이상치 탐지)
    iso = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    df['is_anomaly'] = (iso.fit_predict(df[['amount']]) == -1).astype(int)

    # 라벨 정의 (지도 학습용)
    df['label'] = df['potential_fraud_complex']

    # 특성 및 타겟
    X = df[['amount', 'hour', 'is_late_entry', 'is_holiday']]
    y = df['label']

    # 데이터 분할 및 Random Forest 학습
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # 예측 결과 저장
    df['rf_pred'] = clf.predict(X)

    return df

def get_cv_scores(df: pd.DataFrame) -> list:
    """
    Random Forest에 대한 교차 검증 정확도 점수를 반환합니다.
    """
    df['label'] = df['potential_fraud_complex']

    X = df[['amount', 'hour', 'is_late_entry', 'is_holiday']]
    y = df['label']

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    cv_scores = cross_val_score(clf, X, y, cv=5)

    return list(cv_scores)