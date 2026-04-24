bits 32      
extern exit               
import exit msvcrt.dll     

;Se da un fisier text. Sa se citeasca continutul fisierului, 
;sa se contorizeze numarul de vocale si sa se afiseze aceasta valoare. 
;Numele fisierului text este definit in segmentul de date.
segment data use32 class=data
       vocale db "aeiouAEIOU", 0  ;sir de vocale
       len_vocale equ $-vocale
       nume_fisier db "fisier.txt", 0
       mod_acces db "r",0
       descriptor_fisier dd -1
       len equ 100  ;numarul maxim de elemente citite din fisier 
       text times len db 0 ;sirul in care vom citi ce este in fisier 
       rezultat dd 0
       format db "%d", 0
        
segment code use32 class=code
    start:
        ;deschidem fisierul 
        push dword mod_acces
        push dword nume_fisier
        call [fopen]
        add esp, 4*2
        
        mov [descriptor_fisier], eax ;salvam ce returneaza fopen
        cmp eax, 0
        je sfarsit 
        
        ;citim textul din fisier 
        push dword [descriptor_fisier] ;descriptorul returnaat de functia fopen
        push dword len                 ;numarul maxim de elemente ce se vor citi
        push dword 1                   ;dimensiunea unui element citit 
        push dword text                ;variabila in care se va retine textul citit
        call [fread]
        add esp, 4*4
        
        ;parcurgem sirul 'text' 
        mov ecx, eax    ;in eax vom avea lungimea textului citit
        mov ebx, text
        repeta:
            mov al, [ebx]
            mov edx, vocale
            push ecx
            mov ecx, len_vocale
            repeta1:
                 cmp al, [edx]
                 jnz inegale
                 inc dword[rezultat]
                 
                 inegale:
                 inc edx 
            loop repeta1
            pop ecx 
            inc ebx 
         loop repeta 
         
         ;inchidem fisierul
         push dword [descriptor_fisier]
         call [fclose]
         add esp, 4
         
         ;afisam rezultatul 
         push dword[rezultat]
         push dword format
         call [printf]
         add esp, 4*2
        
        sfarsit:


        ; exit(0)
        push dword 0      
        call [exit]  
