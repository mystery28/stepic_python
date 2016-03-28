
# copy to destination folder
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test

# restart services
#gunicorn -b 0.0.0.0:8080 hello:app &
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi &
sudo /etc/init.d/nginx restart
#sudo /etc/init.d/gunicorn restart
