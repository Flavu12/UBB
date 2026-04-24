bits 32 ; 
global start        


extern exit               
import exit msvcrt.dll    
                          
;12.(a*b+2)/(a+7-c)+d+x
;inmultiri si impartiri - interpretare cu semn
;a,c-byte, b-word, d-double word, x-quadword
segment data use32 class=data
     a db 20
     b dw 2
     c db 3
     d dd 15
     x dq 4
segment code use32 class=code
    start:
        ; a*b+2
        mov al, [a] ; al=a
        cbw         ;ax=a (conversie cu semn)
        imul word[b] ;DX:AX=a*b
        add ax, 2; dx:ax = a*b+2
        
        ;(a+7-c)
        mov bl, [a] 
        add bl, 7 ; al=a+7
        sub bl,[c] ;al= a+7-c 
        
        ;(a*b+2)/(a+7-c)
        idiv bx   ;ax=(a*b+2)/(a+7-c) si dx=rest
        
        ;(a*b+2)/(a+7-c)+d
        add ax, [d] 
        adc dx, [d+2] 
        
        ;(a*b+2)/(a+7-c) +d+x
        push dx
        push ax
        pop eax ; eax=dx:ax=(a*b+2)/(a+7-c) +d
        cdq     ; EDX:EAX = (a*b+2)/(a+7-c) +d (conversie cu semn)
        add eax, [x]
        adc edx, [x+4]  ; EDX:EAX = (a*b+2)/(a+7-c) +d+x
        ; exit(0)
        push    dword 0      
        call    [exit] 