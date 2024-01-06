bits 32      
extern exit               
import exit msvcrt.dll     

;Se da un fisier text. Sa se citeasca continutul fisierului, sa se contorizeze 
;numarul de litere 'y' si 'z' si sa se afiseze aceaste valori. 
;Numele fisierului text este definit in segmentul de date.
  segment data use32 class=data
       nume_fisier db "fisier.txt", 0
       descriptor_fisier dd -1
       mod_acces db "r", 0 
       len equ 100   ;numarul maxim de elemente citite din fisier 
       text times len db 0  ;sirul in care vom citi textul 
       rezultat1 dd 0 
       rezultat2 dd 0
       format db "%d %d", 0       
        
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
         cmp al, 'y'
         jnz urmator
         inc dword[rezultat1]
         
         urmator: 
         cmp al, 'z'
         jnz inegale 
         inc dword[rezultat2]
         
         inegale:
         inc ebx 
       loop repeta 
       
       ;inchidem fisierul 
       push dword [descriptor_fisier]
       call [fclose]
       add esp, 4
       
       ;afisam rezultatul 
       push dword [rezultat2]
       push dword [rezultat1]
       push dword format 
       call [printf]
       add esp, 4*3
         
        
        sfarsit:

        push dword 0
        call [exit]
        
       