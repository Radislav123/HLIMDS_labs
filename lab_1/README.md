# Установить OpenCV на Windows

`python -m pip install opencv-contrib-python`
Делал из cmd с правами администратора и активированным python-окружением (activate.bat).

1) открыть cmd с правами администратора (иначе библиотека не устанавливается)
2) `cd ...\hlimds_py_env\Scripts`                   # на ноутбуке это `cd D:\Quartus_labs\HLIMDS\hlimds_py_env\Scripts`
3) `d:`                                             # если меняется диск | перед ':' стоит литера диска
4) `activate.bat`
5) `python -m pip install opencv-contrib-python`    # просто "pip install..." выдает ошибку