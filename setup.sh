sudo apt-update

sudo raspi-config # Then choose serial "NO" # Using UART in RPi. 
cp boot/config.txt boot/config.txt.bkp #backup
echo "enable_uart=1"  >> /boot/config.txt #Activating UART

sudo apt-get install p7zip
wget https://www.waveshare.com/w/upload/2/29/SIM7600X-4G-HAT-Demo.7z 
7za e SIM7600X-4G-HAT-Demo.7z 
cd SIM7600X-4G-HAT-Demo
chmod 777 sim7600_4G_hat_init
cp /etc/rc.local /etc/rc.local.bkp
echo "sh /home/pi/SIM7600X/sim7600_4G_hat_init" >> /etc/rc.local

sudo apt-get install minicom # Modem control and terminal emulation
minicom-D/dev/ttyS0

## Compile any demo code. ENter into the directory
chmod +x configure && ./configure && sudo make && sudo make install
sudo make clean &&sudo make && sudo ./GPS
