# Show databases
mysql -u qa_admin -p qa_admin -e "SHOW DATABASES"

# Show users grants
mysql -u qa_admin -p qa_admin -e "SHOW GRANTS FOR qa_admin"

# Show all tables
mysql -u qa_admin -p qa_admin -e "SHOW TABLES FROM qa"

# Show tables metadata
mysql -u qa_admin -p qa_admin -e "SHOW CREATE TABLE qa.question"
mysql -u qa_admin -p qa_admin -e "SHOW CREATE TABLE qa.answer"

# Show tables records
mysql -u qa_admin -p qa_admin -e "SELECT * FROM qa.question"
mysql -u qa_admin -p qa_admin -e "SELECT * FROM qa.answer"
