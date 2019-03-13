@i
M=0 // inicio contador de i en 0 (para saber cuantas teclas undi)
@iter
M=0  // creo un iterador para recorrer las teclas
@SCREEN
D=A // guardo la referencia a screen en d
@printiter
M=D // creo un iterador para imporimir en pantalla

(KBLOOP)
  @KBD
  D=M // guardo la tecla en d
  @i // le sumo 1 a i
  M=M+1
  A=M // cargo en a la direccion de memoria a la que me deberia referir (valor de i)
  M=D // en la posicion de memoria correspondiente guardo la tecla undida
  @128
  D=D-A // rest 128 y el valor de la tecla
  @PRINTXOR
  D;JEQ // si el valor de la tecla es 128, salto fuera del loop de entrada de teclado
  @LOOP // sino entonces salto me quedo en el loop de teclado
  0;JMP

(PRINTXOR)
  @iter 
  A=M // cargo valor actual de iter
  D=M // cargo la tecla correspodiente en d
  @170
  D=DxA // hago xor entre la tecla y el número 170 (encripto con 170)
  @printiter
  A=M // miro en que posicion imprimir (cojo el valor del puntero)
  M=D // imprimo en pantalla el binario correspondiente a la tecla undida ya encriptada
  D=A+1 // le sumo 1 a la posicion de memoria en la que quiero imprimir
  @printiter
  M=D // actualizo la posicion de memoria para imprimir
  // si no ha terminado
  @iter
  A=M // cargo valor actual de iter
  D=A+1 // le sumo 1 a la referencia de iterador
  @iter
  M=D // actualizo el valor de iter
  // verificar si ya terminó
  @i
  D=M
  @iter
  A=M
  D=D-A
  @END
  D;JEQ // si el valor de i e iter es el mismo, significa que terminé de recorrer todas las teclas (TERMINA)
  @PRINTXOR
  0;JMP // si no ha terminado, siga buscando teclas en memoria y aplicando el xor para luego imprimir

(END)
  @END
  0;JMP


