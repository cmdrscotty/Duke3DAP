import math
from typing import TYPE_CHECKING, Callable, Union

from BaseClasses import CollectionState

if TYPE_CHECKING:
    from . import D3DWorld


class Rule(object):
    def __call__(self, state: CollectionState) -> bool:
        raise NotImplementedError

    def __or__(self, other: "Rule") -> "Rule":
        # short circuit
        if isinstance(other, RuleTrue):
            return other
        if isinstance(other, RuleFalse):
            return self
        return LambdaRule(lambda state: self(state) or other(state))

    def __and__(self, other: "Rule") -> "Rule":
        # short circuit
        if isinstance(other, RuleTrue):
            return self
        if isinstance(other, RuleFalse):
            return other
        return LambdaRule(lambda state: self(state) and other(state))


RULETYPE = Union[Rule, Callable[[CollectionState], bool]]


class LambdaRule(Rule):
    def __init__(self, func):
        self._func = func

    def __call__(self, state: dict) -> bool:
        return self._func(state)


class RuleTrue(Rule):
    def __call__(self, state: CollectionState) -> bool:
        return True

    def __or__(self, other: "Rule") -> "Rule":
        return self

    def __and__(self, other: "Rule") -> "Rule":
        return other


class RuleFalse(Rule):
    def __call__(self, state: CollectionState) -> bool:
        return False

    def __or__(self, other: "Rule") -> "Rule":
        return other

    def __and__(self, other: "Rule") -> "Rule":
        return self


class Rules(object):
    def __init__(self, world: "D3DWorld"):
        player = world.player

        self.true = RuleTrue()
        self.false = RuleFalse()

        class HasRule(Rule):
            def __init__(self, prop: str):
                self.prop = prop

            def __call__(self, state: CollectionState) -> bool:
                # something based on world, whatever
                return state.has(self.prop, player)

        self.has = HasRule

        class HasGroupRule(Rule):
            def __init__(self, prop: str):
                self.prop = prop

            def __call__(self, state: CollectionState) -> bool:
                # something based on world, whatever
                return state.has_group(self.prop, player)

        self.has_group = HasGroupRule

        class CountRule(Rule):
            def __init__(self, prop: str, count: int):
                self.prop = prop
                self.count = count

            def __call__(self, state: CollectionState) -> bool:
                # something based on world, whatever
                return state.has(self.prop, player, self.count)

        self.count = CountRule

        class CountGroupRule(Rule):
            def __init__(self, prop: str, count: int):
                self.prop = prop
                self.count = count

            def __call__(self, state: CollectionState) -> bool:
                # something based on world, whatever
                return state.has_group(self.prop, player, self.count)

        self.count_group = CountGroupRule

        if world.get_option("unlock_abilities"):
            self.can_jump = HasRule("Jump")
            self.can_crouch = HasRule("Crouch")
            self.can_dive = (
                HasRule("Dive")
                | HasRule("Scuba Gear")
                | HasRule("Progressive Scuba Gear")
            )
            self.can_sprint = HasRule("Sprint")
        else:
            self.can_jump = self.true
            self.can_crouch = self.true
            self.can_sprint = self.true
            self.can_dive = self.true
        self.can_shrink = (
            self.true
        )  # Might make this an ability at some point, a bit narrow in scope

        class CanJetPack(Rule):
            def __init__(self, fuel: int):
                self.fuel = fuel
                self.required = math.ceil(
                    self.fuel / float(world.fuel_per_pickup["Jetpack"])
                )

            def __call__(self, state: CollectionState) -> bool:
                return state.has("Jetpack", player) and state.has_group(
                    "Jetpack", player, self.required
                )

        self.jetpack = CanJetPack

        self.jump = self.can_jump | self.jetpack(50)
        """Any simple jump sequence that doesn't consume a lot of jetpack"""

        class CanDiveTo(Rule):
            def __init__(self, fuel: int):
                self.fuel = fuel
                self.required = math.ceil(
                    self.fuel / float(world.fuel_per_pickup["Scuba Gear"])
                )

            def __call__(self, state: CollectionState) -> bool:
                return state.has_group("Scuba Gear", player, self.required)

        if world.get_option("unlock_abilities"):
            self.dive = lambda fuel: self.can_dive & CanDiveTo(fuel)
            """For chained sequences of dives, where scuba capacity matters for accessibility"""
        else:
            self.dive = lambda x: self.true

        class Difficulty(Rule):
            difficulty_map = {"easy": 0, "medium": 1, "hard": 2, "extreme": 3}

            def __init__(self, difficulty: str):
                self.difficulty = difficulty

            def __call__(self, state: CollectionState) -> bool:
                return self.difficulty_map.get(self.difficulty, 0) <= world.get_option(
                    "difficulty"
                )

        self.difficulty = Difficulty

        self.explosives = self.has_group("Explosives")
        # This is technically not correct because some of them provide more capacity, so this is stricter than it
        # needs to be for now, ToDo
        self.explosives_count = lambda count: self.count_group("Explosives", count)

        # Glitched logic stuff
        if world.get_option("glitch_logic"):
            self.glitched = RuleTrue()
        else:
            self.glitched = RuleFalse()
        # Most clips require run speed
        self.crouch_jump = (
            self.glitched & self.can_jump & self.can_crouch & self.can_sprint
        )

        # General Stuff
        self.level = lambda level_cls: HasRule(level_cls.unlock)
