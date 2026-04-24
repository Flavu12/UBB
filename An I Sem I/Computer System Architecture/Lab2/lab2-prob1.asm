bits 32 ; 
global start        


extern exit               
import exit msvcrt.dll    
                          
;5-6
segment data use32 class=data
     a db 5
     b db 6
     x resb 1
segment code use32 class=code
    start:
        ; a-b
        mov al, [a] ;al=a
        sub al, [b] ; al=a-b
        ;stocare in variabila x
         mov [x], al ; x=a-b
    
        ; exit(0)
        push    dword 0      
        call    [exit] 