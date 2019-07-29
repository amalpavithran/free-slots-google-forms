import csv
file_csv = csv.reader(open('test.csv'))
time = ["8:00-9:00","9:00-10:00","10:15-11:15","11:15-12:15","1:00-2:00","2:00-3:00","3:00-4:00","4:00-5:00","5:00-6:00"]
# days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
file = list(file_csv)
raw = csv.reader(open('final.csv'))
raw2 = csv.reader(open('final.csv'))
raw3 = csv.reader(open('final.csv'))
years = [list(raw),list(raw2),list(raw3)]

lines=len(file)
year=['2nd Year','3rd Year','4th Year']

for row in range(1,lines):
    sname = file[row][3]
    syear = year.index(file[row][4])
    for col in range(5,10):
        times = file[row][col].split(', ')
        day = col-3
        for i in times:
            slot = time.index(i)+1
            years[syear][day][slot]=years[syear][day][slot]+sname+','
for i in year:
    with open(i+'.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(years[year.index(i)])
        print(years)
