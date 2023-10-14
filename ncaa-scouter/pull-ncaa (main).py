import requests
from bs4 import BeautifulSoup
import pandas as pd

def find_second_to_last_stats_pager_li(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, "html.parser")

            # Find all elements with the specified class
            li_elements = soup.find_all("li", class_="stats-pager__li")

            # Check if there are at least two elements
            if len(li_elements) >= 2:
                # Find the second-to-last element
                second_to_last_element = li_elements[-2]

                # Return the text content of the second-to-last element
                return second_to_last_element.text
            else:
                return 1
        else:
            return f"Failed to retrieve the web page. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
player_comps = {
    "2WS": ["Kawhi Leonard", "Klay Thompson", "Reggie Miller"],
    "3DD": ["Khris Middleton", "Robert Covington", "Jrue Holiday"],
    "CS": ["James Harden", "Joel Embiid", "Trae Young"],
    "DTP": ["Anthony Davis", "Jaren Jackson Jr.", "Tim Duncan"],
    "DTS": ["Chris Paul", "John Stockton", "Jason Kidd"],
    "DDFM": ["Shaquille O'Neal", "Dwight Howard", "Charles Barkley"],
    "DDFTA": ["Steve Nash", "Kevin Love", "Larry Bird"],
    "DDGC": ["Bill Russell", "Kareem Abdul-Jabbar", "Hakeem Olajuwon"],
    "DDL": ["Dennis Rodman", "Ben Wallace", "Draymond Green"],
    "DDP": ["Magic Johnson", "Steve Nash", "Oscar Robertson"],
    "DDRP": ["Hakeem Olajuwon", "Kareem Abdul-Jabbar", "Wilt Chamberlain"],
    "DDSC": ["Wilt Chamberlain", "Kareem Abdul-Jabbar", "Karl Malone"],
    "DDSN": ["Larry Bird", "Tim Duncan", "Anthony Davis"],
    "FG": ["Magic Johnson", "John Stockton", "Jason Kidd"],
    "FTA": ["Steve Nash", "Stephen Curry", "Reggie Miller"],
    "GCS": ["Wilt Chamberlain", "Shaquille O'Neal", "Kareem Abdul-Jabbar"],
    "GCL": ["Dennis Rodman", "Bill Russell", "Shaquille O'Neal"],
    "GCP": ["Magic Johnson", "Zion Williamson", "Elgin Baylor"],
    "GCPP": ["Hakeem Olajuwon", "Charles Barkley", "Michael Jordan"],
    "HED": ["Steve Nash", "Magic Johnson", "Chris Paul"],
    "HEGC": ["Kareem Abdul-Jabbar", "Shaquille O'Neal", "Charles Barkley"],
    "HESNA": ["Michael Jordan", "Chris Paul", "Clyde Drexler"],
    "HESNI": ["Stephen Curry", "Larry Bird", "Ray Allen"],
    "IFS": ["Kevin Durant", "Larry Bird", "DeMar DeRozan"],
    "PSCR": ["Michael Jordan", "Kyrie Irving", "Carmelo Anthony"],
    "LP": ["Magic Johnson", "Gary Payton", "Jason Kidd"],
    "LS": ["Michael Jordan", "Allen Iverson", "Dwyane Wade"],
    "OFS": ["Steve Nash", "Stephen Curry", "Larry Bird"],
    "PGC": ["Draymond Green", "Bill Walton", "Kevin Love"],
    "PML": ["Scottie Pippen", "Kawhi Leonard", "Draymond Green"],
    "PMRP": ["Joel Embiid", "Bill Walton", "Zion Williamson"],
    "PMS": ["Zion Williamson", "Chris Paul", "Steve Nash"],
    "PMSC": ["Allen Iverson", "Kyrie Irving", "Chris Paul"],
    "PS": ["Stephen Curry", "Reggie Miller", "Steve Nash"],
    "PGCD": ["Ben Wallace", "Dennis Rodman", "Bill Russell"],
    "PGCO": ["Shaquille O'Neal", "Dwight Howard", "Charles Barkley"],
    "PL": ["Gary Payton", "Tony Allen", "Bruce Bowen"],
    "PPP": ["Alvin Robertson", "Michael Ray Richardson", "Mookie Blaylock"],
    "PPM": ["Magic Johnson", "John Stockton", "Jason Kidd"],
    "PRP": ["Hakeem Olajuwon", "Tim Duncan", "Shaquille O'Neal"],
    "PSM": ["Pete Maravich", "Larry Bird", "Karl Malone"],
    "PSD": ["Stephen Curry", "Ray Allen", "Peja Stojakovic"],
    "PSS": ["Kyle Korver", "Steve Kerr", "Joe Harris"],
    "SGC": ["Charles Barkley", "Karl Malone", "Elvin Hayes"],
    "SM": ["Michael Jordan", "Wilt Chamberlain", "Kevin Durant"],
    "SP": ["Zion Williamson", "Oscar Robertson", "Larry Bird"],
    "SCRP": ["Shaquille O'Neal", "David Robinson", "Patrick Ewing"],
    "SCPRM": ["Dikembe Mutombo", "Ben Wallace", "Rudy Gobert"],
    "SS": ["Dell Curry", "Vinnie Johnson", "Lou Williams"],
    "STGC": ["Kevin Love", "Chris Bosh", "Horace Grant"],
    "SRP": ["Pau Gasol", "Kevin Love", "Kristaps Porzingis"],
    "TGC": ["Dennis Rodman", "Bill Russell", "Wilt Chamberlain"],
    "TL": ["Gary Payton", "Scottie Pippen", "Tony Allen"],
    "TP": ["Magic Johnson", "Jason Kidd", "John Stockton"],
    "TRP": ["Dikembe Mutombo", "Hakeem Olajuwon", "Ben Wallace"],
    "TS": ["Michael Jordan", "Stephen Curry", "Kevin Durant"],
    "VPTS": ["Stephen Curry", "Ray Allen", "Reggie Miller"],
    "VSC": ["Wilt Chamberlain", "Elgin Baylor", "James Harden"],
    "VSH": ["Allen Iverson", "Stephen Curry", "George Gervin"],
    "WG": ["Michael Jordan", "Kevin Durant", "Larry Bird"]
}


