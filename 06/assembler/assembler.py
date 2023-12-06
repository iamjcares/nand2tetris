from code import Code

from parseer import Parser
from symbol_table import SymbolTable


class HackAssembler:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.symbol_table = SymbolTable()
        self.parser = Parser(input_file)
        self.code = Code()
        self.line_number = 0
        self.rom_address = 0
        self.ram_address = 16

    def assemble(self):
        self.first_pass()
        self.second_pass()

    def first_pass(self):
        while self.parser.has_more_commands():
            self.parser.advance()
            if self.parser.command_type() == "COMMENT":
                continue
            elif self.parser.command_type() == "L_COMMAND":
                self.symbol_table.add_entry(self.parser.symbol(), self.rom_address)
            else:
                self.rom_address += 1

    def second_pass(self):
        self.parser.reset()
        with open(self.output_file, "w") as f:
            while self.parser.has_more_commands():
                self.parser.advance()
                if self.parser.command_type() == "A_COMMAND":
                    symbol = self.parser.symbol()
                    if symbol.isdigit():
                        address = int(symbol)
                    else:
                        if not self.symbol_table.contains(symbol):
                            self.symbol_table.add_entry(symbol, self.ram_address)
                            self.ram_address += 1
                        address = self.symbol_table.get_address(symbol)
                    f.write(self.code.a_instruction(address) + "\n")
                elif self.parser.command_type() == "C_COMMAND":
                    dest = self.parser.dest()
                    comp = self.parser.comp()
                    jump = self.parser.jump()
                    f.write(self.code.c_instruction(dest, comp, jump) + "\n")
                    
                    

if __name__ == "__main__":
    import sys
    input_file = sys.argv[1]
    output_file = input_file.replace(".asm", ".hack")
    input_file = open(input_file, "r")
    assembler = HackAssembler(input_file, output_file)
    assembler.assemble()
    input_file.close()