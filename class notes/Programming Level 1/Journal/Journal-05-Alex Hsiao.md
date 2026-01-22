# Weekly Journal
10 October 2025
Alex Hsiao

## Designing a Function

> In your `work-functions.py` file, create a function that calculates the average of three numbers. Here are the requirements in detail:
>
> * call it `average`
> * it should accept three parameters: `num_one`, `num_two`, and `num_three`
> * it should calculate the average value of the three numbers:
> 	* recall that to calculate the average, you add the values then divide by the number of values you have
> * return the result
>
>  *Optional*: write another version that accepts a list and returns the average of all things inside the list

> Test your function and copy and paste your code in the block below.

```python
print("input three number")
num_one = float(input("1: "))
num_two = float(input("2: "))
num_three = float(input("3: "))
average = float(num_one + num_two + num_three)/3
print(average)

name = input("name: ")
mood = input("mood: ")
if mood.lower().strip("!").strip(".") == "happy":
    print(f"Hey {name}, great to see you smiling!")
elif mood.lower().strip("!").strip(".") == "sad":
    print(f"I hope your day gets better, {name}.")
elif mood.lower().strip("!").strip(".") == "neutral":
    print(f"Sometimes you have average days, {name}.")
else:
    print(f"Hi {name}, hope you're having a good day.")
```


## Typing Data

> Drag and drop your typing screenshots below.

![Screenshot 2025-10-09 at 10.56.58 AM.png](../../_resources/Screenshot%202025-10-09%20at%2010.56.58 AM.png) ![Screenshot 2025-10-09 at 10.46.27 AM.png](../../_resources/Screenshot%202025-10-09%20at%2010.46.27 AM.png) ![Screenshot 2025-10-10 at 12.21.20 PM.png](../../_resources/Screenshot%202025-10-10%20at%2012.21.20 PM.png)

## Using your function

> Use the function that you created above to calculate your average WPM and accuracy. What is your average over your three results?

WPM: 28
accuracy: 96

> What plans do you have this long weekend?

play tennis with friend