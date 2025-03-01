import voicemeeterlib

with voicemeeterlib.api('banana') as vm:
    if vm.bus[2].mute==0:
        vm.bus[2].mute=1
    else:
        vm.bus[2].mute=0
