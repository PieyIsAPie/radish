from commandline import command
import sys
import colorama

colorama.init()

def main():
    # Reserve for locking code
    cmd = command(stdin=sys.stdin, stdout=sys.stdout)
    cmd.cmdloop()

if __name__ == "__main__":
    main()