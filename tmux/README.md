Install
-------

```
$ sudo apt update
$ sudo apt install tmux
```

Configure terminal to run tmux every time
-----------------------------------------

Add to `~/.zshrc` (if you use **zsh**) or `~/.bashrc` (if you use **bash**):

```bash
plugins=(tmux git)

if [[ -z "$TMUX" ]]; then
   ID="`tmux ls | grep -vm1 attached | cut -d: -f1`" # get the id of a deattached session
   if [[ -z "$ID" ]]; then # if not available create a new one
      tmux new-session
   else
      tmux attach-session -t "$ID" # if available attach to it
   fi
fi
```
