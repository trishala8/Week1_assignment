import csv
with open('FL_insurance_sample.csv', 'rb') as f,open('out.csv', 'wb') as f_out:
     reader = csv.reader(f)
     writer = csv.writer(f_out)
     for row in reader:
        writer.writerow((row[1], row[2], row[4], row[5], row[8], row[10]))
