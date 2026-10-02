# Reflection
In this assignment I learned about data lineage, which means a pipeline step should add new columns and never change or delete the old ones. To do that, each step uses copy-add-return: make a .copy() of the DataFrame, add a column, and return it. I wrote element functions like parse_hours that turn one messy value into a number, and I used Series.apply to run them down a column. If a value can't be read, I coerce it to 0.0 so the program doesn't crash. The hardest part for me was the merge. The two files have different grain, and I had to pick a left merge so that every timesheet row stays, even when an employee_id like E099 isn't on the roster. Those rows get NaN, so I check for them with pd.isna(). I'm still confused about when to use row apply with axis=1 and when to use Series.apply. Next, I will practice writing a few merges and a row apply on my own.

## Instructions

Reflections are a metcognitive activity where you are encouraged to think about your own thinking. It helps you build a strong understanding of your own learning. A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, think about what you did and share your thoughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Write your reflection in the file code/reflection.txt ---`
In this assignment I learned about data lineage, which means a pipeline step should add new columns and never change or delete the old ones. To do that, each step uses copy-add-return: make a .copy() of the DataFrame, add a column, and return it. I wrote element functions like parse_hours that turn one messy value into a number, and I used Series.apply to run them down a column. If a value can't be read, I coerce it to 0.0 so the program doesn't crash. The hardest part for me was the merge. The two files have different grain, and I had to pick a left merge so that every timesheet row stays, even when an employee_id like E099 isn't on the roster. Those rows get NaN, so I check for them with pd.isna(). I'm still confused about when to use row apply with axis=1 and when to use Series.apply. Next, I will practice writing a few merges and a row apply on my own.