
# copy to destination folder
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
#sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test

# restart services
sudo /etc/init.d/nginx restart
#sudo /etc/init.d/gunicorn restart
