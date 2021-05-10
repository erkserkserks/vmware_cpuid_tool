# VMware CPUID tool

Tool that converts CPUID data from the cpuid tool (http://www.etallen.com/cpuid.html) into
the VMWare .vmx format.

This can be useful for spoofing a particular CPU on the virtual machine.

Usage:
  1. Use `cpuid` tool to get and save raw CPUID data, e.g. `cpuid --raw > cpuid_sandy_bridge`
  2. Use this tool to convert raw CPUID data into VMware .vmx format, e.g.
     `python3 convert.py cpuid_sandy_bridge`
  3. Copy output from this tool and paste into the virtual machine's .vmx file.

License: MIT
