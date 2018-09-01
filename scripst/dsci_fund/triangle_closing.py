import csv
import collections as coll

# open and parse CSV file
csvfile = open("../reviews.csv", newline='')
reader = csv.reader(csvfile)
headers = next(reader)
records = list(reader)

jonathan = "1465258"
jonathan_reviews = []


def find_listings(records, user_id):
    # find listings of users
    listings = set()
    for row in records:
        if row[3] == user_id:
            listings.add(row[0])
    return listings


def find_travelers(records, listings):
     # find fellow travellers
    fellow_travellers = set()
    for row in records:
        if row[0] in listings:
            fellow_travellers.add(row[3])
    return fellow_travellers


def count_triangles(records, fellow_travelers):
    triangles = []
    # fins triangles user is a part of
    for row in records:
        if row[3] in fellow_travelers:
            triangles.append(row[0])
    return coll.Counter(triangles)


def recommend_listings(counts, user_listing):
    for listing in user_listing:
        if listing in counts:
            counts.pop(listing)

    return counts.most_common(5)
