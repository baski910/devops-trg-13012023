create 2 debian instances with 2GB RAM<br>

update the hostname in both instance using the following commands<br>
sudo hostnamectl set-hostname aws-private-dns<br>
sudo hostnamectl set-hostname aws-private-dns<br>
<br>
update /etc/hosts in both master and node with private ip and host name<br>
<br>
Steps to be done in server and agent node<br>
mkdir scm<br>
cd scm<br>
wget https://apt.puppetlabs.com/puppet7-release-bullseye.deb<br>
<br>
sudo dpkg -i puppet7-release-bullseye.deb<br>
<br>
sudo apt-get update<br>
<br>
<br>
server node configuration<br>
sudo apt-get install puppetserver<br>
<br>
edit /etc/puppetlabs/puppet/puppet.conf<br>
# This file can be used to override the default puppet settings.<br>
# See the following links for more details on what settings are available:<br>
# - https://puppet.com/docs/puppet/latest/config_important_settings.html<br>
# - https://puppet.com/docs/puppet/latest/config_about_settings.html<br>
# - https://puppet.com/docs/puppet/latest/config_file_main.html<br>
# - https://puppet.com/docs/puppet/latest/configuration.html<br>
[server]<br>
vardir = /opt/puppetlabs/server/data/puppetserver<br>
logdir = /var/log/puppetlabs/puppetserver<br>
rundir = /var/run/puppetlabs/puppetserver<br>
pidfile = /var/run/puppetlabs/puppetserver/puppetserver.pid<br>
codedir = /etc/puppetlabs/code<br>
<br>
[master]<br>
certname = server-hostname<br> 
server = server-hostname<br>
(save)<br>
<br>
edit /etc/default/puppetserver<br>
# Modify this if you'd like to change the memory allocation, enable JMX, etc<br>
JAVA_ARGS="-Xms1g -Xmx1g -Djruby.logger.class=com.puppetlabs.jruby_utils.jruby.Slf4jLogger<br>
<br>
sudo systemctl start puppetserver<br>
<br>
<br>
From aws console allow traffic to the following ports for server ( edit inbound rules)<br>
443<br>
8140<br>
<br>
<br>
agent node configuration<br>
edit /etc/puppetlabs/puppet/puppet.conf<br>
[main]<br>
certname = agent-hostname 
server = server-hostname
environment = production
runinterval = 1h
<br>
<br>
sudo systemctl restart puppet-agent
<br>
at the server node<br>
/opt/puppetlabs/bin/puppetserver ca list --all<br>
<br>
<br>
<br>
(at the server issue the following command to sign the certificate)<br>
/opt/puppetlabs/bin/puppetserver ca sign --certname agent-hostname<br>
<br>
(at the agent issue the following command to test the communication)<br>
/opt/puppetlabs/bin/puppet agent -t<br>
