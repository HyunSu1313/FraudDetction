# Fraud Detection Ledger

본 프로젝트는 회계 전표 데이터를 분석하여 자금 횡령 및 부정 거래를 탐지하는 시스템입니다.

## 프로젝트 개요
- ERP 회계 전표 데이터 기반 이상 거래 탐지
- 머신러닝 기법을 활용한 이상 패턴 분석
- Streamlit 대시보드로 결과 시각화

## 폴더 구조
- data/: 분석에 사용되는 데이터 파일
- notebooks/: 데이터 분석 및 모델링 코드 (Jupyter Notebook)
- streamlit_app/: 대시보드 웹 애플리케이션 코드
- reports/: 결과 보고서 및 문서

## 사용 기술
- Python (pandas, scikit-learn, PyOD 등)
- Streamlit
- Jupyter Notebook
- Matplotlib, Seaborn

## 시작 방법
1. 필요한 라이브러리 설치  
   `pip install -r requirements.txt`

2. Jupyter Notebook에서 분석 코드 실행 및 검증

3. Streamlit 앱 실행  
   `streamlit run streamlit_app/app.py`