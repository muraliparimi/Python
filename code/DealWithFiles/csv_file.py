import csv
import os

data_loc='/Users/mp/programming/python3/github/Python/data'
file_name='employee_birthday.txt'

file_path = os.path.join(data_loc, file_name)

print(f''' Example to Read files with csv.reader function''')

with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Coumn names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}')
            line_count += 1
    print(f'Processed {line_count} lines.')


    print(f''' Example to Read CSV file with csv.DictReader function ''')

    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count=0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count +=1
            print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}')
            line_count +=1
        print(f'Processed {line_count} lines.')

