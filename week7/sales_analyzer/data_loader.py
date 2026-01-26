import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            if self.file_path.endswith(".csv"):
                df = pd.read_csv(self.file_path)
            elif self.file_path.endswith(".xlsx"):
                df = pd.read_excel(self.file_path)
            else:
                raise ValueError("Unsupported file format")

            if 'order_date' in df.columns:
                df['order_date'] = pd.to_datetime(df['order_date'])

            print(f"Data loaded successfully: {df.shape}")
            return df

        except Exception as e:
            print("Error loading data:", e)
            return None
