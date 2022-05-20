# Functions to clean columns

def format_case_number(case_number_column):
    case_number_column = case_number_column.map(lambda x: x[:10])
    case_number_column = case_number_column.str.replace('.','-', regex=True)
    return case_number_column 
    
def get_month(case_number_column, df):
    import pandas as pd
    return pd.to_numeric(df[case_number_column].map(lambda x: x[5:7]))
    
def format_year(year_column):
    import pandas as pd
    return (pd.to_datetime(year_column, format='%Y')).dt.year
   
###modificar invalid
def format_type(Type_column):
    Type_column.replace('Boat', 'Watercraft', inplace=True)
    Type_column.replace('Boating', 'Watercraft', inplace=True)
    Type_column.replace('Boatomg', 'Watercraft', inplace=True)
    return Type_column

def format_country(country_column):
    country_column.replace('TAIWAN', 'TAIWAN, PROVINCE OF CHINA', inplace=True)
    country_column.replace('TANZANIA', 'TANZANIA, UNITED REPUBLIC OF', inplace=True)
    country_column.replace('THE BALKANS', 'UNKNOWN', inplace=True)
    country_column.replace('TRINIDAD & TOBAGO', 'TRINIDAD AND TOBAGO', inplace=True)
    country_column.replace('TURKS & CAICOS', 'TURKS AND CAICOS ISLANDS', inplace=True)
    country_column.replace('UNITED ARAB EMIRATES (UAE)', 'UNITED ARAB EMIRATES', inplace=True)
    country_column.replace('USA', 'UNITED STATES', inplace=True)
    country_column.replace('VENEZUELA', 'VENEZUELA, BOLIVARIAN REPUBLIC OF', inplace=True)
    country_column.replace('VIETNAM', 'VIET NAM', inplace=True)
    country_column.replace('WESTERN SAMOA', 'SAMOA', inplace=True)    
    country_column.replace('NORTH ATLANTIC OCEAN', 'UNKNOWN', inplace=True)
    country_column.replace('NORTH ATLANTIC OCEAN ', 'UNKNOWN', inplace=True)
    country_column.replace('NORTH PACIFIC OCEAN', 'UNKNOWN', inplace=True)
    country_column.replace('NORTH SEA', 'UNKNOWN', inplace=True)
    country_column.replace('NORTHERN ARABIAN SEA', 'UNKNOWN', inplace=True)
    country_column.replace('PACIFIC OCEAN', 'UNKNOWN', inplace=True)
    country_column.replace('PACIFIC OCEAN ', 'UNKNOWN', inplace=True)
    country_column.replace('PERSIAN GULF', 'UNKNOWN', inplace=True)
    country_column.replace('RED SEA', 'UNKNOWN', inplace=True)
    country_column.replace('RED SEA / INDIAN OCEAN', 'UNKNOWN', inplace=True)
    country_column.replace('REUNION', 'UNKNOWN', inplace=True)
    country_column.replace('RED SEA / INDIAN OCEAN', 'UNKNOWN', inplace=True)
    country_column.replace('SOUTH ATLANTIC OCEAN', 'UNKNOWN', inplace=True)
    country_column.replace('SOUTH PACIFIC OCEAN', 'UNKNOWN', inplace=True)
    country_column.replace('ST. MAARTIN', 'SAINT MARTIN (FRENCH PART)', inplace=True)
    country_column.replace('ST. MARTIN', 'SAINT MARTIN (FRENCH PART)', inplace=True)
    country_column.replace('SUDAN?', 'SUDAN', inplace=True)
    country_column.replace('Seychelles', 'SEYCHELLES', inplace=True)
    country_column.replace('Sierra Leone', 'SIERRA LEONE', inplace=True)
    country_column.replace('ST HELENA, British overseas territory', 'SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA', inplace=True)
    country_column.replace('OKINAWA', 'JAPAN', inplace=True)
    country_column.replace('PALESTINIAN TERRITORIES', 'PALESTINE, STATE OF', inplace=True)
    country_column.replace('RUSSIA', 'RUSSIAN FEDERATION', inplace=True)
    country_column.replace('SCOTLAND', 'UNITED KINGDOM', inplace=True)
    country_column.replace('MALDIVE ISLANDS', 'MALDIVES', inplace=True)
    country_column.replace('SOUTH CHINA SEA', 'CHINA', inplace=True)
    country_column.replace('SOUTH KOREA', 'KOREA, REPUBLIC OF', inplace=True)
    country_column.replace('MALDIVE ISLANDS', 'MALDIVES', inplace=True)
    country_column.replace('MEXICO ', 'MEXICO', inplace=True)
    country_column.replace('MICRONESIA', 'MICRONESIA, FEDERATED STATES OF', inplace=True)
    country_column.replace('MID ATLANTIC OCEAN', 'UNKNOWN', inplace=True)
    country_column.replace('NETHERLANDS ANTILLES', 'NETHERLANDS', inplace=True)
    country_column.replace('NEVIS', 'SAINT KITTS AND NEVIS', inplace=True)
    country_column.replace('NEW BRITAIN', 'PAPUA NEW GUINEA', inplace=True)
    country_column.replace('NEW GUINEA', 'PAPUA NEW GUINEA', inplace=True)
    country_column.replace('NICARAGUA ', 'NICARAGUA', inplace=True)
    country_column.replace(' TONGA', 'TONGA', inplace=True)
    country_column.replace('ADMIRALTY ISLANDS', 'PAPUA NEW GUINEA', inplace=True)
    country_column.replace('ANDAMAN / NICOBAR ISLANDAS', 'INDIA', inplace=True)
    country_column.replace('ANTIGUA', 'ANTIGUA AND BARBUDA', inplace=True)
    country_column.replace('ATLANTIC OCEAN', 'UNKNOWN', inplace=True)
    country_column.replace('AZORES', 'PORTUGAL', inplace=True)
    country_column.replace('BRITISH ISLES', 'UNITED KINGDOM', inplace=True)
    country_column.replace('BRITISH VIRGIN ISLANDS', 'VIRGIN ISLANDS, BRITISH', inplace=True)
    country_column.replace('BRITISH WEST INDIES', 'VIRGIN ISLANDS, BRITISH', inplace=True)
    country_column.replace('CAPE VERDE', 'CABO VERDE', inplace=True)
    country_column.replace('CARIBBEAN SEA', 'UNKNOWN', inplace=True)
    country_column.replace('COLUMBIA', 'COLOMBIA', inplace=True)
    country_column.replace('DIEGO GARCIA', 'UNKNOWN', inplace=True)
    country_column.replace('EGYPT / ISRAEL', 'EGYPT', inplace=True)
    country_column.replace('ENGLAND', 'UNITED KINGDOM', inplace=True)
    country_column.replace('FEDERATED STATES OF MICRONESIA', 'MICRONESIA, FEDERATED STATES OF', inplace=True)
    country_column.replace('Fiji', 'FIJI', inplace=True)
    country_column.replace('GRAND CAYMAN', 'CAYMAN ISLANDS', inplace=True)
    country_column.replace('GULF OF ADEN', 'UNKNOWN', inplace=True)
    country_column.replace('INDIAN OCEAN', 'INDIA', inplace=True)
    country_column.replace('IRAN', 'IRAN, ISLAMIC REPUBLIC OF', inplace=True)
    country_column.replace('JOHNSTON ISLAND', 'UNITED STATES', inplace=True)
    return country_column

