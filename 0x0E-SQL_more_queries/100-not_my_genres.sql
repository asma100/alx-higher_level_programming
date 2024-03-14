--not my g
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN (
    SELECT show_id
        FROM shows_genres
	    JOIN tv_genres ON shows_genres.genre_id = tv_genres.id
	        WHERE tv_genres.name = 'Comedy'
		) AS comedy_shows ON tv_shows.id = comedy_shows.show_id
		WHERE comedy_shows.show_id IS NULL
		ORDER BY tv_shows.title ASC;
