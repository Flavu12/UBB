bits 32      
extern exit               
import exit msvcrt.dll     

;Sa se citeasca de la tastatura doua numere a si b (in baza 16) si sa se calculeze a+b.
;Sa se afiseze rezultatul adunarii in baza 10.

segment data use32 class=data
	a dd 0
    	b dd 0
    	format_citire db "%X%X", 0
    	format_afisare db "%d", 0
segment code use32 class=code
    start:
      ;scanf
      push dword a
      push dword b 
      push dword format_citire
      call [scanf]
      add esp, 4*3
      
      ;a+b
      mov eax, [a]
      add eax, [b]
      
      ;printf 
      push eax 
      push format_afisare
      call [printf]
      add esp, 4*2

        ; exit(0)
        push dword 0      
        call [exit]  
