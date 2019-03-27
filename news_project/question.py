#!/usr/bin/env python2.7

import newspapper

print "Q1. What are the most popular three articles of all time?\n"
rows = newspapper.get(newspapper.three_most_popular_articles)
for row in rows:
    print "%s - %d views" % (row[0], row[1])
print "\n"

print "Q2. Who are the most popular article authors of all time?\n"
rows = newspapper.get(newspapper.most_popular_author)
for row in rows:
    print "%s - %d views" % (row[0], row[1])
print "\n"

print "Q3. On which days did more than 1% of requests lead to errors?\n"
rows = newspapper.get(newspapper.days_highest_errors)
for row in rows:
    print "%s - %s errors" % (row[0], row[1])
