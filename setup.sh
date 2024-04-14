
## Install AWS CLI
sudo apt-get update
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

## Deleting the setup files
rm -rf awscliv2.zip 
rm -rf aws

## Installing Tmux
sudo apt-get -y install tmux

## Installing glances
pip install --user glances