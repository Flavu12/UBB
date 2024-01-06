bits 32      
extern exit               
import exit msvcrt.dll     

;Se da un numar natural a (a: dword, definit in segmentul de date). 
;Sa se citeasca un numar natural b si sa se calculeze: a + a/b. 
;Sa se afiseze rezultatul operatiei. 
;Valorile vor fi afisate in format decimal (baza 10) cu semn.

segment data use32 class=data
        a dd 12
    	b dd 0
    	format_citire db "%d", 0
    	format_afis db "%d", 0
segment code use32 class=code
    start:
        push dword b
        push dword format_citire
        call [scanf]
        add esp, 4*2
        
        mov eax, [a]
        mov edx, 0
        idiv dword[b]
        
        add eax, [a]
        
        push eax
        push dword format_afis
        call [printf]
        add esp, 4*2


        ; exit(0)
        push dword 0      
        call [exit]  
