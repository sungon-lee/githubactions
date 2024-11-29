from decimal import Decimal, ROUND_HALF_UP, ROUND_CEILING

def calculate_point(saving_usage: Decimal, point_per_kwh: int) -> Decimal:
    # 少数点1桁で切り上げ
    point = saving_usage * point_per_kwh
    return point.quantize(Decimal("0"), rounding=ROUND_CEILING)
