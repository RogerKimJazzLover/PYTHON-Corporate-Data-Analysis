import subprocess, os, argparse

def empty_stock():
    folder_path = "./Data/Stocks/"
    file_list = os.listdir(folder_path) # Get a list of files in the folder

    # Iterate through the file list and remove each file
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser()
    # Add arguments for each environmental variable
    parser.add_argument('-u', '--update_name_code', action='store_true', help='Update Name Code')
    # Parse the command-line arguments
    args = parser.parse_args()
    # Set the environmental variables based on the parsed arguments
    if args.update_name_code:
        os.environ['UPDATE_NAME_CODE'] = "True"
    
    file1 = "./create_name_code.py"
    file2 = "./create_stock_prices.py"
    file3 = "./create_basic_info.py"
    file4 = "./create_bf_for_analysis.py"

    update_name_code = os.environ.get("UPDATE_NAME_CODE", "False")

    #WHEN YOU WANT TO UPDATE THE LIST OF COMPANIES SUPPORTED
    if update_name_code == "True":
        #1. Creating the name_code
        print("\n")
        print('#' * 100)
        print("SYSTEM: Creating name_code.pkl file......")
        subprocess.run(['python', file1])
        print("SYSTEM: Finished creating name_code.pkl file")

        #2. Creating all the Stock prices for each cmpny
        print("\n")
        print('#' * 100)
        print("SYSTEM: Emptying folder /API/api_local/Data/Stocks/")
        empty_stock()
        print("SYSTEM: Finished emptying")
        print("\n")
        print('#' * 100)
        print("SYSTEM: Creating stock price files......")
        subprocess.run(['python', file2])
        print("SYSTEM: Finished creating stock price files")

    #3. Creating the basic info
    print("\n")
    print('#' * 100)
    print("SYSTEM: Creating basic_info.csv file......")
    subprocess.run(['python', file3])
    print("SYSTEM: Finished creating basic_info.csv file")
    
    #4. Creating the basic info for analysis
    print("\n")
    print('#' * 100)
    print("SYSTEM: Creating basic_info_for_analysis.csv file......")
    subprocess.run(['python', file4])
    print("SYSTEM: Finished creating basic_info_for_analysis.csv file")

if __name__ == "__main__":
    main()