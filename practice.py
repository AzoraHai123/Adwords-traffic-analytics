import pandas as pd

df = pd.read_excel(r'C:\Users\Lenovo\Downloads\Raw_data.xlsx', sheet_name='Raw_data')

keyword_map = {
    1:  ('PMP',          ['pmp', 'project management', 'pmi', 'proyectos', 'it project']),
    2:  ('CAPM',         ['capm']),
    3:  ('Scrum Master', ['scrum', 'csm', 'smum', 'srum', 'scrummaster']),
    4:  ('CSPO',         ['cspo']),
    5:  ('ITIL',         ['itil', 'itl']),
    6:  ('Simplilearn',  ['simplilearn', 'simpli', 'simpi', 'smpli', 'similearn',
                          'sipli', 'simply', 'simlilearn', 'simplelern',
                          'simplelearn', 'simplylearn', 'simplileanr',
                          'simpllearn', 'simplearn', 'simplilarn', 'simplilerarn',
                          'simplielearn', 'simplielarn', 'simplilear', 'simplilearns',
                          'simplilearning', 'skillup by simplilearn',
                          'simplilern', 'simply lern', 'simple lern']),
    7:  ('SAFe',         ['safe', 'scaled agile', 'scale agile']),
    8:  ('TOGAF',        ['togaf', 'udacity', 'it architect']),
    9:  ('AWS',          ['amazon', 'aws', 'devops']),
    10: ('Cloud',        ['cloud']),
}

def key_id(value):
    val = str(value).lower()
    for id_, (label, keywords) in keyword_map.items():
        if any(k in val for k in keywords):
            return id_
    return None

def key_label(value):
    val = str(value).lower()
    for id_, (label, keywords) in keyword_map.items():
        if any(k in val for k in keywords):
            return label
    return None

# Assign Keyword ID and Label
df['Keyword ID'] = df['Keyword'].apply(key_id)
df['Keyword Label'] = df['Keyword'].apply(key_label)

# Check unmatched
print("Unmatched rows:", df['Keyword ID'].isna().sum())
print("Unmatched keywords:", df[df['Keyword ID'].isna()]['Keyword'].unique())

# Drop Trends column
if 'Trends' in df.columns:
    df = df.drop('Trends', axis=1)

# Reorder columns
cols = [
    'Title', 'Keyword', 'Keyword ID', 'Keyword Label', 'Position',
    'Previous position', 'Last Seen', 'Search Volume', 'CPC', 'Traffic',
    'Traffic (%)', 'Traffic Cost', 'Traffic Cost (%)', 'Competition',
    'Number of Results', 'Keyword Difficulty'
]
df = df[cols]

# Save files
df.to_csv(r'E:\portfolio\my html projects\website_traffic_data.csv', index=False)

keyword_table = df[['Keyword ID', 'Keyword Label']].drop_duplicates().sort_values('Keyword ID')
keyword_table.to_csv(r'E:\portfolio\my html projects\keyword.csv', index=False)

print("\nKeyword lookup table:")
print(keyword_table)
print("\nFiles saved successfully!")