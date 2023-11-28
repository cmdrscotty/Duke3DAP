from ..base_classes import D3DEpisode
from .e1l1 import E1L1
from .e1l2 import E1L2
from .e1l3 import E1L3
from .e1l4 import E1L4
from .e1l5 import E1L5
from .e1l6 import E1L6
from .e1l7 import E1L7
from .e2l1 import E2L1
from .e2l2 import E2L2
from .e2l3 import E2L3


class E1(D3DEpisode):
    name = "L.A. Meltdown"
    volumenum = 0
    levels = [E1L1(), E1L2(), E1L3(), E1L4(), E1L5(), E1L6(), E1L7()]


class E2(D3DEpisode):
    name = "Lunar Apocalypse"
    volumenum = 1
    levels = [E2L1(), E2L2(), E2L3()]


class E3(D3DEpisode):
    name = "Shrapnel City"
    volumenum = 2
    levels = []


class E4(D3DEpisode):
    name = "The Birth"
    volumenum = 3
    levels = []


all_episodes = [E1(), E2(), E3(), E4()]
all_levels = [level for ep in all_episodes for level in ep.levels]
