--not my g
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
    SELECT genre_id
        FROM shows_genres
	    JOIN tv_shows ON shows_genres.show_id = tv_shows.id
	        WHERE tv_shows.title = 'Dexter'
		) AS dexter_genres ON tv_genres.id = dexter_genres.genre_id
		WHERE dexter_genres.genre_id IS NULL
		ORDER BY tv_genres.name ASC;
		
