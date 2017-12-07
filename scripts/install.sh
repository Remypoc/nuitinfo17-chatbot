HOME_DIR="/home/ubuntu"
PROJECT_DIR="/vagrant"

echo 'HOME_DIR="/home/ubuntu"' >> .bashrc
echo 'PROJECT_DIR="/vagrant"' >> .bashrc
source .bashrc

# Dependencies installation on virtual machine
apt-get update
apt-get -y upgrade

apt-get install -y npm
# Install nodejs V8, bug with default 4.2.6 and webpack
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs

# Fix error with shared folder and npm modules
# https://medium.com/@dtinth/isolating-node-modules-in-vagrant-9e646067b36
mkdir $HOME_DIR/vagrant_node_modules
mkdir $PROJECT_DIR/node_modules
mount --bind $HOME_DIR/vagrant_node_modules $PROJECT_DIR/node_modules

cd $PROJECT_DIR
npm install
npm run build

# Manual installation:
# npm install webpack --save-dev
# npm install babel-core babel-preset-env babel-loader babel-preset-react --save-dev
# npm install react react-dom -s
# npm install recharts -s