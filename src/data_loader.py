import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_csv:str, processed_csv:str):
        self.orig_csv = original_csv
        self.proc_csv = processed_csv
    
    def load_and_process(self):
        df = pd.read_csv(self.orig_csv, encoding='utf-8', on_bad_lines='skip').dropna() 
        required_cols = {'Name','Genres','sypnopsis'}

        # Check missing columns
        missing = required_cols - set(df.columns)
        if missing:
            raise ValueError('Required columns missing in CSV file')
        
        df['combined_info'] = (
            'Title : ' + df['Name'] + 'Overview : ' + df['sypnopsis'] + 'Genres : ' + df['Genres']
        )

        # Store new csv with only 1 combined column
        df[['combined_info']].to_csv(self.proc_csv, encoding='utf-8', index=False)

        return self.proc_csv