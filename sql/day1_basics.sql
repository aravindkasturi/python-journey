-- Day 1 - SQL Basics
-- Learning SELECT, WHERE, ORDER BY

-- Basic select
SELECT * FROM employees;

-- Select specific columns
SELECT name, salary FROM employees;

-- WHERE condition
SELECT * FROM employees WHERE salary > 50000;

-- ORDER BY
SELECT * FROM employees ORDER BY salary DESC;

-- LIMIT
SELECT TOP 5 * FROM employees;