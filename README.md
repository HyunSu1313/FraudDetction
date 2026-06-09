# 🔍 Fraud Detection Ledger

**ERP 회계 전표 데이터 기반 이상거래 탐지 시스템**

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org)

---

## 📌 프로젝트 개요

회계법인 및 기업 내부감사 현장에서 ERP 회계 전표 데이터를 분석하여 **자금 횡령 및 부정 거래를 자동으로 탐지**하는 머신러닝 기반 시스템입니다.

내부통제(Internal Control) 및 부정위험 관리(Fraud Risk Management) 관점에서 설계되었으며, 감사인이 수작업으로 수행하던 이상거래 식별 절차를 자동화합니다.

---

## 🎯 배경 및 문제의식

기존 감사 절차에서 이상거래 탐지는 다음과 같은 한계가 있습니다:

- 전표 건수가 많을수록 전수 검토 불가 → 샘플링에 의존
- 규칙 기반(Rule-based) 탐지는 새로운 패턴에 대응 어려움
- 감사인의 경험과 직관에 의존하는 주관적 판단

본 프로젝트는 **비지도·지도 학습을 결합**하여 이상 패턴을 자동으로 식별하고, Streamlit 대시보드로 감사인이 직관적으로 결과를 검토할 수 있도록 구현했습니다.

---

## 🛠️ 사용 기술

| 구분 | 기술 |
|---|---|
| 언어 | Python |
| 이상탐지 모델 | Isolation Forest, Random Forest |
| 데이터 분석 | Pandas, NumPy, Scikit-learn |
| 시각화 | Matplotlib, Seaborn |
| 대시보드 | Streamlit |
| 개발환경 | Jupyter Notebook |

---

## 📁 폴더 구조

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

## 🔬 모델 설계

### 1단계 — 비지도 학습 (Isolation Forest)
레이블 없이 전표 데이터의 이상 패턴을 탐지합니다. 거래 금액, 시간대, 사용자 행동 패턴 등을 기반으로 정상 분포에서 벗어난 거래를 이상치로 분류합니다.

### 2단계 — 지도 학습 (Random Forest)
이상 탐지 결과를 바탕으로 부정 거래 유형을 분류합니다. 특성 중요도(Feature Importance) 분석으로 어떤 요소가 부정 거래와 연관성이 높은지 파악합니다.

### 3단계 — Streamlit 대시보드
감사인이 탐지 결과를 직관적으로 검토할 수 있는 인터페이스를 제공합니다.

---

## 🚀 실행 방법

```bash
# 1. 패키지 설치
pip install -r requirements.txt

# 2. Jupyter Notebook 실행 (모델 학습)
jupyter notebook notebooks/fraud_detection_final.ipynb

# 3. Streamlit 대시보드 실행
streamlit run streamlit_app/app.py
```

---

## 💡 활용 가능 분야

- 회계법인 감사 절차 자동화
- 기업 내부감사팀 이상거래 모니터링
- SoX / 내부회계관리제도 통제 테스트 보조

---

## 👤 개발자

**정현수** | KICPA | EY한영 Risk Consulting (P&C)

📫 mosjeong1@gmail.com
