mkdir bin
nasm -f elf64 -I shared/ ./elf-builder/elf-builder.s -o ./bin/elf-builder.o
gcc ./bin/elf-builder.o -o ./bin/elf-builder -no-pie
./bin/elf-builder