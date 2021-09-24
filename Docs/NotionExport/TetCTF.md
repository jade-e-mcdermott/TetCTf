# TetCTF

[https://ctftime.org/ctf/290](https://ctftime.org/ctf/290)

[https://ctf.hackemall.live/](https://ctf.hackemall.live/)

Web

HPNY

Get some lucky word or number

Super Calc

Pass in a parameter, `?calc=(stuff)

Clue says "Supports many operations

mysqlimit

A php script?

Interesting include of another php script

[Super Calc](TetCTF/Super%20Calc.md)

[HPNY](TetCTF%20db113441280145068d23d09d9027c4f1/HPNY%205f3683427d514e1cb0e88a5f06dc69d5.md)

[MySQLimit](TetCTF%20db113441280145068d23d09d9027c4f1/MySQLimit%20712a043140fb4e02bda483bda3b688eb.md)

## Takeaways

- Header injection is kind of neat
- This site can be used to fuss around with DB stuff
    - [https://www.db-fiddle.com/](https://www.db-fiddle.com/)
- Ray is a python library for running a bunch of async functions on a cluster. Could be handy.
- hd is a linux utility to get a hex dump
    - `hd *` will dump the binary of everything in the current directory, kind of like cat but with fewer letters
- Putting `/**/` into an sql statement can let you break up a word so it can bypass filters looking for that word specificly. Like so:
    - `SELECT * FROM test UNIO/**/N select 999;`

Decent Writeup on SQLLIMIT challenge

[https://drive.google.com/file/d/1vZEsnFT37qzlsMkfFqaYioxUPepdEpVY/view](https://drive.google.com/file/d/1vZEsnFT37qzlsMkfFqaYioxUPepdEpVY/view)