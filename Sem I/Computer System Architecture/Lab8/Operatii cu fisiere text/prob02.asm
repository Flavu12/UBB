bits 32      
extern exit               
import exit msvcrt.dll     

;Se da un fisier text. Sa se citeasca continutul fisierului, sa se contorizeze 
;numarul de consoane si sa se afiseze aceasta valoare. 
;Numele fisierului text este definit in segmentul de date.
segment data use32 class=data
        sir_consoane db "bcdfghjklmnpqrstvwxyz", 0 ; sir de consoane
        lungime equ $-sir_consoane
        nume_fisier db "fisier.txt", 0 ;numele fiserului
        mod_acces db "r", 0 ; modul de acces al fisierului, r - pentru citire
        descriptor_fisier dd -1 ; descriptorul fisierului
        len equ 100 ; numarul maxim de elemente citite din fisier
        text times len db 0 ;sirul in care vom citi ce este in fisier
        ans dd 0 ;variabila in care vom retine raspunsul
        format db "%u", 0
        
segment code use32 class=code
    start:
        push dword mod_acces ; punem pe stiva modul de acces al fisierului
        push dword nume_fisier ; punem pe stiva numele fisierului
        call [fopen]
        add esp, 4*2 ; eliberam parametrii de pe stiva
        
        mov [descriptor_fisier], eax ; salvam ce returneaza fopen in variabila descriptor_fisier
        
        ;verificam daca a fost accesat cu succes fisierul:
        cmp eax, 0
        je sfarsit ;sarim la eticheta final daca eax este 0
        
        ;citim textul din fisier:
        push dword [descriptor_fisier] ; parametrul 4 = descriptor_fisier returnat de apelul functiei fopen
        push dword len ; parametrul 3 = numarul maxim de elemente ce se vor citi din fisier
        push dword 1 ; parametrul 2 = dimensiunea unui element citit
        push dword text ; parametrul 1 = variabila in care se va retine textul citit
        call [fread] ; apelam functia fread, in EAX vom avea lungimea textului citit
        add esp, 4*4 ; eliberam stiva de parametri
        
        
        ;parcurgem sirul 'text' si verificam egalitatea fiecarui element al sau cu un element din sirul 'sir_consoane':
        mov ecx, eax
        mov ebx, text
        Repeta:
                mov al, [ebx] ; AL <- text[i] 
                mov edx, sir_consoane ; ;EDX <- adresa de start a sirului sir_consoane
                push ecx ; folosim mecanismul push-pop pentru a mentine intacta valoarea lui ecx in primul loop
                mov ecx, lungime ; ECX <- lungimea sirului de consoane
                    in_Repeta:
                           cmp al, [edx] ; facem comparatie dintre text[i] si sir_consoane[j], j= 1 -> 21
                           jnz not_equal ; in caz de inegalitatea sarim la eticheta not_equal
                           inc dword [ans] ; in caz de egalitatea incrementam varabila rezultat cu 1
                           not_equal:
                           inc edx ;edx se va incrementa (j+=1)
                    loop in_Repeta
                pop ecx ; folosim mecanismul push-pop pentru a mentine intacta valoarea lui ecx in primul loop
                inc ebx
        loop Repeta
       
        
        ;inchidem fisierul:
        push dword [descriptor_fisier] ; parametrul 1 = descriptorul fisierului
        call [fclose] ;apelam functia fclose
        add esp, 4 ; eliberam parametrul de pe stiva
        
        ;afisarea rezultatului:        
        push dword [ans] ;punem pe stiva valoarea lui ans
        push dword format
        call [printf] ; apelam functia printf
        add esp, 4*2 ;eliberam parametrii de pe stiva
        
        sfarsit:
            push    dword 0      ; push the parameter for exit onto the stack
            call    [exit]       ; call exit to terminate the program   
