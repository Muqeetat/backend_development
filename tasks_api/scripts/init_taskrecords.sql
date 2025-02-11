-- ====================================================================
-- Drop the 'taskrecords' database if it exists
-- ====================================================================
DROP DATABASE IF EXISTS taskrecords;

-- ====================================================================
-- Create a new 'taskrecords' database
-- ====================================================================
CREATE DATABASE taskrecords;

-- ====================================================================
-- Drop the 'tasks' and 'users' tables if they exist
-- ====================================================================
DROP TABLE IF EXISTS public.tasks;
DROP TABLE IF EXISTS public.users;

-- ====================================================================
-- Reset the sequence for 'tasks' table to the max ID value
-- ====================================================================
SELECT setval('tasks_id_seq', (SELECT MAX(id) FROM tasks));

-- ====================================================================
-- Reset the sequence for 'users' table to the max ID value
-- ====================================================================
SELECT setval('users_id_seq', (SELECT MAX(id) FROM users));
