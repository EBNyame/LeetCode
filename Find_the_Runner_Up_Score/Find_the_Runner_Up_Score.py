n = int(input())
arr = map(int, input().split())

arr_to_list = list(arr)
arr_to_list.sort(reverse= True)
runner_up = 0
for i in range(len(arr_to_list)):
    if arr_to_list[i + 1] < arr_to_list[i]:
        print(arr_to_list[i + 1])
        break 
