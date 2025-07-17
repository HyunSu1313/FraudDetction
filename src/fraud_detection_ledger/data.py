import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """CSV 파일을 읽어서 DataFrame으로 반환"""
    return pd.read_csv(path)

def main():
    df = load_data(r"data/fake_journal_entries_500.csv")
    print(df.head()) 

if __name__ == "__main__":
    main()
