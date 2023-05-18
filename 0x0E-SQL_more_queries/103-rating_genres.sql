-- lists all genres by their rating
SELECT genre.name, SUM(r.rate) AS rating
FROM tv_genres AS genre
INNER JOIN tv_show_genres AS showgenre
ON genre.id = showgenre.genre_id
INNER JOIN tv_shows AS show
ON showgenre.show_id = show.id
INNER JOIN tv_show_ratings AS r
ON show.id = r.show_id
GROUP BY genre.name
ORDER BY rating DESC;
