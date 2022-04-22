def taskAssignment(k, tasks):
    result = []
    dictionary = {}
    tasks_length = len(tasks)
    for index, element in enumerate(tasks):
        if element not in dictionary:
            dictionary[element] = [index]
        else:
            array = dictionary[element]
            array.append(index)
            dictionary[element] = array
    tasks.sort()
    i = 0
    while i < (tasks_length // 2):
        j = tasks_length - 1 - i
        smaller_task = tasks[i]
        bigger_task = tasks[j]
        result.append([dictionary[smaller_task].pop(), dictionary[bigger_task].pop()])
        i += 1
    return result


class TaskAssignment:
    k = int(input())
    tasks = list(map(int, input().split()))
    print(taskAssignment(k, tasks))
