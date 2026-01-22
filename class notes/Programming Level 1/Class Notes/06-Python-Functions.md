## Parameters

## `return` values

```python
def some_fun():
	print("hello!")

def some_fun_return() -> str:
	print("hello!")
	return "hello"

return_val = some_fun()

print(return_val) # what's the difference?

return_val = some_fun_return()

print(return_val) # what's the difference?
```

## Default Arguments

```python
# our example from notes-3-functions.py
def say_hello_personal(name: str):
	print(f"hello {name}")
```






