import unittest

from wordle import Wordle, WordTooLong, GameSolved, TooManyAttempts
from word_tracker import WordTracker

class TestWordle(unittest.TestCase):
    def test_correct_length(self):
        self.assertRaises(WordTooLong, Wordle, "abcdef")

    def setUp(self):
        self.game = Wordle("train")

    def test_basics(self):
        self.assertEqual(self.game.answer, "train")
        self.assertFalse(self.game.locked)
        self.assertFalse(self.game.solved)

    def test_guess_1(self):
        self.assertEqual(self.game.guess("trade"), [2, 2, 2, 0, 0])
        self.assertEqual(self.game.attempt, 1)

    def test_guess_2(self):
        self.assertEqual(self.game.guess("raise"), [1, 1, 1, 0, 0])
        self.assertEqual(self.game.attempt, 1)

    def test_correct_answer(self):
        self.assertEqual(self.game.guess("train"), [2,2,2,2,2])
        self.assertTrue(self.game.solved)
        self.assertTrue(self.game.locked)
        self.assertEqual(self.game.attempt, 1)


    def test_correct_locks_game(self):
        self.game.guess("train")
        self.assertRaises(GameSolved, self.game.guess, "nikau")

    def test_non_unique_letters(self):
        my_game = Wordle("sweet")
        self.assertEqual(my_game.guess("event"), [1, 0, 2, 0, 2])
        self.assertEqual(my_game.guess("ivory"), [0, 0, 0, 0, 0])
        self.assertEqual(my_game.guess("women"), [1, 0, 0, 2, 0])
        self.assertEqual(my_game.guess("eette"), [1, 1, 1, 0, 0])

    def test_too_many_guesses(self):
        wordlist = ["women", "nikau", "swack","feens", "fyles", "poled", "clags"]

        def myfunc():
            for word in wordlist:

                self.game.guess(word)
                print(f"Guessing {word} {self.game.attempt}")
        self.assertRaises(TooManyAttempts, myfunc)

class TestTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = WordTracker('shortlist')
        self.game = Wordle("junta")
        self.totalwords = self.tracker.get_current_list_length()

    def test_get_status(self):
        self.assertEqual(self.tracker.get_status(), {
            "initial": self.totalwords,
            "current": self.totalwords
        })

    def test_get_current_list(self):
        self.assertEqual(self.totalwords, len(self.tracker.get_current_list()))

    def test_update_knowledge(self):
        #### souct, nikau, durra
        myguess = self.game.guess('bindi')
        self.tracker.update_knowledge("bindi", myguess)
        self.assertEqual([
            'acefghijklmnopqrstuvwxyz',
            'acefghijklmnopqrstuvwxyz',
            'n',
            'acefghijklmnopqrstuvwxyz',
            'acefghijklmnopqrstuvwxyz',
        ], self.tracker.currentlyknown)
        self.tracker.update_knowledge("souct",self.game.guess("souct"))
        self.assertEqual([
            'aefghijklmnpqrtuvwxyz',
            'aefghijklmnpqrtuvwxyz',
            'n',
            'aefghijklmnpqrtuvwxyz',
            'aefghijklmnpqruvwxyz',
        ], self.tracker.currentlyknown)
        self.tracker.update_knowledge("agust", self.game.guess("agust"))
        self.assertEqual([
            'efhijklmnpqrtuvwxyz',
            'aefhijklmnpqrtuvwxyz',
            'n',
            'aefhijklmnpqrtuvwxyz',
            'aefhijklmnpqruvwxyz',
        ], self.tracker.currentlyknown)
        self.assertLess(len(self.tracker.get_current_list()), self.totalwords)

    def test_update_knowledge_repeat(self):
        mygame = Wordle("tooth")
        self.tracker.update_knowledge("tweet", mygame.guess("tweet"))
        self.assertEqual([
            't',
            'abcdfghijklmnopqrstuvxyz',
            'abcdfghijklmnopqrstuvxyz',
            'abcdfghijklmnopqrstuvxyz',
            'abcdfghijklmnopqrsuvxyz',
        ], self.tracker.currentlyknown)


if __name__ == '__main__':
    unittest.main()
