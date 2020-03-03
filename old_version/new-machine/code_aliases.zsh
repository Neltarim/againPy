#alias
alias aliasedit='vi ~/.oh-my-zsh/custom/code_aliases.zsh'
alias aliasupdate='source ~/.zshrc'
alias aliasup='source ~/.zshrc'

#python
alias py='python3'
alias py2='python2'
alias supy='sudo python3'

#virtualenv
alias virtualnew='virtualenv -p python3 env'
alias virtualstart='source env/bin/activate'
alias virtualstop='deactivate'
alias virtualdelete='rm -rf ./env/'

#hub
alias hubinit='hub init && hub create'
alias hubadd='git add *'
alias hubcommit='git commit -m'
alias hubpush='git push origin master'

#VS code
alias vs='code .'
alias vsdir='code ..'

#againPy
alias again='python3 ~/Documents/againPy/again.py'

#zsh
alias rm='rm -r'
alias sudorm='sudo rm -rf'
alias mk='mkdir'

#pip
alias pip='sudo pip3'
alias freeze='pip3 freeze > requirements.txt'

#django
alias djangonew='django-admin startproject'
