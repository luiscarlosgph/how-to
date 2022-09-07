Why is `pyenv` useful?
----------------------

Because it allows you to change the global Python version on a per-user basis (or per-terminal basis) with a simple command.

Install dependencies
--------------------
```bash
$ sudo apt install sudo build-essential vim git wget curl python zlib1g-dev libbz2-dev libreadline-dev libssl-dev libsqlite3-dev libffi-dev liblzma-dev tk-dev ncurses-dev
```

Install `pyenv` for your user
---------------------------
* Download:
```bash
$  git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

* Configure your terminal to use `pyenv`: add the following lines at the end of your `~/.bashrc` (if you use **bash**) or `~/.zshrc` (if you use **zsh**) 
```bash
export PYENV_ROOT="$HOME/.pyenv"                                                
export PATH="$PYENV_ROOT/bin:$PATH"                                             
eval "$(pyenv init --path)" 
```
For changes to take effect run `$ source ~/.bashrc` (if you use **bash**) or `$ source ~/.zshrc` (if you use **zsh**). Alternatively, you can close your terminal and open it again.

If you have no idea which terminal you use, run: `$ echo $SHELL`.

Usage
-----
* Get the list of Python versions installed in your system: `$ pyenv versions`
* Get the list of Python versions that you could possibly install: `$ pyenv install -l`
* Download and install a new version of Python: `$ pyenv install 3.9.13`
* Change Python version for your user: `$ pyenv global 3.9.13`
* Change Python version, **only** for your current terminal: `$ pyenv shell 3.9.13`
* Get the Python version that `pyenv` is currently using: `$ pyenv version`
* Uninstall one of the Python versions: `$ pyenv uninstall 3.9.13`

Additional information
----------------------
* [pyenv](https://github.com/pyenv/pyenv)
* [pyenv-installer](https://github.com/pyenv/pyenv-installer)
