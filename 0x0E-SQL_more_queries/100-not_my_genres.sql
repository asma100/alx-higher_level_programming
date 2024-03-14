--not my g
SELECT title
FROM tv_shows
WHERE id NOT IN (
    SELECT DISTINCT shows_genres.show_id
        FROM shows_genres
	    JOIN tv_genres ON shows_genres.genre_id = tv_genres.id
	        WHERE tv_genres.name = 'Comedy'
		)
		ORDER BY title ASC;
