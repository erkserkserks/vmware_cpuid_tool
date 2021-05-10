#!/usr/bin/env python3
"""
  Tool that converts CPUID data from the cpuid tool (http://www.etallen.com/cpuid.html) into
  the VMWare .vmx format.

  This can be useful for spoofing a particular CPU on the virtual machine.

  Usage:
    1. Use `cpuid` tool to get and save raw CPUID data, e.g. `cpuid --raw > cpuid_sandy_bridge`
    2. Use this tool to convert raw CPUID data into VMware .vmx format, e.g.
       `python3 convert.py cpuid_sandy_bridge`
    3. Copy output from this tool and paste into the virtual machine's .vmx file.

  License: MIT
"""
import argparse
import re

def add_colon(in_str):
    """Add colon after every 4th character."""
    return ':'.join([in_str[i:i+4] for i in range(0, len(in_str), 4)])


def parse_cpuid_raw_file(filename):
    """Parse output from `cpuid --raw` command."""
    parsed = []
    with open(filename) as file:
        for line in file:
            match = re.match(r"\s*?(0x........) (0x..): eax=(0x........) ebx=(0x........) "
                         r"ecx=(0x........) edx=(0x........)\s*?", line)
            if not match:
                raise RuntimeError(f"Unexpected format in this line: '{line}'!"
                                    "Is the output of `cpuid --raw` used?")
            eax_in = int(match.group(1), 16)
            try_in = int(match.group(2), 16)
            eax = int(match.group(3), 16)
            ebx = int(match.group(4), 16)
            ecx = int(match.group(5), 16)
            edx = int(match.group(6), 16)
            parsed.append((eax_in, try_in, eax, ebx, ecx, edx))
    return parsed


def convert_to_vmx_format(parsed):
    """Convert CPUID info into VMware .vmx format."""
    for (eax_in, try_in, eax, ebx, ecx, edx) in parsed:
        eax_in_str = format(eax_in, 'x')
        try_in_str = format(try_in, 'x')
        eax_str = add_colon(format(eax, '032b'))
        ebx_str = add_colon(format(ebx, '032b'))
        ecx_str = add_colon(format(ecx, '032b'))
        edx_str = add_colon(format(edx, '032b'))

        print(f'cpuid.{eax_in_str}.{try_in_str}.eax = "{eax_str}"')
        print(f'cpuid.{eax_in_str}.{try_in_str}.ebx = "{ebx_str}"')
        print(f'cpuid.{eax_in_str}.{try_in_str}.ecx = "{ecx_str}"')
        print(f'cpuid.{eax_in_str}.{try_in_str}.edx = "{edx_str}"')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cpuid_raw")
    args = parser.parse_args()

    parsed = parse_cpuid_raw_file(args.cpuid_raw)
    convert_to_vmx_format(parsed)
