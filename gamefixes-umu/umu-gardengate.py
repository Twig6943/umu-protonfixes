"""GardenGate https://github.com/nocss42/GardenGate"""

from protonfixes import util

def main() -> None:
    util.protontricks('vcrun2022')
    util.winedll_override('dinput8', util.OverrideOrder.NATIVE_BUILTIN)
    util.winedll_override('winmm', util.OverrideOrder.NATIVE_BUILTIN)
