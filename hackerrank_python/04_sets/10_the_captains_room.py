# Problem: The Captain's Room
# Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem

k = int(input())
rooms = list(map(int, input().split()))

unique_rooms = set(rooms)
captains_room = (sum(unique_rooms) * k - sum(rooms)) // (k - 1)
print(captains_room)
