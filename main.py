import datetime
import os
from datetime import date
import pandas as pd

columns = ['Datum', 'Bundesland', 'Bundesland_Id', 'Altersgruppe',
           '7T_Hospitalisierung_Faelle', '7T_Hospitalisierung_Inzidenz']
url = "https://raw.githubusercontent.com/robert-koch-institut/COVID-19-Hospitalisierungen_in_Deutschland/master" \
      "/Aktuell_Deutschland_COVID-19-Hospitalisierungen.csv"

#date_today = today = str(date.today())

date_today = '2021-11-26'

today = datetime.datetime.utcnow().date()

date_yesterday = today - datetime.timedelta(days=1)

html_name = "index.html"

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

HTML_FILE_PATH = os.path.join(ROOT_DIR, html_name)

def get_csv():
    try:
        df = pd.read_csv(url, sep=',', engine='python')
        df = filter_csv(df)
        return df
    except:
        print("could not get file from Git: " + url)


def filter_csv(df):
    df_filtered = df[(df['Datum'] == date_today) & (df['Altersgruppe'] == '00+')]
    if df_filtered.empty:
        df_filtered = df[(df['Datum'] == str(date_yesterday)) & (df['Altersgruppe'] == '00+')]
        return df_filtered
    return df_filtered

def main():
    df = get_csv()
    df.to_html(html_name)
    os.system("start " + HTML_FILE_PATH)

if __name__ == '__main__':
    main()
