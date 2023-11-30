// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.


(START)
    @SCREEN
    D=A
    @addr
    M=D

    @ispressed
    M=0


(CHECKKEYBOARD)
    @KBD
    D=M
    @KEYISPRESSED
    D;JNE

    @ispressed
    M = 0
    @PRINTSCREEN
    0;JMP
    
(KEYISPRESSED)
    @ispressed
    M = -1

(PRINTSCREEN)
    @8191
    D=A
    @screenLength
    M=D

    @i
    M=0

(LOOP)
    @i
    D=M
    @screenLength
    D=D-M
    @END
    D;JGT

    @ispressed
    D=M
    @addr
    A=M
    M=D


    @i
    M=M+1
    @addr
    M=M+1
    @LOOP
    0;JMP

(END)
    @START // Return to the start of the program
    0;JMP  // Infinite loop

