import pandas as pd

data_best_student_primary = {
    "Year": [
        "2014-15", "2015-16", "2016-17", "2017-18", "2018-19", 
        "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"
    ],
    "Student Name": [
        "K.PRASHANTHI (II CLASS)", "B.SHIVANI (IV CLASS)", "K.KARTHIK (V CLASS)", "CHARITHA (V CLASS)", 
        "PRAVALIKA (V CLASS)", "NAVYA (V CLASS)", "KEERTHANA (V CLASS)", "SHAIK.MAHIN (V CLASS)", 
        "MOHD RAQEEB (V CLASS)", "HADASSA (V CLASS)", "SRIMAAN (V CLASS)"
    ]
}

df_best_student_primary = pd.DataFrame(data_best_student_primary)

# Save to your Desktop instead of /mnt/data
file_path_best_student_primary = r"C:\Users\DELL\Desktop\best_student_primary.xlsx"
df_best_student_primary.to_excel(file_path_best_student_primary, index=False)

print(f"File saved to: {file_path_best_student_primary}")
