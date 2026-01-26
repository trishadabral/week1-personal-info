from sales_analyzer.data_loader import DataLoader
from sales_analyzer.data_cleaner import DataCleaner
from sales_analyzer.analyzer import SalesAnalyzer
from sales_analyzer.visualizer import Visualizer
from sales_analyzer.reporter import Reporter

DATA_PATH = "data/raw/sales_data.csv"

def main():
    loader = DataLoader(DATA_PATH)
    df = loader.load_data()

    cleaner = DataCleaner(df)
    clean_df = cleaner.clean()

    analyzer = SalesAnalyzer(clean_df)
    visualizer = Visualizer(clean_df)
    reporter = Reporter(clean_df, analyzer)

    print("Basic Stats:")
    print(analyzer.basic_stats())

    visualizer.create_charts()
    reporter.generate_excel_report()

if __name__ == "__main__":
    main()
