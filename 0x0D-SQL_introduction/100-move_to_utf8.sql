-- use hbtn_0c_0 database
USE hbtn_0c_0;
-- convert hbtn_0c_0 database to UTF-8
ALTER DATABASE
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- convert first_table table to UTF-8
ALTER TABLE `first_table`
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- convert name column of first_table to UTF-8
ALTER TABLE `first_table` CONVERT TO
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
