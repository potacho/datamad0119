#programa para arrancar el pipeline
import subprocess

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description='EmailOptions')
    parser.add_argument('north', metavar='n', type=int, nargs='+',
                        help='send northern countries table')
    parser.add_argument(('south', metavar='s', type=int, nargs='+',
                        help='send southern countries table')
    parser.add_argument(('northsouth', metavar='c', type=int, nargs='+',
                        help='send graphic')

    args = parser.parse_args()
    print(args.accumulate(args.integers))

    def bash_command(cmd):
        subprocess.Popen(['/bin/bash', '-c', cmd])
        if...
    bash_command(mail -a /NorthVsSouth.png -s 'Pipelines Project' boyander@gmail.com < /dev/null)