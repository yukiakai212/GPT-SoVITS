#!/bin/bash
conda install -c conda-forge gcc -y
conda install -c conda-forge gxx -y
conda install ffmpeg cmake -y
conda install pytorch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 pytorch-cuda=11.8 -c pytorch -c nvidia -y
pip install -r requirements.txt
#conda install conda-forge::gradio -y
#for python 3.10.4 kaggle env
#conda install pytorch-lightning==2.4.0 torchmetrics==1.5.2 -y
