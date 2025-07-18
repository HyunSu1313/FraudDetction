# Fraud Detection Ledger

본 프로젝트는 회계 전표 데이터를 분석하여 자금 횡령 및 부정 거래를 탐지하는 시스템입니다.

## 프로젝트 개요
- ERP 회계 전표 데이터 기반 이상 거래 탐지
- 머신러닝 기법을 활용한 이상 패턴 분석
- Streamlit 대시보드로 결과 시각화

## 폴더 구조
- data/: 분석에 사용되는 fake_journal_entries_500.csv 파일이 포함됩니다. 이 파일은 가상의 ERP 회계 전표 데이터로, 거래 금액, 시간, 사용자 정보 등이 포함되어 있습니다.
- notebooks/: 데이터 분석 및 모델링을 위한 Jupyter Notebook 파일들이 포함됩니다.
- streamlit_app/: Streamlit 대시보드를 위한 Python 코드(app.py)가 포함됩니다.
- src/: 패키지와 모듈 코드, fraud_detection_ledger 패키지가 포함됩니다.
  
## 사용 기술
- Python: pandas, scikit-learn, seaborn 등 데이터 분석 및 머신러닝 라이브러리
- Jupyter Notebook: 데이터 분석 및 모델링을 위한 코드 실행 환경
- Streamlit: 대시보드 웹 애플리케이션
- Matplotlib, Seaborn: 데이터 시각화

## 시작 방법
1. 필요한 라이브러리 설치  
   `pip install -r requirements.txt`

2. Jupyter Notebook에서 코드 실행
notebooks/ 폴더에서 Jupyter Notebook을 통해 fraud_detection_final.ipynb을 실행할 수 있습니다. 모델 학습 및 검증을 진행하세요.

3. Streamlit 앱 실행
Streamlit 대시보드를 실행하려면 아래 명령어를 사용하세요.
앱을 실행하기 전에 streamlit_app 폴더로 이동해야 합니다.
   `streamlit run streamlit_app/app.py`
