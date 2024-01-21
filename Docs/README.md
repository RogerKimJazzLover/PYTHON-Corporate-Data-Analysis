# Corporate Data Analysis

## 💬 Description

This directory does the following things:
1. gather & organize the financial statements of 100 companies listed in KOSPI(Korean Composite Stock Price Index); over the period of ***past six years.***
2. calculate essential & meaningful ***analytical data*** for each company. Some examples of _essential analytical data_:
    - ROA, ROE, PER, 
    - Revenue/Operating Income/Net Income increase rate
    - Profit Status
3. visualize those datas in various types of graphs. (Box plot, scatter plot, etc)


## ⚙️ Frameworks/Modules/Packages Used

**Financial Data Retrieval**
- `OpenDartReader` ***(API)***
- `FinanceDataReader`

**Data Analysis & Manipulation**
- `pandas`
- `numpy`

**Testing & Others**
- `pytest`
- `tqdm`
- `pickle`

These are listed in `requirements.txt` in the `Docs` folder. Use the below command to install these dependencies.
- ```pip install -r requirements.txt```

## 🛐 How to run

- Get an API key from [OpenDart](https://opendart.fss.or.kr/)
- Make sure the require modules are installed (you ran the command above)
- Customize the API key in the source codes
- Create a directory called `Data`
- ```python initialize_data.py``` and VOILA! (Hopefully, any errors should be posted in the "Issues" section)

## 🤖 Contributors

[RogerKimJazzLover]((https://github.com/RogerKimJazzLover)https://github.com/RogerKimJazzLover)

