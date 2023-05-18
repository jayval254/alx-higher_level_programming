-- Lists all show without the genre Comedy
SELECT DISTINCT show.title
FROM tv_shows AS show
LEFT JOIN tv_show_genres AS showgenre
ON show.id = showgenre.show_id
LEFT JOIN tv_genres AS genre
ON showgenre.genre_id = genre.id
WHERE show.title NOT IN (
    SELECT show.title FROM tv_shows AS show
    INNER JOIN tv_show_genres AS showgenre
    ON show.id = showgenre.show_id
    INNER JOIN tv_genres AS genre
    ON showgenre.genre_id = genre.id
    WHERE genre.name = "Comedy"
)
ORDER BY show.title ASC;
