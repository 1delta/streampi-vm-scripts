import voicemeeterlib

with voicemeeterlib.api('banana') as vm:
    if vm.strip[0].B2==0:
        vm.strip[0].B2=1
    else:
        vm.strip[0].B2=0
