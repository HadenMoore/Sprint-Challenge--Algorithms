#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Another way of writing from  a to n3, increating a by n2 each iteration. Will Always Result in n number of iterations. 
Answer: O(n)


b) There is a For Loop doing n number of iterations, making the time complexity at least O(n). Within that loop, there is a While Loop iterating from j to n each time, increasing by j by a factor of 2 each iteration. Since j is increasing exponentially, increasing n does not increase the number of iterations linearly. *Answer: O(n log n)*


c) This is Recursion that will run and then enter itself n times, resulting in n+1 iterations. Answer: O(n)

## Exercise II
1.) Start from the Middle Floor and Drop the Egg. 
2.) If the Egg Breaks, go to the Floor Between the Current and Top Floor and Drop an Egg. 
3.) If Egg does Not Break, go to the Floor Between Current and Top Floor and Drop an Egg. 
4.) Repeat Step 2 and 3 Until Egg Breaks from Current Floor. 

Formula Loops thorugh Floors untili it finds the Lowest Floor that Breaks the Egg, while the number of floors, n, is divided in half at each iteration. *Answer: Complexity is Log Time, 
or O(log n)*

