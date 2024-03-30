bits 32      
extern exit               
import exit msvcrt.dll     

;Sa se citeasca de la tastatura doua numere a si b (in baza 10) si sa se calculeze a/b.
;Catul impartirii se va salva in memorie in variabila "rezultat" (definita in segmentul de
;date). Valorile se considera cu semn.

segment data use32 class=data
	a dd 0       
    b dd 0
	format  db "%d%d", 0  ; %d <=> un numar decimal (baza 10)
    rezultat dw 0

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
        mov ax, [a]  
        mov dx, [a+2]
        idiv word[b]
       
        mov [rezultat], ax
        ; exit(0)
        push dword 0      
        call [exit]  
