sudo apt-get update<br>
sudo apt-get install ca-certificates curl gnupg lsb-release<br>
<br>
<br>
sudo mkdir -p /etc/apt/keyrings<br>
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg<br>
<br>
<br>
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null<br>

<br>
sudo apt-get update<br>
<br>
<br>
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin<br>
<br>
sudo docker run hello-world<br>
<br>
sudo docker pull ubuntu<br>
<br>
sudo docker images<br>
<br>
sudo docker run -it ubuntu bash<br>
