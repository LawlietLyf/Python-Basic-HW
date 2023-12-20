#This file is for Homework in week 5
#Task: Extract hyperlinks from an Excel file

#Author: Yifu Liu 2101111263

import xlrd
import pandas as pd
import re

# Function to extract URL from a text using regex

uploaded_file_path='H1.xls'
def extract_url_from_text(text):
    url_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    url_match = re.search(url_regex, text)
    return url_match.group(0) if url_match else None

# Load the workbook
workbook_xlrd = xlrd.open_workbook(uploaded_file_path, on_demand=True)
sheet = workbook_xlrd.sheet_by_index(0)

# Prepare a new DataFrame to store the results
df_processed = pd.DataFrame(columns=[sheet.cell_value(0, col) for col in range(sheet.ncols)] + ['URLs'])
#  '在线文档地址（必填）' is the n-th column
n=df_processed.columns.get_loc("在线文档地址（必填）")
# Iterate over the rows in the specific column
for row in range(1, sheet.nrows):
    row_values = sheet.row_values(row)
    cell_value = row_values[n]  

    # Check if cell contains a hyperlink
    url = None
    try:
        link = sheet.hyperlink_map.get((row, n))
        if link:
            url = link.url_or_path
    except AttributeError:
        # If hyperlink_map is not available or does not contain the link
        url = extract_url_from_text(cell_value)

    # If no hyperlink, try extracting from text
    if not url:
        url = extract_url_from_text(cell_value)

    # Append to the DataFrame
    df_processed.loc[row-1] = row_values + [url]

# Saving the processed DataFrame to a new .xlsx file
output_file_path = 'New_H1.xls'
df_processed.to_excel(output_file_path, index=False)
