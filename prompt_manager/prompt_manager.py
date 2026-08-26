import json

DEFAULT_PROMPTS = [
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

# JSON 파일 이름과 저장/불러오기 함수 추가
DATA_FILE = "prompts.json"

def save_prompts():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=2)


def load_prompts():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

    except (FileNotFoundError, json.JSONDecodeError):
        pass

    return [prompt.copy() for prompt in DEFAULT_PROMPTS]


prompts = load_prompts()


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

# 메인
def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()

        elif choice == "2":
            show_list()

        elif choice == "3":
            show_by_category()

        elif choice == "4":
            search_prompt()

        elif choice == "5":
            show_detail()

        elif choice == "6":
            toggle_favorite()

        elif choice == "7":
            show_favorites()

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        elif choice in ["8"]:
            print("아직 구현되지 않은 기능입니다.")

        else:
            print("올바른 메뉴 번호를 입력해주세요.")

# 프롬프트 추가
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

    save_prompts()

    print(f"\n'{title}' 프롬프트가 추가되었습니다.")


# 프롬프트 목록조회
def show_list():
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, start=1):
        favorite = " ⭐" if prompt["favorite"] else ""
        print(
            f"{i}. [{prompt['category']}] "
            f"{prompt['title']}{favorite}"
        )

    print(f"\n총 {len(prompts)}개의 프롬프트")


# 카테고리 조회
def show_by_category():
    print("\n=== 카테고리별 조회 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    categories = []

    for prompt in prompts:
        if prompt["category"] not in categories:
            categories.append(prompt["category"])

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    while True:
        choice = input("선택: ").strip()

        if not choice:
            print("카테고리를 선택해주세요.")
            continue

        if not choice.isdigit():
            print("올바른 번호를 입력해주세요.")
            continue

        choice_num = int(choice)

        if not 1 <= choice_num <= len(categories):
            print("올바른 번호를 입력해주세요.")
            continue

        selected_category = categories[choice_num - 1]
        break

    results = []

    for prompt in prompts:
        if prompt["category"] == selected_category:
            results.append(prompt)

    print(f"\n[{selected_category}] 카테고리 프롬프트:")

    if not results:
        print("해당 카테고리의 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(results, start=1):
        favorite = " ⭐" if prompt["favorite"] else ""
        print(f"{i}. {prompt['title']}{favorite}")

    print(f"\n총 {len(results)}개의 프롬프트")

# 검색
def search_prompt():
    print("\n=== 프롬프트 검색 ===")

    while True:
        keyword = input("검색어: ").strip()

        if keyword:
            break

        print("검색어를 입력해주세요.")

    results = []

    for prompt in prompts:
        if (
            keyword.lower() in prompt["title"].lower()
            or keyword.lower() in prompt["content"].lower()
        ):
            results.append(prompt)

    if not results:
        print("검색 결과가 없습니다.")
        return

    print("\n검색 결과:")

    for i, prompt in enumerate(results, start=1):
        favorite = " ⭐" if prompt["favorite"] else ""
        print(
            f"{i}. [{prompt['category']}] "
            f"{prompt['title']}{favorite}"
        )

    print(f"\n총 {len(results)}개의 프롬프트를 찾았습니다.")

def select_prompt():
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return None

    show_list()

    while True:
        choice = input("\n프롬프트 번호 입력: ").strip()

        if not choice:
            print("프롬프트 번호를 입력해주세요.")
            continue

        if not choice.isdigit():
            print("올바른 번호를 입력해주세요.")
            continue

        prompt_num = int(choice)

        if not 1 <= prompt_num <= len(prompts):
            print("존재하지 않는 프롬프트 번호입니다.")
            continue

        return prompt_num - 1

# 상세보기
def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")

    index = select_prompt()

    if index is None:
        return

    prompt = prompts[index]
    favorite = "⭐" if prompt["favorite"] else "아니오"

    print("\n----------------------------")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {favorite}")
    print("----------------------------")
    print("내용:")
    print(prompt["content"])
    print("----------------------------")

# 즐겨찾기 관리
def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")

    index = select_prompt()

    if index is None:
        return

    prompt = prompts[index]
    prompt["favorite"] = not prompt["favorite"]

    save_prompts()

    if prompt["favorite"]:
        print(f"'{prompt['title']}' 프롬프트를 즐겨찾기에 추가했습니다.")
    else:
        print(f"'{prompt['title']}' 프롬프트의 즐겨찾기를 해제했습니다.")

def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")

    favorites = []

    for prompt in prompts:
        if prompt["favorite"]:
            favorites.append(prompt)

    if not favorites:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(favorites, start=1):
        print(
            f"{i}. [{prompt['category']}] "
            f"{prompt['title']} ⭐"
        )

    print(f"\n총 {len(favorites)}개의 즐겨찾기")

if __name__ == "__main__":
    main()