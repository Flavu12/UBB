bits 32      
extern exit               
import exit msvcrt.dll     

;Se da un fisier text. Sa se citeasca continutul fisierului, sa se contorizeze 
;numarul de cifre pare si sa se afiseze aceasta valoare. 
;Numele fisierului text este definit in segmentul de date.
segment data use32 class=data
       cifre db "13579", 0
       len_cifre equ $-cifre
       nume_fisier db "fisier.txt", 0
       descriptor_fisier dd -1
       mod_acces db "r", 0 
       len equ 100   ;numarul maxim de elemente citite din fisier 
       text times len db 0  ;sirul in care vom citi textul 
       rezultat dd 0 
       format db "%d", 0       
        
segment code use32 class=code
    start:
      ;deschidem fisierul 
      push dword mod_acces
      push dword nume_fisier
      call [fopen]
      add esp, 4*2
      
      ;verificam daca fisierul s-a deschis corespunzator
      mov [descriptor_fisier], eax
      cmp eax, 0 
      je sfarsit
      
      ;citim din fisier 
      push dword [descriptor_fisier]
      push dword len
      push dword 1
      push dword text
      call [fread]
      add esp, 4*4
      
      ;parcurgem sirul text
      mov ecx, eax ; in eax avem lungimea textului citit 
      mov ebx, text 
      repeta: 
         mov al, [ebx]
         mov edx, cifre 
         push ecx 
         mov ecx, len_cifre
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
       push dword [rezultat]
       push dword format 
       call [printf]
       add esp, 4*2
         
        
        sfarsit:

            push    dword 0      ; push the parameter for exit onto the stack
            call    [exit]       ; call exit to terminate the program   
