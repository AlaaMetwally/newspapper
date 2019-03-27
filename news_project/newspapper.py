import psycopg2

three_most_popular_articles = """
    select articles.title, count(log.id) as total from articles
    left join log on log.path = ('/article/' || articles.slug)
    group by articles.title order by total desc limit 3 ;
        """
most_popular_author = """
    select authors.name, count(log.id) from authors
    left join articles on articles.author = authors.id
    left join log on log.path = ('/article/' || articles.slug)
    group by authors.name order by count desc;
        """
days_highest_errors = """
    select to_char(errors_by_day.date,'Month DD, YYYY')
    as date,
    to_char
    (((errors_by_day.count::decimal /requests_by_day.count::decimal)*100)
    ,'9.99')
    || '%' as percentage from (select date(time),count(*) from log
    group by date(time)) as requests_by_day,
    (select date(time),count(*) from log where status != '200 OK'
    group by date(time)) as errors_by_day
    where requests_by_day.date = errors_by_day.date
    and
    ((errors_by_day.count::decimal /requests_by_day.count::decimal)*100) > 1;
        """


def get(query):
    db = psycopg2.connect(database="news")
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()
