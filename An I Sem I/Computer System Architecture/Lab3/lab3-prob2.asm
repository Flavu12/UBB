bits 32 ; 
global start        


extern exit               
import exit msvcrt.dll    
                          
;12.(a-b-c)+(d-b-c)-(a-d)
;adunari si scaderi - interpretare cu semn
;a-byte, b-word, c-double word, d-quadword
segment data use32 class=data
     a db 20
     b dw 2
     c dd 3
     d dq 15
     x resq 1
segment code use32 class=code
    start:
        ; a-b
        mov al, [a] ; al=a
        cbw  ;ax=a
        sub al, [b]
        sbb ah, [b+1]; ax= a-b

        ;a-b-c
        cwde         ; EAX = a-b (conversie cu semn)
        sub eax, [c] ; EAX = a-b-c
        cdq          ; EDX:EAX = a-b-c (conversie cu semn)
        
        ;(a-b-c)+d
        add eax, [d] 
        adc edx, [d+4]
        mov [x], eax
        mov [x+4], edx
        
        ;(a-b-c)+d-b
        mov ax, [b]
        cwde      ;eax=b (conversie cu semn)
        cdq       ;edx:eax= b (conversie cu semn)
        sub [x],eax
        sbb [x+4], edx ;x=(a-b-c)+d-b
        
        ;(a-b-c)+(d-b-c)
        mov ax,[c] 
        mov dx, [c+2] ;dx:ax=c
        cdq         ;edx:eax=c (conversie cu semn)
        sub [x], eax
        sbb [x+4],edx  ;x=(a-b-c)+(d-b-c)
        
        ;a-d
        mov al, [a] ; al = a
        cbw         ;ax=a
        cwde        ; EAX = a (conversie cu semn)
        cdq         ;edx:eax=a
        sub eax, [d]
        sbb edx, [d+4]   ; edx:eax = a-d
        
        ;(a-b-c)+(d-b-c)-(a-d)
        sub [x],eax 
        sbb [x+4], edx   ;x=(a-b-c)+(d-b-c)-(a-d)
        ; exit(0)
        push    dword 0      
        call    [exit] 