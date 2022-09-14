def pre_dash(m):
    if m != 0:
        for i in range(m):
            print("_", end="")
        
def print_ask(n):
    pre_dash(n)
    print("\"재귀함수가 뭔가요?\"")
    pre_dash(n)
    print("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
    pre_dash(n)
    print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    pre_dash(n)
    print("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
    
def recursive_func(N, n):
    if 1 <= N <= 50:
        if n != N*4:
            if n == 0:
                print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
            print_ask(n)
            recursive_func(N, n+4)
        elif n == N*4:
            pre_dash(n)
            print("\"재귀함수가 뭔가요?\"")
            pre_dash(n)
            print("\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        pre_dash(n)
        print("라고 답변하였지.")
        
N = int(input())
recursive_func(N, 0)