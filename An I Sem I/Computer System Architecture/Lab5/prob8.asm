bits 32 ;
global start        

extern exit              
import exit msvcrt.dll    
;8. Se da un sir de caractere S. Sa se construiasca sirul D care sa contina toate literele mari din sirul S
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s db 'a','F', 'b', 'c','S', 'm', 'n', 'X'    ; declararea sirului initial s
	len equ $-s                     ; stabilirea lungimea sirului initial l
	d times len db 0                ; rezervarea unui spatiu de dimensiune l pentru sirul destinatie d 
                                    ;si initializarea acestuia

; our code starts here
segment code use32 class=code
    start:
        mov ecx, len    ; ECX = lungimea sirului initial s
        jecxz sfarsit
        mov esi, 0      ; i = 0
        mov edi, 0      ; j = 0
        
        ; citesc s[i]
        mov al, [s+esi]
        
        ;verific elementele din sirul s
        cmp [s+esi], 'A'
        jae pozitiv
        jb negativ
        
        pozitiv:
        cmp [s+esi], 'Z'
        jna  pozitiv_2
  
        
        pozitiv_2:
        mov [d+edi], [s+esi]
        jump sfarsit
        
        negativ:
        jump sfarsit
        
        inc esi         ; i++
        inc edi         ; j++
    loop repeta
        
    sfarsit:
    
        ; exit(0)
        push    dword 0      
        call    [exit]       
