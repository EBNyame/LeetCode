# def report(name_and_score):
#     name_and_score = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())

#         name_and_score.append([name, score])

#         scores = []
#         for i in range(len(name_and_score)):
#             scores += name_and_score[i][1]
        
#         set_scores = set(scores)
#         sort_set_scores = sorted(set_scores)

#         second_lowest = 0
#         for i in range(len(sort_set_scores)):
#             if sort_set_scores[i] < sort_set_scores[i + 1]:
#                 second_lowest += sort_set_scores[i + 1] 
#                 break

#         people_with_second_lowest = []
#         for i in range(len(name_and_score)):
#             for second_lowest in name_and_score:
#                 people_with_second_lowest.append(name_and_score[i][0])

#         people_with_second_lowest.sort()


nums = [1, 3, 4, 6, 7, 7, 7 ,6 ,6, 7]
m = max(nums)
x = nums.index(m)

for i in range(4, 7):
    if nums[i] == 7:
        print(nums[i])
        continue
