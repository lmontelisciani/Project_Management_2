-- name: create_new_team<!
INSERT INTO teams (team_name)
VALUES (:team_name)
RETURNING
    id, team_name;

-- name: get_team_by_id^
SELECT id,
       team_name
FROM teams
WHERE id = :team_id
LIMIT 1;

-- name: get_team_by_name^
SELECT id,
       team_name
FROM teams
WHERE team_name = :team_name
LIMIT 1;

-- name: get_all_teams
SELECT id,
       team_name
FROM teams
LIMIT :limit
OFFSET :offset;