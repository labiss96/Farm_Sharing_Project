## 중요! Git 개발 규칙

##### * Branch

개인이 개발하는 모든 내용은 feature에 따라서 feature branch를 파서 개발할 것

##### * Branch name

- feature/맡은 기능 혹은 개발 진행 중인 기능

##### * Commit Rule

- commit message : 본인이니셜 | 맡은 기능 혹은 개발 진행 중인 기능
- develop에 바로 push하지 말 것)
- merge request를 보낼시에 코드 리뷰를 위해서 간단한 description을 작성할 것
- 그 후 develop branch로 merge request를 보낼 것
- master는 건들지 말 것(마지막에 합칠 예정)

#### Merge 과정에 Conflict 나거나 모르겠으면 혼자 해결하지 말고 꼭 옆 사람에게 물어보기!:smile:

푸쉬할때
git add .
git commit -m "이름"
git push origin 자기브랜치

깃헙 페이지에 develop으로 머지를 합니다
conflict없이 잘 되면 확인 안되면 말하셈

풀땡길때
git checkout master 마스터 브랜치로 옮기고
git pull origin develop

git pull origin develop
git stash pop



## 농사직설

### 기능

- 필터기능
  - 지역
  - 사용목적
  - 비용여부
  - 기간
  - 유저이름
  - 글제목
- 채팅(미정) -> 쪽지
- 상점(미정)

- 좋아요
  - 성공사례 게시판
- 스크랩
  - 팀원모집
  - 마이페이지 연결

### DB모델

- User
  - username
  - pw
  - nickname
  - email
  - SNS_ID
  - 자기소개란
  - 땅(Foreignkey)
  - score
- 땅
  - 지역
  - 면적
  - 땅 상태
  - score
- Farming Board
  - 슈퍼게시판 (Abstract)
    - 제목 : char
    - 지역 : char
    - 면적 : float
    - 기간 : char
    - 비용여부 : boolean
    - 금액 : int
    - 작성자 : user (Foreinkey)
    - 내용 : textarea
    - 모집현황 :
    - 별점 : float
    - 성공사례 : 사례게시판 (Foreinkey)
  - 이용자 게시판(땅 상속) request_Board
    - 사용목적 : enum
  - 소유자 게시판(땅 상속) supplierBoard
    - 사진 : Image
- 성공사례 게시판 success_case
  - 제목
  - 작성자
  - 내용
  - 사진
  - 별점
- 팀 모집 게시판  team_recruitment 
  - 제목
  - 지역
  - 모집인원
  - 모집현황
  - 활동기간
  - 사용목적
  - 내용
- request
  - 땅 소유자 (Foreinkey)
  - 땅 이용자 (Foreinkey)
  - 땅 (Foreinkey)
  - 신청 현황
- 댓글/리뷰 review
  - 땅
  - 땅 이용자
  - 별점
  - 내용
  - 작성일

### App

- landBoard
  - 땅 이용자 게시판
  - 땅 소유자 게시판
  - 댓글
  - 게시판(모델)
  - 댓글(모델)
- otherBoard
  - 성공사례 게시판
  - 팀 구성 게시판
  - 댓글
  - 게시판(모델)
  - 댓글(모델)
- Accounts
  - 로그인/회원가입
  - 마이페이지
  - user(모델)
  - request(모델)
  - 땅(모델)
- main
  - 메인페이지만

### 개인임무분담

종민 : landBoard CRUD

승원 : otherBoard CRUD

정우 : 로그인/로그아웃/마이페이지

정연 : 디자인/프론트

정현 : 땅, 디비 관계



## 구현할 것들

- 땅 생성에 다음 우편번호 api 적용 v
- 수확물쇼핑몰 - 성공사례 매핑 v
- 땅과 게시물 1:1 관계 v
  - 게시물 등록 시 , 등록된 땅은 재등록 못하도록 막고, 마이페이지에서 등록된 땅이라고 표기되도록 함
- 필터링 기능 수정 / 검색기능 추가로 구현 v
- 쇼핑몰 글 좋아요 순으로 정렬 -> 추후 메인페이지에 띄울 것임.
- 디자인 이뿌게
  - 땅 요청 게시판 
  - 땅 등록 게시판 카드형식(그리드) - 사진 추가 v
  - 성공사례 게시판
  - 마이페이지
  - 팀원모집 게시판
  - 전문가 질문하기
  - 메인페이지

- 게시물 생성 시간 필드 추가 v
- 땅 없을 때 게시물 생성 안되게 예외처리 -> alert?? 해봄
- 