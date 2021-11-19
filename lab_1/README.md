# Установить OpenCV
## На Windows
1) открыть cmd с правами администратора (иначе библиотека не устанавливается)
2) `cd ...\hlimds_py_env\Scripts`  
	2.1 на ноутбуке это `cd D:\Quartus_labs\HLIMDS\hlimds_py_env\Scripts`
3) `d:`  
    3.1 если меняется диск  
	3.2 перед ':' стоит литера диска
4) `activate.bat`
5) `python -m pip install opencv-contrib-python`  
	5.1 просто "pip install..." выдает ошибку

## На Raspberry Pi
1) следовать [*OpenCV_start_guide*](https://docs.google.com/document/d/11pA2lgObwpOZl51K4_CmMOTmWCd2NKq7ogmkU3c9kXg/edit)
до момента установки OpenCV
2) установить OpenCV согласно [*комментарию*](https://raspberrypi.stackexchange.com/questions/101672/pre-built-opencv-on-raspbian-buster/101688#101688)
3) продолжить следовать гайду после с момента после установки OpenCV


# Установить PyTorch
[*Сайт*](https://pytorch.org/) PyTorch.

## На Windows
1) `pip install torch torchvision torchaudio`  
   	1.1 для ПК
	1.2 на ПК у меня AMD видеокарты, поэтому CUDA нельзя использовать, поэтому используется CPU
2) `pip3 install torch==1.10.0+cu113 torchvision==0.11.1+cu113 torchaudio===0.10.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html`
	2.1 для ноутбука
   	2.2 на ноутбуке GeForce

## На Raspberry Pi
1) `pip3 install torch==1.10.0+cpu torchvision==0.11.1+cpu torchaudio==0.10.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html`
	1.1 сочли лучшим вариант на процессоре, так как планируется только запускать модели (не тренировать)
