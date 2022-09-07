Why is `pyenv` useful?
----------------------

Because it allows you to have many Python versions (on a per-user basis or per-terminal basis) and change among them quickly with a simple command.

Install dependencies
--------------------
```bash
$ sudo apt install build-essential vim git wget curl python zlib1g-dev libbz2-dev libreadline-dev libssl-dev libsqlite3-dev libffi-dev liblzma-dev tk-dev ncurses-dev
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

FAQ
---

* After I install **pyenv** and select a particular version of Python with `$ pyenv global <version>`, where is my Python binary? If you followed this tutorial, then you installed **pyenv** in your home, i.e. `~/.pyenv` and your Python binary should be in `~/.pyenv/shims/python`. Run `$ which python` to check it.

* After I install **pyenv**, where do the packages that I install with pip go? As an example, for Python version `3.9.13`, you should find the packages that you install with `pip` in `~/.pyenv/versions/3.9.13/lib/python3.9/site-packages`.


Additional information
----------------------
* [pyenv](https://github.com/pyenv/pyenv)
* [pyenv-installer](https://github.com/pyenv/pyenv-installer)
