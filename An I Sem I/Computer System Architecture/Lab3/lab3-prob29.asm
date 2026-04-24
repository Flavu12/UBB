bits 32 ; 
global start        


extern exit               
import exit msvcrt.dll    
                          
;d-[3*(a+b+2)-5*(c+2)]
;inmultiri si impartiri
;a, b, c-byte d-word
segment data use32 class=data
     a db 20
     b dw 2
     c dd 3
     d dq 15
     x resq 1
segment code use32 class=code
    start:
        ; a+b+2
        mov al, [a] ; al=a
        add al, [b] ; al=a+b
        add al, 2; al =a+b+2
        
        ;3*(a+b+2)
        mov bl, 3
        mul bl     ;ax=bl*al= 3*(a+b+2)
        mov cx, ax ;cx=3*(a+b+2)
        
        ;c+2
        mov al, 2  ;al=2
        add al,[c] ;al= c+2
        
        ;5*(c+2)
        mov bl, 5
        mul bl     ;ax=al*bl=5*(c+2)
        mov bx, ax ;bx=5*(c+2)
        
        ;3*(a+b+2)-5*(c+2)
        sub cx, bx ;cx=3*(a+b+2)-5*(c+2)
        
        ;d-[3*(a+b+2)-5*(c+2)]
        mov ax, d 
        sub ax, cx ;ax=d-[3*(a+b+2)-5*(c+2)]
        
        ; exit(0)
        push    dword 0      
        call    [exit] 