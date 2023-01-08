def switch_0_1(num):    ## 0 to 1 / 1 to 0 함수
    if num == 0:
        return 1
    elif num == 1:
        return 0

def switch(number_list, student_list):  ## 스위치 켜고 끄기 함수
    for i in range(len(student_list)):
        if student_list[i][0] == 1:     ## 남자
          for j in range(len(number_list)):
                if (j+1) % student_list[i][1] == 0:                     # number_list 인덱스가 주어진 숫자의 배수인 경우
                    number_list[j] = switch_0_1(number_list[j])         # switch
            
        elif student_list[i][0] == 2:   ## 여자
            for_end = -1    ## 스위치 변경 여부 확인 범위
            scope = 0       ## 주어진 숫자 기준 스위치 변경 범위
            if len(number_list) == 1:
                number_list[0] = switch_0_1(number_list[0])
            else:
                if student_list[i][1] <= len(number_list)//2:           # 주어진 숫자가 number_list 길이의 절반 이하인 경우
                    for_end = student_list[i][1] - 1
                else:                                                   # "" 아닌 경우
                    for_end = len(number_list) - student_list[i][1]
                for j in range(1, for_end+1):                           # 주어진 숫자 기준 for_end 반경만큼 검사
                    if number_list[student_list[i][1]-j-1] == number_list[student_list[i][1]+j-1]:
                        scope += 1  # 대칭인 경우 스위치 변경 반경 증가
                    else:
                        break       # 대칭이 아닌 경우 break
                for k in range(student_list[i][1]-scope-1, student_list[i][1]+scope):   # 대칭 구간 범위 내 스위치
                    number_list[k] = switch_0_1(number_list[k])           
    
    return number_list
    
""" 입력 """    
how_many_number = int(input())
number_list = list(map(int, input().split(' ')))
how_many_students = int(input())
student_list = []
for i in range(how_many_students):
    student_list.append(list(map(int, input().split(' '))))

""" 20개씩 결과 출력 """
result = switch(number_list, student_list)  ## switch() 호출
for i in range(len(result)):
    if (i+1)%20 == 0:
        print(result[i], end="\n")
    else:
        print(result[i], end=" ")