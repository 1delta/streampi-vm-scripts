import voicemeeterlib

with voicemeeterlib.api('banana') as vm:
    if vm.strip[4].B1==0:
        vm.strip[4].B1=1
    else:
        vm.strip[4].B1=0
