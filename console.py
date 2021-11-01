#!/usr/bin/python3
"""
framework for writing line-oriented command interpreters.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        """
        Method called when an empty line is entered in response to the prompt.
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """envoking EOF
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
