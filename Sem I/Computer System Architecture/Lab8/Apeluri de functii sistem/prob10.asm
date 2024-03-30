bits 32      
extern exit               
import exit msvcrt.dll     

;Sa se citeasca de la tastatura un numar in baza 10 
;si sa se afiseze valoarea acelui numar in baza 16.
;Exemplu: Se citeste: 28 se afiseaza: 1C

segment data use32 class=data
	a dd 0
   	 format_citire db "%d", 0
    	format_afis db "%x", 0
segment code use32 class=code
    start:
        push dword a
        push dword format_citire
        call [scanf]
        add esp, 4*2
                
        push dword[a]
        push dword format_afis
        call [printf]
        add esp, 4*2


        ; exit(0)
        push dword 0      
        call [exit]  
