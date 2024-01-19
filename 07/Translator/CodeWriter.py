

class CodeWriter:
    def __init__(self, output_file):
        self.output_file = output_file
        self.label_count = 0
        # self.function_name = ""
        # self.return_count = 0
        # self.call_count = 0

    # def set_file_name(self, file_name):
    #     self.output_file = file_name

    def write_arithmetic(self, command):
        if command == "add":
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n") # A = SP - 1
            self.output_file.write("D=M\n") # D = *SP
            self.output_file.write("A=A-1\n") # A = SP - 2, writes to *SP
            self.output_file.write("M=D+M\n") # Writes to *SP, But next SP will be the same (the first pop)
        elif command == "sub":
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            self.output_file.write("A=A-1\n")
            self.output_file.write("M=M-D\n")
        elif command == "neg":
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=-M\n")
        elif command == "eq":
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            self.output_file.write("A=A-1\n")
            self.output_file.write("D=M-D\n")
            self.output_file.write("@EQUAL" + str(self.label_count) + "\n")
            self.output_file.write("D;JEQ\n")
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=0\n")
            self.output_file.write("@END" + str(self.label_count) + "\n")
            self.output_file.write("0;JMP\n")
            self.output_file.write("(EQUAL" + str(self.label_count) + ")\n")
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=-1\n")
            self.output_file.write("(END" + str(self.label_count) + ")\n")
            self.label_count += 1
        elif command == "gt":
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            self.output_file.write("A=A-1\n")
            self.output_file.write("D=M-D\n")
            self.output_file.write("@GREATER" + str(self.label_count) + "\n")
            self.output_file.write("D;JGT\n")
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=0\n")
            self.output_file.write("@END" + str(self.label_count) + "\n")
            self.output_file.write("0;JMP\n")
            self.output_file.write("(GREATER" + str(self.label_count) + ")\n")
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=-1\n")
            self.output_file.write("(END" + str(self.label_count) + ")\n")
            self.label_count += 1
        elif command == "lt":
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            self.output_file.write("A=A-1\n")
            self.output_file.write("D=M-D\n")
            self.output_file.write("@LESS" + str(self.label_count) + "\n")
            self.output_file.write("D;JLT\n")
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=0\n")
            self.output_file.write("@END" + str(self.label_count) + "\n")
            self.output_file.write("0;JMP\n")
            self.output_file.write("(LESS" + str(self.label_count) + ")\n")
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=-1\n")
            self.output_file.write("(END" + str(self.label_count) + ")\n")
            self.label_count += 1
        elif command == "and":
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            self.output_file.write("A=A-1\n")
            self.output_file.write("M=D&M\n")
        elif command == "or":
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            self.output_file.write("A=A-1\n")
            self.output_file.write("M=D|M\n")
        elif command == "not":
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=!M\n")
        else:
            raise ValueError("unknown command: {}".format(command))
        
    def write_push_pop(self, command, segment, index):
        if command == "C_PUSH":
            if segment == "constant":
                self.output_file.write("@" + str(index) + "\n")
                self.output_file.write("D=A\n")
                # to be added back here
            elif segment == "static":
                self.output_file.write("@Static." + str(index) + "\n")
                self.output_file.write("D=M\n")
                # to be added back here
                    
            else:
                if segment == "local":
                    self.output_file.write("@LCL\n")
                elif segment == "argument":
                    self.output_file.write("@ARG\n")
                elif segment == "this":
                    self.output_file.write("@THIS\n")
                elif segment == "that":
                    self.output_file.write("@THAT\n")
                elif segment == "pointer":
                    self.output_file.write("@3\n")
                elif segment == "temp":
                    self.output_file.write("@5\n")
                else:
                    raise ValueError("unknown segment: {}".format(segment))
                
                if segment in ["local", "argument", "this", "that"]:
                    self.output_file.write("D=M\n")
                else:
                    self.output_file.write("D=A\n")
                    
                self.output_file.write("@" + str(index) + "\n")
                self.output_file.write("A=D+A\n")
                self.output_file.write("D=M\n")
                # to be added back here
                
            self.output_file.write("@SP\n")
            self.output_file.write("A=M\n")
            self.output_file.write("M=D\n")
            self.output_file.write("@SP\n")
            self.output_file.write("M=M+1\n")
                
        elif command == "C_POP":
            if segment == "static":
                self.output_file.write("@SP\n")
                self.output_file.write("AM=M-1\n")
                self.output_file.write("D=M\n")
                self.output_file.write("@Static." + str(index) + "\n")
                self.output_file.write("M=D\n")
                return # no further action needed
            
            if segment == "local":
                self.output_file.write("@LCL\n")
            elif segment == "argument":
                self.output_file.write("@ARG\n")
            elif segment == "this":
                self.output_file.write("@THIS\n")
            elif segment == "that":
                self.output_file.write("@THAT\n")
            elif segment == "pointer":
                self.output_file.write("@3\n")
            elif segment == "temp":
                self.output_file.write("@5\n")
            else:
                raise ValueError("unknown segment: {}".format(segment))
            
            if segment in ["local", "argument", "this", "that"]:
                    self.output_file.write("D=M\n")
            else:
                    self.output_file.write("D=A\n")
            
            self.output_file.write("@" + str(index) + "\n")
            self.output_file.write("D=D+A\n")
            self.output_file.write("@R13\n")
            self.output_file.write("M=D\n")

            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            self.output_file.write("@R13\n")
            self.output_file.write("A=M\n")
            self.output_file.write("M=D\n")
 
        else:
            raise ValueError("unknown command: {}".format(command))
        
    def close(self):
        self.output_file.close()
        