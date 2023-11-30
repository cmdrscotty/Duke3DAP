from dataclasses import dataclass

from Options import Choice, NamedRange, PerGameCommonOptions, Toggle


class SkillLevel(Choice):
    """In-Game difficulty. Primarily affects number of Enemies spawned"""

    display_name = "SkillLevel"
    option_piece_of_cake = 0
    option_lets_rock = 1
    option_come_get_some = 2
    option_damn_im_good = 3
    default = 1


class Difficulty(Choice):
    """Randomizer difficulty. Higher levels offer less resources and require harder tricks in logic
    such as jumping on enemies or better use of jetpack and scuba gear fuel"""

    display_name = "Difficulty"
    option_easy = 0
    option_medium = 1
    option_hard = 2
    option_extreme = 3
    default = 1


class GlitchLogic(Toggle):
    """Include glitches in the logic. Higher difficulty settings may require more complicated glitches."""

    display_name = "Include Glitches"
    default = False


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


class GoalPercentage(NamedRange):
    """Percentage of chosen goals that need to be reached to win the game"""

    display_name = "Percentage of Goals required"
    range_start = 25
    range_end = 100
    special_range_names: {
        "half": 50,
        "all": 100,
    }
    default = 100


class IncludeSecrets(Toggle):
    """Include secret areas into the location pool. This only has an effect if **goal** is set to *beat_all_levels*"""

    display_name = "Include Secrets as Locations"
    default = False


class IncludeMultiplayerItems(Toggle):
    """Add location checks for multiplayer only item spawns"""

    display_name = "Use Multiplayer Only Items"
    default = False


# ToDo find a way to generate this dynamically from the episodes list
class Episode1(Toggle):
    """Include Episode 1: Hollywood Holocaust in the randomizer"""

    display_name = "Use Episode 1"
    default = True


class Episode2(Toggle):
    """Include Episode 2: Lunar Apocalypse in the randomizer"""

    display_name = "Use Episode 2"
    default = False


class Episode3(Toggle):
    """Include Episode 3: Shrapnel City in the randomizer"""

    display_name = "Use Episode 3"
    default = False


class Episode4(Toggle):
    """Include Episode 4: Hollywood Holocaust in the randomizer"""

    display_name = "The Birth"
    default = False


@dataclass
class Duke3DOptions(PerGameCommonOptions):
    difficulty: Difficulty
    glitch_logic: GlitchLogic
    skill_level: SkillLevel
    unlock_abilities: UnlockAbilities
    area_maps: AreaMaps
    goal: Goal
    goal_percentage: GoalPercentage
    include_mp_items: IncludeMultiplayerItems
    include_secrets: IncludeSecrets
    episode1: Episode1
    episode2: Episode2
    episode3: Episode3
    episode4: Episode4
