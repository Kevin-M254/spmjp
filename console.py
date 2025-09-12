#!/usr/bin/python3
""" Module for the entry point of command interpreter """
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.country import Country
from models.league import League
from models.match import Match
from models.prediction import Prediction
import cmd
import re


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class SPMJPCommand(cmd.Cmd):
    """ Class for the command interpreter """

    prompt = "(spmjp) "
    __classes = {"BaseModel",
                 "User",
                 "Country",
                 "League",
                 "Match",
                 "Prediction"}

    def default(self, arg):
        """ Default behaviour for cmd module when input is invalid """
        arg_dict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg):
        """ Creates a new class instance with given keys/values
            and prints its id.
            Usage:
                create <class> <key 1>=<value 1> <key 2>=<value 2...
        """
        #argl = parse(arg)
        try:
            if not arg:
                raise SyntaxError()
            my_list = arg.split(" ")

            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = tuple(my_list[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Display string representation of a class instance
            Usage:
                show <class> <id> or <class>.show(<id>)
        """
        argl = parse(arg)
        obj_dict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in SPMJPCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """ Deletes a class instance of a given id
            Usage:
                destroy <class> <id> or <class>.destroy(<id>)
        """
        argl = parse(arg)
        obj_dict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in SPMJPCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """ Display string representations of all instances of a given class
            Usage:
                all or all <class> or <class>.all()
        """
        argl = parse(arg)
        if not argl:
            o = storage.all()
            print([o[k].__str__() for k in o])
            return
        try:
            if argl[0] not in self.__classes:
                raise NameError()

            o = storage.all(eval(argl[0]))
            print([o[k].__str__() for k in o])
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates a class instance of a given id by adding
            or updating a given attribute key/value pair or dictionary
                Usage:
                    <class>.update(<id>, <attribute_name>, attribute_value) or
                    <class>.update(<id>, <dictionary>)
        """
        argl = parse(arg)
        obj_dict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in SPMJPCommand.__classes:
            print("** class doen't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = obj_dict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = obj_dict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                    type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


    def do_EOF(self, line):
        """ Handles end of file character """
        print()
        return True

    def do_quit(self, line):
        """ Exits the program """
        return True

    def emptyline(self):
        """ Passes empty line """
        pass


if __name__ == '__main__':
    SPMJPCommand().cmdloop()
