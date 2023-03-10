from typing import List


def purity_show_binary_data(input_bytes: bytes):
    line: List[str] = []
    for byte in input_bytes:
        line.append('{0:02x}'.format(byte))

    output: str = ''
    for idx in range(len(line)):
        if idx % 16 != 15:
            output += f'{line[idx]} '
        else:
            output += f'{line[idx]}\n'
    output.rstrip()
    print(output)
