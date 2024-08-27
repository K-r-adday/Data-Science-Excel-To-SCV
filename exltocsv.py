import pandas as pd

def excel_to_csv(excel_file_path, csv_file_path):
    # Read the Excel file
    df = pd.read_excel(excel_file_path)
    
    # Write the data to a CSV file
    df.to_csv(csv_file_path, index=False)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python exltocsv.py <excel_file_path> <csv_file_path>")
    else:
        excel_file_path = sys.argv[1]
        csv_file_path = sys.argv[2]
        excel_to_csv(excel_file_path, csv_file_path)
        print(f"Converted '{excel_file_path}' to '{csv_file_path}'.")
        
        
### install 
### pip install pandas openpyxl
