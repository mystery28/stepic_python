# Create database
mysql -u root -e "CREATE DATABASE qa"

# Add User
mysql -u root -e "CREATE USER 'qa_admin' IDENTIFIED BY 'qa_admin'"
mysql -u root -e "GRANT ALL ON qa.* TO 'qa_admin'"
mysql -u root -e "FLUSH PRIVILEGES"
