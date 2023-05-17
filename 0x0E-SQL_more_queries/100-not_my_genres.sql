-- uses hbtn_od_tvshows database to list all genres linked to the show Dexter
SELECT DISTINCT     genre.name
FROM                tv_genres               AS genre
    INNER JOIN      tv_show_genres          AS showgenre
        ON genre.id = showgenre.genre_id
        INNER JOIN tv_shows                 AS show
            ON showgenre.show_id = show.id
WHERE genre.name NOT IN (
    SELECT          genre.name 
    FROM            tv_genres               AS genre
        INNER JOIN tv_show_genres           AS showgenre
            ON genre.id = showgenre.genre_id
            INNER JOIN tv_shows             AS show
                ON showgenre.show_id = show.id
    WHERE show.title = "Dexter"
)
ORDER BY genre.`name` ASC;
