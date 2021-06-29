import sys
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]
s = set()
for a0 in range(k):
    rObstacle,cObstacle = input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    
    s.add((rObstacle, cObstacle))
    
mx = [0, 1, 1, 1, 0, -1, -1, -1]
my = [-1, -1, 0, 1, 1, 1, 0, -1]
ans = 0
for i in range(8):
    cur_y, cur_x = rQueen, cQueen
    while 0 < cur_y <= n and 0 < cur_x <= n:
        if (cur_y, cur_x) not in s:
            ans += 1
        else:
            break
        cur_y += my[i]
        cur_x += mx[i]
    ans -= 1
print (ans)