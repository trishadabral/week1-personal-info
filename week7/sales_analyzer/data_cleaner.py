import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def fill_missing(self):
        """
        Fill missing values in numeric columns with median,
        and categorical columns with mode.
        """
        for col in self.df.columns:
            if self.df[col].dtype in [np.float64, np.int64]:
                # Fill numeric columns with median
                self.df[col] = self.df[col].fillna(self.df[col].median())
            else:
                # Fill categorical columns with mode
                self.df[col] = self.df[col].fillna(self.df[col].mode()[0])

    def basic_stats(self):
        """
        Compute basic stats for sales analysis.
        """
        stats = {
            'total_sales': self.df['sales'].sum(),
            'average_order_value': self.df['sales'].mean(),
            'total_orders': len(self.df),
            'unique_customers': self.df['customer_id'].nunique(),
            'unique_products': self.df['product_id'].nunique()
        }
        return stats

    def export_to_excel(self, file_name='sales_report.xlsx'):
        """
        Export cleaned DataFrame to Excel.
        """
        self.df.to_excel(file_name, index=False)
        print("Excel report generated successfully")
