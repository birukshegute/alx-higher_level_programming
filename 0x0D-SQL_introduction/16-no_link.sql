-- lists all records of the table second_table ignoring nameless entries.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
