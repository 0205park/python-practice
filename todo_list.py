
tasks = []

while True:
    print("\n=== 할 일 관리 ===")
    print("1. 할 일 추가")
    print("2. 할 일 목록")
    print("3. 할 일 삭제")
    print("4. 종료")

    menu = input("메뉴 선택: ")

    if menu == "1":
        task = input("할 일을 입력하세요: ")
        tasks.append(task)
        print("추가되었습니다.")

    elif menu == "2":
        if not tasks:
            print("할 일이 없습니다.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif menu == "3":
        try:
            num = int(input("삭제할 번호: "))
            removed = tasks.pop(num - 1) if 1 <= num <= len(tasks) else None
            if removed is None:
                print("잘못된 번호입니다.")
            else:
                print("삭제 완료:", removed)
        except ValueError:
            print("숫자를 입력하세요.")

    elif menu == "4":
        print("프로그램 종료")
        break

    else:
        print("잘못된 메뉴입니다.")
