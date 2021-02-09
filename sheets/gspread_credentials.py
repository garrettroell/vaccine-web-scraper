import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def gspread_credentials():
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  if sys.platform == 'darwin':
    creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/garrettroell/Documents/VS_code_projects/covid-vaccine-monitor/vaccine-status-credentials.json', scope)
  # raspberry pi file location
  else:
    creds = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/covid-vaccine-monitor/vaccine-status-credentials.json', scope)
  return gspread.authorize(creds)