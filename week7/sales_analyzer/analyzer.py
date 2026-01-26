import pandas as pd
import numpy as np

class SalesAnalyzer:
    def __init__(self, df):
        self.df = df

    def basic_stats(self):
        return {
            "total_sales": self.df['total_amount'].sum(),
            "average_order_value": self.df['total_amount'].mean(),
            "total_orders": len(self.df),
            "unique_customers": self.df['customer_id'].nunique(),
            "unique_products": self.df['product_id'].nunique()
        }

    def sales_by_category(self):
        return self.df.groupby('category').agg(
            total_sales=('total_amount', 'sum'),
            total_quantity=('quantity', 'sum'),
            orders=('order_id', 'count')
        ).sort_values('total_sales', ascending=False)

    def monthly_trends(self):
        self.df['month_year'] = self.df['order_date'].dt.to_period('M')
        monthly = self.df.groupby('month_year').agg(
            total_sales=('total_amount', 'sum'),
            orders=('order_id', 'count'),
            customers=('customer_id', 'nunique')
        )
        monthly['growth_rate'] = monthly['total_sales'].pct_change() * 100
        return monthly
