# Check users grants
mysql -u qa_admin -p qa_admin -e "SHOW GRANTS FOR qa_admin"

# Test new tables
mysql -u qa_admin -p qa_admin -e "SELECT * FROM qa.question"
mysql -u qa_admin -p qa_admin -e "SELECT * FROM qa.answer"
