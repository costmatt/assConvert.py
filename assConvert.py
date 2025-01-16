import re

# Assembly instructions to C/C++ equivalents
instruction_map = {
    "mov": " = ",
    "add": " += ",
    "sub": " -= ",
    "push": "// push ",
    "pop": "// pop ",
    "call": "// call ",
    "ret": "return",
    # Add more mappings as needed
}

def convert_assembly_to_c(assembly_code):
    c_code = []
    for line in assembly_code.split('\n'):
        # Remove comments and unnecessary whitespace
        line = line.split(';')[0].strip()
        if not line:
            continue

        # Match assembly instruction and operands
        match = re.match(r"(\w+)\s+(.*)", line)
        if match:
            instr, operands = match.groups()
            if instr in instruction_map:
                c_instr = instruction_map[instr]
                if instr == "mov":
                    src, dst = operands.split(', ')
                    c_line = f"{dst}{c_instr}{src};"
                elif instr in {"add", "sub"}:
                    dst, src = operands.split(', ')
                    c_line = f"{dst}{c_instr}{src};"
                else:
                    c_line = f"{c_instr}({operands});"
                c_code.append(c_line)
            else:
                c_code.append(f"// Unknown instruction: {line}")
        else:
            c_code.append(f"// Cannot parse: {line}")
    return '\n'.join(c_code)

if __name__ == "__main__":
    assembly_code = """
    mov eax, 1
    add eax, 2
    sub eax, 1
    push eax
    pop ebx
    call some_function
    ret
    """
    c_code = convert_assembly_to_c(assembly_code)
    print("Converted C Code:")
    print(c_code)
