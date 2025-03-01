import voicemeeterlib

with voicemeeterlib.api('banana') as vm:
    if vm.strip[2].mute==0:
        vm.strip[2].mute=1
    else:
        vm.strip[2].mute=0
