# VMware CPUID tool

Tool that converts CPUID data from the [cpuid tool](http://www.etallen.com/cpuid.html) into
the VMWare .vmx format.

This can be useful for spoofing a particular CPU on the virtual machine.

Usage:
  1. Use `cpuid` tool to get and save raw CPUID data, e.g. `cpuid --raw > cpuid_sandy_bridge`
  2. Use this tool to convert raw CPUID data into VMware .vmx format, e.g.
     `python3 convert.py cpuid_sandy_bridge`
  3. Copy output from this tool and paste into the virtual machine's .vmx file.

## License:
MIT

## References:
[VMware CPUID masks](https://news.ycombinator.com/item?id=14084148)

[Mac OS X 10.4 Tiger on a Modern Intel Mac (Virtualization)](https://forums.macrumors.com/threads/mac-os-x-10-4-tiger-on-a-modern-intel-mac-virtualization.2162582/)

[How to fake a VMs guest OS CPUID](https://web.archive.org/web/20220924202501/http://vknowledge.net/2014/04/17/how-to-fake-a-vms-guest-os-cpuid/)
