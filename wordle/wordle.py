class GameSolved(Exception):
    pass


class WordTooLong(Exception):
    pass


class TooManyAttempts(Exception):
    pass


class Wordle():
    locked = False
    solved = False
    attempt = 0

    def __init__(self, word):
        if len(word) != 5:
            raise WordTooLong
        self.answer = word

    def guess(self, guess):
        if self.attempt >= 6:
            raise TooManyAttempts
        if self.solved:
            raise GameSolved

        self.attempt += 1
        report = [0, 0, 0, 0, 0]
        if guess == self.answer:
            self.locked = True
            self.solved = True
            return [2, 2, 2, 2, 2]

        # first see the matching letters
        notinplace = ""
        for i in range(5):
            if guess[i] == self.answer[i]:
                report[i] = 2
            else:
                notinplace = notinplace + self.answer[i]

            # print(f"Not in place: {notinplace} for {guess} {self.answer} {report}")

        # Now to find the letters not correctly placed
        for i in range(5):
            if report[i] == 2:
                continue
            # print(f"checking if {guess[i]} in {notinplace} ", end="")
            if guess[i] in notinplace:
                report[i] = 1
                notinplace = notinplace.replace(guess[i], "", 1)
            # print(report)

        return report
