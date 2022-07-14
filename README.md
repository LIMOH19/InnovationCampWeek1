# Innovation Camp 8조 - World On Plate
서울에 있는 다양한 맛집들!  
양식, 한식, 중식, 일식 등등 뭐 먹지 고민될 땐?

World on Plate에서 대륙별 레스토랑을 추천 받고 나만의 맛집도 추천할 수 있습니다.

## 1. 제작기간 & 팀원 소개
2022년 7월 11일 ~ 2022년 7월 14일 (총 4일)

4인 1조 팀 프로젝트 : 이종현, 이현규, 임도이, 장혜진

## 2. 사용 기술
- Back-end
    - python3
    - Flask (python framework)
    - MongoDB


- Front-end
  - bootstrap
  - fontawesome
  - bulma
  - JQuery
  - Ajax


- Deploy
  - AWS EC2

## 3. 핵심 기능
- 회원가입 : 아이디 중복 확인 가능
- 로그인 : 아이디/비번 일치 확인 가능
- 지도 : 버튼을 누르면 해당 대륙 레스토랑 필터링
- 레스토랑 등록 : 등록 시 모달이 떠서 사용자가 레스토랑 등록 및 사진 첨부 가능
- 메인페이지 : 전체 레스토랑 목록 확인 가능
- 상세페이지 : 레스토랑 목록을 대륙별로 나누어 확인 가능
- 검색 필터 및 검색 기능 : 레스토랑 이름 검색 가능
- 로그아웃 기능 : 로그아웃 메세지 후 로그인 페이지로 돌아감

## 4. 실행 영상

[World on Plate-site demonstration](https://youtu.be/_xBOYowI7rc)

## 5. 프로젝트 과정 중 이슈 사항
**Issue1. Jinja2 서버 사이드 렌더링 타입 변환 문제**

*문제*: 아래 코드에서 place_star 숫자를 위한 변수가 str 형식으로 저장되어 '⭐' 이모지를 숫자만큼 곱해서 렌더링하는 데에 오류가 났었음 

>{% set place_star = place['star']%}{set star_img='⭐'*place_star%}

*해결*: (VScode 환경 기준)
>{set star_img='⭐'*place_star%}

를

>{% set star_img = '⭐'*place_star|int %}

로 변경하여 명시적으로 place_star 변수를 int 타입으로 변환하여 별점 곱하기 성공


**Issue2. JWT로 받은 토큰이 클라이언트 쪽에서 로그아웃 시 미삭제**

*문제*: 로그아웃 버튼의 onclick 함수 내에
>$.removeCookie('mytoken', { path: '/' });

를 추가하였으나 콘솔창에서는 removeCookie 라는 함수는 없음을 명시. 로그아웃 후 로그인 페이지로 이동했을 때 토큰이 그대로 남아 로그아웃 상태여도 메인페이지로 이동이 가능

*해결*: <head> 태그 안에 아래의 jquery cookie script 링크 추가
>       <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.js"></script>

**Issue3. Bootstrap Modal 비작동**
*문제*: 예시 Modal을 복사하여 html 파일에 붙여넣기 했으나 Modal창이 팝업하지 않음

*해결*: Bootstrap을 위한 link 태그 뿐만 아니라 script(bundle) 태그도 필요

**Issue4. 사진 첨부 시 브라우저에서 사진 깨짐 발생**
*문제*: url 첨부에서 사진 첨부로 기능 변경 후 첨부한 사진이 static 폴더에는 제대로 들어가나 화면 상에서는 나오지 않음

*해결*: 이전에는 url 링크로 사진을 불러왔기 때문에 다른 정보들과 같은 방식으로 불러와도 문제가 없었음. 하지만 파일 업로드 시에는 static 폴더에 업로드 되는 사진이기 때문에 body의 card내에서
>       <img src="{{ place_file }}" class="card-img-top" alt="{{place_name}}">
에서 url_for 사용하여 아래처럼 static 폴더로 연결
>       <img src="{{ url_for('static',filename=place_file) }}" class="card-img-top" alt="{{place_name}}">

같은 방식으로 temp_html에서도
>       <img src="${file}" class="card-img-top" alt="${name}">
에서 아래처럼 static 폴더 내의 파일을 받아주는 걸로 변경
>       <img src="../static/${file}" class="card-img-top" alt="${name}">


**Issue5. 검색 필터링 기능에서 card 정렬 문제**
*문제*: 검색 필터링 할 때 input으로 들어온 값과 대조해서 card-title에 해당하는 값이 없으면 안 보이게 설정했는데 card들이 정렬되지 않고 필터링된 부분만 안 보이게 됨
*해결*: 필터링할 때 필터링된 부분을 style.display = 'none' 이라고 설정했는데 필터링된 부분의 상위 div 태그 (카드들을 감싸고 있는 div 태그)가 남아있어서 문제가 생겼음. 필터링할 부분의 class name을 card가 아닌 상위 태그의 col 형태로 바꿔줌


> 필터링 할 let temp_html = `document.getElementsByClassName("card")`

에서 'card' 를 'col' 로 변경

>let temp_html = `document.getElementsByClassName("col")`





