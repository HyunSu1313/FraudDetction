import pandas as pd
import holidays

def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    date, time 컬럼을 이용해
    - hour: 시간(0~23)
    - is_late_entry: 18시 이후 입력 여부(0/1)
    를 추가합니다.
    """
    df['date'] = pd.to_datetime(df['date'])
    df['time'] = pd.to_datetime(df['time'], format='%H:%M')
    df['hour'] = df['time'].dt.hour
    df['is_late_entry'] = (df['hour'] >= 18).astype(int)
    return df

def add_holiday_flag(df: pd.DataFrame, year: int = 2025) -> pd.DataFrame:
    """
    한국 공휴일을 불러와
    - is_holiday: 공휴일 여부(0/1)
    플래그를 추가합니다.
    """
    kr_holidays = holidays.KR(years=year)
    holiday_dates = pd.to_datetime(list(kr_holidays.keys()))
    df['is_holiday'] = df['date'].isin(holiday_dates).astype(int)
    return df

def main():
    # 데이터 불러오기
    df = pd.read_csv(r"../../data/fake_journal_entries_500.csv")
    # 함수 적용
    df = add_time_features(df)
    df = add_holiday_flag(df)
    # 결과 확인
    print(df[['date','time','hour','is_late_entry','is_holiday']].head())

if __name__ == "__main__":
    main()