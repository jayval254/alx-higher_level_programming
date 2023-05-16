-- convert hbtn_0c_0 database to UTF8(utf8mb4, collate utf8mb4_unicode_ci) 
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Alter the charset coding in the table first_table
ALTER TABLE first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Alter the charset coding in first_table.name
ALTER TABLE first_table
MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
