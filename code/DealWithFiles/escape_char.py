import csv
import os

data_loc='/Users/mp/programming/python3/github/Python/data'
file_name='quote_wrapping.csv'

file_path = os.path.join(data_loc, file_name)

print(f''' Example to Read files with csv.reader function''')

with open(file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ',',escapechar='|')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Coumn names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} lives at {row["address"]} and joined on {row["date joined"]}')
        line_count += 1
    print(f'Processed {line_count} lines.')