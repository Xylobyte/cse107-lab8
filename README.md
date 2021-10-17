# CSE107 - Lab 8

This lab plays with writing recursive functions.

## Purpose

### cesaro.py

This program uses recursion to draw a cesaro fractal. Every iteration 
draws a new fractal at each side.

### palindrome.py

This program takes a word as an input and checks if it is a palindrome.
It works by trimming the first and last characters if they are the 
same then passing the word minues them into the function again. This
continues until it's short enough to be true.

### nested.py

This program uses recursion in two functions. Element_of looks at each
element and checks if its the one it's looking for. If it's a list 
it iterated through the list in a new call. Filter_by_depth iterates
though the elements and deletes any lists that are greater than the 
given depth.

## Conclusion

* In this lab I practiced implementing recursion to write functions
  to solve problems that are normally very difficult without it.
* Pair programming aided in giving me an outside look at my code
  and allowed me to ask questions and give help to my partner when
  it was needed.
* I did not work with my buddy on the lab.
* I had some trouble with nested at first where element_of would 
  return false after a nested list instead of continuing to look 
  through the rest of the elements. I fixed it by storing the 
  intermittent call returns and ignoring false one until I have
  reached the end of the first list.
* I think I could improve the way I did cesaro next time. At the 
  moment it decreases the line width too much at higher depths such
  as 6. It makes the fractal very small and hard to see.