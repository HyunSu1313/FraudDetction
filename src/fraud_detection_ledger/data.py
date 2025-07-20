import os
import pandas as pd

def load_data(filename: str) -> pd.DataFrame:
    """
    상대 경로를 기반으로 CSV 파일을 불러옵니다.
    날짜 및 시간 컬럼도 datetime 형식으로 파싱합니다.
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    full_path = os.path.join(base_dir, filename)

    df = pd.read_csv(full_path)

    # 날짜 및 시간 컬럼 전처리
    df['date'] = pd.to_datetime(df['date'])
    df['time'] = pd.to_datetime(df['time'], format='%H:%M', errors='coerce')
    df['hour'] = df['time'].dt.hour

    return df

def save_data(df: pd.DataFrame, filename: str):
    """
    상대 경로를 기반으로 CSV 파일로 저장합니다.
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    full_path = os.path.join(base_dir, filename)
    df.to_csv(full_path, index=False)

# 테스트용 main 함수 (선택적으로 사용)
if __name__ == "__main__":
    df = load_data("data/fake_journal_entries_500_final.csv")
    print(df.head())
