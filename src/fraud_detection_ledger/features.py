import pandas as pd
import holidays

def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    시간 기반 피처 추가:
    - hour: 시간대
    - is_late_entry: 18시 이후 야간 입력 여부
    """
    df['date'] = pd.to_datetime(df['date'])
    df['time'] = pd.to_datetime(df['time'], format='%H:%M', errors='coerce')
    df['hour'] = df['time'].dt.hour
    df['is_late_entry'] = (df['hour'] >= 18).astype(int)
    return df

def add_holiday_flag(df: pd.DataFrame, year: int = 2025) -> pd.DataFrame:
    """
    공휴일 플래그 추가 (한국)
    """
    kr_holidays = holidays.KR(years=year)
    holiday_dates = pd.to_datetime(list(kr_holidays.keys()))
    df['is_holiday'] = df['date'].isin(holiday_dates).astype(int)
    return df

def add_transaction_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    거래 관련 피처 추가:
    - high_amount: 100만원 초과 여부
    - user_high_transfer_count: 사용자별 고액 이체 횟수
    - vendor_contains_ltd: 공급업체명에 'Ltd' 포함 여부
    """
    df['high_amount'] = df['amount'].abs() > 1_000_000
    df['user_high_transfer_count'] = df.groupby('entered_by')['high_amount'].transform('sum')
    df['vendor_contains_ltd'] = df['vendor'].str.contains('Ltd', na=False).astype(int)
    return df

def add_label(df: pd.DataFrame) -> pd.DataFrame:
    """
    조건 3개 이상 만족 시 부정 거래로 간주:
    - high_amount
    - is_holiday
    - is_late_entry
    - user_high_transfer_count >= 3
    - vendor_contains_ltd
    => potential_fraud_complex (0 또는 1)
    """
    conditions = [
        df['high_amount'],
        df['is_holiday'] == 1,
        df['is_late_entry'] == 1,
        df['user_high_transfer_count'] >= 3,
        df['vendor_contains_ltd'] == 1,
    ]
    df['potential_fraud_complex'] = (sum(conditions) >= 3).astype(int)
    return df

def main():
    df = pd.read_csv("../../data/fake_journal_entries_500.csv")
    df = add_time_features(df)
    df = add_holiday_flag(df)
    df = add_transaction_features(df)
    df = add_label(df)
    print(df[['amount', 'hour', 'is_late_entry', 'is_holiday', 
              'high_amount', 'user_high_transfer_count', 
              'vendor_contains_ltd', 'potential_fraud_complex']].head())

if __name__ == "__main__":
    main()
