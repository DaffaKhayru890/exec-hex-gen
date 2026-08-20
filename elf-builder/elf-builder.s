%include "abi.inc"

section .data 
    fmt db "Hello, World!", 10, 0

section .text
    global main
    extern CSYM(printf)
    extern CSYM(exit)

main: 
    push rbp
    mov rbp, rsp
    sub rsp, SHADOW + 16

    lea ARG1, [rel fmt]
    call CSYM(printf)

    mov ARG1, 0
    call CSYM(exit)    