bits 32 ; 
global start        


extern exit               
import exit msvcrt.dll    
;–a*a + 2*(b-1) – d                      
;a,b,c-byte, d-word
segment data use32 class=data
     a db 2
     b db 4
     c db 7
     d dw 1
segment code use32 class=code
    start:
        ; a*a
        mov al, [a] ;al=a
        mul al   ; ax=al*al=a*a
        
        ;-a*a
        neg ax ; ax=-ax=-a*a
        mov bx,ax ;bx=ax=-a*a
        
        ;2*(b-1)
        mov ah,2 ; ah=2
        mov al, [b] ;al=b
        sub al, 1 ;al=b-1
        mul ah ;ax=al*ah=2*(b-1)
        
        
        ;–a*a + 2*(b-1)
        add bx, ax ; bx=–a*a + 2*(b-1)
        mov ax, bx
        
        ;–a*a + 2*(b-1)-d
        sub ax, [d]  ;ax=–a*a + 2*(b-1)-d
    
        ; exit(0)
        push    dword 0      
        call    [exit]  