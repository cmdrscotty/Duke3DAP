from typing import Callable, Union

from BaseClasses import CollectionState, MultiWorld


class Rule(object):
    def __call__(self, state: CollectionState) -> bool:
        raise NotImplementedError

    def __or__(self, other: "Rule") -> "Rule":
        return LambdaRule(lambda state: self(state) or other(state))

    def __and__(self, other: "Rule") -> "Rule":
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
    def __init__(self, world: MultiWorld, player: int):
        class HasRule(Rule):
            def __init__(self, prop: str):
                self.prop = prop

            def __call__(self, state: CollectionState) -> bool:
                # something based on world, whatever
                return state.has(self.prop, player)

        self.has = HasRule

        class CountRule(Rule):
            def __init__(self, prop: str, count: int):
                self.prop = prop
                self.count = count

            def __call__(self, state: CollectionState) -> bool:
                # something based on world, whatever
                return state.has(self.prop, player, self.count)

        self.count = CountRule

        # ToDo make conditional on world settings if these are even in the pool
        self.can_jump = HasRule("Jump")
        self.can_crouch = HasRule("Crouch")
        self.can_dive = HasRule("Dive")
        self.can_sprint = HasRule("Sprint")

        class CanJetPack(Rule):
            def __init__(self, fuel: int):
                self.fuel = fuel

            def __call__(self, state: CollectionState) -> bool:
                # something based on world, whatever
                return True
                return state.has("Jetpack", 0, self.fuel)

        self.jetpack = CanJetPack

        self.jump = self.can_jump | self.jetpack(50)
        """Any simple jump sequence that doesn't consume a lot of jetpack"""

        class Difficulty(Rule):
            def __init__(self, difficulty: str):
                self.difficulty = difficulty

            def __call__(self, state: CollectionState) -> bool:
                # something based on world, whatever
                return True

        self.difficulty = Difficulty

        self.explosives = self.has("RPG") | self.has("Pipebombs") | self.has("Tripmine")

        # Glitched logic stuff
        self.glitched = RuleFalse()
        # Most clips require run speed
        self.crouch_jump = (
            self.glitched & self.can_jump & self.can_crouch & self.can_sprint
        )

        # General Stuff
        self.level = lambda level_cls: HasRule(level_cls.unlock)
