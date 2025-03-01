import voicemeeterlib

with voicemeeterlib.api('banana') as vm:
    if vm.strip[1].mute==0:
        vm.strip[1].mute=1
    else:
        vm.strip[1].mute=0
