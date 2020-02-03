import pandas as pd
from sys import stderr, argv, exit


if len(argv) != 3:
    stderr.write("Arguments error. Usage:\n")
    stderr.write("\tpython data_reformat.py infile.parquet \n")
    exit(1)

with pd.read_parquet(argv[0]) as df:
    pass
