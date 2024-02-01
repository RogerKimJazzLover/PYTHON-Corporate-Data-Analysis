from matplotlib import pyplot as plt
from matplotlib import rcParams
from tabulate import tabulate
import seaborn as sns
import pandas as pd

def ShowStatusBoxPlot(data: pd.DataFrame, key: str):
    plt.figure(figsize = (10, 6))
    graph_data = []
    for state in ["P_Contd", "L_Contd", "P_Turned", "L_Turned"]:
        value = data[data[key] == state]
        if value.empty:
            graph_data.append(0)
        else:
            graph_data.append(value["Profit"])
    plt.boxplot(graph_data)
    plt.ylim(-100, 100)
    plt.xticks([1, 2, 3, 4], ["P_Contd", "L_Contd", "P_Turned", "L_Turned"])
    plt.ylabel("Profit")
    plt.show()

def ShowStatusLineGraph(data: pd.DataFrame, key: str):
    result = []
    for year in range(2018, 2023):
        year_data = data.loc[data["Year"] == year]
        for state in ["P_Contd", "L_Contd", "P_Turned", "L_Turned"]:
            ror_list = year_data.loc[year_data[key] == state, "Profit"] #rate of return
            inve_per_stock = 10 ** 8 / len(ror_list)
            profit = (inve_per_stock * ror_list / 100).sum()
            profit_ratio = profit / 10 ** 8 * 100
            result.append([year, state, profit_ratio])
    result = pd.DataFrame(result, columns = ["Year", key, "Profit"])

    plt.figure(figsize = (10, 4))
    for state in ["P_Contd", "L_Contd", "P_Turned", "L_Turned"]:
        graph_data = result.loc[(result[key] ==  state), "Profit"].values    
        plt.plot(graph_data, marker = "o", label = state)
    plt.xticks(range(5), range(2018, 2023))
    plt.legend()
    plt.ylabel("P_rate")
    plt.xlabel("Year")
    plt.show()

def main():
    company_name = "HMM"

    cols = ["Company_Name", "Year", "Current_Stock", "Future_Stock", "Operating_Income(added)_Profit_Status","Net_Income(added)_Profit_Status" ]
    data = pd.read_csv("./Data/basic_info_for_analysis.csv", usecols=cols, encoding="euc-kr")
    data.dropna(inplace=True)

    # data = data[data["Company_Name"] == company_name]

    data["Profit"] = (data["Current_Stock"] - data["Future_Stock"]) / data["Current_Stock"] * 100

    # #Visualizing Operating Income
    # ShowStatusBoxPlot(data, key="Operating_Income(added)_Profit_Status")
    # #Visualizing Net Income
    # ShowStatusBoxPlot(data, key="Net_Income(added)_Profit_Status")

    ShowStatusLineGraph(data, key="Operating_Income(added)_Profit_Status")

if __name__ == "__main__":
    main()