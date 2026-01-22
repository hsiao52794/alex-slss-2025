# Weekly Journal
23 October 2025
Alex Hsiao

## Recursion

***Please use your brain for these, no LLMs. I'm not looking for right answers, just your answers.***

> There are two things that you need to make a recursive function.
> What are those two things?

use the function when defining the function, will stops

> Why is this a recursive definition?
> 	![From Archive.org](https://web.archive.org/web/20180710012425im_/http://assets.amuniversal.com/d4ec32609f70012f2fe600163e41dd5b)

the result is a part of the definition

> Consider the function below. How many times will it call itself not including the initial function call?
> (It's poorly documented on purpose.)

```python
def some_recursive_function(int):
	if num > 1:
		return num + some_recursive_function(num-1)
	else:
		return 0

result = some_recursive_function(10)
```

8 times

## Closing Questions

![](https://preview.redd.it/recursionquestion-v0-6i9x1wlfyxuf1.jpeg?width=320&crop=smart&auto=webp&s=c64dae05bef67ff2f70c9c449c7c2ddbfc6a17bc)

[I finally understood Recursion.](https://www.reddit.com/r/ProgrammerHumor/comments/12q3kbk/i_finally_understood_recursion/)

> What emoji best describes how you feel in this class this week? Explain why you chose this one.

😵‍💫

> What plans do you have this weekend?

sleep











