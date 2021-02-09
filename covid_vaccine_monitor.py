import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys
sys.path.append('/Users/garrettroell/Documents/VS_code_projects/covid-vaccine-monitor/')
sys.path.append('/home/pi/covid-vaccine-monitor/')
from sheets.write_google_sheet import write_google_sheet
from sheets.read_google_sheet import read_google_sheet
from sheets.gspread_credentials import gspread_credentials




def get_vaccine_status():
  url = 'https://www.northshorepharmacy.org/covid-services'
  test = requests.get(url).text
  soup = BeautifulSoup(test, 'html.parser')
  vaccine_status = soup.find_all("div", {'class': 'easy-block-v1-badge'})[3].text
  return vaccine_status

def send_email(vaccine_status):
  client = gspread_credentials()
  message_list = read_google_sheet(client, 'Covid Vaccine Status Grandma', 'Email List')

  if vaccine_status == 'Unknown status':
    message_list['Message'] = f'''Hi Grandma,\n\nThe north shore pharmacy updated its website. 
                                  This may mean that the vaccine is available. Please check the 
                                  website to see.\n\nLove,\nGarrett\n\nThis was sent by an automated 
                                  program.'''
  else:
    message_list['Message'] = f'''Hi Grandma,\n\nThe north shore pharmacy has updated its vaccine 
                                  status to {vaccine_status}.\n\nLove,\nGarrett\n\nThis was sent 
                                  by an automated program.'''

  write_google_sheet(client, 'Covid Vaccine Status Grandma', 'Email List', message_list)
  print(message_list)

if __name__ == '__main__':
  try:
    vaccine_status = get_vaccine_status()
    vaccine_status = "vaccine available"
  except:
    send_email('Unknown status')
  
  if vaccine_status != 'Awaiting Supplies':
    send_email(vaccine_status)
  else:
    print('Site says awaiting supplies')

  