bits 32 ; 
global start        


extern exit               
import exit msvcrt.dll    
                          
segment data use32 class=data
     a dd  12348a9fh ;10011101010111000001101010011010b
     b dd  5678af9ah ;01011010100101010111010001000010b 
     c dq  0         ;002a5091h
     
    ;Se dau dublucuvintele A si B. Sa se formeze qwordul C in felul urmator:
    ;bitii 0-7 ai lui C sunt bitii 21-28 ai lui A
    ;bitii 8-15 ai lui C sunt bitii 23-30 ai lui B complementati
    ;bitii 16-21 ai lui C sunt 101010
    ;bitii 22-31 ai lui C au valoarea 0
    ;bitii 32-42 ai lui C sunt bitii 21-31 ai lui B
    ;bitii 43-55 ai lui C sunt bitii 1-13 ai lui A
    ;bitii 56-63 ai lui C sunt bitii 24-31 ai rezultatului A XOR 0ABh
segment code use32 class=code
    start:
        ;Vom forma quadwordul C in registrii EDX:EBX
        mov ebx, 0
        mov ecx, 0
        
        ;bitii 0-7 ai lui C sunt bitii 21-28 ai lui A
        mov eax, [a]
        and eax, 00011111111000000000000000000000b ;izolez bitii 21-28 a lui A
        mov cl, 21
        ror eax, cl   ;deplasez bitii 21-28 in pozitia 0-7 
        or ebx, eax   ;concatenez rezultatul

        ;bitii 8-15 ai lui C sunt bitii 23-30 ai lui B complementati
        mov eax, [b]
        not eax   ;inversez dublucuvantul b
        and eax, 01111111100000000000000000000000b  ;izolex bitii 23-30 ai lui b
        mov cl, 15
        ror eax,cl  ;deplasez bitii 23-30 in pozitia 8-15
        or ebx, eax ;concatenez rezultatul
        
        ;bitii 16-21 ai lui C sunt 101010
        mov eax, 00000000001010100000000000000000b
        and eax, 00000000001111110000000000000000b  ;izolez bitii 16-21
        or ebx, eax ;concatenez rezultatul
                
        ;bitii 22-31 ai lui C au valoarea 0
        and ebx, 00000000001111111111111111111111b
        
        ;bitii 32-42 ai lui C sunt bitii 21-31 ai lui B
        mov eax, [b]
        and eax, 11111111111000000000000000000000b  ;izolez bitii 21-31 ai lui b
        mov cl, 11
        rol eax, cl ; deplasez bitii 21-31 in pozitia 32-42
        or edx, eax ;concatenez rezultatul
        
        ;bitii 43-55 ai lui C sunt bitii 1-13 ai lui A
        mov eax,[a]
        and eax, 00000000000000000011111111111110b ;izolez bitii 1-13 ai lui a
        mov cl, 10
        rol edx, cl
        or edx, eax
        
        
        ;bitii 56-63 ai lui C sunt bitii 24-31 ai rezultatului A XOR 0ABh
        mov eax, [a]
        xor eax, 0ABh
        and eax, 11111111000000000000000000000000b
        or edx, eax
        
        mov [c], ebx
        mov [c+4], edx
        
        ; exit(0)
        push    dword 0      
        call    [exit] 