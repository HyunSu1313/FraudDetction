import os
import pandas as pd
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_PATH = os.path.join(BASE_DIR, "data", "fake_journal_entries_500.csv")
df = pd.read_csv(DATA_PATH)
df = pd.read_csv(r"C:\Users\HyunSu\Desktop\Fraud Detection Ledger\data\fake_journal_entries_500.csv")
import pandas as pd
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from fraud_detection_ledger.features import add_time_features, add_holiday_flag

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_PATH = os.path.join(BASE_DIR, "data", "fake_journal_entries_500.csv")
def train_isolation_forest(X: pd.DataFrame,
                           contamination: float = 0.1,
                           random_state: int = 57) -> IsolationForest:
    """
    Isolation Forest 모델을 학습하여 반환합니다.
    """
    iso = IsolationForest(contamination=contamination, random_state=random_state)
    iso.fit(X)
    return iso

def train_random_forest(X: pd.DataFrame,
                        y: pd.Series,
                        random_state: int = 57) -> RandomForestClassifier:
    """
    Random Forest 모델을 학습하여 반환합니다.
    """
    clf = RandomForestClassifier(random_state=random_state)
    clf.fit(X, y)
    return clf

def evaluate_model(model, X_test: pd.DataFrame, y_test: pd.Series) -> str:
    """
    학습된 모델을 평가한 classification report 문자열을 반환합니다.
    """
    y_pred = model.predict(X_test)
    return classification_report(y_test, y_pred)

def split_data(X: pd.DataFrame,
               y: pd.Series,
               test_size: float = 0.3,
               stratify: pd.Series = None,
               random_state: int = 57):
    """
    학습/테스트 데이터를 분할하여 반환합니다.
    """
    return train_test_split(X, y, test_size=test_size, stratify=stratify, random_state=random_state)

def main():
    # 1) 데이터 로딩
    df = pd.read_csv(r"data/fake_journal_entries_500.csv")
    
    # 2) 피처 생성 (시간 및 공휴일)
    df = add_time_features(df)
    df = add_holiday_flag(df)
    
    # 3) 학습용 X, y 준비
    X = df[['amount', 'hour', 'is_late_entry', 'is_holiday']]
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

if __name__ == "__main__":
    main()
