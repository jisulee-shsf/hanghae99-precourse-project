####
## Hanghae99 Pre-course Project
####
#### 📌 [Introduction]
- 2023.12.6.~2023.12.8.(3일) | 항해99 Pre-course 프로젝트
- 여행 장소를 추천하는 기본 구조의 웹 사이트 만들기 / 6인 팀 프로젝트
- 세션을 사용해 회원가입, 로그인, 로그아웃, 사용자 인증에 기반한 액세스 제한 처리 기능 구현 담당
##
#### 📌 [Tech Stack]
- <div align="left"><img src="https://img.shields.io/badge/[frontend]-HTML / Bootstrap (CSS) / JavaScript (with jQuery)-FF6600"/>
- <div align="left"><img src="https://img.shields.io/badge/[backend]- Flask (Python web framework) / SQLite (database) / SQLAlchemy (ORM for database) / Python (programming language)-4479A1"/>
##
#### 📌 [Features]
1. 회원가입 기능
- 회원가입 폼으로 입력한 데이터를 받아와 입력값 누락 여부, 이메일 중복 여부, 비밀번호 일치 여부의 유효성 검사를 수행함
- 유효성 검사에 성공한 경우: 사용자 정보를 데이터베이스에 저장한 후, 회원가입된 사용자를 홈 페이지로 리다이렉트함
- 유효성 검사에 실패한 경우: 에러 플래시를 띄운 후, 회원가입 프로세스를 중단함에 따라 사용자를 홈 페이지로 리다이렉트함
####
|회원가입 유효성 검사에 성공한 경우|회원가입 유효성 검사에 실패한 경우|
|:---:|:---:|
|![회원가입1_out](https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/98d38873-d658-44d5-a98a-0d5ef7fd2744)|![회원가입2_out](https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/3128c571-9376-4905-9add-69c4cfc01263)|
####
2. 로그인 기능
- 로그인 폼으로 입력한 데이터를 받아와 입력값 누락 여부, 이메일 중복 여부, 비밀번호 일치 여부의 유효성 검사를 수행함
- 유효성 검사에 성공한 경우: 로그인 상태를 유지하기 위해 세션 정보를 저장한 후, 로그인된 사용자를 홈 페이지로 리다이렉트함
- 유효성 검사에 실패한 경우: 에러 플래시를 띄운 후, 로그인 프로세스를 중단함에 따라 사용자를 홈 페이지로 리다이렉트함
####
|로그인 유효성 검사에 성공한 경우|로그인 유효성 검사에 실패한 경우|
|:---:|:---:|
|![로그인1_out](https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/d82b948a-d34c-4d98-bd42-d1a84744eaaf)|![로그인2_out](https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/5cc3c89b-1aa3-4f52-8cf2-881d9d6537fd)|
####
####
3. 사용자 인증에 기반한 액세스 제한 처리 기능 / 4. 로그아웃 기능
- 사용자가 로그인하지 않아 세션에 'email' 키가 없는 경우, 로그인하라는 플래시를 띄운 후 사용자를 홈 페이지로 리다이렉트함
- 로그아웃 버튼을 클릭할 경우, 현재 세션의 모든 데이터가 지워지고 로그인 상태에서 로그아웃 상태로 전환됨
##
#### 📌 [Troubleshooting]
- 원인: Flask의 세션 관리 시 데이터를 안전하게 처리하기 위한 secret key가 설정되지 않아 RuntimeError 에러가 발생함
- 해결: secrets 모듈을 사용해 세션 데이터를 안전하게 처리할 수 있는 임의의 secret key를 설정해 에러를 해결함
##
#### 📌 [Afterthoughts]
- 단기 프로젝트임에도 불구하고, frontend와 backend의 다양한 기술을 경험해볼 수 있어 매우 흥미로웠습니다. 
- 쿠키와 세션의 차이를 이해하고 세션을 사용해 다양한 기능을 구현함으로써 개발의 전반적인 흐름을 이해할 수 있었습니다.
- 다음에는 JWT(JSON Web Tokens)를 기반으로 사용자 인증 기능을 구현하고 싶습니다.
- 협업 과정을 별도 기록으로 남기지 못해 아쉬웠습니다.
####
