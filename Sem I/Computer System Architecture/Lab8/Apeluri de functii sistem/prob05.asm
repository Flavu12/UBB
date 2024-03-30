bits 32      
extern exit               
import exit msvcrt.dll     

;Se dau doua numere naturale a si b (a, b: word, definite in segmentul de date). 
;Sa se calculeze a/b si sa se afiseze catul si restul impartirii in urmatorul format:
; "Cat = <cat>, rest = <rest>"
;Exemplu: pentru a=23 si b=10 se va afisa: "Cat = 2, rest = 3"
;Valorile vor fi afisate in format decimal (baza 10) cu semn.

segment data use32 class=data
	a dd 0
    b dd 0
    format_citire db "%d%d", 0
    format_afis db "Cat = %d , Rest = %d ", 0

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
       
       push dword edx
       push dword eax 
       push dword format_afis
       call [printf]
       add esp, 4*3



        ; exit(0)
        push dword 0      
        call [exit]  
