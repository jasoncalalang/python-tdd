import unittest
from unittest.mock import MagicMock
from spending_tracker import SpendingTracker
from transaction_repository import TransactionRepository
from notification_service import NotificationService

class TestUnusualSpending(unittest.TestCase):
    def setUp(self):
        self.mock_transaction_repo = MagicMock()
        self.spending_tracker = SpendingTracker(self.mock_transaction_repo)

    def test_detects_increase_in_spending(self):
        # Mock transaction data
        last_month_transactions = [{'amount': 100}, {'amount': 200}]
        this_month_transactions = [{'amount': 300}, {'amount': 400}]
        self.mock_transaction_repo.get_transactions.side_effect = [
            last_month_transactions, this_month_transactions
        ]

        # Analyze spending
        result = self.spending_tracker.analyze_spending(user_id=1, month=6)

        # Expect an increase in spending
        self.assertTrue(result)  # Adjust assertion based on implementation

if __name__ == '__main__':
    unittest.main()

