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
        mov ecx, len-1 ;mutam in ecx lungimea sirului s- 1
        jecxz final
        mov esi, 0    ;index pt sirul s
        mov edi, 0    ;index pentru sirul d
    repeta:
        mov al, [s+esi] ;al<-s[i]
        inc esi         ;i++
        mov bl, [s+esi] ;bl<-s[i+1]
        mul bl          ;ax<-al*bl
        mov [d+edi], al ;d[j]<-al
        inc edi         ;j++
    loop repeta
   final:

        ; exit(0)
        push    dword 0      
        call    [exit]       
