


class Code:
    """
    Translates Hack assembly language mnemonics into binary codes.
    """
    def __init__(self):
        self.dest_dict = {
            None: '000',
            'M': '001',
            'D': '010',
            'MD': '011',
            'A': '100',
            'AM': '101',
            'AD': '110',
            'AMD': '111',
        }
        self.jump_dict = {
            None: '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111',
        }
        self.comp_dict = {
            '0': '0101010',
            '1': '0111111',
            '-1': '0111010',
            'D': '0001100',
            'A': '0110000',
            '!D': '0001101',
            '!A': '0110001',
            '-D': '0001111',
            '-A': '0110011',
            'D+1': '0011111',
            'A+1': '0110111',
            'D-1': '0001110',
            'A-1': '0110010',
            'D+A': '0000010',
            'D-A': '0010011',
            'A-D': '0000111',
            'D&A': '0000000',
            'D|A': '0010101',
            'M': '1110000',
            '!M': '1110001',
            '-M': '1110011',
            'M+1': '1110111',
            'M-1': '1110010',
            'D+M': '1000010',
            'D-M': '1010011',
            'M-D': '1000111',
            'D&M': '1000000',
            'D|M': '1010101',
        }

    def dest(self, mnemonic):
        """
        Returns the binary code of the dest mnemonic.
        """
        return self.dest_dict[mnemonic]

    def comp(self, mnemonic):
        """
        Returns the binary code of the comp mnemonic.
        """
        return self.comp_dict[mnemonic]
    
    def jump(self, mnemonic):
        """
        Returns the binary code of the jump mnemonic.
        """
        return self.jump_dict[mnemonic]
    
    def to_binary(self, decimal):
        """
        Returns the binary code of the decimal number.
        """
        return bin(int(decimal))[2:].zfill(16)
    
    def to_decimal(self, binary):
        """
        Returns the decimal number of the binary code.
        """
        return int(binary, 2)
    
    def to_binary_15(self, decimal):
        """
        Returns the binary code of the decimal number.
        """
        return bin(int(decimal))[2:].zfill(15)
    
    def a_instruction(self, address):
        """
        Returns the binary code of the A-instruction.
        """
        return self.to_binary(address)
    
    def c_instruction(self, dest, comp, jump):
        """
        Returns the binary code of the C-instruction.
        """
        return '111' + self.comp(comp) + self.dest(dest) + self.jump(jump)
    
    