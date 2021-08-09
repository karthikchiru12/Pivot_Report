# Pivot_Report

A simple python program to generate the pivot report and save it in excel sheet.

```
from pivot_report.report import Pivot

pv = Pivot('input_file.csv','Row','Column','output_file_name')
pv.generate()

```
