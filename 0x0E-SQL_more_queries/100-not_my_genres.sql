--not my g
SELECT name
FROM tv_genres
WHERE id NOT IN (
SELECT genre_id
FROM shows_genres
WHERE show_id = (
SELECT id
FROM tv_shows
WHERE title = 'Dexter'
)
)
ORDER BY name ASC;
