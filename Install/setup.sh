#/bin/bash

sudo cp ./portfolio-webpages.service /lib/systemd/system/

sudo systemctl daemon-reload
sudo systemctl enable portfolio-webpages
sudo systemctl restart portfolio-webpages

sleep 15s

sudo service portfolio-webpages status
