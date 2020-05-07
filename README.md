# MAYLONG-challenge

This contains the solutions of the codechef maylong cahllenge 2020.
be safe and keep coding.


CORUS.py

As a health expert, Vinay is keeping a close watch on the ongoing pandemic of coronavirus disease (COVID-19). He thought of a different situation where there are 26 types of viruses, named "aorona", "borona", "corona", …, "zorona".

You are given a string S with length N. There are N people (numbered 1 through N) and for each valid i, the i-th person is infected by exactly one type of virus named Siorona (i.e. "corona" with the first letter replaced by the i-th character of S).

You should answer Q queries. In each query:

You are given an integer C denoting the number of available isolation centers.
Each isolation center has an infinite capacity, but with the restriction that two people infected with the same type of virus cannot stay in the same isolation center.
There is also a pending queue with an infinite capacity and there are no restrictions on which people can be in the pending queue.
Initially, the isolation centers and pending queue are empty.
Each of the N people should be placed in either the pending queue or one of the isolation centers.
Since Vinay is busy finding a vaccine, he asks Swapnil to find a way to place the people in the pending queue and isolation centers such that the number of people in the pending queue is the smallest possible.
Help Swapnil find the size of the pending queue in that case.

INPUT:-

The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and Q.
The second line contains a single string S.
Each of the following Q lines contains a single integer C describing a query








COVID19.py

There are N people on a street (numbered 1 through N). For simplicity, we'll view them as points on a line. For each valid i, the position of the i-th person is Xi.

It turns out that exactly one of these people is infected with the virus COVID-19, but we do not know which one. The virus will spread from an infected person to a non-infected person whenever the distance between them is at most 2. If we wait long enough, a specific set of people (depending on the person that was infected initially) will become infected; let's call the size of this set the final number of infected people.

Your task is to find the smallest and largest value of the final number of infected people, i.e. this number in the best and in the worst possible scenario.

Input


The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-seperated integers X1,X2,…,XN.


Output


For each test case, print a single line containing two space-separated integers ― the minimum and maximum possible final number of infected people.
