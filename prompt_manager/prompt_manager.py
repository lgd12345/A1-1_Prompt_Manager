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


show_menu()