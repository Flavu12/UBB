bits 32      
extern exit               
import exit msvcrt.dll     

;Sa se citeasca de la tastatura doua numere a si b (in baza 10) şi 
;să se determine relaţia de ordine dintre ele (a < b, a = b sau a > b). 
;Afisati rezultatul în următorul format: "<a> < <b>, <a> = <b> sau <a> > <b>".
segment data use32 class=data
	a dd 0
    b dd 0
    format_citire db "%d %d", 0
    format_afisare1 db "%d < %d", 0
    format_afisare2 db "%d = %d ", 0
    format_afisare3 db "%d > %d", 0
segment code use32 class=code
    start:
     push dword b
     push dword a
     push dword format_citire
     call [scanf]
     add esp, 4*3 
          
     mov eax, [a]
     mov ebx, [b]
     
     cmp eax, ebx 
     jb mai_mic 
     
     cmp eax, ebx 
     ja mai_mare
     
     push dword[b]
     push dword[a]
     push dword format_afisare2
     call [printf]
     add esp, 4*3
     jmp final
     
     mai_mic:
     push dword[b]
     push dword[a]
     push dword format_afisare1
     call [printf]
     add esp, 4*3
     jmp final
     
     mai_mare:
     push dword[b]
     push dword[a]
     push dword format_afisare3
     call [printf]
     add esp, 4*3
     final:

        ; exit(0)
        push dword 0      
        call [exit]  
