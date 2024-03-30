bits 32      
extern exit               
import exit msvcrt.dll     

;Sa se citeasca de la tastatura un numar in baza 10 si un numar in baza 16. 
;Sa se afiseze in baza 10 numarul de biti 1 ai sumei celor doua numere citite. Exemplu:
;a = 32 = 0010 0000b
;b = 1Ah = 0001 1010b
;32 + 1Ah = 0011 1010b
;Se va afisa pe ecran valoarea 4.
segment data use32 class=data
	a dd 0
    	b dd 0
    	format_citire db "%d %X", 0
    	format_afisare db "%d", 0
segment code use32 class=code
    start:
     push dword b
     push dword a
     push dword format_citire
     call [scanf]
     add esp, 4*3 
          
     mov eax, [a]
     add eax, [b]
     
     mov ecx, 32 
     jecxz final 
     mov ebx, 0
     cld 
     repeta:
     shl eax, 1
     adc ebx, 0
     loop repeta
     
    
     push ebx 
     push dword format_afisare
     call [printf]
     add esp, 4*2
     final:

        ; exit(0)
        push dword 0      
        call [exit]  
