// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// Infinite cicle starts here
(RESTART)
  @SCREEN    // get screen position
  D = A 
  @current
  M = D      // initialize index to first position of screen

// Checks for input
(CHECKKB)
  @KBD
  D = M
  @BLACK     // if greater than 0 it paints black
  D;JGT
  @WHITE     // if 0 it paints white
  D;JEQ
  @CHECKKB   // else it loops to itself
  0;JMP

// Sets the painting color to black
(BLACK)
  @color
  M = -1     // -1 = (1111111111111111), puts every bit to true
  @CHANGEPIXEL
  0;JMP

// Sets the painting color to white
(WHITE)
  @color
  M = 0
  @CHANGEPIXEL
  0;JMP

// Paints the pixel and changes the current pixel to the next one
(CHANGEPIXEL)
  @color
  D = M      // Store the painting color in D
  @current
  A = M      // Get direction of current pixel
  M = D      // Go the the direction of the current pixel and paint it
  @current
  D = M + 1  // Add 1 to the current pixel in order to check if there is a next pixel or not
  @KBD
  D = A - D  // Check if all the pixels have been visited (Last position of SCREEN is followed by first position of KBD)
  @current
  M = M + 1  // Actualy add 1 to the current pixel
  @CHANGEPIXEL
  D;JGT      // If KBD - current > 0 => it has not painted all the pixels yet, so it loops to itself until it paints every pixel
  @RESTART   
  0;JMP      // Else, it loops back around to the infinite cicle
