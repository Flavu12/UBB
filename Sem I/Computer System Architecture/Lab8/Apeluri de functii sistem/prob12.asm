bits 32      
extern exit               
import exit msvcrt.dll     

;Se da un numar natural negativ a (a: dword). 
;Sa se afiseze valoarea lui in baza 10 si in baza 16, in urmatorul format: 
;"a = <base_10> (baza 10), a = <base_16> (baza 16)"

segment data use32 class=data
	a dd 0
    	format_citire db "%d", 0
    	format_afis db "a=%d (baza 10), a=%x (baza 16)", 0

segment code use32 class=code
    start:
        push dword a
        push dword format_citire
        call [scanf]
        add esp, 4*2
                
        push dword[a]
        push dword[a]
        push dword format_afis
        call [printf]
        add esp, 4*2


        ; exit(0)
        push dword 0      
        call [exit]  
