import pandas as pd

class CSVHandler:
    def __init__(self, file):
        self.file = file
        self.df = None
        self.filtered_df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file)
            self.filtered_df = self.df.copy()
            return True, ""
        except Exception as e:
            return False, str(e)

    def get_info(self):
        return self.df.shape, self.df.columns.tolist()

    def get_summary(self):
        return self.df.describe()

    def get_filtered(self, column, keyword):
        if column in self.df.columns:
            self.filtered_df = self.df[self.df[column].astype(str).str.contains(keyword, case=False, na=False)]
        return self.filtered_df

    def get_chart_data(self, column):
        if column in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[column]):
                return self.df[column]
            else:
                return self.df[column].value_counts()
        return None

    def download_csv(self):
        return self.filtered_df.to_csv(index=False)
