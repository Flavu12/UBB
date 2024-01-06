bits 32      
extern exit               
import exit msvcrt.dll     

;Se dau doua numere natural a si b (a: dword, b: word, definite in segmentul de date). 
;Sa se calculeze a/b si sa se afiseze restul impartirii in urmatorul format: 
;"<a> mod <b> = <rest>"
;Exemplu: pentru a = 23 si b = 5 se va afisa: "23 mod 5 = 3"
;Valorile vor fi afisate in format decimal (baza 10) cu semn.

segment data use32 class=data
	a dd 0
    	b dd 0
    	format_citire db "%d%d", 0
    	format_afis db "%d mod %d = %d ", 0
segment code use32 class=code
    start:
        push dword b
        push dword a
        push dword format_citire
        call [scanf]
        add esp, 4*3
        
        mov eax, [a]
        mov edx, 0
        idiv dword[b]
        
        push edx
        push dword[b]
        push dword[a]
        push dword format_afis
        call [printf]
        add esp, 4*4

        ; exit(0)
        push dword 0      
        call [exit]  
