-- lists all shows by their rating descending
SELECT show.title, sum(r.rate) AS rating
FROM tv_shows AS show
INNER JOIN tv_show_ratings AS r
ON show.id = r.show_id
GROUP BY show.title
ORDER BY rating DESC;
