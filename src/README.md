Mark43 Poker Assignment
=======================

This is a python3 program that will determine the winner of 3 card poker game given the following inputs example:

```
4
0 Qc Kc 4s
1 Ah 2c Js
2 3h 9h Th
3 Tc 9c 3c
```

where the first input is the number of players and the subsequent inputs are the user id and there cards.

to run this using the run_test.py file, you would use the following line:

```
    python run_tests.py "python ./src/poker.py"

or you can navigate to the src folder and just run

    python run_tests.py "python poker.py"

or to run without run_tests script:

    python poker.py 

then you would provide the input plus an additional enter to indicate the eof
```

# Notes

## OOP Design
I went with a OOP design where I seperated the concepts of players and cards into classes as well as the class for determining the value of a players hand.

I chose this design since it made more sense to encapsulate the data in a more readable way in the case where this would need to be expanded upon or if there are bugs.

I designed the ranking class to be used with any number of cards and not just 3 so that if there was a need to implement other types of poker, the ranking system could still be used and expanded upon to include more hand types.

I also used a enum to map the values for the hand rankings so that it would be easier to add/remove rankings as rules/design changed.

## Limitations
Issues with only using user input in the above form would make expanding the functionality as a whole more difficult, but since the objects are seperated into classes, I would just have to change the parsing functionality to fit whatever input that was used such as json or even a file and the system as a whole would still work correctly.

There could also be issues if a user would enter in unregistered characters that weren't outlined in the original design, such as an diamond emoji instead of the character 'd'
