from setuptools import setup, find_packages

setup(
    name="sl_learn",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.0",
        "scipy>=1.10.0",
        "pandas>=2.0.0",
        "scikit-learn>=1.3.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "statsmodels>=0.14.0",
        "jupyter>=1.0.0",
        "notebook>=6.5.0",
        "ipython>=8.12.0",
    ],
)

