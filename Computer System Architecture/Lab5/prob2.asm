bits 32      
extern exit               
import exit msvcrt.dll     

;2.	Se da un sir de caractere S. Sa se construiasca sirul D care sa contina toate caracterele ;speciale (!@#$%^&*) din sirul S.
segment data use32 class=data
     s1 db "#524@ lvmtror&"
     len1 equ $-s1 
     s2 db "!@#$%^&*"
     len2 equ $-s2
     d times len1 db 0

segment code use32 class=code
    start:
        mov esi, 0
        mov edi, 0 
        mov ecx, len1 
        jecxz final
        
        repeta:
        mov al,[s1+esi]
        mov ebx, 0
        cauta: 
            mov dl,[s2+ebx]
            cmp al, dl
            je gasit
            inc ebx 
            cmp ebx, len2
        jb cauta
        inc esi 
        cmp esi, len1
        jb repeta 
        
        gasit:    
        mov [d+edi], al
        inc edi
        inc esi 
        dec ecx
        cmp ecx, len1
        jae final
        cmp esi, len1
        jb repeta 
        jmp final
        loop repeta

        final: 


        ; exit(0)
        push    dword 0      
        call    [exit]       
