import voicemeeterlib

with voicemeeterlib.api('banana') as vm:
    if vm.strip[2].A1==0:
        vm.strip[2].A1=1
    else:
        vm.strip[2].A1=0
