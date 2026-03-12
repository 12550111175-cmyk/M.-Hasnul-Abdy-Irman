import unittest

from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """Menyiapkan akun contoh sebelum menguji program"""
        # Kita buat akunnya dengan saldo awal 100000
        self.account = BankAccount(owner="Abdy", balance=100000)

    def test_deposit_valid(self):
        """Menguji apakah setor uang (deposit) berhasil mnambah saldo"""
        self.account.deposit(50000)
        self.assertEqual(self.account.get_balance(), 150000)

    def test_withdraw_within_balance(self):
        """Menguji penarikan yang jumlahnya masih dibawah saldo """
        self.account.withdraw(40000)
        self.assertEqual(self.account.get_balance(), 60000)

    def test_withdraw_full_balance(self):
        """Menarik semua saldo menjadi nol"""
        self.account.withdraw(100000)
        self.assertEqual(self.account.get_balance(), 0)

    def test_withdraw_insufficient_funds(self):
        """Menguji penarikan uang yang melebihi saldo"""
        with self.assertRaises(ValueError):
            self.account.withdraw(101000)

    def test_deposit_negative(self):
        """Menguji setor uang dengan angka negatif"""
        with self.assertRaises(ValueError):
             self.account.deposit(-10000)

if __name__ == '__main__':
    unittest.main()