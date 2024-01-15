### Introduction to AI
#### Assignment 1 : Getting started

##### Due: Wed Sept 6, 2023 at start of class.

##### 100 points.

Note: please make sure that your name is someplace in your assignment! This is especially true if it's not obvious from your GitHub handle.

To turn in: please submit everything to your github repo. For the written portion of the assignment, please add a document to your repository, as PDF, containing the answers to these questions.


##### Question 1: Environments. (10 points - 2 points each)

a) What does it mean for an environment to be stochastic? Please give an example of an environment that is stochastic, and one that is deterministic, and explain the difference.

b) What does it mean for an environment to be partially observable? Please give an example of an environment that is fully observable, an environment that is partially observable, and explain the difference.

c) What does it mean for an environment to be sequential? Please give an example of an environment that is episodic and an environment that is sequential, and explain the difference.

d) What does it mean for an environment to be dynamic? Please give an example of an environment that is static, an environment that is dynamic, and explain the difference. 

e) What does it mean for an environment to be online? Please give an example of environment that is offline, an environment that is online, and explain the difference.

##### Question 2: Approach. (20 points)

A common technique for estimation of complex problems is Monte Carlo simulation. It's also our first exposure to <i> generative</i> algorithms, which are algorithms that
can generate novel data from a distribution. We'll use it here to try to estimate 
an optimal stopping point (or policy) for a simple dice game, called approach. This will also give you some practice with Python.

Approach works like this: There are two players, and they choose a target number (n).
Player 1 repeatedly rolls a six-sided die and adds up their total. 
Whenever they want, they can "hold." Then player 2 must roll. Their goal is 
to beat (not tie) player 1's score without going past n. The problem we want to solve is this:

For player 1, for a given n and a particular total so far (called s) should they: 
'hold' (action 1) or 'roll' (action 2).

To figure this out, we'll try to estimate the probability of winning for each possible hold value. Then we can just choose the one with the highest probability.

(note that player 2's strategy in this game is pretty boring - they just roll until they either beat player 1's score or exceed n.)

I've provided the beginnings of this program for you. 
It should: take as input a limit n.:
  For all values from n-5:n, estimate the probability of winning, given that we use that value as our 'hold' value.

For example, if n=10, you might see:
<pre>
monte_carlo_approach(10)
5: 0.255314
6: 0.360087
7: 0.431315
8: 0.435367
9: 0.371685
10: 0.205657
</pre>

Since our probability of winning is highest when hold=8, we should roll when we're at 7 or lower, and hold on 8, 9 or 10.

To estimate these probabilities, we'll play the game 1000000 times for each possible hold. 
A round of the game works like this:
   - player 1 sets their hold value. They then 'roll the die' (generate a random int between 1 and 6) and add to their score until:
     - They exceed n, in which case they lose.
     - Their total is >= to their hold value, and less than n. In this case player 2 goes.
       - Player 2 rolls until their total either:
         - Exceeds player 1, but is less than or equal to n. Player 1 loses.
         - Exceeds n. Player 1 wins.
         
 
##### Question 3 (10 points): Blackjack

Now that we understand how to do Monte Carlo simulation, let's extend it to a harder domain, namely Blackjack.

If you don't know the game Blackjack, you can read the description [here:](https://en.wikipedia.org/wiki/Blackjack)

