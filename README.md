####
# Hanghae99 Pre-course Project
####
#### 📌 [Introduction]
- 2023.12.6.~2023.12.8.(3일) | 항해99 웹 미니 팀 프로젝트
- 여행 장소를 추천하는 기본 구조의 웹 사이트 만들기 진행
- 세션을 사용해 회원가입, 로그인, 로그아웃, 사용자 인증을 기반으로 페이지별 접근 제한 기능 구현 담당
##
#### 📌 [Tech Stack]
- <div align="left"><img src="https://img.shields.io/badge/[Frontend]-HTML5 / Bootstrap (CSS) / JavaScript (with jQuery)-FF6600"/>
- <div align="left"><img src="https://img.shields.io/badge/[Backend]- Flask (Python web framework) / SQLite (database) / SQLAlchemy (ORM for database) / Python (programming language)-4479A1"/>
##
#### 📌 [Features]
1. 회원가입 기능
- 회원가입 폼으로 입력한 데이터를 받아와 입력값 누락 여부, 이메일 중복 여부, 비밀번호 일치 여부의 유효성 검사를 수행함
- 유효성 검사에 성공한 경우: 사용자 정보를 데이터베이스에 저장한 후, 회원가입된 사용자를 홈 페이지로 리다이렉트함
- 유효성 검사에 실패한 경우: 에러 플래시를 띄운 후, 회원가입 프로세스를 중단함에 따라 사용자를 홈 페이지로 리다이렉트함
####
|회원가입 유효성 검사에 성공한 경우|회원가입 유효성 검사에 실패한 경우|
|:---:|:---:|
|![가입1_out](https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/c5dee2af-8e1d-49cc-8349-19532064503d)|![가입2_out](https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/8790fa4f-617a-4dcb-a5f4-96874a20fcc2)|
####
2. 로그인 기능
- 로그인 폼으로 입력한 데이터를 받아와 입력값 누락 여부, 이메일 중복 여부, 비밀번호 일치 여부의 유효성 검사를 수행함
- 유효성 검사에 성공한 경우: 로그인 상태를 유지하기 위해 세션 정보를 저정한 후, 로그인된 사용자를 홈 페이지로 리다이렉트함
- 유효성 검사에 실패한 경우: 에러 플래시를 띄운 후, 로그인 프로세스를 중단함에 따라 사용자를 홈 페이지로 리다이렉트함
####
|로그인 유효성 검사에 성공한 경우|로그인 유효성 검사에 실패한 경우|
|:---:|:---:|
|![ezgif com-gif-maker](https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/8275f268-f855-4930-83df-6d2516ccd9cf)|![ezgif com-gif-maker](https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/8275f268-f855-4930-83df-6d2516ccd9cf)|
####
####
3. 사용자 인증에 기반한 페이지별 접근 제한 기능 / 4. 로그아웃 기능
- 사용자가 로그인하지 않아 세션에 'email' 키가 없는 경우, 로그인하라는 플래시를 띄운 후 사용자를 홈 페이지로 리다이렉트함
- 로그아웃 버튼을 클릭할 경우, 현재 세션의 모든 데이터가 지워지고 로그인 상태에서 로그아웃 상태로 전환됨
####
|로그인하지 않아 접근이 제한된 경우|로그아웃한 경우|
|:---:|:---:|
|![ezgif com-gif-maker](https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/8275f268-f855-4930-83df-6d2516ccd9cf)|![ezgif com-gif-maker](https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/8275f268-f855-4930-83df-6d2516ccd9cf)|
##
#### 📌 [Troubleshooting]
- 원인: Flask의 세션 관리 시 데이터를 안전하게 처리하기 위해 secret key가 설정되지 않아 RuntimeError 에러가 발생함
- 해결: secrets 모듈을 사용해 세션 데이터를 안전하게 처리할 수 있는 임의의 secret key를 설정해 에러를 해결함
<img width="1239" alt="image" src="https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/4a28a4db-75ba-4513-8428-ce27bf4244b6">

##
#### ► [Afterthoughts]
- 도메인 지식이 없는 데이터로 EDA를 포함한 modeling 전 과정을 스스로 고민해 구현하는 과정이 매우 유익했습니다.
- 특히 게임 도메인을 학습해 다양한 가설을 설정하고 correlation 분석 방법으로 검증해 나가는 과정이 흥미로웠습니다.
- 다방면의 도메인 데이터를 핸들링하며 더욱 심층적인 분석 경험을 쌓을 예정입니다.
##
#### ► [Deployment]
- 🔗 [[항해99 웹 미니 팀 프로젝트 | 8조] 여행 추천 사이트](https://minyonghyun.pythonanywhere.com/)
####
