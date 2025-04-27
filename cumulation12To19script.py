import pandas as pd
import re
from ace_tools import display_dataframe_to_user

# Load the Excel file
file_path = '/mnt/data/G Charts.xlsx'
xls = pd.ExcelFile(file_path)
sheets = xls.sheet_names

all_structures = {}
skip_keywords = ['Structure', 'Grammatical', 'S#', 'Chinese Sentence']

# Parse each sheet
for sheet in sheets:
    df = pd.read_excel(file_path, sheet_name=sheet, header=None)
    if sheet == 'L13':
        # L13 has a separate format
        for idx, row in df.iloc[1:].iterrows():
            struct = row[2]
            if pd.isna(struct):
                continue
            struct_str = str(struct).strip()
            if any(sk in struct_str for sk in skip_keywords):
                continue
            explanation = row[3] if not pd.isna(row[3]) else ''
            freq = row[4] if not pd.isna(row[4]) else 0
            try:
                freq_int = int(freq)
            except:
                freq_int = 0
            example_field = row[5] if 5 in row.index and not pd.isna(row[5]) else ''
            if example_field:
                m = re.match(r'(.+?)\s*[（(]\s*["]?(.+?)[”"]?\s*[）)]', example_field)
                if m:
                    example = m.group(1).strip()
                    translation = m.group(2).strip()
                else:
                    example = example_field.strip()
                    translation = ''
            else:
                example = ''
                translation = ''
            if struct_str not in all_structures:
                all_structures[struct_str] = {
                    'explanation': explanation,
                    'frequency': freq_int,
                    'example': example,
                    'translation': translation
                }
            else:
                all_structures[struct_str]['frequency'] += freq_int
    else:
        # Standard format sheets
        for idx, row in df.iloc[1:].iterrows():
            struct = row[0]
            if pd.isna(struct):
                continue
            struct_str = str(struct).strip()
            # Stop at next header if present
            if any(sk in struct_str for sk in ['Grammatical Structure', 'Structure', 'S#']):
                break
            if any(sk in struct_str for sk in skip_keywords):
                continue
            explanation = row[1] if not pd.isna(row[1]) else ''
            freq = row[2] if not pd.isna(row[2]) else 0
            try:
                freq_int = int(freq)
            except:
                freq_int = 0
            example = row[3] if 3 in row.index and not pd.isna(row[3]) else ''
            translation = row[4] if 4 in row.index and not pd.isna(row[4]) else ''
            if struct_str not in all_structures:
                all_structures[struct_str] = {
                    'explanation': explanation,
                    'frequency': freq_int,
                    'example': example,
                    'translation': translation
                }
            else:
                all_structures[struct_str]['frequency'] += freq_int

# Build DataFrame
df_out = pd.DataFrame([
    {
        'Structure': k,
        'English Explanation': v['explanation'],
        'Frequency': v['frequency'],
        'Example': v['example'],
        'Translation': v['translation']
    }
    for k, v in all_structures.items()
])
df_out = df_out.sort_values('Structure').reset_index(drop=True)

# Display to user
display_dataframe_to_user(name='Grammar Structures', dataframe=df_out)
