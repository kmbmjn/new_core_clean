import pickle
import os
import time
from colorama import Fore, Back, Style

import torch
import psutil

import argparse
import pdb
# pip install gpustat

parser = argparse.ArgumentParser(description="resnet_teacher")
parser.add_argument('--id_list', nargs='+', help='<Required> Set flag', required=True)
args = parser.parse_args()


class command():
    def __init__(self, command_str, status, end_time, elapsed_time):
        self.command_str = command_str
        self.status = status
        self.end_time = end_time
        self.elapsed_time = elapsed_time


torch_version = torch.__version__
torch_cuda_version = torch.version.cuda
torch_cuda_available = torch.cuda.is_available()

while True:

    # terminal clear
    os.system("clear")

    print("[Status Monitoring]")
    print("* Torch version:", torch_version)
    print("* CUDA version:", torch_cuda_version)
    print("* Torch CUDA available:", torch_cuda_available)
    print("")

    print("* CPU usage:", psutil.cpu_percent())
    print("* Memory usage:", psutil.virtual_memory().percent)
    print("* Disk usage:", psutil.disk_usage("/").percent)
    print("")

    os.system("duf /home")
    print("")
    os.system("gpustat -c")
    print("")

    from rich.console import Console
    from rich.table import Table
    table = Table(title="Monitoring", show_lines=True)
    table.add_column("GPU ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Command", style="magenta")
    table.add_column("Status", justify="right", style="green")
    table.add_column("End Time", justify="right", style="green")
    table.add_column("Elapsed Time", justify="right", style="green")

    for gpu_id in args.id_list:
        ## print("#####################################")
        ## print("GPU ID: " + str(gpu_id))
        ## with open("log.pkl", "rb") as f:
        with open("log" + str(gpu_id) + ".pkl", "rb") as f:
            c_list = pickle.load(f)

        for i, c in enumerate(c_list):

            ## print(str(i + 1) + "/" + str(len(c_list)))
            ## print(c.command_str)

            if c.status == " Done ":
                ## print(c.end_time)
                ## print(c.elapsed_time)
                ## print(Fore.BLACK + Back.GREEN + c.status)
                ## print(Style.RESET_ALL)
                rich_status = "[green]Done[/]"

            if c.status == " Running ":
                ## print(Fore.BLACK + Back.YELLOW + " Running ")
                ## print(Style.RESET_ALL)
                rich_status = "[yellow]Running[/]"

            if c.status == " Waiting ":
                ## print(Fore.BLACK + Back.RED + " Waiting ")
                ## print(Style.RESET_ALL)
                rich_status = "[red]Waiting[/]"

            table.add_row(gpu_id, c.command_str, rich_status, c.end_time, c.elapsed_time)

    console = Console()
    console.print(table)


    time.sleep(2)

