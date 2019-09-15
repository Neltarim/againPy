sudo apt-get update
sudo apt-get install curl
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install snap
snap install hub --classic
sudo apt-get install virtualenv

#uncomment thoses lines if the install of vs code failed
#sudo apt-get install software-properties-common apt-transport-https wget
#wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
#sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo apt-get install code

cp ./code_aliases.zsh ~/.oh-my-zsh/custom/
source ~/.zshrc