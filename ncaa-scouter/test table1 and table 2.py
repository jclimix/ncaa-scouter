import requests
from bs4 import BeautifulSoup
import pandas as pd

archetypes = {
    "2WS": {"Archetype Name": "2-Way Sharpshooter", "Primary Endpoint": 139, "Secondary Endpoint": 621},
    "3DD": {"Archetype Name": "3 & D", "Primary Endpoint": 143, "Secondary Endpoint": 139},
    "CS": {"Archetype Name": "Clock Stopper", "Primary Endpoint": 851, "Secondary Endpoint": 628},
    "DTP": {"Archetype Name": "Defensive Threat (Packer)", "Primary Endpoint": 608, "Secondary Endpoint": 615},
    "DTS": {"Archetype Name": "Defensive Threat (Snatcher)", "Primary Endpoint": 615, "Secondary Endpoint": 608},
    "DDFM": {"Archetype Name": "Double Down Foul-Magnet", "Primary Endpoint": 556, "Secondary Endpoint": 851},
    "DDFTA": {"Archetype Name": "Double Down Free Throw Ace", "Primary Endpoint": 556, "Secondary Endpoint": 141},
    "DDGC": {"Archetype Name": "Double Down Glass Cleaner", "Primary Endpoint": 556, "Secondary Endpoint": 137},
    "DDL": {"Archetype Name": "Double Down Lockdown", "Primary Endpoint": 556, "Secondary Endpoint": 139},
    "DDP": {"Archetype Name": "Double Down Playmaker", "Primary Endpoint": 556, "Secondary Endpoint": 473},
    "DDRP": {"Archetype Name": "Double Down Rim Protector", "Primary Endpoint": 556, "Secondary Endpoint": 138},
    "DDSC": {"Archetype Name": "Double Down Scorer", "Primary Endpoint": 556, "Secondary Endpoint": 136},
    "DDSN": {"Archetype Name": "Double Down Sniper", "Primary Endpoint": 556, "Secondary Endpoint": 143},
    "FG": {"Archetype Name": "Floor General", "Primary Endpoint": 140, "Secondary Endpoint": 628},
    "FTA": {"Archetype Name": "Free Throw Ace", "Primary Endpoint": 141, "Secondary Endpoint": 851},
    "GCS": {"Archetype Name": "Glass Cleaning Scorer", "Primary Endpoint": 608, "Secondary Endpoint": 136},
    "GCL": {"Archetype Name": "Glass Cleaning Lockdown", "Primary Endpoint": 137, "Secondary Endpoint": 138},
    "GCP": {"Archetype Name": "Glass Cleaning Playmaker", "Primary Endpoint": 137, "Secondary Endpoint": 473},
    "GCPP": {"Archetype Name": "Glass Cleaning Pickpocket", "Primary Endpoint": 137, "Secondary Endpoint": 139},
    "HED": {"Archetype Name": "High Efficiency Dimer", "Primary Endpoint": 141, "Secondary Endpoint": 140},
    "HEGC": {"Archetype Name": "High Efficiency Glass Cleaner", "Primary Endpoint": 141, "Secondary Endpoint": 137},
    "HESNA": {"Archetype Name": "High Efficiency Snatcher", "Primary Endpoint": 141, "Secondary Endpoint": 139},
    "HESNI": {"Archetype Name": "High Efficiency Sniper", "Primary Endpoint": 141, "Secondary Endpoint": 143},
    "IFS": {"Archetype Name": "Inside Form Shooter (FG)", "Primary Endpoint": 142, "Secondary Endpoint": 141},
    "PSCR": {"Archetype Name": "Pure Shot Creator", "Primary Endpoint": 611, "Secondary Endpoint": 136},
    "LP": {"Archetype Name": "Lockdown Playmaker", "Primary Endpoint": 139, "Secondary Endpoint": 140},
    "LS": {"Archetype Name": "Lockdown Scorer", "Primary Endpoint": 139, "Secondary Endpoint": 136},
    "OFS": {"Archetype Name": "Outside Form Shooter (3FG)", "Primary Endpoint": 141, "Secondary Endpoint": 143},
    "PGC": {"Archetype Name": "Playmaking Glass Cleaner", "Primary Endpoint": 473, "Secondary Endpoint": 137},
    "PML": {"Archetype Name": "Playmaking Lockdown", "Primary Endpoint": 473, "Secondary Endpoint": 139},
    "PMRP": {"Archetype Name": "Playmaking Rim Protector", "Primary Endpoint": 473, "Secondary Endpoint": 138},
    "PMS": {"Archetype Name": "Playmaking Scorer", "Primary Endpoint": 473, "Secondary Endpoint": 136},
    "PMSC": {"Archetype Name": "Playmaking Shot Creator", "Primary Endpoint": 473, "Secondary Endpoint": 141},
    "PS": {"Archetype Name": "Playmaking Sniper", "Primary Endpoint": 473, "Secondary Endpoint": 144},
    "PGCD": {"Archetype Name": "Pure Glass Cleaner (Defensive)", "Primary Endpoint": 601, "Secondary Endpoint": 858},
    "PGCO": {"Archetype Name": "Pure Glass Cleaner (Offensive)", "Primary Endpoint": 601, "Secondary Endpoint": 856},
    "PL": {"Archetype Name": "Pure Lockdown", "Primary Endpoint": 615, "Secondary Endpoint": 138},
    "PPP": {"Archetype Name": "Pure Pickpocket", "Primary Endpoint": 615, "Secondary Endpoint": 139},
    "PPM": {"Archetype Name": "Pure Playmaker", "Primary Endpoint": 140, "Secondary Endpoint": 473},
    "PRP": {"Archetype Name": "Pure Rim Protector", "Primary Endpoint": 608, "Secondary Endpoint": 138},
    "PSM": {"Archetype Name": "Pure Scoring Machine", "Primary Endpoint": 136, "Secondary Endpoint": 600},
    "PSD": {"Archetype Name": "Pure Sharpshooter (Deadeye)", "Primary Endpoint": 143, "Secondary Endpoint": 621},
    "PSS": {"Archetype Name": "Pure Sharpshooter (Sniper)", "Primary Endpoint": 143, "Secondary Endpoint": 144},
    "SGC": {"Archetype Name": "Scoring Glass Cleaner", "Primary Endpoint": 136, "Secondary Endpoint": 137},
    "SM": {"Archetype Name": "Scoring Machine", "Primary Endpoint": 141, "Secondary Endpoint": 136},
    "SP": {"Archetype Name": "Scoring Playmaker", "Primary Endpoint": 136, "Secondary Endpoint": 473},
    "SCRP": {"Archetype Name": "Scoring Rim Protector", "Primary Endpoint": 136, "Secondary Endpoint": 138},
    "SCPRM": {"Archetype Name": "Scrappy Rim Protector", "Primary Endpoint": 139, "Secondary Endpoint": 138},
    "SS": {"Archetype Name": "Scrappy Scorer", "Primary Endpoint": 139, "Secondary Endpoint": 600},
    "STGC": {"Archetype Name": "Stretch Glass Cleaner", "Primary Endpoint": 621, "Secondary Endpoint": 601},
    "SRP": {"Archetype Name": "Stretch Rim Protector", "Primary Endpoint": 621, "Secondary Endpoint": 138},
    "TGC": {"Archetype Name": "Tempo Glass Cleaner", "Primary Endpoint": 628, "Secondary Endpoint": 137},
    "TL": {"Archetype Name": "Tempo Lockdown", "Primary Endpoint": 628, "Secondary Endpoint": 139},
    "TP": {"Archetype Name": "Tempo Playmaker", "Primary Endpoint": 628, "Secondary Endpoint": 473},
    "TRP": {"Archetype Name": "Tempo Rim Protector", "Primary Endpoint": 628, "Secondary Endpoint": 138},
    "TS": {"Archetype Name": "Tempo Scorer", "Primary Endpoint": 628, "Secondary Endpoint": 136},
    "VPTS": {"Archetype Name": "Volume 3PT Shooter", "Primary Endpoint": 618, "Secondary Endpoint": 621},
    "VSC": {"Archetype Name": "Volume Scorer", "Primary Endpoint": 618, "Secondary Endpoint": 136},
    "VSH": {"Archetype Name": "Volume Shooter", "Primary Endpoint": 618, "Secondary Endpoint": 611},
    "WG": {"Archetype Name": "Wing God", "Primary Endpoint": 140, "Secondary Endpoint": 144},
}

