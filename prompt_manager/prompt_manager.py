prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "주어진 주제에 대해 이해하기 쉬운 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": False,
    },
    {
        "title": "제품 이미지 생성",
        "content": "제품의 특징이 잘 드러나는 광고 이미지를 생성해주세요.",
        "category": "이미지 생성",
        "favorite": False,
    },
    {
        "title": "IT 전문가 페르소나",
        "content": "당신은 친절하고 경험이 풍부한 IT 전문가입니다.",
        "category": "페르소나",
        "favorite": True,
    },
]


CATEGORIES = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타",
    "직접 입력",
]


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. Markdown 내보내기")
    print("0. 종료")


def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        elif choice in ["2", "3", "4", "5", "6", "7", "8"]:
            print("아직 구현되지 않은 기능입니다.")

        else:
            print("올바른 메뉴 번호를 입력해주세요.")


def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("제목을 입력해주세요.")

    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("내용을 입력해주세요.")

    print("\n카테고리 선택:")
    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}. {category}")

    while True:
        choice = input("선택: ").strip()

        if not choice:
            print("카테고리를 선택하거나 직접 입력해주세요.")
            continue

        if not choice.isdigit():
            print("카테고리를 선택하거나 직접 입력해주세요.")
            continue

        choice_num = int(choice)

        if not 1 <= choice_num <= len(CATEGORIES):
            print("카테고리를 선택하거나 직접 입력해주세요.")
            continue

        selected = CATEGORIES[choice_num - 1]

        if selected == "직접 입력":
            while True:
                category = input("카테고리 직접 입력: ").strip()

                if category:
                    break

                print("카테고리를 입력해주세요.")
        else:
            category = selected

        break

    prompts.append(
        {
            "title": title,
            "content": content,
            "category": category,
            "favorite": False,
        }
    )

    print(f"\n'{title}' 프롬프트가 추가되었습니다.")


if __name__ == "__main__":
    main()