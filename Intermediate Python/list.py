import pandas as pd
from urllib.request import urlretrieve


#italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'
#urlretrieve(italy_covid_url,'italy-covid-daywise.csv')

covid_df = pd.read_csv('italy-covid-daywise.csv')


total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()

print(total_cases,total_deaths)