bits 32      
extern exit               
import exit msvcrt.dll     

;Sa se citeasca de la tastatura doua numere (in baza 10) si sa se calculeze produsul lor.
;Rezultatul inmultirii se va salva in memorie in variabila "rezultat" (definita in
;segmentul de date).

segment data use32 class=data
	a dd 0       
   	b dd 0
	format  db "%d%d", 0  ; %d <=> un numar decimal (baza 10)
    	rezultat dq 0
segment code use32 class=code
    start: 
        ; vom apela scanf(format, a, b) => se va citi un numar in variabila a si unul in variabila b
        ; punem parametrii pe stiva de la dreapta la stanga
        push dword b       ; !punem pe stiva adresa lui b, nu valoarea
        push dword a       ; punem pe stiva adresa lui a
        push dword format  ;punem pe stiva formatul numerelor
        call [scanf]       ; apelam functia scanf pentru citire
        add esp, 4 * 3     ; eliberam parametrii de pe stiva
                           ; 4 = dimensiunea unui dword; 3 = nr de parametri
        ;a*b
        mov eax, [a]        
        imul dword[b]
       
        mov [rezultat], eax
        mov [rezultat+4], edx
        ; exit(0)
        push dword 0      
        call [exit] 