division = 'd1'

endpoint1 = '139'
endpoint2 = '621'

table_loop_stop = 5

tables_list = []


get_table_loop = 0

while get_table_loop < table_loop_stop:

    if get_table_loop == 0:
        page = ''
    else:
        page = 'p' + str(get_table_loop + 1)
    
    
    url = f'https://www.ncaa.com/stats/basketball-men/{division}/current/individual/{endpoint1}/{page}'
    response = requests.get(url)

    if response.status_code == 200:
        tables = pd.read_html(response.text)
        if len(tables) > 0:
            if get_table_loop == 0:
                table1 = tables[0]
            elif get_table_loop == 1:
                df = tables[0]
                table1 = pd.concat([table1, df], axis=0, ignore_index=True)
            elif get_table_loop == 2:
                df = tables[0]
                table1 = pd.concat([table1, df], axis=0, ignore_index=True)
            elif get_table_loop == 3:
                df = tables[0]
                table1 = pd.concat([table1, df], axis=0, ignore_index=True)
            elif get_table_loop == 4:
                table1 = pd.concat([table1, df], axis=0, ignore_index=True)
            elif get_table_loop == 5:
                table1 = pd.concat([table1, df], axis=0, ignore_index=True)
            elif get_table_loop == 6:
                table1 = pd.concat([table1, df], axis=0, ignore_index=True)
            elif get_table_loop == 7:
                table1 = pd.concat([table1, df], axis=0, ignore_index=True)
            elif get_table_loop == 8:
                table1 = pd.concat([table1, df], axis=0, ignore_index=True)

        else:
            print("No tables found on the webpage.")
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

    get_table_loop += 1

