import pickle
import os
import time
import datetime
from pushbullet import Pushbullet
import getpass
import argparse
import pdb


parser = argparse.ArgumentParser(description="resnet_teacher")
parser.add_argument("--id", default=0, type=int)
args = parser.parse_args()


class command():
    def __init__(self, command_str, status, end_time, elapsed_time):
        self.command_str = command_str
        self.status = status
        self.end_time = end_time
        self.elapsed_time = elapsed_time



command_list = [
###

"python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --hp_ep 200 --hp_id 0",
"python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --hp_ep 200 --hp_id 1",


# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad gc --hp_th 1e+0 --hp_ep 200 --hp_id 0",

# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad g  --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad g  --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad g  --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 1e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 3e+0 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 1e+1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 3e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 1e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 3e+2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 1e+3 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 3e+3 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 1e+4 --hp_ep 200 --hp_id 5",

# "python ../s_core_code/train.py --model_name resnet18_f --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad g  --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18_f --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad g  --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18_f --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad g  --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18_f --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 1e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18_f --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 3e+0 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18_f --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 1e+1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18_f --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 3e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18_f --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 1e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18_f --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 3e+2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18_f --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 1e+3 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18_f --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 3e+3 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18_f --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_de 1e+4 --hp_ep 200 --hp_id 5",









# resnet18 wd 0 sgd
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 1",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 0",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+5 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+5 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+5 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+5 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+6 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+6 --hp_ep 200 --hp_id 1",

# resnet18 wd 0 adam
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 1",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 4",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-5 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-5 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-5 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 5",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 2",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+5 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+5 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+5 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+5 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+6 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+6 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+6 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+6 --hp_ep 200 --hp_id 3",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adam --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 1",


# resnet18 wd 0 rmsprop
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 1",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 4",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 5",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 5",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 5",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 3",














# adadelta
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e+1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e+1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e+1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-0 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-0 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-0 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 3",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 3",


# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 5",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+5 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+5 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 1e+5 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+5 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+5 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adadelta --hp_lr 1e-1 --grad sg --hp_wd 0. --hp_de 3e+5 --hp_ep 200 --hp_id 5",













# adagrad
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 4",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 4",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 5",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-4 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-4 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-4 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 5",


# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 0",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",









# adamax
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 0",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 0",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 1",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-5 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-5 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-5 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 1",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 2",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adamax --hp_lr 1e-4 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 3",













# sgd_ori
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-0 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-0 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-0 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 3",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 3",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 4",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt sgd_ori --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 5",



# nag
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-0 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-0 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-0 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 4",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-1 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 4",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 5",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 5",


# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-11 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-10 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-10 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-9 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-9 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-8 --hp_ep 200 --hp_id 5",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-8 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-7 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-7 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-6 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-6 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-5 --hp_ep 200 --hp_id 5",


# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 5",

# asgd
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-1 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-1 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-3 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-3 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt asgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 0",

# nadam
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-2 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-3 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-6 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-6 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-6 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nadam --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 1",

# radam
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-1 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-2 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-3 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-5 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-5 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-6 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e-5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e-5 --hp_ep 200 --hp_id 0",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 0",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt radam --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 1",

# # rprop
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-0 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-1 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-2 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-3 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad g --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 0",

# adagrad
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-2 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt adagrad --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+5 --hp_ep 200 --hp_id 0",

# rmsprop
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-0 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-0 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-0 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-1 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-1 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-1 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-2 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-2 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-2 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-3 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-3 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-3 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 0",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 0",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-6 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-6 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 0",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 0",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+5 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 1e+5 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+5 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt rmsprop --hp_lr 1e-5 --grad sg --hp_wd 0. --hp_de 3e+5 --hp_ep 200 --hp_id 1",


# nag
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-0 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-0 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-0 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-1 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-1 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-1 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-2 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-4 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-5 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-5 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-5 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-6 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-6 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-6 --grad g --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-5 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-4 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+4 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+5 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+5 --hp_ep 200 --hp_id 1",

# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+6 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+6 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+6 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+6 --hp_ep 200 --hp_id 0",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+7 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+7 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+7 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+7 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+8 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 1e+8 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet18 --mode train --data_name pet --hp_opt nag --hp_lr 1e-3 --grad sg --hp_wd 0. --hp_de 3e+8 --hp_ep 200 --hp_id 1",












# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad g  --hp_wd 0. --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 5",

# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e-1 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+0 --hp_ep 200 --hp_id 1",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+0 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+1 --hp_ep 200 --hp_id 2",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+1 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+2 --hp_ep 200 --hp_id 3",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+2 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+3 --hp_ep 200 --hp_id 4",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 3e+3 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 5",
# "python ../s_core_code/train.py --model_name resnet50 --mode train --data_name pet --hp_opt sgd --hp_lr 1e-2 --grad sg --hp_wd 0. --hp_de 1e+4 --hp_ep 200 --hp_id 5",





###
]

# add id
command_list = [elem for elem in command_list if ("hp_id " + str(args.id) in elem)]

# initially, generate command objects.
c_list = []
for command_elem in command_list:
    c_i = command(command_elem, " Waiting ", "", "")
    c_list.append(c_i)


# run commands.
for i, c_i in enumerate(c_list):
    # start of command
    print("")
    print("Command: {}/{}".format((i + 1), len(c_list)))
    print("start_time:", str(datetime.datetime.now()))
    print(c_i.command_str)
    print("")

    # logging
    c_i.status = " Running "
    ## with open("log.pkl", "wb") as f:
    with open("log" + str(args.id) + ".pkl", "wb") as f:
        pickle.dump(c_list, f)

    start_time = time.time()
    os.system(c_i.command_str)
    ##
    time.sleep(0.1)
    ##
    end_time = time.time()

    # end of command
    print("")
    print("end_time:", str(datetime.datetime.now()))

    hours, rem = divmod(end_time - start_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))

    # logging
    c_i.status = " Done "
    c_i.end_time = "End time: " + str(datetime.datetime.now())
    c_i.elapsed_time = "Elapsed time: {:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds)
    ## with open("log.pkl", "wb") as f:
    with open("log" + str(args.id) + ".pkl", "wb") as f:
        pickle.dump(c_list, f)

# push
api_key = "o.EePlquoGSmUa2ktvw92G7OjaVka3Uii3"  # new
# api_key = "o.LcPgEyU7O8z2bF0BAQ63pD7VFljwOFVY"
pb = Pushbullet(api_key)
user = getpass.getuser()
push_title = "[" + user + "] Execution ended. Last command was: " + command_list[-1]
push_body = str(datetime.datetime.now())
push = pb.push_note(push_title, push_body)
