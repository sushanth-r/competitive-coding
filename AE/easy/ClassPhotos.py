def classPhotos(red_shirt_heights: list, blue_shirt_heights: list):
    red_shirt_heights.sort()
    blue_shirt_heights.sort()
    flag = True
    taller_students = "RED" if red_shirt_heights[0] > blue_shirt_heights[0] else "BLUE"
    for index, temp in enumerate(red_shirt_heights):
        if taller_students == "RED":
            if red_shirt_heights[index] <= blue_shirt_heights[index]:
                flag = False
                break
        else:
            if blue_shirt_heights[index] <= red_shirt_heights[index]:
                flag = False
                break
    return flag


class ClassPhotos:
    red_shirt_heights = list(map(int, input().split()))
    blue_shirt_heights = list(map(int, input().split()))
    print(classPhotos(red_shirt_heights, blue_shirt_heights))
