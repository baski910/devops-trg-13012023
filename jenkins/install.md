sudo apt-get update<br>
<br>
sudo apt install openjdk-11-jre<br>
<br>
sudo apt install openjdk-11-jdk<br>
<br>
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null<br>
<br>
<br>
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null<br>
<br>
sudo apt-get update<br>
<br>
sudo apt-get install jenkins<br>
