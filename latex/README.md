Install Latex in Ubuntu
-----------------------

```
$ sudo apt update && sudo apt install -y texlive-full texstudio
```


Convert a hierarchy of latex files into a single latex file
-----------------------------------------------------------

**User case**: you have a project where you have a main latex file, e.g. the typical `root.tex` or `main.tex` where you use `\input{sections/introduction}` because you have a folder called `sections` where you store the tex files for each section of the manuscript (e.g. `introduction.tex` for the previous example). However, when you want to submit your paper to [Arxiv](https://arxiv.org/) or the publisher, the upload system expects all the latex in a single `.tex` file, and all the figures in the root directory of the project. 

The commands below will help you to convert all the tex files into a single file:

```bash
$ sudo apt update
$ sudo apt install perl
$ cd <project_folder>
$ wget 
```
