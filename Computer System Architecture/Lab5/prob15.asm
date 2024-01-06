bits 32
global start        
extern exit               
import exit msvcrt.dll    
 
;Se dau 2 siruri de octeti A si B. Sa se construiasca sirul R care sa contina elementele lui B in ordine inversa urmate de elementele impare ale lui A.
;Exemplu:
;A: 2, 1, 3, 3, 4, 2, 6
;B: 4, 5, 7, 6, 2, 1
;R: 1, 2, 6, 7, 5, 4, 1, 3, 3
segment data use32 class=data
    A db 1,2,3,4 
    len_A equ $-A    
    B db 5,6,7,8
    len_B equ $-B
    R times len_B+len_A db 0
    
segment code use32 class=code
    start:
        ;construim R cu elementele lui B in ordine inversa
        mov ecx, len_B      ; ciclul se executa de len_B ori
        jecxz final			; prevenim intrarea intr-un ciclu infinit
        mov esi, len_B-1    ; ESI - index in sirul B(de la coada la cap)
        mov edi, 0          ;EDI - index in sirul R
        
    repeta:
        mov al, [B+esi]     ; AL <- B[ESI]
        dec esi             ; trec la urmatorul element din sirul B
        mov [R+edi], al     ; R[EDI] <- AL
        inc edi             ; trec la urmatorul element din sirul R
    loop repeta
        
        ;adaugam la finalul lui R elementele impare din A
        
        mov esi, 0          ;resetam indexul pentru a parcurge sirul A
        mov ecx, len_A      ; ciclul se executa de len_A ori
        jecxz final			; prevenim intrarea intr-un ciclu infinit
        
    repeta1:
        mov al, [A+esi]     ; AL <- A[ESI]
        test al, 1          ;verificam daca elementul este impar
        jz mai_departe      ;daca nu este impar sarim la eticheta mai_departe
        
        mov[R+edi], al      ;punem elementul impar in R
        inc edi             ;trecem la urmatorul element din sirul R
        
        mai_departe:
            inc esi         ;trecem la urmatorul element din A
    loop repeta1
    
    final:
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
