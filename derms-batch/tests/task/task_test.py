from decimal import Decimal
from typing import Dict, Any
import unittest
from unittest.mock import Mock, call
from task.task import calculate_point


class TestTaskDeliveryDrHistoryByUser(unittest.TestCase):

    def test_calculate_point_round_up(self):
        result = calculate_point(Decimal('100'), 2)
        self.assertEqual(result, Decimal('100'))

    def test_calculate_point_no_rounding_needed(self):
        result = calculate_point(Decimal('2.0'), 10)
        self.assertEqual(result, Decimal('200'))

    def test_calculate_point_round_up_edge_case(self):
        result = calculate_point(Decimal('1.1'), 10)
        self.assertEqual(result, Decimal('11'))

    def test_calculate_point_zero_usage(self):
        result = calculate_point(Decimal('0'), 10)
        self.assertEqual(result, Decimal('0'))

    def test_calculate_point_negative_usage(self):
        result = calculate_point(Decimal('-1.5'), 10)
        self.assertEqual(result, Decimal('-15'))

if __name__ == '__main__':
    unittest.main()
