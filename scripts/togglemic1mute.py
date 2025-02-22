import voicemeeterlib

with voicemeeterlib.api('banana') as vm:
    if vm.strip[0].mute==0:
        vm.strip[0].mute=1
    else:
        vm.strip[0].mute=0
