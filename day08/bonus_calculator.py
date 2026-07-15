
def bonus_calculator(
        salary: float, 
        bonus_percentage: float = 10
        ) -> float:
    """
    Calculates the bonus amount based on the salary and bonus percentage.
    """
    return salary * (bonus_percentage / 100)

bonus = bonus_calculator(50000)
print(bonus)