archetypes = {
    "2WS": {"Archetype Name": "2-Way Sharpshooter", "Primary Endpoint": 139, "Secondary Endpoint": 621},
    "3DD": {"Archetype Name": "3 & D", "Primary Endpoint": 143, "Secondary Endpoint": 139},
    "CS": {"Archetype Name": "Clock Stopper", "Primary Endpoint": 851, "Secondary Endpoint": 628},
    "DTP": {"Archetype Name": "Defensive Threat (Packer)", "Primary Endpoint": 608, "Secondary Endpoint": 615},
    "DTS": {"Archetype Name": "Defensive Threat (Snatcher)", "Primary Endpoint": 615, "Secondary Endpoint": 608},
    "DDFM": {"Archetype Name": "Double Down Foul-Magnet", "Primary Endpoint": 556, "Secondary Endpoint": 851},
    "DDFTA": {"Archetype Name": "Double Down Free Throw Ace", "Primary Endpoint": 556, "Secondary Endpoint": 142},
    "DDGC": {"Archetype Name": "Double Down Glass Cleaner", "Primary Endpoint": 556, "Secondary Endpoint": 137},
    "DDL": {"Archetype Name": "Double Down Lockdown", "Primary Endpoint": 556, "Secondary Endpoint": 139},
    "DDP": {"Archetype Name": "Double Down Playmaker", "Primary Endpoint": 556, "Secondary Endpoint": 473},
    "DDRP": {"Archetype Name": "Double Down Rim Protector", "Primary Endpoint": 556, "Secondary Endpoint": 138},
    "DDSC": {"Archetype Name": "Double Down Scorer", "Primary Endpoint": 556, "Secondary Endpoint": 136},
    "DDSN": {"Archetype Name": "Double Down Sniper", "Primary Endpoint": 556, "Secondary Endpoint": 143},
    "FG": {"Archetype Name": "Floor General", "Primary Endpoint": 140, "Secondary Endpoint": 628},
    "FTA": {"Archetype Name": "Free Throw Ace", "Primary Endpoint": 142, "Secondary Endpoint": 851},
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
    "OFS": {"Archetype Name": "Outside Form Shooter (3FG)", "Primary Endpoint": 142, "Secondary Endpoint": 143},
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

category = [0] * 26
endpnt = [0] * 26

category [0] = 'Steals Per Game'
category [1] = '3PT%'
category [2] = 'FTA'
category [3] = 'Total Blocks'
category [4] = 'Total Steals'
category [5] = 'Double Doubles'
category [6] = 'Assists Per Game'
category [7] = 'FT%'
category [8] = 'Rebounds Per Game'
category [9] = 'FG%'
category [10] = 'FGM'
category [11] = 'Assist TO Ratio'
category [12] = 'Total Rebounds'
category [13] = 'Points Per Game'
category [14] = '3PT FGM'
category [15] = 'Minutes Per Game'
category [16] = '3PT FGA'
category [17] = 'FGA'
category [18] = 'Assists TO Ratio'
category [19] = 'Blocks Per Game'
category [20] = 'Field Goal %'
category [21] = '3PT Per Game'
category [22] = 'Defensive Rebounds Per Game'
category [23] = 'Offensive Rebounds Per Game'
category [24] = 'Total Points'
category [25] = 'Total FGs'

endpnt [0] = 139
endpnt [1] = 143
endpnt [2] = 851
endpnt [3] = 608
endpnt [4] = 615
endpnt [5] = 556
endpnt [6] = 140
endpnt [7] = 142
endpnt [8] = 137
endpnt [9] = 141
endpnt [10] = 611
endpnt [11] = 473
endpnt [12] = 601
endpnt [13] = 136
endpnt [14] = 621
endpnt [15] = 628
endpnt [16] = 618
endpnt [17] = 618
endpnt [18] = 473
endpnt [19] = 138
endpnt [20] = 141
endpnt [21] = 144
endpnt [22] = 858
endpnt [23] = 856
endpnt [24] = 600
endpnt [25] = 611


# declare input

code = "WG"

division = 'd1'

endpoint1 = str(archetypes[code]["Primary Endpoint"])
endpoint2 = str(archetypes[code]["Secondary Endpoint"])

url1 = f"https://www.ncaa.com/stats/basketball-men/{division}/current/individual/{endpoint1}/"
url2 = f"https://www.ncaa.com/stats/basketball-men/{division}/current/individual/{endpoint2}/"

pagecnt1 = find_second_to_last_stats_pager_li(url1)
pagecnt2 = find_second_to_last_stats_pager_li(url2)


if int(pagecnt1) < int(pagecnt2):
    table_loop_stop = int(pagecnt1)

if int(pagecnt2) < int(pagecnt1):
    table_loop_stop = int(pagecnt2)

if int(pagecnt2) == int(pagecnt1):
    table_loop_stop = int(pagecnt2)

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
                df = tables[0]
                table1 = pd.concat([table1, df], axis=0, ignore_index=True)
            elif get_table_loop == 5:
                df = tables[0]
                table1 = pd.concat([table1, df], axis=0, ignore_index=True)
            elif get_table_loop == 6:
                df = tables[0]
                table1 = pd.concat([table1, df], axis=0, ignore_index=True)
            elif get_table_loop == 7:
                df = tables[0]
                table1 = pd.concat([table1, df], axis=0, ignore_index=True)
            elif get_table_loop == 8:
                df = tables[0]
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

# Initialize a variable to keep track of the previous rank
previous_rank = None

# Replace dashes in the 'Rank' column with the appropriate rank
for index, row in table1.iterrows():
    if row['Rank'] == '-':
        table1.at[index, 'Rank'] = previous_rank
    else:
        previous_rank = row['Rank']

# Initialize a variable to keep track of the previous rank
previous_rank = None

# Replace dashes in the 'Rank' column with the appropriate rank
for index, row in table2.iterrows():
    if row['Rank'] == '-':
        table2.at[index, 'Rank'] = previous_rank
    else:
        previous_rank = row['Rank']

# Find the common columns in both table1 and table2
common_columns = set(table1.columns) & set(table2.columns)

# Exclude the 'Rank' column if it exists in the common columns
if 'Rank' in common_columns:
    common_columns.remove('Rank')

# Perform an inner join on the common columns
ncaa_table = pd.merge(table1, table2, on=list(common_columns), how='inner')

string_to_search = 'Rank_x'
replacement_variable = last_table1

for column_name in ncaa_table.columns:
    if column_name.startswith(string_to_search):
        new_column_name = column_name[:-1] + replacement_variable
        ncaa_rnk1 = new_column_name
        ncaa_table.rename(columns={column_name: new_column_name}, inplace=True)

string_to_search = 'Rank_y'
replacement_variable = last_table2

for column_name in ncaa_table.columns:
    if column_name.startswith(string_to_search):
        new_column_name = column_name[:-1] + replacement_variable
        ncaa_rnk2 = new_column_name
        ncaa_table.rename(columns={column_name: new_column_name}, inplace=True)


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
                df_draft1 = pd.read_html(str(tables[0]))[0]
                df_draft2 = pd.read_html(str(tables[1]))[0]

                merged_table1 = pd.concat([df_draft1, df_draft2], axis=0)

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
                df_draft3 = pd.read_html(str(tables[0]))[0]
                df_draft4 = pd.read_html(str(tables[1]))[0]

                merged_table2 = pd.concat([df_draft3, df_draft4], axis=0)

            else:
                print("Not enough tables found on the webpage.")
        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)

    draft_loop += 1

