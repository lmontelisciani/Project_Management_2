-- name: get-user-by-email^
SELECT id,
       username,
       email,
       hashed_password,
       salt,
       created_at,
       updated_at,
       first_name,
       last_name,
       is_active,
       is_project_manager,
       photo
FROM users
WHERE email = :email
LIMIT 1;


-- name: get-user-by-username^
SELECT id,
       username,
       email,
       hashed_password,
       salt,
       created_at,
       updated_at,
       first_name,
       last_name,
       is_active,
       is_project_manager,
       photo
FROM users
WHERE username = :username
LIMIT 1;


-- name: create-new-user<!
INSERT INTO users (username, email, hashed_password, salt, first_name, last_name, photo)
VALUES (:username, :email, :hashed_password, :salt, :first_name, :last_name, :photo)
RETURNING
    id, username, email, first_name, last_name, is_active, is_project_manager, photo, created_at, updated_at;


-- name: update-user-by-username<!
UPDATE
    users
SET username           = :new_username,
    email              = :new_email,
    hashed_password    = :hashed_password,
    salt               = :salt,
    first_name         = :new_first_name,
    last_name          = :new_last_name,
    photo              = :photo
WHERE username = :username
RETURNING
    username, email, first_name, last_name, is_active, is_project_manager, photo, created_at, updated_at;

-- name: get_users_by_team
SELECT u.id,
       u.username,
       u.email,
       u.hashed_password,
       u.salt,
       u.created_at,
       u.updated_at,
       u.first_name,
       u.last_name,
       u.is_active,
       u.is_project_manager,
       u.photo
FROM users u
INNER JOIN teams_users AS tu
    ON u.id = tu.user_id
WHERE tu.team_id = (SELECT teams.id FROM teams WHERE teams.team_name = :team_name);

-- name: get_all_users
SELECT u.id,
       u.username,
       u.email,
       u.hashed_password,
       u.salt,
       u.created_at,
       u.updated_at,
       u.first_name,
       u.last_name,
       u.is_active,
       u.is_project_manager,
       u.photo
FROM users u;