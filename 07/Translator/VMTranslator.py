import sys

from CodeWriter import CodeWriter
from Parsar import Parser


def main():
    
    if len(sys.argv) != 2:
        print('Usage: python Main.py filepath')
        sys.exit(1)
    
    input_file = sys.argv[1]
    # output_file = input_file.split('.')[0] + '.asm'
    output_file = input_file[0: input_file.rfind('.')] + '.asm'
    print('Input file: {}'.format(input_file))
    print('Output file: {}'.format(output_file))
    
    
    with open(input_file, 'r') as f:
        with open(output_file, 'w') as of:
            parser = Parser(f)
            codeWriter = CodeWriter(of)
            
            while parser.has_more_commands():
                parser.advance()
                
                if parser.command_type() == 'C_ARITHMETIC':
                    # print(parser.command_type())
                    codeWriter.write_arithmetic(parser.current_command)
                    
                elif parser.command_type() == 'C_PUSH' or parser.command_type() == 'C_POP':
                    # print(parser.command_type())
                    codeWriter.write_push_pop(parser.command_type(), parser.arg1(), parser.arg2())
                    

if __name__ == '__main__':
    main()
    