full_draft = pd.concat([merged_table1, merged_table2], axis=0)

ncaa_table['DRFT PROJ'] = 'N/A'
ncaa_table['DRFT RNK'] = 'N/A'

for ncaa_name in ncaa_table['Name']:
    # Check if the 'Name' exists in the 'Player' column of 'full_draft'
    if ncaa_name in full_draft['Player'].values:

        ncaa_table.loc[ncaa_table['Name'] == ncaa_name, 'DRFT PROJ'] = 'Y'

        # If a match is found, get the corresponding draft ranking from 'full_draft'
        draft_rank = full_draft.loc[full_draft['Player'] == ncaa_name, '#'].values[0]
        # Update the 'DRFT RNK' column with the draft ranking
        ncaa_table.loc[ncaa_table['Name'] == ncaa_name, 'DRFT RNK'] = draft_rank

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

target_column_header = ncaa_rnk1

# Define the column you want to move
column_to_move = ncaa_rnk2

# Check if the target column exists in the DataFrame
if target_column_header in ncaa_table.columns:
    # Find the position of the target column
    target_column_position = ncaa_table.columns.get_loc(target_column_header)

    # Extract the column you want to move
    column_data = ncaa_table.pop(column_to_move)

    # Insert the extracted column right after the target column
    ncaa_table.insert(target_column_position + 1, column_to_move, column_data)

