# Python side channel attack

This program demonstrates a simple side channel attack on a password validator function. The attacker is able to find the password by timing how long the checker executes. Run the attack with

```bash
$ python attack.py
```

## How it works

By looking at the password validator (in `check.py`), it is clear that a correct password takes longer to check than an incorrect one. That is because the checker short circuits once it knows that the passwords can't match. Thus, the attacker is able to time the execution time of the checker and find a correct password.

The chosen algorithm checks those candidate passwords that take the longest to execute and appends all possible characters at the end. At the end it is faster to just brute force the answer.
