import numpy as np
import pandas as pd
from pathlib import Path
import os


class Pivot:
    """
    Generating the pivot table report
    """

    def __init__(self, file_name, row, column, output_file_name, aggregation="count"):
        """
        Initializing
        """
        self.file_name = file_name
        if Path(os.getcwd()+"/"+self.file_name).is_file():
            self.data = pd.read_csv(os.getcwd()+"/"+self.file_name)
        else:
            raise Exception("File not found")
        self.row = row
        self.column = column
        self.output_file_name = output_file_name
        self.aggregation = aggregation

    def generate_pivot_table(self):
        """
        Generating the pivot table
        """
        if self.aggregation == "count":
            table = pd.DataFrame(self.data.groupby([self.row])[
                                 self.column].value_counts()).unstack(level=-1).fillna(0)
            for i in table.columns.values:
                table[i] = table[i].astype('int64')
            table['Total'] = table.sum(axis=1).values
            table_dict = table.to_dict()
            col_sum = table.sum(axis=0).values
            idx = 0
            for i in table_dict:
                table_dict[i]['Total'] = col_sum[idx]
                idx = idx + 1
            return pd.DataFrame(table_dict)

        else:
            raise Exception("Other aggregations are not yet supported")

    def generate(self):
        """
        Saves the generated pivot file as excel_file
        """
        self.result = self.generate_pivot_table()
        self.result.to_excel(os.getcwd()+"/"+self.output_file_name+".xlsx",index_label=self.row)
        return None
