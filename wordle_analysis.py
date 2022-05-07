from wordle import Wordle, WordTracker
import random


def play_game(wordlist, word=None, debug=True):
    """Function to play a wordle game

    :param wordlist:
    :return:
    """
    if not word:
        word = wordlist[random.randint(0, len(wordlist)-1)]
    if debug:
        print(f"Playing with {word} against a list of {len(wordlist)}")


    # TODO: validate word is in the wordlist
    game = Wordle(word)
    tracker = WordTracker(wordlist=wordlist)

    for i in range(6):
        guess_list = tracker.get_current_list()
        wordcount = len(guess_list)
        guess = guess_list[random.randint(0, wordcount-1)]
        result = game.guess(guess)
        if result == [2,2,2,2,2]:
            if debug:
                print(f"We have a winner after {game.attempt} attempts")
            return game.attempt

        tracker.update_knowledge(guess, result)
        debug and print(f"{guess} {result} reduces us to {tracker.get_current_list_length()}")




            #     elif result[i] == 2 and guess[i] != word[i]:
            #         debug and print(f"\t{i}: {guess[i]} {result[i]} not in correct position: {word}")
            #         new_guess_list.remove(word)
            #         next(word)
            #     else:
            #         print(f"\t{i}: {guess[i]} {result[i]} still checking {word}")

        # guess_list = list(new_guess_list)
        # debug and print(f"Removed {old_list_len - len(guess_list)}")
        # debug and print(guess_list)






def main():
    with open("words") as fp:
        words = fp.read().splitlines()

    random.seed(10)

    attempt_count = play_game(words, words[random.randint(0, len(words)-1)])
    print(f"Solution found in {attempt_count}")
    return attempt_count

    random_word = words[random.randint(0, wordcount-1)]
    print(random_word)

    game = Wordle(random_word)
    guess_list = words
    for i in range(6):
        wordcount = len(guess_list)
        guess = guess_list[random.randint(0, wordcount-1)]
        result = game.guess(guess)

        print(f"Guess {i+1} {guess} {result} out of {len(guess_list)} options")
        # Let's reduce the guess_list.

        # First lets remove all the words with the 0s
        old_list_len = len(guess_list)
        # First the zero words
        for i in range(5):
            for word in guess_list:
                print(f"Analysing {guess}: {word} ", end="")
                if result[i] == 0 and guess[i] in word:
                    print(f"{i}: {guess[i]} {result[i]} not found in {word}")
                    guess_list.remove(word)
                elif result[i] == 2 and guess[i] != word[i]:
                    guess_list.remove(word)



        # for word in guess_list:
        #     print(f"Analysing {word}")
        #     for i in range(5):
        #         if result[i] == 0 and guess[i] not in word:
        #             print(f"{i}: {guess[i]} not found in {word}")
        #             try:
        #                 guess_list.remove(word)
        #             except ValueError:
        #                 print(f"Tried to remove {word} from list - already gone")

        print(f"Removed {old_list_len - len(guess_list)}")
        print(guess_list)





if __name__ == "__main__":
    main()