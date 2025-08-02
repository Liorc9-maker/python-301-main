# create a unittest suite for the RPG game
import unittest
import main
from actors import Hero, Opponent, SmallOpponent, FinalBoss

class TestRPGGame(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('Link', 42)
        self.small_opponent = SmallOpponent('.docx', 1, is_buggy=True)
        self.opponent = Opponent('Pop-up Ad', 20)
        self.final_boss = FinalBoss('Google Data Center', 500)

    def test_hero_initialization(self):
        self.assertEqual(self.hero.name, 'Link')
        self.assertEqual(self.hero.level, 42)

    def test_small_opponent_initialization(self):
        self.assertEqual(self.small_opponent.name, '.docx')
        self.assertEqual(self.small_opponent.level, 1)
        self.assertTrue(self.small_opponent.is_buggy)

    def test_opponent_initialization(self):
        self.assertEqual(self.opponent.name, 'Pop-up Ad')
        self.assertEqual(self.opponent.level, 20)

    def test_final_boss_initialization(self):
        self.assertEqual(self.final_boss.name, 'Google Data Center')
        self.assertEqual(self.final_boss.level, 500)


if __name__ == '__main__':
    unittest.main()        