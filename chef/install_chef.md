ec2 instance 4G - Server       - chefserver.example.com   -  18.233.158.184 	172.31.90.31
ec2 instance 2G - Workstation  - chefworkstation.example.com - 54.234.101.246	172.31.21.211
ec2 instance 1G - Node	       - chefnode1.example.com		54.162.252.223 	172.31.94.76


sudo apt-get update ( in each instance)<br>
<br>
Server
<br>
VERSION="14.12.21"<br>
wget https://packages.chef.io/files/stable/chef-server/${VERSION}/ubuntu/20.04/chef-server-core_${VERSION}-1_amd64.deb<br>
<br>
<br>
sudo apt install ./chef-server-core_${VERSION}-1_amd64.deb
<br>
<br>
sudo chef-server-ctl reconfigure
<br>
(create bash variables)<br>
USERNAME="chefadmin"<br>
FIRST_NAME="Chef"<br>
LAST_NAME="Administrator"<br>
EMAIL="chefadmin@example.com"<br>
PASSWORD="Passw0rd"<br>
KEY_PATH="/home/admin/chefadmin.pem"<br>
<br>
sudo chef-server-ctl user-create ${USERNAME} ${FIRST_NAME} ${LAST_NAME} ${EMAIL} ${PASSWORD} -f ${KEY_PATH}<br>
<br>
<br>
sudo chef-server-ctl user-list<br>
<br>
sudo chef-server-ctl org-create exampleorg 'example, Inc.' --association_user chefadmin --filename /home/admin/exampleorg-validator.pem<br>
<br>
sudo chef-server-ctl org-list<br>
<br>
<br>
Workstation<br>
<br>
VERSION="22.1.745"<br>
wget https://packages.chef.io/files/stable/chef-workstation/${VERSION}/debian/11/chef-workstation_${VERSION}-1_amd64.deb<br>
#wget https://packages.chef.io/files/stable/chef-workstation/${VERSION}/ubuntu/20.04/chef-workstation_${VERSION}-1_amd64.deb<br>
<br>
<br>
<br>
sudo dpkg -i chef-workstation_${VERSION}-1_amd64.deb<br>
<br>
chef generate repo chef-repo<br>
<br>
mkdir ~/chef-repo/.chef<br>
cd chef-repo<br>
<br>
scp root@IP_OF_CHER_SERVER:/root/*.pem ~/chef-repo/.chef/<br>
<br>
chef generate cookbook cheffirstcookbook<br>
<br>
vim ~/chef-repo/.chef/config.rb<br>
(add the below contents)<br>
<br>
current_dir = File.dirname(__FILE__)<br>
log_level                :info<br>
log_location             STDOUT<br>
node_name                'chefadmin'<br>
client_key               "chefadmin.pem"<br>
validation_client_name   'exampleorg-validator'<br>
validation_key           "exampleorg-validator.pem"<br>
chef_server_url          'https://chefserver.example.com/organizations/exampleorg'<br>
cache_type               'BasicFile'<br>
cache_options( :path => "#{ENV['HOME']}/.chef/checksums" )<br>
cookbook_path            ["#{current_dir}/../cookbooks"]<br>
<br>
(save)<br>
<br>
<br>
knife ssl fetch<br>
<br>
knife client list<br>
<br>
<br>
bootstrap a node<br>
(pwd = ~/chef-repo )<br>
knife bootstrap <ip address of EC2> -x ec2-user --sudo --ssh-identity-file ./.chef/<file of pem> --node_name <hostname><br>
<br>
knife bootstrap IP_OF_CHEF_NODE -x ubuntu --sudo --ssh-identity-file ./.chef/keyforchef.pem --node_name chefnode1.example.com<br>
<br>
cd cookbooks<br>
<br>
chef generate cookbook myfirstcookbook<br>
<br>
edit ~/chef-repo/cookbooks/myfirstcookbook/recipes/default.rb<br>
<br>
execute "upgrade-update" do<br>
  command "sudo apt-get update"<br>
  action :run<br>
end<br>
<br>
cd ../   (pwd = ~/chef-repo )<br>
<br>
Execute the following command (from chef-repo)<br>
knife cookbook upload myfirstcookbook<br>
Add the recipe to a node’s run-list, replacing nodename with your chosen node’s name:<br>
<br>
knife node run_list add nodename "recipe[myfirstcookbook]"<br>
<br>
knife ssh "name:nodename" 'sudo chef-client' -x ubuntu --ssh-identity-file ./.chef/keyforchef.pem<br>
<br>
edit ~/chef-repo/cookbooks/myfirstcookbook/recipes/apache.rb<br>
<br>
package "apache2" do<br>
  action :install<br>
end<br>
<br>
service "apache2" do<br>
  action [:enable, :start]<br>
end<br>	
<br>
<br>
knife cookbook upload lamp_stack<br>
Add the recipe to a node’s run-list, replacing nodename with your chosen node’s name:<br>
<br>
knife node run_list add nodename "recipe[myfirstcookbook::apache]"<br>
<br>
knife ssh "name:nodename" 'sudo chef-client' -x ubuntu --ssh-identity-file ./.chef/keyforchef.pem<br>
