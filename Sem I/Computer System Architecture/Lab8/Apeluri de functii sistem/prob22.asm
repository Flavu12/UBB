bits 32      
extern exit               
import exit msvcrt.dll     

;Se citesc de la tastatura doua numere a si b. 
;Sa se calculeze valoarea expresiei (a+b)*k, k fiind o constanta definita 
;in segmentul de date. Afisati valoarea expresiei (in baza 10).
segment data use32 class=data
	a dd 0
    b dd 0
    k dd 2
    format_citire db "%d%d", 0
    format_afisare db "%d", 0
segment code use32 class=code
    start:
        push dword b
        push dword a
        push dword format_citire
        call [scanf]
        add esp, 4*3
        
        
        mov eax, [a]
        add eax, [b]
        mov edx, 0
        idiv dword[k]
        
        push dword eax
        push dword format_afisare
        call [printf]
        add esp, 4*2

        ; exit(0)
        push dword 0      
        call [exit]  
