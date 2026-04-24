bits 32 ; 
global start        


extern exit               
import exit msvcrt.dll    
;(a-b)+(c-b-d)+d                        
;a,b,c,d words
segment data use32 class=data
     a dw 9
     b dw 2
     c dw 7
     d dw 5
     x resb 2
segment code use32 class=code
    start:
        ; a-b
        mov al, [a] ;al=a
        sub al, [b] ; al=a-b
        
        ;(a-b)+(c-b-d)
        add al, [c]  ;al=(a-b)+c
        sub al, [b]  ;al=(a-b)+c-b
        sub al, [d]  ;al=(a-b)+c-b-d
        ;(a-b)+(c-b-d)+d
        add al, [d] ; al=(a-b)+(c-b-d)+d
        
        ;stocare in variabila x
         mov [x], al ; x=al=(a-b)+(c-b-d)+d
    
        ; exit(0)
        push    dword 0      
        call    [exit]