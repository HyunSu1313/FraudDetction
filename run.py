from fraud_detection_ledger.data import load_data
from fraud_detection_ledger.visualization import plot_cv_accuracy
import matplotlib.pyplot as plt

df = load_data("data/fake_journal_entries_500.csv")
print(df.head())

cv_scores = [0.93, 0.88, 0.89, 0.92, 0.89]
plot_cv_accuracy(cv_scores)  # 그래프 생성 함수 호출
plt.show()                   # 생성된 그래프를 화면에 표시
