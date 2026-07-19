# Fraud Detection Ledger (ERP 이상거래 탐지 시스템)

> ERP 회계 전표 데이터 기반 머신러닝 이상거래 탐지 및 Streamlit 대시보드

---

## 프로젝트 개요

회계법인 및 기업 내부감사 현장에서 ERP 전표 데이터를 분석하여 자금 횡령 및 부정 거래를 자동으로 탐지하는 시스템입니다.

**기존 방식의 문제:**
- 전표 건수가 많을수록 전수 검토 불가 → 샘플링에 의존
- 규칙 기반(Rule-based) 탐지는 새로운 패턴에 대응 어려움
- 감사인의 경험과 직관에 의존하는 주관적 판단

**해결:**
- 비지도·지도 학습을 결합하여 이상 패턴 자동 식별
- Streamlit 대시보드로 감사인이 결과를 직관적으로 검토

---

## 주요 기능

### 1. 비지도 학습 — Isolation Forest
레이블 없이 전표 데이터의 이상 패턴을 탐지합니다. 거래 금액, 시간대, 사용자 행동 패턴 등을 기반으로 정상 분포에서 벗어난 거래를 이상치로 분류합니다.

### 2. 지도 학습 — Random Forest
이상 탐지 결과를 바탕으로 부정 거래 유형을 분류합니다. 특성 중요도(Feature Importance) 분석으로 어떤 요소가 부정 거래와 연관성이 높은지 파악합니다.

### 3. Streamlit 대시보드
감사인이 탐지 결과를 직관적으로 검토할 수 있는 인터페이스를 제공합니다.

---

## 활용 가능 분야

- 회계법인 감사 절차 자동화
- 기업 내부감사팀 이상거래 모니터링
- SoX / 내부회계관리제도 통제 테스트 보조

---

## 사용 방법

```bash
# 1. 패키지 설치
pip install -r requirements.txt

# 2. Jupyter Notebook 실행 (모델 학습)
jupyter notebook notebooks/fraud_detection_final.ipynb

# 3. Streamlit 대시보드 실행
streamlit run streamlit_app/app.py
```

---

## 파일 구조

```
FraudDetction/
├── data/
│   └── fake_journal_entries_500.csv   # 가상 ERP 전표 데이터 (500건)
├── notebooks/
│   └── fraud_detection_final.ipynb    # 데이터 분석 및 모델 학습
├── src/
│   └── fraud_detection_ledger/        # 메인 패키지
├── streamlit_app/
│   └── app.py                         # 대시보드 앱
├── requirements.txt
└── setup.py
```

---

## 기술 스택

- **Python** — 데이터 분석 및 모델 학습
- **Isolation Forest / Random Forest** — 이상탐지 및 분류
- **Pandas, NumPy, Scikit-learn** — 데이터 처리
- **Streamlit** — 대시보드
- **Jupyter Notebook** — 개발 환경

---

## 개발자

**정현수** | KICPA | EY한영 Risk Consulting (P&C)
📫 mosjeong1@gmail.com
