import os
import shutil
import calendar

path = "/Users/hari/Documents/"
emp_id = 123456
file_format = '.pdf'
years = range(2011, 2026)  # 2011 to 2025 inclusive
month_abbrs = [calendar.month_abbr[i].upper() for i in range(1, 13)]

for year in years:
    folder_path = os.path.join(path, str(year))
    if os.path.exists(folder_path):
        print(f"Folder already exists: {folder_path}")
    else:
        os.mkdir(folder_path)
        print(f"Created folder: {folder_path}")

missing_payslips = []
for year in years:
    for month_abbr in month_abbrs:
        file_name = f"{emp_id}_{month_abbr}_{year}{file_format}"
        source_path = os.path.join(path, file_name)
        dest_path = os.path.join(path, str(year), file_name)
        
        if os.path.exists(source_path):
            shutil.move(source_path, dest_path)
        else:
            missing_payslips.append(file_name)

if missing_payslips:
    print("\nMissing payslips:")
    for payslip in missing_payslips:
        print(payslip)
else:
    print("\nAll payslips are properly organized!")