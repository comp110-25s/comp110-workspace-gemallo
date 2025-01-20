"""Planning a Tea Party """

__author__: str = "730468661"


def main_planner(guests: int) -> none:
    """Main function for planning tea party"""
    return none


def tea_bags(people: int) -> int:
    """Calculates how many tea bags are needed"""
    return 2 * people


def treats(people: int) -> int:
    """Calculates how many treats are needed"""
    return int(1.5 * tea_bags(people))


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost of the tea party based on number of tea bags and treats needed"""
    return 0.5 * tea_count + 0.75 * treat_count
