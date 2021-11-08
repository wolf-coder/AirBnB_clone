#!/usr/bin/python3
"""
framework for writing line-oriented command interpreters.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

Def_classes = {'BaseModel', 'User'}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    """
    DRY Problem:
    - Calling storage.all().keys() and splitting the keys,
    ... In order to operate on them is performance exhausting --"
    Improvement:
    - Get The Ids One time and not forget to updating them when
    ... crating a model
    """
    Ids = {Key.split('.', 1)[1] for Key in storage.all().keys()}

    def do_create(self, arg):
        """
        This method will:
        - Creates a new instance of `arg`
        - Saves it (to the JSON file) and prints the id. Ex:
        $ create BaseModel
        """
        if arg:
            if arg in Def_classes:
                my_model = eval(arg)()
                my_model.save()
                self.Ids.add(my_model.id)
                print(my_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        show: Prints the string representation of an instance based on
        ... the class name and id. Ex: $ show BaseModel 1234-1234-1234.
        """
        Arg_List = arg.split()
        if len(Arg_List) == 0:
            print("** class name missing **")
        elif Arg_List[0] not in Def_classes:
            print("** class doesn't exist **")
        elif len(Arg_List) == 1:
            print("** instance id missing **")
        elif Arg_List[1] not in self.Ids:
            print("** no instance found **")
        else:
            try:
                print(storage.all()['.'.join((Arg_List[0], Arg_List[1]))])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        ... (save the change into the JSON file).
        """
        Arg_List = arg.split()
        if len(Arg_List) == 0:
            print("** class name missing **")
        elif Arg_List[0] not in Def_classes:
            print("** class doesn't exist **")
        elif len(Arg_List) == 1:
            print("** instance id missing **")
        elif Arg_List[1] not in self.Ids:
            print("** no instance found **")
        else:
            try:
                del storage.all()['.'.join((Arg_List[0], Arg_List[1]))]
            except KeyError:
                print("** no instance found **")
            else:
                self.Ids.discard(Arg_List[1])
                storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        ...or not on the class name.
        Note : Note that the DRY rule is broken here , and it's a temporarely
        ... as more classes will be added further
        """
        if not arg:
            print([str(obj) for Key, obj in storage.all().items()])
        else:
            CLASS = arg.split()[0]
            if CLASS not in Def_classes:
                print("** class doesn't exist **")
            else:
                print([str(obj) for Key, obj in storage.all().items()])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        ... or updating attribute (save the change into the JSON file).
        Ex: $
        update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        Arg_List = arg.split()
        if len(Arg_List) == 0:
            print("** class name missing **")
        elif Arg_List[0] not in Def_classes:
            print("** class doesn't exist **")
        elif len(Arg_List) == 1:
            print("** instance id missing **")
        elif Arg_List[1] not in self.Ids:
            print("** no instance found **")
        elif len(Arg_List) == 2:
            print("** attribute name missing **")
        elif len(Arg_List) == 3:
            print("** value missing **")
        else:
            try:
                Obj = storage.all()['.'.join(Arg_List[:2])]
            except KeyError:
                print("** value missing **")
            else:
                setattr(Obj, Arg_List[2], Arg_List[3].strip('\'"'))
                storage.save()

    def emptyline(self):
        """
        Method called when an empty line is entered in response to the prompt.
        """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        print("line :{}".format(line))
        return True

    def do_EOF(self, line):
        """envoking EOF
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
