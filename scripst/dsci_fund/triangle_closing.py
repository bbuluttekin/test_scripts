import csv

# open and parse CSV file
csvfile = open("../reviews.csv", newline='')
reader = csv.reader(csvfile)
headers = next(reader)
records = list(reader)

jonathan = "1465258"
jonathan_reviews = []

# find listings of users
for row in records:
    if row[3] == jonathan:
        jonathan_reviews.append(row)

 # find fellow travellers
fellow_travellers = set()

listings = set([review[0] for review in jonathan_reviews])

for row in records:
    if row[0] in listings:
        fellow_travellers.add(row[3])

fellow_listing = []

# fins triangles user is a part of
for row in records:
    if row[3] in fellow_travellers:
        fellow_listing.append(row[0])
