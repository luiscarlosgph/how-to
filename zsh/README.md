Install zsh and make it the default user terminal
-------------------------------------------------

```
$ sudo apt install zsh wget
$ chsh -s $(which zsh)
$ sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```
