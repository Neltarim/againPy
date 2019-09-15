sudo apt-get update
sudo apt-get install curl
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
sudo apt-get install snap
snap install hub --classic
sudo apt-get install virtualenv

cp ./new-machine/code_aliases.zsh ~/.oh-my-zsh/custom/
source ~/.zshrc