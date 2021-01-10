### Steps to run the product
- On Ubuntu 20:
    detect the gpu device - `$ ubuntu-drivers devices`
    install the recommended driver - `$ sudo apt install nvidia-driver-440`
    reboot - `$ sudo reboot`

    install toolkit - `$ sudo apt install nvidia-cuda-toolkit`
    check installation `$ nvcc -V`
    installation path - `$ whereis cuda`

- On Windows10: