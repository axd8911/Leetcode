## 03/20/2019
Due to the work load of ME interviews, I do more easy questions these days.
### 136 Single Number:
  You may choose either less memory, or shorter run time. Hard to get both. Leetcode has a few solutions and it may worth to take a look, especially for the hash table one, and the logic relation one.
### 017 Letter Combination of a Phone Number:
  May check if others have anything faster than O(n**3)  

## 03/21/2019
### 049 Group Anagram:
  Spent a lot of time on comparing letter by letter in strings, while finally figured out that it can be easily solved by dictionary. Each dict key is the sorted string. Then output is the list of values for each key.
### 048 Rotate Image:
  Assign some value to a variable: assign the value itself or assign the memory location?
  One line to loop over lists in list
  Sometimes it is useful to calculate the first few items in hand writing and then try to find the rule or equaion for bigger set.
  Another solution uses zip command in Python. Should learn about how to use it.

## 03/22/2019
Did an interview with Facebook in hardware development

## 03/23/3019
No update. Did some heavy house work.

## 03/24/2019
### 070 Climbing Stairs
  It is a fibonacci list. Like what I found in 048, it is useful to calculate the first few items and find the rules.
  Later, it may be useful to try dynamic programming

## 03/25/2019
Started CC189 study
### 961 N-Repeated Element in Size 2N Array
  Not so challenge. a easy question. Easier than what the question describes.

## 03/27/2019
### 066 Plus One
  An easy one. Not much to add.

## 03/30/2019
### 021 Merge Two Sorted Lists
  Useful to understand linked list
  Could do it shorter, see the 5 line python solution in leetcode.

## 03/31/2019
### 028 Implement strStr()
  Another easy question. Pay attention to the concer cases.

## 04/08/2019
### 141 Linked List Cycle
  Another easy question
### 023 Merge k Sorted Lists
  A good practice for linked list address allocation and exchange.
  Sometimes it may be helpful to jump out of a fixed frame. For example, list in this problem will be very helpful.
### 024 Swap Nodes in Pairs
  A good practice for linked list address allocation and exchange. Should repeat it and do some similar ones soon.

## 04/22/2019
### 127 Word Ladder
  BFS question. Needs to pay attention to the defaultdict function.
  Think further about which way is more efficient, when facing with some tedious logic.

## 05/04/2019
### 043 Multiply Strings
  A strange problem. Multiply digit by digit and add them up.

## 05/05/2019
### 034	Find First and Last Position of Element in Sorted Array
  Binary search. Try to be more proficient in binary search
### 038 Count and Say
  Normal string problem. Be more careful with boundary conditions
### 046 Permutations
  Similar to 017. It is a backtracking problem. I did not use recursive way, but rescursion should definitely be practised.

## 05/10/2019
### 033 Search in Rotated Sorted Array
  Form a way to do binary search and repeat the way.
  Duplicate the data then do operate. Using pointers and movers is not so efficient.

## 05/11/2019
  Try to understand shallow copy and deep copy!!
  Try to understand shallow copy and deep copy!!
  Try to understand shallow copy and deep copy!!
### 039 Combination Sum
  Backtracking. Very typical question. Should try to deeply understand the circles. Make the circles and loops clear.

## 07/30/2019
### 310 Minimum Height Trees
To be learning the better idea.
### 417 Pacific Atlantic Water Flow
It is BFS. Sometimes if it is hard to solve a problem in normal order, reserve it and think it from backend.


## 08/02/2019
### 079 Word search
Backtracking
There is one way to mark a item you visited: create a set or create a visited list
There is another way: visit it, then change the value, so that later comers cannot find it -- change it back in time if it is still needed in the future.

## 08/03/2019
1st round done with BFS. More harder problems to go.

## 08/04/2019
Start of Greedy algorithm
### 435 Non-overlapping interval
Sort by end so that early item does not impact later ones

### 452 Minimum number of Arrows to burst balloons
Almost the same as 435. As far as it does not go exceed end point, items can be treated the same way.

## 08/05/2019
### 714 Best Time to buy and sell stock with transaction fee
### 309 Best Time to buy and sell stock with cooldown
These stock problems are really a lot of fun. Make clear the dynamic programming in status of each node.

## 08/06/2019
Backtracking
### 526 Beautiful Arrangement
Try to change a direction and see if it can be done faster

## 08/07/2019
Some crucial points in backtracking:
1. When should I use FOR LOOP in backtracking function
2. how to control the flow in Backtracking
3. when should I use self.var when var is an external variable to be used in a function?
4. when to use 'return' and when not to, in a if condition in function
    return means that we are executing for loop and now the for loop finished this and is going next
    typical question 017 letter combinations of a phone number
5. time complexity calculation

## 08/08/2019
Start going through DFS. Make it!!!
### 394 Decode strings
DFS and stack, both works.
isdigit() tells whether a string is all made of numbers

### 473 Matchsticks to Square
DFS: recursion: how to stop it and return the value?
Got it but TLE.
A solution with Python is available. Some DFS thoughts are really amazing. Thinking about a quesiton smartly.

### 494 Target Sum
DFS or DP. It is important to judge which makes the question easier before starting the implementation.
Now i am reviewing DFS, but obviously this question can be solved by DP much easier.
When list takes too long, use dict.
When we need count of some item, use dict instead of list. Are we going to count the amount in the list? No!

## 08/11/2019
Still unsure about DFS return values. Others are fine, needing more practices.
Starting heap
### 974 Subarray Sums Divisible by K
what a amazing prefix sum question. It is the reason that we need to refer to solutions instead of struggling all by ourselves.

### 313 Super ugly number
Now this is a heap question. Pop the smallest number from a list each time.
Knowledge I need to enhance: heap functions, map(), generator, yield

## 08/12/2019
Today let me start the second round of leetcode - following appearance frequency. Expect at least 10 per day.
A summary is needed for each question, with the following bullets.
- my code in another file
- the algorithm I used (could be multiple). The time and space complexity.
- some new coding techs I learned from solutions.
- If I looked at the solution first, mark it.
- If there are extended quesitons, think about them.

a few rules, try to follow
- Try to inspect the code and be bug free, even before submitting
- Come up with test cases all by yourself
- Use English to write down the thoughts
- Use the write board itself to do the draft calculation
- Time is valuable. Think about a question in limited time, if no ideas come up, read solutions. Easy: 10 min, medium: 15min, hard: 25min. Finish a problem in at most 1 hour!!!

### 001 Two sum
- hash table
- time O(N), space O(N)
- new tech or new learn: throw exception
```python
raise Exception('No matches')
```

### 002 Add two numbers
- linked list, basic math
- time O(N), space O(N)
- new tech or new learn: when we are creating a linked list or other node, we need a backup which keeps at the initial node.

### 005 Longest Palindromic Substring
- The solution is amazing. tracking the string until we find the palindromic part, then track the part and see how long it is. if another palindromic part appears, start tracking when its length is standing out.
- time O(N^2),space O(1)
- new tech or new learn:
    1. I was trying to finish one step when seeing different items. It is possible that I can only find same items till the end. As a result, I may not be able to get a wanted values
    2. in a for loop, if not sure about edge, draw it on a paper. Very easy to make mistakes here.
- I saw solutions for the fastest algorithm

## 08/13/2019
### 004 Median of Two Sorted Arrays
- binary search. Constant amount of values should be in front of the median. The approach is to locate the position where we should split into 'front' and 'end'. Binary search such a Position
- time O(log(m+n)), space O(1)
- new tech or new learn: Try to control pointers: start, end, mid, when to break
- I saw solutions for the fastest algorithm

### 200 Number of Islands
- DFS using recursion or stack
- time O(mn), space O(mn)
- new tech or new learn: instead of using a 'visited' matrix, you can also change the cell, if they will not be used in the future. It can save space.

### 042 Trapping Rain Water
- two pointers: left and right work together to collect water
- time O(n),spaceO(1)
- I saw solutions for the fastest algorithm

### 003 Longest Substring without Repeating Characters
- hashmap: save appeared letter in hashmap and search for it in the future. If it appeared before refresh, fine. Else, do refresh.
- Time O(n), space O(n)

### 015 3Sum
- Two pointers: skip repeated items in time, jump out when rest no longer meets requirement
- Time O(n^2), space O(1)
- I saw solutions for some extra if conditions to optimize the computing

### 053 Maximum Subarray
- Mathematics
- time O(n), space O(1)

### 021 Merge Two Sorted Lists
- Linked list
- time O(n), space O(n)
- Do not forget how to implement a linked list or a list node.

### 023 Merge k Sorted Lists
- Heap
- time O(Nlogk), space O(N) ???
- new tech or new learn: Memorize the time complexity of heap functions

### 273 Integer to English Words
- Play with strings
- time O(N), space O(1)

## 08/14/2019
### 056 Merge Intervals
- Sorting: based on small end. There is another intervals question 435, sorting based on big end.
- time O(NlogN), space O(N) or O(1)

### 206 Reverse Linked List
- linked list, recursion
- time O(N), space O(1)
- Linked list: very careful about the nodes assigning.
- I saw solution for this question. Memorize the recursion please.

### 020 Valid Parentheses
- Stack. Remember to delete element after comparison
- time O(N), space O(N)

### 301 Remove Invalid Parentheses
- String. Could be done in DFS
- time O(2^N), space O(N)

### 937 Reorder Log Files
- String
- time O(NlogN), space O(N)

### 007 Reverse Integer
- Digit
- time O(logN), space O(1)
- New tech or new learn: signed 32 digits integer: [-2**31,2**31-1]

## 08/15/2019
### 076 Minimum Window Substring
- Two pointer: keep a record when the window just matches our needs
- time O(S+T), space O(S+T)
- New tech or new learn
    1. collections.defaultdict(int) - a dictionary, if you call a key which is not defined, it will be assigned a default value. value type defined in the bracket
- I saw solution for the fastest algorithm

### 033 Search in Rorated Sorted Array
- Binary Search
- time O(logN), space O(1)
- New tech or new learn
    1. binary search in this question:
    ```python
        while start <= end:
            mid = (start + end) // 2
            if some condition:
                return output
            if (matched item is in left):
                end -= 1
            else:
                start += 1
    ```

### 121 Best Time to Buy and Sell Stock
- Dynamic programming
- time O(N), space O(1)
- New tech or new learn: max() or min() is slower than if a>largest: largest = a.

### 238 Product of Array Except Self
- Dynamic programming
- time O(N), space O(1)
- New tech or new learn: sometimes there is no need to track whole list, only 1 unit of space is needed for a single number

### 022 Generate Parentheses
- backtracking
- time O(), space O() - so complicated please refer to CC189 time complexity

### 011 Container with Most Water
- Two pointer
- time O(N), space O(1)

### 049 Group Anagrams
- hashmap
- time O(Nklogk), space O(Nk)

### 771 Jewels and Stones
- hashmap
- time O(N), space O(N)

##08/16/2019
### 560 Subarray Sum Equals K
- Prefix sum, hashmap
- time O(N), space O(N)

### 010 Regular Expression Matching
- Dynamic programming
- time O(TP), space O(TP)
- Know how to implement dp and recursion both. Although dp is much faster

### 289 Game of Life
- Array
- time O(MN), space O(1)
- change the local value for convenience

### 79 Word search
- DFS
- time O(MN*4^s), space O(1)

### 88 Merge Sorted Array
- Array: do it smartly - if you work from back side,there is no need to pop and insert
- time O(N), space O(1)

### 336 Palindrome Pairs
- hashmap
- time O(N*k^2), space O(Nk)
- New tech or new learn
    1. key of this question is split the string. As palindrome, it has to have some part PLD itself, and other part PLF other string.
    2. It seems this can be done in Trie.

### 031 Next Permutation
- Array - know how permutation is created - 355421 --> 412355
- time O(N), space O(1)
- new tech or new learn:
    1. binary search:
    ```python
    while start<=end:
        mid = (start+end)//2
        if (some conditions):
            (mid is /*what you need)
            break
        if some conditions:
            start = mid + 1
        else:
            end = mid - 1

    ```

### 054 Spiral Matrix
- Array - a way to cut a matrix through margin
- time O(MN), space O(MN)

### 046 Permutation
- backtracking
- time O(N!), space O(N!)

### 215 Kth_Largest_Element_in_an_Array.py
- heap
- time O(klogN), space O(n)

##08/17/2019
### 811 Subdomain Visit Count
- String
- time O(N), space O(N)

### 013 Roman to integer
- Hashmap
- time O(N), space O(1)

### 068 Text Justification
- Array
- time O(Nk), space O(N)

## 08/18/2019
### 394 Decode String
- Array: please clearly discuss the possible situations and their operations
- time O(N), space O(N)

### 17 Letter Combinations of a Phone number
- backtracking
- time O(3^N), space O(3^N)

### 332 Reconstruct Itinerary
- directed graph
- time O(N), space O(N)
- I saw solution for this question: convert graph to tree and do a post traverse

### 344 Reverse String
- Array
- time O(N), space O(1)

### 91 Decode Ways
- Dynamic Programming
- time O(N), space O(1)

## 08/19/2019
### 138 Copy List with Random Pointer
- Linked list, hashmap
- time O(N), space O(N)

### 139 Word Break
- Dynamic Programming, Backtracking
- time O(Nk), space O(N)
- I saw solutions for this question

### 008 String to integer
- Array
- time O(N), space O(N)
- new tech or new learn:
    1. ```python string.strip()  ``` remove start and end spaces or other characters specified in ()
    2. ```python number.bit_length()``` show the bit length of a number


## skipped questions
253 (prime), 146 (to do), 297 (to do), 380 (to do), 295 (to do), 269 (prime), 410 (to do)


## Summarize a good binary search method
### 4, 33

## Summarize a way to return value accurately from recursion/DFS/backtracking
### 79,10

## repeat these questions.
### 10, 37, 79, 473, 974, 5, 4, 42, 206,33,76
