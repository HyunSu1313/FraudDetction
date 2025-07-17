import os
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
setup(
    name="fraud_detection_ledger",           # 패키지 이름 :contentReference[oaicite:1]{index=1}
    version="0.1.0",                         # 버전 정보
    description="ERP 회계전표 기반 이상 거래 탐지 시스템",  # 간단 설명
    long_description=long_description,       # 상세 설명(README.md)
    long_description_content_type="text/markdown",
    author="HyunSu",                         # 작성자
    author_email="your.email@example.com",   # 작성자 이메일
    url="https://github.com/HyunSu/FraudDetectionLedger",  # 프로젝트 URL

    package_dir={"": "src"},                                 # 소스 디렉터리 지정 :contentReference[oaicite:2]{index=2}
    packages=find_packages(where="src"),                     # src 아래 패키지 탐색 :contentReference[oaicite:3]{index=3}
    include_package_data=True,         # MANIFEST.in에 정의된 파일 포함
    license="MIT",                     # 라이선스
    classifiers=[                      # PyPI 분류(선택)
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[                 # 런타임 의존성
        "pandas>=2.0",
        "scikit-learn>=1.7",
        "seaborn>=0.13",
        "streamlit>=1.46",
        "holidays>=0.76",
    ],
    extras_require={                   # 선택적(development/test) 의존성
        "dev": ["pytest>=7.0", "flake8>=6.0"],
    },
)
