#programa para arrancar el pipeline
if __name__ == '__main__':

import subprocess

def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])
