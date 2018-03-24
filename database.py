import psycopg2


class Data:
    """
        Creates a data object that is used to represent a connection to a
        database.
    """

    def __init__(self, db_name):
        """Opens up a connection to the database."""
        self.connection = psycopg2.connect("dbname={}".format(db_name))
        self.cursor = self.connection.cursor()

    def close(self):
        """Closes and terminates the connection to the database."""
        self.connection.close()

    def get_top_articles(self, num):
        """Returns a list of articles with the most number of views."""

        query = '''
                SELECT articles.title, COUNT(*) AS views FROM articles
                INNER JOIN log ON CONCAT('/article/', articles.slug) =
                log.path GROUP BY articles.title ORDER BY views DESC
                LIMIT {};
                '''.format(num)

        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_top_authors(self):
        """
        Returns a list of authors with the most number of total views for
        their articles.
        """

        query = '''
                SELECT authors.name, SUM(article_author_view.views) AS views
                FROM (SELECT articles.title, articles.author, COUNT(*) AS views
                FROM articles INNER JOIN log ON CONCAT('/article/',
                articles.slug) = log.path GROUP BY articles.title,
                articles.author ORDER BY views DESC) AS article_author_view
                JOIN authors ON article_author_view.author = authors.id
                GROUP BY authors.name ORDER BY views DESC;
                '''

        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_error_request_days(self):
        """
        Returns a list of days that had more than 1% of requests leading to
        errors.
        """

        query = '''
                SELECT total_request_table.day, ROUND(((bad_requests * 1.0) /
                (total_requests * 1.0)) * 100, 2) AS errors FROM (SELECT
                DATE(time) AS day, COUNT(DATE(time)) AS total_requests FROM log
                GROUP BY DATE(time)) AS total_request_table JOIN (SELECT
                DATE(time) AS day, COUNT(DATE(time)) AS bad_requests FROM log
                WHERE status NOT LIKE '200 OK' GROUP BY DATE(time)) AS
                bad_request_table ON total_request_table.day =
                bad_request_table.day WHERE (((bad_requests * 1.0) /
                (total_requests * 1.0)) * 100) > 1.0;
                '''

        self.cursor.execute(query)
        return self.cursor.fetchall()
