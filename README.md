## while loops

repeat sets of statements as long as condition true

## dry: Don't repeat yourself

### formula
```python
while (Condition):
  # body

else: # optional
  #body
```python
while(true):
  print ("this statement prints forever")
  ```

### rules

a loop becomes a infinite loop if a condition never becomes
__FALSE__

to avoid a infinite loop make sure to use a variable and keep track of its value

*ex*

```python
counter = 0

while (counter < 3):
  print("inside loop")
  counter+= 1 # counter = counter + 1

print("outside loop")

>inside loop
>inside loop
>inside loop
>outside loop 
