import unittest
import pandas as pd
import os

class TestDataProcessing(unittest.TestCase):
    
    def setUp(self):
        """Set up paths and load data before each test runs."""
        # Using project-relative pathing for portability
        self.data_path = os.path.join("Data", "final_training_data.csv")
        
    def test_target_column_and_values(self):
        """Test 1: Ensure the proxy target variable exists and is strictly binary (0 or 1)."""
        self.assertTrue(os.path.exists(self.data_path), f"Training data file missing at {self.data_path}")
        
        df = pd.read_csv(self.data_path)
        self.assertIn('is_high_risk', df.columns, "Target variable 'is_high_risk' was not integrated successfully.")
        
        # Verify that the labels are only 0 and 1
        unique_values = set(df['is_high_risk'].unique())
        self.assertTrue(unique_values.issubset({0, 1}), f"Found unexpected values in target column: {unique_values}")

    def test_features_are_strictly_numeric(self):
        """Test 2: Ensure that non-numeric categorical strings (like 'UGX') are filtered out of features."""
        df = pd.read_csv(self.data_path)
        
        # Apply your exact feature drop/selection logic from Task 5
        base_drops = ['is_high_risk', 'CustomerId', 'TransactionId', 'BatchId', 
                      'AccountId', 'SubscriptionId', 'TransactionStartTime']
        existing_drops = [c for c in base_drops if c in df.columns]
        X_processed = df.drop(columns=existing_drops).select_dtypes(include=['number'])
        
        # Check that no string/object or category data types remain
        invalid_cols = X_processed.select_dtypes(include=['object', 'category']).columns.tolist()
        self.assertEqual(len(invalid_cols), 0, f"Critical Bug: Non-numeric columns passed type filtering: {invalid_cols}")

if __name__ == '__main__':
    unittest.main()