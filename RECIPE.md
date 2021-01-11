### Steps to run the product
- On Ubuntu 20:
    PARAMS:
        `Ubuntu20`
        `nvidia-driver-460`
        `GTX-980 ti`
        `CUDA 10.1`
        `cudnn-10.1-7.6.5.32`
        `tensorflow-2.2.0`
    detect the gpu device - `$ ubuntu-drivers devices`
    install the recommended driver - `$ sudo apt install nvidia-driver-460`
    reboot - `$ sudo reboot`

    install toolkit - `$ sudo apt install nvidia-cuda-toolkit`
    check installation `$ nvcc -V`
    installation path - `$ whereis cuda`

    signup to Nvidia Developer Program
    download cudnn corresponds to cuda version, os
    unpack - `$ tar -xzvf cudnn-10.1-VERSION.tgz`
    copy the extracted files to CUDA installation path 
        - `$ sudo cp cuda/include/cudnn.h /usr/lib/cuda/include/`
        - `$ sudo cp cuda/lib64/libcudnn* /usr/lib/cuda/lib64/`
    set the permission - `$ sudo chmod a+r /usr/lib/cuda/include/cudnn.h /usr/lib/cuda/lib64/libcudnn*`

    export CUDA env vars
        - `$ echo 'export LD_LIBRARY_PATH=/usr/lib/cuda/lib64:$LD_LIBRARY_PATH >> ~/.bashrc`
        - `$ echo 'export LD_LIBRARY_PATH=/usr/lib/cuda:$LD_LIBRARY_PATH >> ~/.bashrc`
    load env vars - `$ source ~/.bashrc`

    create venv - `$ python3 -m venv env`
    install tensorflow - `pip install tensorflow==2.2.0`
    verify 
        - `>> import tensorflow as tf`
        - `>> tf.config.list_physical_devices("GPU")` - if unsuccessful, check tensorflow version, or driver, or cuda, or cudnn

    run `main.py` - `$ python main.py`

- On Windows10: