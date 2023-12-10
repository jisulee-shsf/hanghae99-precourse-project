####
# Hanghae99 Pre-course Project
####
#### 📌 [Introduction]
- 2023.12.6.~2023.12.8.(3일) | 항해99 웹 미니 팀 프로젝트
- 여행 장소를 추천하는 기본 구조의 웹 사이트 만들기 진행
- 세션을 사용해 회원가입, 로그인, 로그아웃, 사용자 인증을 기반으로 페이지별 접근 제한 기능 구현 담당
####
#### 📌 [Tech Stack]
- <div align="left"><img src="https://img.shields.io/badge/[Frontend]-HTML5 / Bootstrap (CSS) / JavaScript (with jQuery)-FF6600"/>
- <div align="left"><img src="https://img.shields.io/badge/[Backend]- Flask (Python web framework) / SQLite (database) / SQLAlchemy (ORM for database) / Python (programming language)-4479A1"/>
####
#### 📌 [Features]
1. 회원가입 기능: 사용자가 회원가입 폼을 제출한 경우, 입력한 데이터를 받아와 유효성 검사를 수행함
- 유효성 검사에 성공한 경우: 새로운 사용자 정보를 데이터베이스에 추가함 / 회원가입 후, 홈 페이지로 리다이렉트함
- 유효성 검사에 실패한 경우: 에러에 대한 플래시를 띄우고 홈 페이지로 리다이렉트함
####
|유효성 검사에 성공한 경우|유효성 검사에 실패한 경우|
|:---:|:---:|
|![ezgif com-gif-maker](https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/8275f268-f855-4930-83df-6d2516ccd9cf)|![ezgif com-gif-maker](https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/8275f268-f855-4930-83df-6d2516ccd9cf)|
####
2. 로그인 기능: 사용자가 로그인 폼을 제출한 경우, 이메일과 비밀번호를 받아와 유효성 검사를 수행함
- 유효성 검사에 성공한 경우: 입력받은 이메일을 가진 사용자를 데이터베이스에서 찾음 / 로그인 후, 로그아웃 및 마이 페이지 버튼이 활성화됨
- 유효성 검사에 실패한 경우: 에러에 대한 플래시를 띄우고 홈 페이지로 리다이렉트함
####
|유효성 검사에 성공한 경우|유효성 검사에 실패한 경우|
|:---:|:---:|
|![ezgif com-gif-maker](https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/8275f268-f855-4930-83df-6d2516ccd9cf)|![ezgif com-gif-maker](https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/8275f268-f855-4930-83df-6d2516ccd9cf)|
####
####
2. 로그아웃 기능: 사용자가 로그인 폼을 제출한 경우, 이메일과 비밀번호를 받아와 유효성 검사를 수행함
- 유효성 검사에 성공한 경우: 데이터베이스에서 입력받은 이메일을 가진 사용자를 찾음 / 로그인이 완료된 후, 홈 페이지로 리다이렉트함
- 유효성 검사에 실패한 경우: 에러에 대한 플래시를 띄우고 홈 페이지로 리다이렉트함
####
|유효성 검사에 성공한 경우|유효성 검사에 실패한 경우|
|:---:|:---:|
|![ezgif com-gif-maker](https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/8275f268-f855-4930-83df-6d2516ccd9cf)|![ezgif com-gif-maker](https://github.com/jisulee-shsf/hanghae99-precourse-project/assets/109773795/8275f268-f855-4930-83df-6d2516ccd9cf)|
####
#### ► [Troubleshooting]
- 유효하지 않은 키:
####
#### ► [Afterthoughts]
- 도메인 지식이 없는 데이터로 EDA를 포함한 modeling 전 과정을 스스로 고민해 구현하는 과정이 매우 유익했습니다.
- 특히 게임 도메인을 학습해 다양한 가설을 설정하고 correlation 분석 방법으로 검증해 나가는 과정이 흥미로웠습니다.
- 다방면의 도메인 데이터를 핸들링하며 더욱 심층적인 분석 경험을 쌓을 예정입니다.
####
#### ► [Reference]
- [[Kaggle] PUBG Finish Placement Prediction](https://www.kaggle.com/competitions/pubg-finish-placement-prediction)
####
