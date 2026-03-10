import subprocess

running = {}

def start_bot(file):

    p = subprocess.Popen(["python", file])

    running[file] = p


def stop_bot(file):

    if file in running:
        running[file].terminate()


def restart_bot(file):

    stop_bot(file)
    start_bot(file)
