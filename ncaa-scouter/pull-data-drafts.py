import requests
from bs4 import BeautifulSoup
import pandas as pd

draft_loop = 0

while draft_loop < 2:

    if draft_loop == 0:

        draft_year = '2024'

        # URL of the website with the tables
        url = f'https://www.nbadraft.net/nba-mock-drafts/?year-mock={draft_year}'

        # Send an HTTP GET request to fetch the webpage's HTML content
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all tables in the HTML
            tables = soup.find_all('table')

            if len(tables) >= 2:
                # Use pandas to read the first two tables into DataFrames
                df1 = pd.read_html(str(tables[0]))[0]
                df2 = pd.read_html(str(tables[1]))[0]

                merged_table1 = pd.concat([df1, df2], axis=0)

            else:
                print("Not enough tables found on the webpage.")
        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)

    if draft_loop == 1:

        draft_year = '2025'

        # URL of the website with the tables
        url = f'https://www.nbadraft.net/nba-mock-drafts/?year-mock={draft_year}'

        # Send an HTTP GET request to fetch the webpage's HTML content
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all tables in the HTML
            tables = soup.find_all('table')

            if len(tables) >= 2:
                # Use pandas to read the first two tables into DataFrames
                df1 = pd.read_html(str(tables[0]))[0]
                df2 = pd.read_html(str(tables[1]))[0]

                merged_table2 = pd.concat([df1, df2], axis=0)

            else:
                print("Not enough tables found on the webpage.")
        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)

    draft_loop += 1


full_draft = pd.concat([merged_table1, merged_table2], axis=0)

print(full_draft)