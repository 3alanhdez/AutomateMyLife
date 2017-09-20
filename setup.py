import os
import subprocess
import logging
import tarfile

# Terminal: python3 setup.py
#	Created 2017 by Alan Hernandez
# automate updating and installing software to 
# linux machines on initial OS install

user = 'pi'
password = 'raspberry'
static_ip = '192.168.2.143'

def initialize():
	updateOS()
	set_static_ip()
	network_folder()
	return

#initialize
def updateOS():
	subprocess.call('sudo apt-get update -y', shell=True)
	subprocess.call('sudo apt-get upgrade -y', shell=True)
	return

#static ip address
def set_static_ip(static_ip):
	subprocess.call('sudo ifconfig eth0 down', shell=True)
	subprocess.call('sudo ifconfig eth0 ' + static_ip, shell=True)
	subprocess.call('sudo ifconfig eth0 up', shell=True)
	return

#install samba network folder
# samba not complete, need nano conf file
def network_folder():
	subprocess.call('sudo apt-get install samba samba-common-bin', shell=True)
	subprocess.call('sudo nano /etc/samba/smb.conf', shell=True)
	#http://raspberrypihq.com/how-to-share-a-folder-with-a-windows-computer-from-a-raspberry-pi/
	return	

#install apache
def apache():
	subprocess.call('cd', shell=True)
	subprocess.call('sudo apt-get install apache2 -y', shell=True)
	subprocess.call('cd /var/www/html', 'ls -al', shell=True)
	return

#install php
#complete: write to file
def php():
	subprocess.call('sudo apt-get install php5 libapache2-mod-php5 -y', shell=True)
	subprocess.call(["sudo leafpad index.php"])
#^^ write to file: <?php echo "hello world"; ?>"
	subprocess.call('sudo rm index.html', shell=True)
	subprocess.call('sudo service apache2 restart', shell=True)
	return

#install mySQL
def mySQL(password):
	subprocess.call('sudo apt-get install mysql-server php5-mysql -y', shell=True)
#insert password	
	subprocess.call('sudo service apache2 restart', shell=True)
	return

#install wordpress
#-P / downloads files to specific folder
def wordpress(user, password):
	subprocess.call('sudo wget -P /var/www/html http://wordpress.org/latest.tar.gz', shell=True)
	subprocess.call('cd /var/www/html && sudo tar xzf latest.tar.gz', shell=True)
	subprocess.call('sudo mv  -v /var/www/html/wordpress/* /var/www/html', shell=True)
	subprocess.call('cd /var/www/html && sudo rm -rf wordpress latest.tar.gz', shell=True)
	subprocess.call('mysql -uroot -phalo$', shell=True) #enter password
	subprocess.call('create database wordpress;', shell=True) #not sure if will run correctly in subprocess.call
	return
	
##########
#insert functions below

	
#scrap code (do not uncomment)
#-----------------------
#tar = tarfile.open(/var/www/html/latest.tar.gz) #tar created for wordpress install below
#tar.extractall()
#tar.close()

#subprocess.call('cd /var/www/html; sudo tar xzf latest.tar.gz -C /var/www/html')

#subprocess.call(['mysql ', user, password], shell=True)
#-----------------------
