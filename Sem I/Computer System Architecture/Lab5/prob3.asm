bits 32      
extern exit               
import exit msvcrt.dll     

;3.	Se dau doua siruri de octeti S1 si S2. Sa se construiasca sirul D prin concatenarea
;elementelor din sirul S1 1uate de la stanga spre dreapta si a elementelor din sirul S2
;luate de la dreapta spre stanga.

;Exemplu: S1: 1, 2, 3, 4
;         S2: 5, 6, 7
;         D: 1, 2, 3, 4, 7, 6, 5

segment data use32 class=data
     s1 db 1,2,3,4
     len1 equ $-s1 
     s2 db 5,6,7
     len2 equ $-s2
     d times len1 db 0

segment code use32 class=code
     start:
        mov ecx, len1
        jecxz final
        mov esi, 0
        mov edi, 0
        repeta: 
            mov al, [s1+esi]
            mov [d+edi], al
            inc esi
            inc edi
        loop repeta
        
        mov ecx, len2
        jecxz final
        mov esi, len2-1
        repeta1:
            mov al, [s2+esi]
            mov [d+edi], al
            dec esi
            inc edi
        loop repeta1

        final: 


        ; exit(0)
        push    dword 0      
        call    [exit]       