get_table_loop = 0

while get_table_loop < table_loop_stop:

    if get_table_loop == 0:
        page = ''
    else:
        page = 'p' + str(get_table_loop + 1)
    
    url = f'https://www.ncaa.com/stats/basketball-men/{division}/current/individual/{endpoint2}/{page}'
    response = requests.get(url)

    if response.status_code == 200:
        tables = pd.read_html(response.text)
        tables = pd.read_html(response.text)
        if len(tables) > 0:
            if get_table_loop == 0:
                df = tables[0]
                table2 = df
            elif get_table_loop == 1:
                df = tables[0]
                table2 = pd.concat([table2, df], axis=0, ignore_index=True)
            elif get_table_loop == 2:
                df = tables[0]
                table2 = pd.concat([table2, df], axis=0, ignore_index=True)
            elif get_table_loop == 3:
                df = tables[0]
                table2 = pd.concat([table2, df], axis=0, ignore_index=True)
            elif get_table_loop == 4:
                df = tables[0]
                table2 = pd.concat([table2, df], axis=0, ignore_index=True)
            elif get_table_loop == 5:
                df = tables[0]
                table2 = pd.concat([table2, df], axis=0, ignore_index=True)
            elif get_table_loop == 6:
                df = tables[0]
                table2 = pd.concat([table2, df], axis=0, ignore_index=True)
            elif get_table_loop == 7:
                df = tables[0]
                table2 = pd.concat([table2, df], axis=0, ignore_index=True)
            elif get_table_loop == 8:
                df = tables[0]
                table2 = pd.concat([table2, df], axis=0, ignore_index=True)
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
