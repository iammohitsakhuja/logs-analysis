#!/usr/bin/env python3

import database


def main():
    # Create a data object and open a connection to 'news' database
    db = database.Data("news")

    # Get the top three most viewed articles of all time
    print("The most popular three articles of all time are:")
    articles = db.get_top_articles(3)
    for article, views in articles:
        print('\t' + article.ljust(35) + '----  ' + str(views) + ' views')

    # Get the most popular article authors of all time
    print("\nThe most popular article authors of all time are:")
    authors = db.get_top_authors()
    for author, views in authors:
        print('\t' + author.ljust(35) + '----  ' + str(views) + ' views')

    # Get the days with more than 1% of requests leading to errors
    print("\nDays with more than 1% of requests leading to errors:")
    days = db.get_error_request_days()
    for day, percentage in days:
        print('\t' + str(day).ljust(35) + '----  ' + str(percentage) +
              '% errors')

    db.close()


if __name__ == "__main__":
    main()
