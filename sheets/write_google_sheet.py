import pandas as pd

def write_google_sheet(client, file_name, sheet_name, df):
  df.fillna('', inplace=True)
  print('inside write_google_sheet', df)
  sheet = client.open(file_name)
  sheet_instance = sheet.worksheet(sheet_name)
  sheet_instance.clear()
  sheet_instance.update([df.columns.values.tolist()] + df.values.tolist())