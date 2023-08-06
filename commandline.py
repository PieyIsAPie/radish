import os
import platform
import cmd
import colorama

class command(cmd.Cmd):
    intro = f"{colorama.Fore.RED}Radish{colorama.Style.RESET_ALL} <v>, on Python {platform.python_version()}"
    file = None
    def do_list(self, arg):
        """List files and directories in the specified or current directory."""
        target_dir = os.path.join(os.getcwd(), arg) if arg else os.getcwd()
        if not os.path.exists(target_dir):
            print(f"Directory '{target_dir}' not found.")
            return

        items = os.listdir(target_dir)
        dirs = [item for item in items if os.path.isdir(os.path.join(target_dir, item))]
        files = [item for item in items if os.path.isfile(os.path.join(target_dir, item))]

        for item in dirs:
            print(f"{colorama.Fore.BLUE}{item}/{colorama.Style.RESET_ALL}")

        for item in files:
            print(item)

    def do_cd(self, arg):
        """Change the current working directory."""
        new_dir = os.path.abspath(arg)
        if os.path.exists(new_dir) and os.path.isdir(new_dir):
            os.chdir(new_dir)
            print(f"Current directory changed to {new_dir}")
        else:
            print(f"Invalid directory: {arg}")

    def do_rem(self, arg):
        os.remove(arg)
    def get_prompt(self):
        return f"{colorama.Fore.RED}Radish{colorama.Style.RESET_ALL} {os.getcwd()}> "

    def update_prompt(self):
        self.prompt = self.get_prompt()
    def preloop(self) -> None:
        self.update_prompt()
    def precmd(self, line: str) -> str:
        self.update_prompt()
        return super().precmd(line)
    def postcmd(self, stop, line):
        """Update the prompt after each command."""
        self.update_prompt()
        return stop
    def do_leave(self, arg):
        """Exit TickTK."""
        print("leaving")
        return True