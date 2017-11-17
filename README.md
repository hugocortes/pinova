# pinova
Simple wireless anova + cayenne

Credit goes to: [kreggly](http://community.mydevices.com/t/connecting-the-anova-precision-cooker-to-cayenne/3670)

## Libraries used:
[Cayenne-MQTT-Python](https://github.com/myDevicesIoT/Cayenne-MQTT-Python/)  
[pycirculate](https://github.com/erikcw/pycirculate)

## Install these first
```
sudo apt-get install python-pip
sudo apt-get install libglib2.0-dev
sudo pip install bluepy
sudo pip install pycirculate --pre
sudo pip install cayenne-mqtt
```

## Getting your Anova's MAC
`sudo hcitool lescan`

Store your MQTT credentials and Anova MAC into the config file and run!
