Install Latex in Ubuntu
-----------------------

```
$ sudo apt update && sudo apt install -y texlive-full texstudio
```
Then you can run the LaTeX IDE simply running `$ texstudio` on a terminal.



Convert a hierarchy of latex files into a single latex file
-----------------------------------------------------------

**User case**: you have a project where you have a main latex file, e.g. the typical `root.tex` or `main.tex` where you use `\input{sections/introduction}` because you have a folder called `sections` where you store the tex files for each section of the manuscript (e.g. `introduction.tex` for the previous example). However, when you want to submit your paper to [Arxiv](https://arxiv.org/) or the publisher, the upload system expects a single `.tex` file.

The commands below will help you to generate a single `.tex` file:

```bash
$ sudo apt update
$ sudo apt install perl
$ cd <project_folder>
$ wget https://raw.githubusercontent.com/luiscarlosgph/how-to/main/latex/latexpand.pl
$ perl latexpand.pl main.tex > all_in_one.tex
```
