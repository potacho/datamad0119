#programa para arrancar el pipeline
import subprocess

if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--north", help="send north data", action="store_true")
    args = parser.parse_args()
    if args.north:
        df_dec_north.to_html(open('north.html', 'w'))
        print("Se ha enviado un correo electrónico con los resultados para los países del norte de Europa")

    #def bash_command(cmd):
    #    subprocess.Popen(['/bin/bash', '-c', cmd])
    #    if...
    #bash_command(mail -a /NorthVsSouth.png -s 'Pipelines Project' boyander@gmail.com < /dev/null)