def get_country_codes(clean_country_column):
    import pycountry
    input_countries = list(clean_country_column)
    countries = {}
    for country in pycountry.countries:
        countries[country.name.upper()] = country.alpha_2
    codes = []
    for country in input_countries:
        if country in list(countries.keys()):
            codes.append(countries.get(country, countries))
        else: 
            codes.append('UNKNOWN')
    return codes

#Mirar por que sale standing en vez de wading
def format_activity(activity_column, df):
    import numpy as np
    import pandas as pd
    df[activity_column] = df[activity_column].fillna('')
    df[activity_column] = df[activity_column].str.lower()
    activity_df = pd.DataFrame({'Activity': {0: 'surfing', 1: 'swimming', 2: 'wading', 3: 'spearfishing',
                                             4: 'fishing', 5: 'snorkeling', 6: 'windsurfing',
                                             7: 'sea disaster', 8: 'rowing sports'},
                                'Keywords': {0: 'surfing,surf,boogie,body', 1: 'swim,swimming,floating,bathing', 
                                             2: 'wading,walking,standing',3: 'spearfishing', 4: 'fishing', 
                                             5: 'snorkeling,diving,freediving', 6: 'windsurfing', 7: 'disaster', 
                                             8: 'kayaking,paddle,rowing,canoeing,paddling'}})
    activity_df['Keywords'] = activity_df['Keywords'].str.split(',')
    df[activity_column] = (df[activity_column].str.split(' ').apply(
                        lambda x: list(set([str(a) for y in
                        x for a,b in
                        zip(activity_df['Activity'], activity_df['Keywords']) for c in
                        b if str(c) in
                        str(y)]))).str.join(', '))
    df[activity_column].replace('spearfishing, fishing','spearfishing')
    df[activity_column].replace('windsurfing, surfing', 'windsurfing')
    df.loc[df[activity_column].str.contains(','), activity_column] = 'multiple activities'
    df[activity_column].replace('', np.nan, regex=True, inplace=True)
    return


