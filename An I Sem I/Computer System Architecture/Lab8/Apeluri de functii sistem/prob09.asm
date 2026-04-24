bits 32      
extern exit               
import exit msvcrt.dll     

;Sa se citeasca de la tastatura doua numere a si b (in baza 10) si sa se calculeze:
;(a+b) / (a-b). Catul impartirii se va salva in memorie in variabila "rezultat"
;(definita in segmentul de date). Valorile se considera cu semn.

segment data use32 class=data
	a dd 0
    	b dd 0
    	rezultat dd 0
    	format_citire db "%d%d", 0
segment code use32 class=code
    start:
        push dword b
        push dword a
        push dword format_citire
        call [scanf]
        add esp, 4*3
        
        mov eax, [a]
        add eax, [b]
        
        mov ebx, [a]
        sub ebx, [b]
        
        mov edx, 0 
        idiv ebx 
        mov [rezultat], eax

        ; exit(0)
        push dword 0      
        call [exit]  
