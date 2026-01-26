import pandas as pd

class Reporter:
    def __init__(self, df, analyzer):
        self.df = df
        self.analyzer = analyzer

    def generate_excel_report(self, path="data/reports/sales_report.xlsx"):
        with pd.ExcelWriter(path, engine="openpyxl") as writer:
            pd.DataFrame([self.analyzer.basic_stats()]).to_excel(
                writer, sheet_name="Summary", index=False
            )

            self.analyzer.monthly_trends().to_excel(
                writer, sheet_name="Monthly Trends"
            )

            self.analyzer.sales_by_category().to_excel(
                writer, sheet_name="Category Analysis"
            )

            self.df.head(1000).to_excel(
                writer, sheet_name="Sample Data", index=False
            )

        print("Excel report generated successfully")
