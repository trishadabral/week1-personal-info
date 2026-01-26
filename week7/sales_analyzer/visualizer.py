import matplotlib.pyplot as plt
import os

class Visualizer:
    def __init__(self, df):
        self.df = df

    def create_charts(self, output_dir="data/reports"):
        os.makedirs(output_dir, exist_ok=True)

        # Monthly sales trend
        monthly = self.df.groupby(self.df['order_date'].dt.to_period('M'))['total_amount'].sum()
        plt.figure(figsize=(10,5))
        monthly.plot(marker='o')
        plt.title("Monthly Sales Trend")
        plt.xlabel("Month")
        plt.ylabel("Sales")
        plt.grid()
        plt.savefig(f"{output_dir}/monthly_sales.png")
        plt.close()

        # Category sales
        category = self.df.groupby('category')['total_amount'].sum()
        plt.figure(figsize=(10,5))
        category.plot(kind='bar')
        plt.title("Sales by Category")
        plt.xlabel("Category")
        plt.ylabel("Sales")
        plt.tight_layout()
        plt.savefig(f"{output_dir}/category_sales.png")
        plt.close()

        # Pie chart
        plt.figure(figsize=(8,8))
        category.plot(kind='pie', autopct='%1.1f%%')
        plt.title("Category Contribution")
        plt.ylabel("")
        plt.savefig(f"{output_dir}/category_pie.png")
        plt.close()