def format_sex(sex_column, df):
    import numpy as np
    x = set(df.groupby(sex_column).agg({sex_column: ['count']}).index)
    df[sex_column].replace(list(x - {'F', 'M'}), np.nan, inplace=True)
    return

def format_age(age_column):
    import pandas as pd
    import numpy as np
    age_column = pd.to_numeric(age_column, errors='coerce').fillna(0).astype(int)
    age_column.replace(0, np.nan, inplace=True)
    return age_column

def format_fatal(fatal_column, df):
    import numpy as np
    x = set(df.groupby(fatal_column).agg({fatal_column: ['count']}).index)
    df[fatal_column].replace(list(x - {'Y', 'N'}), np.nan, inplace=True)
    return

def format_species(species_column, df):
    import numpy as np
    sharks = ['white shark', 'tiger shark', 'bull shark', 'mako shark', 'lemon shark', 
          'oceanic whitetip shark', 'blue shark', 'galapagos shark', 'caribbean reef shark',
         'dusky shark', 'blacktip shark', 'silky shark', 'grey reef shark', 'hammerhead shark', 
         'blacktip reef shark', 'sevengill shark', 'nurse shark', 'wobbegong', 'basking shark', 
          'spinner shark', 'bronze whaler shark']
    
    df[species_column] = df[species_column].fillna('')
    df[species_column] = df[species_column].str.lower()
    df[species_column] = df[species_column].str.findall('|'.join(sharks)).apply(set).str.join(', ')
    df.loc[df[species_column].str.contains(','), species_column] = np.nan
    df[species_column].replace('', np.nan, inplace=True)
    return df[species_column]
    
def get_season(month_column, latitute_column):
    import pandas as pd
    import numpy as np
    conditions = [
    (month_column == 0),
    (latitute_column < 0) & (month_column >= 1) & (month_column <= 3),
    (latitute_column < 0) & (month_column >= 4) & (month_column <= 6),
    (latitute_column < 0) & (month_column >= 7) & (month_column <= 9),
    (latitute_column < 0) & (month_column >= 10),
    (latitute_column > 0) & (month_column >= 1) & (month_column <= 3),
    (latitute_column > 0) & (month_column >= 4) & (month_column <= 6),
    (latitute_column > 0) & (month_column >= 7) & (month_column <= 9),
    (latitute_column > 0) & (month_column >= 10)
    ]

    values = ['Unknown', 'Summer', 'Autumn', 'Winter', 'Spring', 'Winter', 'Spring', 'Summer', 'Autumn']

    season_column = pd.Series(np.select(conditions, values))
    season_column.replace('Unknown', np.nan, inplace=True)
    return season_column