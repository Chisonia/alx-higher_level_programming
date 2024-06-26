-- Import the database dump from hbtn_0d_tvshows to your MySQL server: 
-- download (same as 100-not_my_genres.sql)
-- Write a script that lists all shows 
-- without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record 
-- where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT title
FROM tv_shows
WHERE id NOT IN (
    SELECT tv_shows.id
    FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY title ASC;