[This page](https://gymnasium.farama.org/environments/toy_text/blackjack/#blackjack) from gymnasium might also help - 
we'll see this again later in the semester.


Our state space, or win table, is much larger now. Rather than just having a single
value to consider, we have three values: our total, the dealer's visible total, and a boolean
indicating whether we have an ace:

e.g. (16, 5, 0) would indicate that we have a total of 16 in our hand, the dealer has a 5 visible (we don't know what's hidden), and we do not have an ace. (The environment is partially observable!)

We'll stick to the situation where the dealer follows a strict rule - they 'hit'
(or take another card) at 16 or lower, and 'stick' (or stop taking cards) at 17 or above.
We will leave out betting, splitting, and other complexities. We'll have two participants: a player and a dealer.
The player goes first, and draws cards until they 'bust' or choose to hold. Then the dealer goes.

As in the gymnasium implementation, we will keep things simple by assuming that the
deck is infinitely large, with replacement, so we don't need to keep track of the cards
that have already been played. (in probability terms, our observations are independent.)

I've provided a framework for you - you fill in the blanks. As you're doing so, think about efficiency; how can you avoid
creating extra objects or making copies? Are you doing unnecessary loops or creating extra data structures?
We'll think about that more as the semester goes on.

I've also provided a simple unit test for you to test the get_total() method. Feel free to extend this as much as you want! 
We'll look more at unit testing in Python later in the semester.

Once you have these both working, take a step back and think about what they are telling us. For any given outcome, we have an estimate of the probability of winning if we hold. This lets us choose the best action for any state. We'll call this a **policy**.


##### Question 4 (20 points): Word frequencies. 

One of the primary domains we'll  work with this semester is text. The most common approach to dealing with
  large bodies of text is statistical, which requires counting the number of words in a document.

wc.py gives you a starting point for a program that will read words from a file and construct a frequency distribution. This question will let you explore the Python standard library and extend it. 

Please add the following features - 
you may need to explore the Python documentation a little to figure these out.

1. The way we're processing command-line args is icky. Please replace this with the [argparse module](https://docs.python.org/3/library/argparse.html).

2. The current wc.py will only process a single file. Fix it to be able to take as input a directory name or path and call wc for all files in that directory, or subdirectories. (look at [os.walk()](https://docs.python.org/3/library/os.html) to see how to do this.)

3. Add a '--load=pickleFile' argument and a --save=pickleFile. If these are present, read or write (or both) the freqency distribution from the file indicated by 'pickleFile' using [pickle](https://docs.python.org/3/library/pickle.html).
4. 
   If the '-s' argument is present, print the words in order of increasing frequency.


##### Question 4 (20 points): Intro to Pandas. 

This problem will give you some experience working with Pandas. Please add a file called pandasExercise.py to your repo containing this part.

First, read through [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html#min). There's a ton of other useful documentation of the pandas site as well.

The rest of these exercises use [The Pandas Cookbook](https://github.com/jvns/pandas-cookbook).
We'll also use the breast cancer dataset included in the GitHub repo. This is a classic ML dataset originally from the [UCI ML data repository](https://archive.ics.uci.edu/ml/index.php).

a) read Chapter 1.  Then, write a function that will read in the breast cancer dataset.

b) read Chapter 2. Then, write a function that determines the most common classification for the breast cancer data. (either 'recurrence-events' or 'no-recurrence-events')

c) read Chapter 3. Then write a function that determines the most common value for age and menopause for patients with recurrences?

d) Read Chapter 4. Write a function that plots the number of recurrences for each age group.

##### Question 6 (20 points): Detecting Intelligence. 

Large Language Models, or LLMs, have had a massive impact both on the field of AI and on culture more broadly since their introduction a few years ago.

For this question, we'll consider three of the most well-known LLMS:

- [ChatGPT](https://chat.openai.com/auth/login) from OpenAI.</li>
- [Bard](https://bard.google.com/) from Google </li>
- [Claude](https://claude.ai/login) from Anthropic. </li>

You will need to create accounts for each of these, but should not need to sign up for any paid services.

Choose one of the environment questions from question 1, and paste it into each of the three LLMs, and provide their responses.
Are they correct? How do they differ? Can you distinguish between your answer and an LLM?

Now pick one of the LLMs and craft a prompt in which you give it the original question, your answer, and an answer from one of the other LLMs, and ask it to determine which answer was written by a human and why. Does it get the answer right?

 Include a copy of your prompt and the LLM's reply. 

##### Question 7: (Grad Students only):  

A classic thought experiment in response to the Turing Test is the Chinese Room, proposed by John Searle.
To begin, please read [this webpage](https://mind.ilstu.edu/curriculum/searle_chinese_room/searle_chinese_room.html), which presents the Chinese Room thought experiment, intended to show that a computer can manipulate symbols to produce replies without understanding what they mean.

Then, read section 2 (Replies and Rejoinders) of [this page](https://iep.utm.edu/chineser/), which summarizes many of the responses to the Chinese Room argument.

a) Summarize the Chinese Room argument.

b) What does this have to do with computers? 

c) Why does Searle believe that it shows that a computer can pass the Turing test without understanding?

d) Do you find Searle's argument convincing? Or do you find one of the responses more appealing? Explain your position. 

