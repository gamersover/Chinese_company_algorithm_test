#coding=UTF-8
'''
定义交换：数组的任意两个数可以进行交换
输入一组数，这组数最小需要经过多少次交换，变为升序排序
思路：比如5 3 1 2 4 3 a
1.首先排序1 2 3 3 4 5 b

2.依次遍历，使用map_li记录a映射到b的信息
  如果a[i] == b[i] 那就不记录，说明不用交换
  map_li = [[5, 1]]
  然后看下一个[b[i], a[i]]时候在map_li中，下一个是3,2不在，则
  map_li = [[5,1], [3,2]]
  再看3 1不在map_li中
  map_li = [[5,1], [3,2], [1,3]]
  再看3 2 在map_li中，则表示存在交换一次就可以得到升序的，则times+1,并在map_li中去掉3,2
  map_li = [[5,1], [1,3]]
  再看4 4 两个值相等，直接进行下一步
  再看5 3 不在map_li中
  map_li = [[5,1], [1,3], [3,5]] 
  最后表示map_li中不存在交换一次就可以得到升序的，则times=len(map_li)-1

'''
def minSwapTimes(arr, n):
    sorted_arr = sorted(arr)
    map_li = []
    times = 0
    for i in range(len(arr)):
      if arr[i] != sorted_arr[i]:
        if len(map_li) == 0:
            map_li.append([arr[i], sorted_arr[i]])
        elif [sorted_arr[i], arr[i]] in map_li:
            times += 1
            map_li.remove([sorted_arr[i], arr[i]])
        else:
            map_li.append([arr[i], sorted_arr[i]])
    times += len(map_li) - 1
    return times

arr = [2,3,3,1,2,3]
print(minSwapTimes(arr, 6))
        
    