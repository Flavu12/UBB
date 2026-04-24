bits 32      
extern exit               
import exit msvcrt.dll     

;Se da un nume de fisier (definit in segmentul de date). Sa se creeze un fisier 
;cu numele dat, apoi sa se citeasca de la tastatura numere si sa se scrie valorile citite
;in fisier pana cand se citeste de la tastatura valoarea 0.
segment data use32 class=data
       nume_fisier db "fisier.txt", 0
       descriptor_fisier dd -1
       mod_acces db "a", 0 
       len equ 100    ;nr maxim     
       format db "%s", 0 
       a db 0       
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
      
      citire:
      ;citim de la tastatura
      push dword a
      push dword format
      call[scanf]
      add esp, 4*2
      
     cmp byte[a], '0'
     jz final
     
     ;daca al nu este 0 il scriem in fisier 
     push dword a
     push dword  [descriptor_fisier]
     call [fprintf]
     add esp, 4*2
     jmp citire
      
      
       final:
       ;inchidem fisierul
       push dword [descriptor_fisier]
       call [fclose]
       add esp, 4
       
       sfarsit:


            push    dword 0      ; push the parameter for exit onto the stack
            call    [exit]       ; call exit to terminate the program   
