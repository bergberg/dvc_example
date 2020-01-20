import pandas
import rarfile
import sys
from pathlib import Path

if len(sys.argv) != 3:
    sys.stderr.write('Arguments error. Usage:\n')
    sys.stderr.write('\tpython data_reformat.py infile.csv.rar outfile\n')
    sys.exit(1)

rar_path = rarfile.RarFile(sys.argv[1])

for f in rar_path.infolist():
    foutname = Path.cwd() / sys.argv[2] / (f.filename + '.parquet')
    print(f.filename + ' => ' + str(foutname))
    df = pandas.read_csv(rar_path.open(f))
    df.to_parquet(foutname)
