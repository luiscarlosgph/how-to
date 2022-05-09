Flash
-----

![photo1](https://user-images.githubusercontent.com/3996630/167399938-5545671e-5336-4ad1-a789-3491d13597d4.png)

![photo2](https://user-images.githubusercontent.com/3996630/167399950-2782c21c-b1c9-4544-be77-ba222e4b8c35.png)

![photo3](https://user-images.githubusercontent.com/3996630/167399961-28a2241d-e91b-444b-8752-a5aacc2c4b93.png)

![photo4](https://user-images.githubusercontent.com/3996630/167399979-14e309a7-32cd-4d35-9374-94b38e505fa1.png)

![photo5](https://user-images.githubusercontent.com/3996630/167399997-fee1b3a4-11d7-42df-976f-78b6da45e1b5.png)

![photo6](https://user-images.githubusercontent.com/3996630/167400014-990df518-f514-4664-b34f-4e4026084d86.png)


Install Ubuntu 20.04
--------------------

1. Install the Ubuntu 18.04 with Jetpack kernel using the NVIDIA Clara SDK.

1. Basic setup to avoid some problems when upgrading to 20.04:
```
$ sudo apt remove chromium-browser
$ sudo apt remove unity
$ sudo apt autoremove
$ sudo apt autoclean
```

3. Install discrete graphics (this script comes with the Ubuntu 18.04 that you install with the SDK):
```
sudo nvgpuswitch.py install dGPU
```
