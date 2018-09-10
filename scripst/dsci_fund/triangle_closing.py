import csv
import sys
import webbrowser
import collections as coll


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


def recommend_listings(counts, user_listing, num=10):
    for listing in user_listing:
        if listing in counts:
            counts.pop(listing)

    return counts.most_common(num)


if __name__ == '__main__':
    filename, user_id = sys.argv[1:]
    # open and parse CSV file
    csvfile = open(filename, newline='')
    reader = csv.reader(csvfile)
    headers = next(reader)
    records = list(reader)

    user_listing = find_listings(records, user_id)
    user_fellow = find_travelers(records, user_listing)
    counts = count_triangles(records, user_fellow)
    recommendations = recommend_listings(counts, user_listing)

    for rec in recommendations:
        pass
        """
        Un comment the line below to see the suggestions on webbrowser
        """
        #webbrowser.open("http://airbnb.com/rooms/" + rec[0])
    print(recommendations)
