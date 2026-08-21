import struct

def gen_elf_header(
	entry_point, phoff, ehsize=52, phentsize=32, phnum=1,
	shoff=0, shentsize=0, shnum=0, shstrndx=0, e_type=2,
	e_machine=0x28
):
	e_ident = bytearray(b'\x7fELF' + bytes([1,1,1,0,0]) + bytes(7))

	e_header = struct.pack(
		'<16sHHIIIIIHHHHHH',
		bytes(e_ident), e_type, e_machine, 1, entry_point,
		phoff, shoff, 0, ehsize, phentsize, phnum,
		shentsize, shnum, shstrndx
	)

	return e_header

def gen_prog_header(
	p_type=1, p_flags=5, p_offset=0, p_vaddr=0,
	p_paddr=0, p_filesz=0, p_memsz=0, p_align=0x10000
):
	return struct.pack(
		'<IIIIIIII',
		p_type, p_offset, p_vaddr, p_paddr,
		p_filesz, p_memsz, p_flags, p_align
	)

if __name__ == '__main__':
	EH_SIZE=52
	PH_SIZE=32

	entry_point=0x8078
	phoff=EH_SIZE

	elf_header=gen_elf_header(
		entry_point=entry_point,
		phoff=phoff,
		phnum=1,
		e_machine=0x28
	)

	program_header=gen_prog_header(
		p_type=1, p_flags=1, p_offset=0, p_vaddr=0x8000,
		p_paddr=0x8000, p_filesz=0x80, p_memsz=0x80, p_align=0x10000
	)

	result = elf_header + program_header

	print(result.hex())