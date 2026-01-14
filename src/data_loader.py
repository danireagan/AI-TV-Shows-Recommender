import pandas as pd

class ShowsDataLoader:
    def __init__(self, original_csv: str, processed_csv: str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv
    
    def load_and_process_data(self):
        # Load the original CSV file
        df = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines='skip').dropna()
        
        # Process the data: select relevant columns and drop duplicates
        required_columns = {'title', 'overview', 'genre'}
        missing_columns = required_columns - set(df.columns)
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
        df['combined_info'] = (
            "Title: " + df['title'] + " Overview: " + df['overview'] + " Genres: " + df['genre']
        )

        # Save the processed data to a new CSV file
        df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')
        
        return self.processed_csv