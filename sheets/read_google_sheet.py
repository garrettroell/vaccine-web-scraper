import pandas as pd

# try to drop level/blank columns
def read_google_sheet(client, file_name, sheet_name):
  sheet = client.open(file_name)
  sheet_instance = sheet.worksheet(sheet_name)
  data = sheet_instance.get_all_records()
  return pd.DataFrame.from_dict(data)