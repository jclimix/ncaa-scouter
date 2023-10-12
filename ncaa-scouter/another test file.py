import requests
from bs4 import BeautifulSoup
import pandas as pd

division = 'd1'
category1 = '473'
category2 = '143'
tripdouble = '557'
threepct = '143'

table_loop_stop = 2


if category1 != '':

    get_table_loop = 0

    while get_table_loop < table_loop_stop:
        if get_table_loop == 0:
            page = ''
        elif get_table_loop == 1:
            page = 'p2'
        elif get_table_loop == 2:
            page = 'p3'
        elif get_table_loop == 3:
            page = 'p4'
        elif get_table_loop == 4:
            page = 'p5'
        
        url = f'https://www.ncaa.com/stats/basketball-men/{division}/current/individual/{category1}/{page}'
        response = requests.get(url)

        if response.status_code == 200:
            tables = pd.read_html(response.text)
            if len(tables) > 0:
                if get_table_loop == 0:
                    df = tables[0]
                    table1 = df
                elif get_table_loop == 1:
                    df2 = tables[0]
                elif get_table_loop == 2:
                    df3 = tables[0]
                elif get_table_loop == 3:
                    df4 = tables[0]
                elif get_table_loop == 4:
                    df5 = tables[0]
                    table1 = pd.concat([df, df2, df3, df4, df5], axis=0)

            else:
                print("No tables found on the webpage.")
        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)

        get_table_loop += 1

if category2 != '':

    get_table_loop = 0

    while get_table_loop < table_loop_stop:

        if get_table_loop == 0:
            page = ''
        elif get_table_loop == 1:
            page = 'p2'
        elif get_table_loop == 2:
            page = 'p3'
        elif get_table_loop == 3:
            page = 'p4'
        elif get_table_loop == 4:
            page = 'p5'
        
        url = f'https://www.ncaa.com/stats/basketball-men/{division}/current/individual/{category2}/{page}'
        response = requests.get(url)

        if response.status_code == 200:
            tables = pd.read_html(response.text)
            if len(tables) > 0:
                if get_table_loop == 0:
                    df = tables[0]
                    table2 = df
                elif get_table_loop == 1:
                    df2 = tables[0]
                elif get_table_loop == 2:
                    df3 = tables[0]
                elif get_table_loop == 3:
                    df4 = tables[0]
                elif get_table_loop == 4:
                    df5 = tables[0]
                    table2 = pd.concat([df, df2, df3, df4, df5], axis=0)
            else:
                print("No tables found on the webpage.")
        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)

        get_table_loop += 1

last_table1 = table1.columns[-1]
last_table2 = table2.columns[-1]

# Find the common columns in both table1 and table2
common_columns = set(table1.columns) & set(table2.columns)

# Exclude the 'Rank' column if it exists in the common columns
if 'Rank' in common_columns:
    common_columns.remove('Rank')

# Perform an inner join on the common columns
ncaa_table = pd.merge(table1, table2, on=list(common_columns), how='inner')



print(ncaa_table)
