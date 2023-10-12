import pandas as pd

# Define the data as a list of strings
data = [
    "1	Darius McGhee	Liberty	Sr.	9-May	G	36	162	411",
    "2	Antoine Davis	Detroit Mercy	Sr.	1-Jun	G	33	159	386",
    "3	Jordan Walker	UAB	Sr.	11-May	G	33	135	357",
    "4	Ja'Monta Black	Northwestern St.	Jr.	3-Jun	G	32	122	326",
    "5	Max Abmas	Oral Roberts	Sr.	Jun-00	G	34	119	319",
    "6	Tre Jackson	Western Caro.	Jr.	Jun-00	G	33	113	265",
    "7	Andrew Funk	Penn St.	Sr.	5-Jun	G	37	112	272",
    "-	Tylor Perry	North Texas	Sr.	11-May	G	36	112	271",
    "9	Steven Ashworth	Utah St.	Jr.	1-Jun	G	35	111	256",
    "-	Courvoisier McCauley	Indiana St.	Sr.	5-Jun	G	35	111	292",
    "11	Xavier Castaneda	Akron	Sr.	1-Jun	G	31	110	282",
    "12	Jordan Hawkins	UConn	So.	5-Jun	G	37	109	281",
    "13	Brandon Miller	Alabama	Fr.	9-Jun	F	37	106	276",
    "14	Daniel Ortiz	North Ala.	So.	Jun-00	G	33	105	257",
    "15	Kamdyn Curfman	Marshall	Jr.	Jun-00	G	32	103	255",
    "-	Demaree King	Jacksonville St.	Sr.	Jun-00	G	31	103	250",
    "17	Austin Ash	The Citadel	Sr.	3-Jun	G	30	102	257",
    "18	D'Moi Hodge	Missouri	Sr.	4-Jun	G	35	100	250",
    "-	Kam Jones	Marquette	So.	4-Jun	G	36	100	278",
    "-	Trevian Tennyson	A&M-Corpus Christi	Sr.	4-Jun	G	35	100	249",
    "21	Tajion Jones	UNC Asheville	Sr.	5-Jun	G	35	99	221",
    "-	Erik Reynolds II	Saint Joseph's	So.	2-Jun	G	33	99	261",
    "23	Drew Friberg	Belmont	Sr.	7-Jun	F	32	97	213",
    "-	Tyler Harris	South Fla.	Sr.	9-May	G	32	97	252"
]

# Create a Pandas DataFrame from the data
table2 = pd.DataFrame([line.split('\t') for line in data], columns=["Rank", "Name", "Team", "Cl", "Height", "Position", "G", "3FG", "3FGA"])

# Initialize a variable to keep track of the previous rank
previous_rank = None

# Replace dashes in the 'Rank' column with the appropriate rank
for index, row in table2.iterrows():
    if row['Rank'] == '-':
        table2.at[index, 'Rank'] = previous_rank
    else:
        previous_rank = row['Rank']

# Print the updated DataFrame
print(table2)
