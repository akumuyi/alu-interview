Enterprise Web Development: Minimum Operations

# Minimum Operations

## Task Description
In a text file, there is a single character 'H'. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number `n`, the task is to write a method that calculates the fewest number of operations needed to result in exactly `n` 'H' characters in the file.

## Prototype
```python
def minOperations(n)
```

### Returns
An integer representing the minimum number of operations. If `n` is impossible to achieve, the function returns 0.

## Example
```python
n = 9

# Operations:
# H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
# Number of operations: 6
result = minOperations(n)
print("Min number of operations to reach {} characters: {}".format(n, result))
```

## Usage
```python
n = 4
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 12
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
```

## Running the Example
```bash
$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
```
