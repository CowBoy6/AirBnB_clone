import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    def do_create(self, agrs):
        if not agrs :
            print("** class name missing **")
            print("** class doesn't exist **")


    def do_EOF(self):

        """Quit command to exit the program"""
        return True

    def do_quit(self):

        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
