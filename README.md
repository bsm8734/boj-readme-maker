# boj-readme-maker

## 만든이유

- [coding-test-study](https://github.com/boostcamp-ai-tech-4/coding-test-study) 레포에서 내가 원하는 포맷을 쉽게 readme를 만들기 위해
- 문제 유형 추가될 때마다 번호랑 이름 일일히 입력하는게 번거로움
- 문제 번호만 넣어주면, 자동으로 readme 만들고자 함

## README 포맷(output format)

- [coding-test-study/sally/README](https://github.com/boostcamp-ai-tech-4/coding-test-study/blob/main/sally/README.md) 참고

## 사용법

- 두가지 버전으로 만듦
    1. 문제 번호를 리스트로 입력받아서 readme 생성(`main.py` 실행)
    2. [coding-test-study/README.md](https://github.com/boostcamp-ai-tech-4/coding-test-study/README.md) 페이지에서 원하는 카테고리만 긁어와서 재구성(`restruct_main.py` 실행)

## output file

- defuault: `./problem_list.md`
- 기본 저장 위치 변경하고 싶으면, `utils.py` 상단의 `FILEPATH` 변수를 바꾸면 됨

## 사용법 - main.py

### input (예시)

```text
# python3 main.py (문제유형) (문제번호)
python3 main.py 'Implementation' 3151 29366 29442
```

### 원하는 output (예시)

```text
## Implementation

- [ ] **3151_합이 0** / [문제](https://www.acmicpc.net/problem/3151) / [풀이]()
- [ ] **20366_같이 눈사람 만들래?** / [문제](https://www.acmicpc.net/problem/20366) / [풀이]()
- [ ] **20442_ㅋㅋ루ㅋㅋ** / [문제](https://www.acmicpc.net/problem/20442) / [풀이]()
```

## 사용법 - restruct_main.py

### input (예시)

```text
# python3 restruct_main.py (카테고리 이름)
python3 restruct_main.py '투 포인터'
```

### 원하는 output (예시)

```text
## 투 포인터

- [ ] 11728_배열 합치기 / [문제](https://www.acmicpc.net/problem/11728) / [풀이]()  
- [ ] 11659_구간 합 구하기 4 / [문제](https://www.acmicpc.net/problem/11659) / [풀이]()  
```
