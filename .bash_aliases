# custom aliases

# User specific aliases and functions
alias dback='python3 /home/curtis/Scripts/DiamondBack/DiamondBack.py'
# run cd and clear together
alias cdclear='cd && clear'
# sync .files for git
#alias gitSync='python3 ~/Scripts/gitSync/gitSync.py'
# make quickbackup of file
#alias bakupFile='/home/curtis/Scripts/bakupFile.sh'

alias ls="ls -atl --color=auto"
alias dir="dir --color=auto"
alias grep="grep --color=auto"
alias dmesg="dmesg --color"

alias filebackup="/home/curtis/Scripts/filebackup"

# because speedtest needs to be secure or it fails
alias speedtest-cli="speedtest-cli --secure"

# make a directory and then cd into it
mkcd(){
	mkdir $1 && cd $_
}
