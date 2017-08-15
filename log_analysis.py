#! /usr/bin/env python

import psycopg2


def get_query_results(query):
    # connect to news database
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    # execute the first query
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def question1():
    # JOIN log with articles to find all requests that lead to all articles
    # THEN GROUP BY articles and ORDER BY counts and LIMIT output to 3
    query1 = "SELECT title, count(*) AS num FROM log JOIN articles "\
        "ON path = CONCAT('/article/', slug) GROUP BY title ORDER "\
        "BY num DESC LIMIT 3;"
    print
    print "Most Popular Three Articles of All Time:"
    for row in get_query_results(query1):
        print '"{}" -- {} views'.format(row[0], row[1])
    return


def question2():
    # FIRST JOIN log and articles on slug matches path
    # select author id and counts from the previuos results
    # THEN join again with TABLE authors to get authots' names
    query2 = "SELECT name, num FROM authors JOIN (SELECT author, "\
        "count(*) AS num FROM log JOIN articles ON path LIKE CONCAT("\
        "'/article/', slug) GROUP BY author) AS author_views ON autho"\
        "rs.id = author_views.author ORDER BY num DESC;"
    print
    print "Most Popular Article Authors of All Time:"
    for row in get_query_results(query2):
        print '{} -- {} views'.format(row[0], row[1])
    return


def question3():
    # SUM all the error requests in a single day
    # count all the requests on that day
    # divide them to percentage and select all percentage more than 1%
    query3 = "SELECT time, percentage FROM (SELECT CAST(time AS DATE), "\
        "CAST(CAST(SUM(CASE WHEN status!= '200 OK' THEN 1 END) AS FLOAT)*"\
        "100/CAST(count(*) AS FLOAT) AS DECIMAL(18,2)) AS percentage FROM "\
        "log GROUP BY CAST(time AS DATE)) AS date_o WHERE percentage > 1;"
    print
    print "Days Did More Than 1% of Requests Lead to Errors"
    for row in get_query_results(query3):
    	print '{} -- {}% errors'.format(row[0], row[1])
    return


if __name__ == "__main__":
    question1()
    question2()
    question3()