last_table1x = last_table1 + '_x'

last_table2x = last_table2 + '_x'

column_name_to_remove = last_table1x

if len(ncaa_table) > 0 and column_name_to_remove in ncaa_table:
    # Remove the column from each row in the table
    for row in ncaa_table:
        del row[column_name_to_remove]
    print(f"Column '{column_name_to_remove}' removed from the table.")
else:
    print(f"Column '{column_name_to_remove}' does not exist in the table.")

column_name_to_remove = last_table2x

if len(ncaa_table) > 0 and column_name_to_remove in ncaa_table:
    # Remove the column from each row in the table
    for row in ncaa_table:
        del row[column_name_to_remove]
    print(f"Column '{column_name_to_remove}' removed from the table.")
else:
    print(f"Column '{column_name_to_remove}' does not exist in the table.")

z = 0
for num in endpnt:
    if endpnt[z] == archetypes[code]["Primary Endpoint"]:
        PrE = category[z]
    z += 1

z = 0
for num in endpnt:
    if endpnt[z] == archetypes[code]["Secondary Endpoint"]:
        SeE = category[z]
    z += 1

arch_title = division.upper() + " - " + archetypes[code]["Archetype Name"]
print(arch_title)
print("Primary: " + PrE + " | Secondary: " + SeE)
print(player_comps[code][0] + " | " + player_comps[code][1] + " | " + player_comps[code][2])

if ncaa_table.empty:
    ncaa_table.loc[0] = ["N/A"] * len(ncaa_table.columns)
    print(ncaa_table)
else:
    # ncaa_table['Normalized'] = 94.9 - ((94.9 - 60) * ncaa_table['Avg_First_Second'] - 1) / (max_average + 100 - 1)
    ncaa_table.iloc[:, 0:2] = ncaa_table.iloc[:, 0:2].astype(int)

    means = ncaa_table.iloc[:, 0:2].mean(axis=1)

    max = max(means)

    ovr_data = ((94.9 - ((94.9 - 70.5) * means - 1) / ((max + 150) - 1)) + .1).apply(lambda x: round(x, 1))

    ncaa_table.insert(0, 'OVR', ovr_data)

    print(ncaa_table)

arch = archetypes[code]["Archetype Name"]