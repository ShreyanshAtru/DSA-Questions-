# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/?envType=daily-question&envId=2025-02-07

"""
You are given an integer limit and a 2D array queries of size n x 2.

There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.

Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.

Note that when answering a query, lack of a color will not be considered as a color.

Example 1:

Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]

Output: [1,2,2,3]
"""

def colorBall(queries, limit):
    ballmap = {}
    colormap = {}
    res = []
    for i in range(len(queries)):
        ball = queries[i][0]
        color = queries[i][1]
        # add tha ball in ball map and in color map we'readding color and its count
        # when ballmap is empty
        if ball not in ballmap:
            ballmap[ball] = color
            colormap[color] = colormap.get(color, 0)+1
        # when ball map is have elements 
        #we have to check in colormap if the the same color is exits or not 
        else:
            oldcolor = ballmap.get(ball)
            colormap[oldcolor] = colormap.get(oldcolor)-1
            if colormap.get(oldcolor) == 0:
                del colormap[oldcolor]
            ballmap[ball] = color
            colormap[color] = colormap.get(color, 0)+1
        res.append(len(colormap))
    return res


queries = [[1,4],[2,5],[1,3],[3,4]]
l = 4 # [0,1,2,3,4]
limit = []
for i in range(0,l+1):
    limit.append(i)
print(colorBall(queries, limit))