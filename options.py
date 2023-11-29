from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, Toggle


class Difficulty(Choice):
    """In-Game difficulty. Primarily affects number of Enemies spawned"""

    display_name = "Difficulty"
    option_piece_of_cake = 0
    option_lets_rock = 1
    option_come_get_some = 2
    option_damn_im_good = 3
    default = 1


class UnlockAbilities(Toggle):
    """Unlock Jumping, Crouching, Diving and Running as items"""

    display_name = "Unlock Abilities"
    default = True


class AreaMaps(Choice):
    """Select if full game maps are available"""

    display_name = "Area Maps"
    option_none = 0
    option_unlockable = 1
    option_start_with = 2
    default = 1


class Goal(Choice):
    """Choose the goal of the game"""

    display_name = "Goal"
    option_beat_all_levels = 0
    option_collect_all_secrets = 1
    option_both = 2
    default = 2


@dataclass
class Duke3DOptions(PerGameCommonOptions):
    difficulty: Difficulty
    unlock_abilities: UnlockAbilities
    area_maps: AreaMaps
    goal: Goal
