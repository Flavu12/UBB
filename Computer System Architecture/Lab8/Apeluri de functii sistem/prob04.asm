bits 32      
extern exit               
import exit msvcrt.dll     

;Se dau doua numere naturale a si b (a, b: word, definite in segmentul de date). 
;Sa se calculeze produsul lor si sa se afiseze in urmatorul format: "<a> * <b> = <result>"
;Valorile vor fi afisate in format decimal (baza 10) cu semn.


segment data use32 class=data
	a dd 0       
    	b dd 0
    	r dq 0  
	format  db "%d%d", 0  ; %d <=> un numar decimal (baza 10)
    	format_afis db "%d x %d = %lld",0
segment code use32 class=code
    start:                               
        ; vom apela scanf(format, a, b) => se va citi un numar in variabila a si unul in variabila b
        ; punem parametrii pe stiva de la dreapta la stanga
        push dword b       ; ! adresa lui b, nu valoarea
        push dword a
        push dword format
        call [scanf]       ; apelam functia scanf pentru citire
        add esp, 4 * 3     ; eliberam parametrii de pe stiva
                           ; 4 = dimensiunea unui dword; 3 = nr de parametri
        ;r = a*b
        mov eax, [a]
        imul dword[b]       ;dx:ax = a*b
       
        
        ;printf(mesaj, <a>*<b>=<r>)
        push dword edx 
        push dword eax
        push dword [b]
        push dword [a]
        push dword format_afis
        call [printf]
        add esp, 4*3


        ; exit(0)
        push dword 0      
        call [exit]  
