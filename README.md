# pybilder_start
The simple pybuilder project. It use unittest.

For Ubuntu Linux:
sudo apt-get install python3 python3-pip git
sudo pip3 install pybuilder flake8 coverage selenium
git clone https://github.com/alex-pf/pybilder_start.git

Setup selenium server:
mkdir /var/selenium/
wget http://selenium-release.storage.googleapis.com/2.43/selenium-server-standalone-2.43.1.jar
mv selenium-server-standalone-2.43.1.jar /var/selenium/server.jar
(set acthual vercion for  selenium-server-standalone)

Run server:
java -jar /var/selenium/server.jar

Build project:
cd pybilder_start
pyb

Project was build, tests run.
