bits 32 ; 
global start        


extern exit               
import exit msvcrt.dll    
                          
;12.(a+b+d)-(a-c+d)+(b-c)
;interpretare fara semn
;a-byte b-word c-double word d-quadword
segment data use32 class=data
     a db 20
     b dw 2
     c dd 3
     d dq 15
     x resq 1
segment code use32 class=code
    start:
        ; a+b
        mov al, [a] ; al=a
        mov ah, 0 ; conversie fara semn de la al la ax
        add al, [b]
        adc ah, [b+1]; ax= a+b
        
        ;a+b+d
        mov dx, 0 ; conversie fara semn de la ax la dx:ax
        push dx
        push ax
        pop eax
        mov edx, 0      ; EDX:EAX = a+b (conversie fara semn)
        add eax, [d]
        adc edx, [d+4]  ; EDX:EAX = a+b+d
        mov [x], eax
        mov [x+4], edx   ; x=a+b+d
        
        ;a-c
        mov al, [a] ; al=a
        mov ah, 0 ; conversie fara semn de la al la ax
        mov dx, 0 ; conversie fara semn de la ax la dx:ax
        sub ax, [c]
        sbb dx, [c+2] ; dx:ax=a-c
     
        ;a-c+d
        push dx
        push ax
        pop eax ;eax =dx:ax=a-c
        mov edx, 0      ; EDX:EAX = a-c (conversie fara semn)
        add eax, [d]
        adc edx, [d+4]  ; EDX:EAX = a-c+d
        
        
        ;(a+b+d)-(a-c+d)
        sub [x],eax
        sbb [x+4], edx ;x=(a+b+d)-(a-c+d)
        
        ;b-c
        mov ax, [b] ; ax = b
        mov dx, 0       ; DX:AX = b (conversie fara semn)
        sub ax, [c]
        sbb dx, [c+2]   ; DX:AX = b-c
        
        ;(a+b+d)-(a-c+d)+(b-c)
        push dx
        push ax
        pop eax ;eax =dx:ax=b-c
        mov edx, 0      ; EDX:EAX = b-c (conversie fara semn)
        add [x],eax
        adc [x+4], edx  ; x=(a+b+d)-(a-c+d)+(b-c)
        ; exit(0)
        push    dword 0      
        call    [exit] 