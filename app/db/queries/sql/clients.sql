-- name: create_new_client<!
INSERT INTO clients (client_name)
VALUES (:client_name)
RETURNING
    id, client_name;

-- name: get_client_by_id^
SELECT id,
       client_name
FROM clients
WHERE id = :client_id
LIMIT 1;

-- name: get_client_by_name^
SELECT id,
       client_name
FROM clients
WHERE client_name = :client_name
LIMIT 1;

-- name: get_all_clients
SELECT id,
       client_name
FROM clients
LIMIT :limit
OFFSET :offset;