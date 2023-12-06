


class Parser:
    """
        Parses a single .asm file, and encapsulates access to the input code. 
        It reads an assembly language command, parses it, and provides convenient access to the command's components (fields and symbols). 
        In addition, it removes all white space and comments.
    """

    def __init__(self, file):
        """
            Opens the input file/stream and gets ready to parse it.
        """
        self.file = file
        self.current_command = None
        self.next_command = None
        self.commands = []
        
        
    def reset(self):
        """Resets the parser to the beginning of the input."""
        self.file.seek(0)
        self.current_command = None
        self.next_command = None
        
    def has_more_commands(self):
        """Are there more commands in the input?"""
        if self.next_command is None:
            self.next_command = self.file.readline()
        return self.next_command != ''

    def advance(self):
        """Reads the next command from the input and makes it the current command. Should be called only if has_more_commands() is true. Initially there is no current command."""
        self.current_command = self.next_command.split('//')[0].strip()
        self.next_command = None

    def command_type(self):
        """
        Returns the type of the current command: 
        A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number 
        C_COMMAND for dest=comp;jump 
        COMMENT for //comment
        L_COMMAND (actually, pseudo-command) for (Xxx) where Xxx is a symbol.
        """
        if self.current_command.startswith('@'):
            return 'A_COMMAND'
        elif self.current_command.startswith('('):
            return 'L_COMMAND'
        elif self.current_command.startswith('//') or self.current_command == '':
            return 'COMMENT'
        else:
            return 'C_COMMAND'

    def symbol(self):
        """Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx). Should be called only when command_type() is A_COMMAND or L_COMMAND."""
        if self.command_type() == 'A_COMMAND':
            return self.current_command[1:].strip()
        else:
            return self.current_command[1:-1].strip()

    def dest(self):
        """
        Returns the dest mnemonic in the current C-command (8 possibilities). Should be called only when command_type() is C_COMMAND.
        """
        if '=' in self.current_command:
            return self.current_command.split('=')[0].strip()
        else:
            return None

    def comp(self):
        """Returns the comp mnemonic in the current C-command (28 possibilities). Should be called only when command_type() is C_COMMAND."""
        if '=' in self.current_command:
            return self.current_command.split('=')[1].split(';')[0].strip()
        else:
            return self.current_command.split(';')[0].strip()
        
    def jump(self):
        """Returns the jump mnemonic in the current C-command (8 possibilities). Should be called only when command_type() is C_COMMAND."""
        if ';' in self.current_command:
            return self.current_command.split(';')[1].strip()
        else:
            return None
        
    