import voicemeeterlib

with voicemeeterlib.api('banana') as vm:
    if vm.bus[0].mute==0:
        vm.bus[0].mute=1
    else:
        vm.bus[0].mute=0
