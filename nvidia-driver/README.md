Description
-----------

This guide explains you how to install any version of the NVIDIA driver without using the repositories of your Linux distribution. 

* Why not using the repositories? There are many ocassions when you need a specific version of the NVIDIA driver (e.g. CUDA support, bugs), and there is a limited offer of NVIDIA driver versions in the repos.

Install
-------

1. Find out which graphics card you have:
  ```
  $ lspci | grep VGA
  01:00.0 VGA compatible controller: NVIDIA Corporation GP102 [TITAN X] (rev a1)
  ```

2. Go to the NVIDIA website [here](https://www.nvidia.com/Download/Find.aspx) and search for your model:
 ![nvidia_search](https://user-images.githubusercontent.com/3996630/189359318-debc0b8a-7060-4c7d-a8b5-978ee308a218.png)
