from pivot_report.report import Pivot

pv = Pivot('incident.csv','assignment_group','state','result')
pv.generate()