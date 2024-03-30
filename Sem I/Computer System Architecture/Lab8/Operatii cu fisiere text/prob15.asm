bits 32      
extern exit               
import exit msvcrt.dll     

;Se dau un nume de fisier si un text (definite in segmentul de date). 
;Textul contine litere mici, litere mari, cifre si caractere speciale. 
;Sa se inlocuiasca toate caracterele speciale din textul dat cu caracterul 'X'. 
;Sa se creeze un fisier cu numele dat si sa se scrie textul obtinut in fisier.
segment data use32 class=data
    text db "Ana are 5 mere & @ndk3l +", 0  ; textul care va fi scris in fisier
    mod_acces db "w", 0                                 ; modul de deschidere a fisierului 
                                                 ; w - pentru scriere. daca fiserul nu exista, se va crea 
    max equ 100                             ;numarul maxim de caractere din fisier
    result times max+1 db 0                 ;stocam textul modificat in result
    len dd 0
    speciale db "!@#$%^&*()_+-=:;{}[]'\/|."     ;sir de caractere speciale
    len_s equ $-speciale                    ;lungimea sirului de caractere speciale
    nume_fisier db "prob15.txt", 0          ; numele fisierului care va fi creat
    descriptor_fisier dd 0                  ; variabila in care vom salva descriptorul fisierului - necesar pentru a putea face referire la fisier

    segment code use32 class=code
    start: 
        ; apelam fopen pentru a crea fisierul
        ; functia va returna in EAX descriptorul fisierului sau 0 in caz de eroare
        ; eax = fopen(nume_fisier, mod_acces)
        
        push dword mod_acces   
        push dword nume_fisier       
        call [fopen]       ; apelam functia fopen 
        add esp, 4 * 2     ; eliberam parametrii de pe stiva
                           ; 4 = dimensiunea unui dword; 2 = nr de parametri
       
        mov [descriptor_fisier], eax   ; salvam valoarea returnata de fopen in variabila descriptor_fis
        
        ; verificam daca functia fopen a creat cu succes fisierul (daca EAX != 0)
        cmp eax, 0
        je final
        
         ; parcurgem textul si inlocuim caracterele speciale cu 'X'
         mov ebx, 0         ;ebx- calculam lungimea sirului text
         mov esi, 0         ;esi-index pentru text
    repeta:
        mov al, [text+esi]  ;Al<-text[esi]
        
        cmp al, 0           ;verificam daca am ajuns la finalul textului
        je scrie
        
        mov byte [result+esi], al; scriem caracterul in result
        
        ; verific daca e caracter special
        call verifica       ;apelam subprogramul verifica
        cmp edx, 1          ;daca edx=1 e un caracter special, altfel nu e caracter special
        jne nu_e_special    
        
        ; inlocuiesc caracterul curent cu 'X'
        mov byte [result+esi], 'X'
        
    nu_e_special:
        inc ebx           ;incrementam lungimea
        inc esi           ;incrementam indexul 
        jmp repeta
        
    scrie:
        mov [len], ebx    ;len= lungimea textului 
        
        ;apelam functia de scriere in fisier
        ; fwrite(void* buffer, int size, int count, FILE* stream)
        push dword [descriptor_fisier] ;punem pe stiva descriptorul fisierului
        push dword [len]               ;punem pe stiva lungimea 
        push dword 1                   ;punem pe stiva dimensiunea unui element
        push dword result              ;punem pe stiva textul modificat 
        call [fwrite]                  ;apelam functia de scriere in fisier
        add esp, 4*4                   ;eliberam parametrii de pe stiva
        
        ; inchid fisierul
        ; fclose(descriptor_fisier)
        push dword [descriptor_fisier]  ;punem pe stiva descriptorul fisierului
        call [fclose]                   ;apelam functia de inchidere a fisierului 
        add esp, 1*4                    ;eliberam parametrii de pe stiva
        
    final:
        push dword 0
        call [exit]
        
        ;SUBPROGRAM PENTRU VERIFICREA CARACTERELOR SPECIALE
        ; AL = caracterul curent
        ; verifica daca caracterul din AL e special
    verifica:
        push esi       ;punem pe stiva esi
        mov ecx, len_s ;ecx=lungimea sirului speciale
        mov esi, 0     ;index pentru sirul speciale
    cauta:
        mov dl, [speciale+esi] ;dl<- speciale[esi]
        
        cmp al, dl    ;comparam caracterele
        je e_special  ;daca sunt egale e caracter special
        
        inc esi       
        loop cauta
         
        mov edx, 0   ;daca al nu e caracter special edx=0   
        jmp nu_e
        
    e_special:
        mov edx, 1   ;daca al e caracter special edx=1
        
    nu_e:
        pop esi    ;extragem de pe stiva
        ret 

