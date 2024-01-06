bits 32      
extern exit               
import exit msvcrt.dll     

;Se dă un sir de caractere (definit in segmentul de date). Să se citească de la tastatură
;un caracter, să se determine numărul de apariţii al acelui caracter în şirul dat şi să se
;afişeze acel caracter împreună cu numărul de apariţii al acestuia.
segment data use32 class=data
    s db "ana are mere si pere multe", 0
    len equ $-s
    a dd 0
    format_citire db "%c", 0
    format_afisare db "%c %d", 0
segment code use32 class=code
    start:
        push dword a
        push dword format_citire
        call [scanf]
        add esp, 4*2
        
        mov dl, [a]
        mov ebx, 0
        mov esi, 0
        mov ecx, len
        jecxz final
        repeta:
        mov al, [s+esi]
        cmp al, dl
        jne departe
        inc ebx 
        departe:
        inc esi
        loop repeta
        
        push dword ebx
        push dword edx
        push dword format_afisare
        call [printf]
        add esp, 4*2
    
     final:

        ; exit(0)
        push dword 0      
        call [exit]  
