# Game Jackpot

> [!CAUTION]
> This is for educational purposes only and should not be used as an instrument to cheat people!

Certainly, there are many ways in which today's machines can be programmed to produce desired results in advance, and before you is one of them.
Let's suppose that you are the owner of the slot machine "Jackpot" and you want the players, buying chips or paying with a card, to try to play for as long as possible so that the amount you would have to pay out in the case of "7 7 7" or "Jackpot" would be far less than the amount they spend until the moment of payment.
Let's say that the "Jackpot" is 50 of something (dollars, euros...) and you want only after the players have spent chips worth 100 (each chip is worth 10) to allow them to get the "Jackpot"

How to do that?

For example, here is a Python code [Complete Python code](GUI_jack_pot.py)

With the help of the Python "random choices()" method, 2 procedures can be used:
1. when 2 lists of symbols are used (here we are using words instead of symbols), one of which is incomplete (there is no one `7` so "Jackpot" cannot happen at all)

``` py
complete = ['watermelon', 'watermelon', 'watermelon', 'cherry', 'cherry', 'cherry',
            'grapes', 'grapes', 'grapes', 'plum', 'plum', 'plum', 'diamond', 'diamond',
            'diamond', 'lemon', 'lemon', 'lemon', '7', '7', '7']

without = ['watermelon', 'watermelon', 'watermelon', 'cherry', 'cherry', 'cherry',
            'grapes', 'grapes', 'grapes', 'plum', 'plum', 'plum', 'diamond', 'diamond',
            'diamond', 'lemon', 'lemon', 'lemon', '7', '7']
```

or

2. and the second one using the **`weights`** parameter in `random.choices()` method, which is a list where you can weigh the possibility of each value

``` py
result = random.choices(complete, weights= [25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25, 25, 25, 1], k=3)
```

here one `7` has 25 times less weight than the others (including the remaining two `7`)

> [!NOTE]
> A "Jackpot" can theoretically happen here (2.), but depending on how much weight you give to each symbol individually, the probability of getting a "Jackpot" is almost impossible

> [!NOTE]
> Given Python code works in such a way that after ten attempts the probability of winning the "Jackpot" is huge and certain in every subsequent attempt.
> This is just an indication of how the **weights** of individual elements in the list affect the probability of the outcome

> [!NOTE]
> Additional code clarifications:
> 1. `attempt = 10` this is the value of a chip, of course, it can be changed as desired
> 2. `if attempt < 100:` this is the amount of money before the slot machine owner doesn't want to pay the player,  **100** can be changed as desired
> 3. `start_button.config(state=tk.DISABLED)` the game stops in case the "Jackpot" has been won and the button can be used further
