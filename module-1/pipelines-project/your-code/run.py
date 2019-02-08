#programa para arrancar el pipeline
import subprocess

if __name__ == '__main__':


    def bash_command(cmd):
        subprocess.Popen(['/bin/bash', '-c', cmd])

bash_command(mail -a /NorthVsSouth.png -s "Pipelines Project" boyander@gmail.com < /dev/null)