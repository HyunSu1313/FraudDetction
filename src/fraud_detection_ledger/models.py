import os
import pandas as pd
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 시간 관련 파생 피처 추가: `is_late_entry` (야간 거래 여부)
def add_time_features(df):
    """
    시간 관련 파생 피처 추가: `is_late_entry` (야간 거래 여부)
    """
    df['time'] = pd.to_datetime(df['time'], format='%H:%M')
    df['hour'] = df['time'].dt.hour
    df['is_late_entry'] = (df['hour'] >= 18).astype(int)  # 18시 이후는 야간 거래
    return df

# 공휴일 여부 판단: `is_holiday` (공휴일 여부)
def add_holiday_flag(df):
    """
    공휴일 여부를 판단하는 `is_holiday` 플래그 추가
    """
    import holidays
    kr_holidays = holidays.KR(years=2025)
    kr_holiday_dates = pd.to_datetime(list(kr_holidays.keys()))
    df['is_holiday'] = df['date'].isin(kr_holiday_dates).astype(int)  
    return df

# 추가적인 피처 생성: 금액 기준, 고액 이체 횟수, 공급업체 이름에 'Ltd' 포함 여부
def add_additional_features(df):
    """
    추가적인 피처들 (금액 기준, 고액 이체 횟수, 공급업체 이름에 'Ltd' 포함 여부)
    """
    # 1. 금액 절대값 > 1,000,000을 이상으로 간주
    df['high_amount'] = df['amount'].abs() > 1_000_000
    
    # 2. 사용자별 고액 이체 횟수
    user_high_transfer_count = df.groupby('entered_by')['high_amount'].transform('sum')
    df['user_high_transfer_count'] = user_high_transfer_count
    
    # 3. 공급업체 이름에 'Ltd' 포함 여부
    df['vendor_contains_ltd'] = df['vendor'].str.contains('Ltd')
    
    return df

# Isolation Forest 모델 학습 함수
def train_isolation_forest(X: pd.DataFrame, contamination: float = 0.1, random_state: int = 57) -> IsolationForest:
    """
    Isolation Forest 모델을 학습하여 반환합니다.
    """
    iso = IsolationForest(contamination=contamination, random_state=random_state)
    iso.fit(X)
    return iso

# Random Forest 모델 학습 함수
def train_random_forest(X: pd.DataFrame, y: pd.Series, random_state: int = 57) -> RandomForestClassifier:
    """
    Random Forest 모델을 학습하여 반환합니다.
    """
    clf = RandomForestClassifier(random_state=random_state)
    clf.fit(X, y)
    return clf

# 모델 평가 함수
def evaluate_model(model, X_test: pd.DataFrame, y_test: pd.Series) -> str:
    """
    학습된 모델을 평가한 classification report 문자열을 반환합니다.
    """
    y_pred = model.predict(X_test)
    return classification_report(y_test, y_pred)

# 데이터 분할 함수
def split_data(X: pd.DataFrame, y: pd.Series, test_size: float = 0.3, stratify: pd.Series = None, random_state: int = 57):
    """
    학습/테스트 데이터를 분할하여 반환합니다.
    """
    return train_test_split(X, y, test_size=test_size, stratify=stratify, random_state=random_state)

# 메인 함수
def main():
    # 1) 데이터 로딩
    df = pd.read_csv(r"data/fake_journal_entries_500.csv")
    
    # 2) 피처 생성 (시간, 공휴일, 금액 기준 등)
    df = add_time_features(df)
    df = add_holiday_flag(df)
    df = add_additional_features(df)  # 추가적인 피처 생성 (5가지 조건 모두 반영)
    
    # 3) 학습용 X, y 준비
    X = df[['amount', 'hour', 'is_late_entry', 'is_holiday', 'high_amount', 'user_high_transfer_count', 'vendor_contains_ltd']]
    y = (df['amount'].abs() > 1_000_000).astype(int)  # 금액 기준 라벨 예시
    
    # 4) 데이터 분할
    X_train, X_test, y_train, y_test = split_data(X, y, stratify=y)
    
    # 5) 모델 학습 및 평가
    print("=== Isolation Forest 평가 ===")
    iso = train_isolation_forest(X_train)
    print(evaluate_model(iso, X_test, y_test))
    
    print("=== Random Forest 평가 ===")
    rf = train_random_forest(X_train, y_train)
    print(evaluate_model(rf, X_test, y_test))

# 프로그램 실행
if __name__ == "__main__":
    main()
