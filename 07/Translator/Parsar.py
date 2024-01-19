class Parser:
    """
    
    
    """
    
    def __init__(self, file):
        """
            Opens the input file/stream and gets ready to parse it.
        """
        self.file = file
        self.current_command = None
        self.next_command = None
        
    
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
        C_ARITHMETIC for all the arithmetic commands.
        C_PUSH for push commands.
        C_POP for pop commands.
        C_LABEL for label commands.
        C_GOTO for goto commands.
        C_IF for if-goto commands.
        C_FUNCTION for function commands.
        C_RETURN for return commands.
        C_CALL for call commands.
        C_COMMENT for comments.
        """
        
        if self.current_command in ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']:
            return 'C_ARITHMETIC'
        elif self.current_command.startswith('push'):
            return 'C_PUSH'
        elif self.current_command.startswith('pop'):
            return 'C_POP'
        elif self.current_command.startswith('label'):
            return 'C_LABEL'
        elif self.current_command.startswith('goto'):
            return 'C_GOTO'
        elif self.current_command.startswith('if-goto'):
            return 'C_IF'
        elif self.current_command.startswith('Function'):
            return 'C_FUNCTION'
        elif self.current_command.startswith('return'):
            return 'C_RETURN'
        elif self.current_command.startswith('Call'):
            return 'C_CALL'
        elif self.current_command.startswith('//') or self.current_command == '':
            return 'C_COMMENT'
        else:
            raise ValueError('unknown command: {}'.format(self.current_command))
        
        
    def arg1(self):
        """
        Returns the first argument of the current command. In the case of C_ARITHMETIC, the command itself (add, sub, etc.) is returned. Should not be called if the current command is C_RETURN.
        """
        if self.command_type() == 'C_ARITHMETIC':
            return self.current_command
        else:
            return self.current_command.split(' ')[1]
        
    def arg2(self):
        """
        Returns the second argument of the current command. Should be called only if the current command is C_PUSH, C_POP, C_FUNCTION, or C_CALL.
        """
        
        if self.command_type() in ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL']:
            return self.current_command.split(' ')[2]
        
        return None
        
        