bits 32
global start        
extern exit               
import exit msvcrt.dll    
 
;Se dau doua siruri de caractere S1 si S2. Sa se construiasca sirul D prin concatenarea elementelor de pe pozitiile impare din S2 cu elementele de pe pozitiile pare din S1.
;Exemplu:
;S1: 'a', 'b', 'c', 'b', 'e', 'f'
;S2: '1', '2', '3', '4', '5'
;D: '1', '3', '5', 'b', 'b', 'f'
segment data use32 class=data
    S1 db 'a', 'b', 'c', 'd', 'e', 'f'
    len_s1 equ $-S1
    S2 db '1', '2', '3', '4', '5'
    len_s2 equ $-S2
    
    D times len_s1+len_s2 db 0
segment code use32 class=code
    start:
        ;construim D cu elementele lui S2 de pe pozitiile impare
        mov esi, 0          ; ESI - index in sirul S2
        mov edi, 0          ;EDI - index in sirul D
    repeta_sir1:
        mov al, [S2+esi]    ; AL <- S2[ESI]
        mov [D+edi], al     ; D[EDI] <- AL
        inc esi             ;trecem la urmatorul element din sirul s2(pozitie para)
        inc esi             ;trecem la urmatorul element din sirul s2(pozitia impara)
        inc edi             ; trec la urmatorul element din sirul D
        cmp esi, len_s2     ; verificăm dacă am parcurs complet S2
        jge mai_departe     ;sarim l aeticheta mai_departe daca am parcurs complet s2
        
    jmp repeta_sir1
    
    mai_departe:
        mov esi, 1          ;ESI-index in sirul S1
    repeta_sir2:
        mov al, [S1 + esi]  ; luăm elementul din S1
        mov [D + edi], al   ; adăugăm elementul la șirul rezultat D
        inc edi             ; mărim indicele pentru D
        add esi, 2          ; trecem la următorul element din S1 (pozițiile pare)
        cmp esi, len_s1     ; verificăm dacă am parcurs complet S1
        jge final           ;sarim la eticheta final daca am parcurs tot s1
        
    jmp repeta_sir2
    
        
    final:
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
