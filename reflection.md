# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It was simple to start the game-- I just had to type my guess and submit it.  
The first game basically gave me no prolems.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
I could guess numbers not in the range of 1 to 100 (i.e. negatives, 0, over 100).
If I guess a number below 1, it says go lower even though that is not possible.
It would not let me submit guesses after my first full game ended.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude response: "The issue is a Streamlit rendering order problem. The 
st.info(...) display on line 114 renders before the if submit: block runs and 
increments attempts. So in the same pass where you submit a guess, the display
still shows the old value.

The fix is to move the display to after the submit block so it reads the 
already-updated attempts."

This response fixed a bug where the number of attempts didn't decrement at the 
first guess,meaning when I made the max attempts (7), it displayed that I had 1
attempt left instead of 0. I played a couple of games after this fix to verify 
it was addressed.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Claude response: "The attempt_limit for Normal is 8, so attempt_limit - attempts
starts at 8. The simplest fix is to change Normal's limit to 7 so the display, 
the actual attempt count, and game-over all align." 

This was Claude's initial response to the problem I mentioned in the previous 
question. This was misleading as it did not seem to do anything to address the 
attempts not decrementing on the first guess-- this was only a tweak to the 
initial display from 8 guesses to 7. I verified this by playing a couple of 
games and seeing it start at 7 attempts but not decrement at my first guess.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I made sure to play the game checking for each specific bug right after 
implementing a fix, rather than change a bunch of code all at once. Doing it in
a more segmented manner made it easier to identify whether the bug was addressed
as I wanted it to be.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I used Claude to help refactor the helper functions used in test_game_logic.py
from app.py to logic_utils.py to successfully run pytest, as per the test 
summary from when I initially tried to use pytest. This made sense to me since
test_game_logic.py imports logic_utils.py, not app.py, so the functions imported
needed to be declared in logic_utils to make the test file run properly.

- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns re-execute the Python code in its entirety, kind of like 
refreshing a page. The session state seems to be a dictionary that stores
attributes which persist even after reruns (as I could see when I make a new guess;
the program lets me make new guesses but any data that is relevant, such as number of
attempts made, is not reset).

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  It's important to specify in advance what the goal should be from changing the
  code, not just what the error is. That way, I have more control over what the AI
  is suggesting-- rather than making changes that address problems I was not yet
  ready to address, I can specify what I want the end result to be so I do not
  introduce problems or fix something I am not yet ready to address. 

- What is one thing you would do differently next time you work with AI on a coding task?
Seeing as I am prone to error, just as AI is, it may be worth my time to ask AI
to check for errors before I run the program, so I can get an idea of what to 
look out for when testing the program initially.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
Seeing as I was not responsible for writing the pre-fork code, using AI was very
useful for this project as it saved me from having to do a deep analysis of the
files. Instead, I could run the program as normal and use AI to help me address
things I saw, even if I was not sure where to start with resolving an issue.