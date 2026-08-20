; abi.inc detect current platform abi

%ifidn __OUTPUT_FORMAT__, wind64
    %define SHADOW 32
    %define ARG1 rcx
    %define ARG2 rdx
    %define ARG3 r8
    %define ARG3D r8d
    %define ARG4 r9
    %define CSYM(name) name

%elifidn __OUTPUT_FORMAT__, elf64
    %define SHADOW 32
    %define ARG1 rdi
    %define ARG2 rsi
    %define ARG3 rdx
    %define ARG3D edx
    %define ARG4 rcx 
    %define CSYM(name) name

%endif

%macro VARIADIC_ARG_SETUP 0 

%ifidn __OUTPUT_FORMAT__, wind64

%elifidn __OUTPUT_FORMAT__, elf64
    xor eax, eax
%endif 

%endmacro