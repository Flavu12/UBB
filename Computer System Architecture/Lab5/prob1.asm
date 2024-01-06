bits 32      
extern exit               
import exit msvcrt.dll     

;1.Se da un sir de octeti S de lungime l. Sa se construiasca sirul D de lungime l-1 astfel 
;incat elementele din D sa reprezinte produsul dintre fiecare 2 elemente consecutive S(i) si 
;S(i+1) din S.
segment data use32 class=data
   s db 1, 2, 3, 4, 5, 6
   len equ $-s
   d times len db 0

segment code use32 class=code
    start:
        mov ecx, len-1
        jecxz final
        mov esi, 0
        mov edi, 0
    repeta:
        mov al, [s+esi]
        inc esi 
        mov bl, [s+esi]
        mul bl
        mov [d+edi], al
        inc edi
    loop repeta
   final:

        ; exit(0)
        push    dword 0      
        call    [exit]       
