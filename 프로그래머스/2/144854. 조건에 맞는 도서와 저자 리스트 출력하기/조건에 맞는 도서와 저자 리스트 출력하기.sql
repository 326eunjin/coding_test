SELECT a.book_id, b.author_name, DATE_FORMAT(a.published_date, '%Y-%m-%d') AS published_date
FROM book a
left JOIN author b ON a.author_id = b.author_id where a.category='경제'

UNION

SELECT a.book_id, b.author_name, DATE_FORMAT(a.published_date, '%Y-%m-%d') AS published_date
FROM book a
RIGHT JOIN author b ON a.author_id = b.author_id where a.category='경제'

order by published_date;