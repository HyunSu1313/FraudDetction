import os
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
setup(
    name="fraud_detection_ledger",           
    version="0.1.0",                         
    description="ERP 회계전표 기반 이상 거래 탐지 시스템",  
    long_description=long_description,    
    long_description_content_type="text/markdown",
    author="HyunSu",                         
    author_email="your.email@example.com",   
    url="https://github.com/HyunSu/FraudDetectionLedger", 

    package_dir={"": "src"},                                
    packages=find_packages(where="src"),                    
    include_package_data=True,        
    license="MIT",                   
    classifiers=[               
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[                 
        "pandas>=2.0",
        "scikit-learn>=1.7",
        "seaborn>=0.13",
        "streamlit>=1.46",
        "holidays>=0.76",
    ],
    extras_require={                
        "dev": ["pytest>=7.0", "flake8>=6.0"],
    },
)
