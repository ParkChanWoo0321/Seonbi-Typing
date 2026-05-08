# 선비타이핑

사진 넣을 곳

## 1. 프로젝트 소개

**선비타이핑**는 고전 문장, 사자성어, 고사성어, 전통적인 우리말 표현을 퀴즈 형태로 학습할 수 있는 **AI 기반 고전 언어 학습 서비스**입니다.

사용자는 짧은 문제를 반복적으로 풀면서 고전 표현의 의미와 독음을 익히고, 답안을 제출하면 AI 훈장님 피드백을 통해 정답 여부와 해설을 확인할 수 있습니다.

단순한 문제 풀이 서비스가 아니라, 고전 언어 자산을 현대적인 디지털 학습 콘텐츠로 재구성하고, 사용자의 학습 기록과 성장 단계를 관리하는 백엔드 중심의 학습 플랫폼입니다.

---

## 2. 프로젝트 기획 배경

사진 넣을 곳

디지털 환경이 확산되면서 짧고 자극적인 콘텐츠 소비가 증가하고, 줄임말과 신조어 중심의 언어 사용이 일상화되고 있습니다. 이러한 변화 속에서 고전 문장, 사자성어, 전통적인 우리말 표현과 같은 언어 자산은 일상에서 접하기 어려워지고 있습니다.

현재 영어 학습 서비스나 게임형 언어 학습 플랫폼은 다양하게 존재하지만, 우리 고유의 고전 표현을 쉽고 재미있게 학습할 수 있는 서비스는 상대적으로 부족합니다.

선비타이핑는 이러한 문제를 해결하기 위해 고전 문장을 데이터베이스화하고, 퀴즈 학습 구조와 AI 피드백 시스템을 결합하여 사용자가 부담 없이 고전 표현을 학습할 수 있도록 설계하였습니다.

---

## 3. 주요 기능

사진 넣을 곳

### 3.1 고전 문장 기반 퀴즈 학습

사용자는 고전 문장, 사자성어, 고사성어를 기반으로 구성된 문제를 풀 수 있습니다.  
문제는 원문, 독음, 뜻, 해설 데이터를 기반으로 제공되며, 사용자의 답변에 따라 정답 여부가 판별됩니다.

### 3.2 AI 훈장님 피드백

사용자가 답안을 제출하면 AI가 사용자의 답변을 분석하고, 훈장님 말투의 피드백을 제공합니다.  
단순히 정답과 오답만 반환하는 것이 아니라, 왜 맞았는지 또는 왜 틀렸는지를 설명하여 학습 효과를 높였습니다.

### 3.3 학습 기록 저장

사용자가 푼 문제는 학습 기록으로 저장됩니다.  
사용자는 자신이 어떤 문제를 풀었는지, 제출한 답변이 무엇이었는지, 정답 여부와 해설을 다시 확인할 수 있습니다.

### 3.4 레벨 기반 성장 시스템

사용자의 학습 참여를 유도하기 위해 전통 관직 명칭을 활용한 레벨 시스템을 적용하였습니다.

| 레벨 | 명칭 |
|---|---|
| 1 | 도사 |
| 2 | 정랑 |
| 3 | 첨정 |
| 4 | 사인 |
| 5 | 집의 |
| 6 | 참의 |
| 7 | 동지사 |
| 8 | 지사 |
| 9 | 판사 |
| 10 | 영의정 |

퀴즈를 풀고 학습 경험을 쌓으면 단계적으로 승급할 수 있으며, 최종 단계인 영의정에 도달하면 프로필 이미지 변경과 같은 보상 요소를 제공할 수 있도록 설계하였습니다.

### 3.5 고전 문장 데이터 관리

고전 문장 데이터는 `classic_sentences` 테이블에 저장됩니다.  
원문, 독음, 현대어 뜻, 사용 여부, 생성일, 수정일을 관리하여 문제 출제 데이터로 활용합니다.

---

## 4. 기술 스택

| 구분 | 기술 |
|---|---|
| Language | Java |
| Framework | Spring Boot |
| Web | Spring Web |
| ORM | Spring Data JPA |
| Database | MySQL |
| Security | Spring Security, JWT |
| AI | OpenAI API |
| Build Tool | Gradle |
| API Test | Postman |
| Deploy | GCP VM |
| Version Control | Git, GitHub |

---

## 5. 시스템 구조

사진 넣을 곳

```text
[Client]
   |
   | HTTP Request
   v
[Spring Boot Backend]
   |
   |-- Auth Module
   |     |-- 회원가입
   |     |-- 로그인
   |     |-- JWT 인증
   |
   |-- Problem Module
   |     |-- 고전 문장 문제 조회
   |     |-- 답안 제출
   |     |-- 정답 판별
   |
   |-- AI Feedback Module
   |     |-- 사용자 답안 분석
   |     |-- AI 훈장님 피드백 생성
   |
   |-- History Module
   |     |-- 사용자가 푼 문제 기록 저장
   |     |-- 내 학습 기록 조회
   |
   |-- Level Module
   |     |-- 경험치 관리
   |     |-- 문패 등급 관리
   |
   v
[MySQL Database]
   |
   |-- users
   |-- classic_sentences
   |-- problem_histories
   |-- user_levels
```
## 6. 백엔드 핵심 구현 내용

### 6.1 고전 문장 데이터 기반 문제 출제 구조

고전 문장은 `classic_sentences` 테이블에 저장하고, 문제 출제 시 사용되지 않은 데이터를 우선적으로 조회하도록 설계하였습니다.

각 문장은 다음 정보를 포함합니다.

- 원문
- 독음
- 현대어 뜻
- 사용 여부
- 생성일
- 수정일

이를 통해 고전 문장 데이터를 문제 출제 단위로 관리할 수 있으며, 사용자가 이미 풀었던 문제와 중복되지 않도록 확장 가능한 구조를 구성하였습니다.

---

### 6.2 사용자 답안 채점 및 학습 기록 저장

사용자가 답안을 제출하면 서버는 문제의 정답 데이터와 사용자 답변을 비교하여 정답 여부를 판단합니다.

채점 결과는 단순 응답으로 끝나지 않고 `problem_histories` 테이블에 저장됩니다.

이를 통해 사용자는 자신이 푼 문제 목록을 다시 확인할 수 있고, 서비스는 사용자의 학습 이력을 기반으로 복습 기능이나 개인화 추천 기능으로 확장할 수 있습니다.

---

### 6.3 AI 훈장님 피드백 연동

정답 여부가 결정되면 AI API를 통해 사용자 답변에 대한 해설을 생성합니다.

AI 피드백은 일반적인 설명이 아니라 서비스 콘셉트에 맞게 훈장님 캐릭터의 말투로 제공되도록 구성하였습니다.

사용자가 정답을 맞힌 경우에는 긍정적인 피드백과 함께 표현의 의미를 다시 설명하고, 오답인 경우에는 사용자가 혼동한 지점을 중심으로 해설을 제공합니다.

---

### 6.4 JWT 기반 인증 구조

로그인 이후 발급된 Access Token을 사용하여 인증이 필요한 API를 호출할 수 있도록 구성하였습니다.

특히 사용자의 학습 기록 조회, 문제 풀이 기록 저장, 레벨 정보 관리와 같은 기능은 사용자 식별이 필요하므로 JWT 인증을 기반으로 처리하였습니다.

---

### 6.5 학습 기록 기반 확장 가능한 레벨 시스템

사용자의 문제 풀이 기록과 정답 여부를 기반으로 경험치를 누적하고, 특정 기준에 도달하면 레벨이 상승하는 구조를 설계하였습니다.

레벨 명칭은 서비스의 고전 학습 콘셉트에 맞게 전통 관직 명칭을 활용하였으며, 단순 점수 시스템보다 사용자에게 더 직관적인 성장 경험을 제공할 수 있도록 구성하였습니다.

---

## 7. API 명세

사진 넣을 곳

### Auth API

| Method | URL | 설명 | 인증 |
|---|---|---|---|
| POST | `/api/auth/signup` | 회원가입 | X |
| POST | `/api/auth/login` | 로그인 및 토큰 발급 | X |
| POST | `/api/auth/refresh` | Access Token 재발급 | X |
| POST | `/api/auth/logout` | 로그아웃 | O |

### Problem API

| Method | URL | 설명 | 인증 |
|---|---|---|---|
| GET | `/api/problems/blind-typing/{level}` | 단계별 고전 문장 문제 조회 | O |
| POST | `/api/problems/{problemId}/answer` | 문제 답안 제출 및 AI 피드백 반환 | O |

### My Page API

| Method | URL | 설명 | 인증 |
|---|---|---|---|
| GET | `/api/me/problem-history` | 내가 푼 문제 기록 조회 | O |
| GET | `/api/me/level` | 내 레벨 및 경험치 조회 | O |
| GET | `/api/me/profile` | 내 프로필 조회 | O |

### Classic Sentence API

| Method | URL | 설명 | 인증 |
|---|---|---|---|
| GET | `/api/classic-sentences` | 고전 문장 목록 조회 | O |
| POST | `/api/admin/classic-sentences` | 고전 문장 등록 | O |
| PATCH | `/api/admin/classic-sentences/{id}` | 고전 문장 수정 | O |
| DELETE | `/api/admin/classic-sentences/{id}` | 고전 문장 삭제 | O |

---

## 8. API 요청/응답 예시

### 8.1 로그인 요청

```http
POST /api/auth/login
Content-Type: application/json
```

```json
{
  "loginId": "testuser",
  "password": "1234"
}
```

### 8.2 로그인 응답

```json
{
  "accessToken": "Bearer access-token-value",
  "userId": 1,
  "loginId": "testuser",
  "name": "홍길동"
}
```

---

### 8.3 문제 조회 요청

```http
GET /api/problems/blind-typing/1
Authorization: Bearer access-token-value
```

### 8.4 문제 조회 응답

```json
{
  "problemId": 1,
  "originalText": "聘禮竣事。海陸無恙。",
  "readingText": "빙례준사해륙무양",
  "question": "다음 고전 문장의 뜻을 입력하시오."
}
```

---

### 8.5 답안 제출 요청

```http
POST /api/problems/1/answer
Authorization: Bearer access-token-value
Content-Type: application/json
```

```json
{
  "answer": "사신의 예가 끝나고 바다와 육지가 모두 평안하도다."
}
```

### 8.6 답안 제출 응답

```json
{
  "problemId": 1,
  "correct": true,
  "userAnswer": "사신의 예가 끝나고 바다와 육지가 모두 평안하도다.",
  "meaning": "사신의 예가 끝나고 바다와 육지가 모두 평안하도다.",
  "explanation": "아주 잘하였네. 제시된 뜻과 답이 정확히 일치하였네.",
  "earnedExp": 10
}
```

---

### 8.7 내가 푼 문제 조회 요청

```http
GET /api/me/problem-history
Authorization: Bearer access-token-value
```

### 8.8 내가 푼 문제 조회 응답

```json
[
  {
    "historyId": 6,
    "originalText": "聘禮竣事。海陸無恙。",
    "readingText": "빙례준사해륙무양",
    "meaning": "사신의 예가 끝나고 바다와 육지가 모두 평안하도다.",
    "userAnswer": "사신의 예가 끝나고 바다와 육지가 모두 평안하도다.",
    "correct": true,
    "explanation": "아주 잘하였네. 제시된 뜻과 답이 글자 하나 다르지 않게 같아서, 바른 풀이로 인정하네."
  }
]
```

---

## 9. 데이터베이스 설계

사진 넣을 곳

### 주요 테이블

| 테이블명 | 역할 |
|---|---|
| `users` | 사용자 계정 정보 저장 |
| `classic_sentences` | 고전 문장 원문, 독음, 뜻 데이터 저장 |
| `problem_histories` | 사용자가 푼 문제 기록 저장 |
| `user_levels` | 사용자 경험치 및 레벨 정보 저장 |

---

### users

| 컬럼명 | 설명 |
|---|---|
| `id` | 사용자 PK |
| `login_id` | 로그인 ID |
| `password` | 암호화된 비밀번호 |
| `name` | 사용자 이름 |
| `created_at` | 생성일 |
| `updated_at` | 수정일 |

---

### classic_sentences

| 컬럼명 | 설명 |
|---|---|
| `id` | 고전 문장 PK |
| `original_text` | 고전 문장 원문 |
| `reading_text` | 독음 |
| `meaning` | 현대어 뜻 |
| `used` | 문제 사용 여부 |
| `created_at` | 생성일 |
| `updated_at` | 수정일 |

---

### problem_histories

| 컬럼명 | 설명 |
|---|---|
| `id` | 학습 기록 PK |
| `user_id` | 사용자 FK |
| `classic_sentence_id` | 고전 문장 FK |
| `user_answer` | 사용자가 입력한 답변 |
| `correct` | 정답 여부 |
| `explanation` | AI 피드백 및 해설 |
| `created_at` | 풀이 일시 |

---

### user_levels

| 컬럼명 | 설명 |
|---|---|
| `id` | 레벨 정보 PK |
| `user_id` | 사용자 FK |
| `level` | 현재 레벨 |
| `level_name` | 현재 문패 명칭 |
| `exp` | 누적 경험치 |
| `updated_at` | 수정일 |

---

### ERD 개요

```text
users
  1 ─── N problem_histories
  1 ─── 1 user_levels

classic_sentences
  1 ─── N problem_histories
```

---

## 10. 프로젝트 구조

```text
seonbi-mind
├── src
│   ├── main
│   │   ├── java
│   │   │   └── youngju
│   │   │       └── seonbimind
│   │   │           ├── SeonbiMindApplication.java
│   │   │           │
│   │   │           ├── auth
│   │   │           │   ├── config
│   │   │           │   │   └── SecurityConfig.java
│   │   │           │   │
│   │   │           │   ├── controller
│   │   │           │   │   └── AuthController.java
│   │   │           │   │
│   │   │           │   ├── dto
│   │   │           │   │   ├── AuthResponse.java
│   │   │           │   │   ├── AuthResult.java
│   │   │           │   │   ├── LoginRequest.java
│   │   │           │   │   ├── SignupRequest.java
│   │   │           │   │   └── TodaySentenceResponse.java
│   │   │           │   │
│   │   │           │   ├── entity
│   │   │           │   │   └── AuthMember.java
│   │   │           │   │
│   │   │           │   ├── jwt
│   │   │           │   │   ├── JwtAuthenticationFilter.java
│   │   │           │   │   └── JwtTokenProvider.java
│   │   │           │   │
│   │   │           │   ├── repository
│   │   │           │   │   └── AuthMemberRepository.java
│   │   │           │   │
│   │   │           │   └── service
│   │   │           │       ├── AuthService.java
│   │   │           │       └── CurrentMemberService.java
│   │   │           │
│   │   │           ├── classic
│   │   │           │   ├── gpt
│   │   │           │   │   ├── dto
│   │   │           │   │   │   └── MeaningEvaluationResult.java
│   │   │           │   │   │
│   │   │           │   │   └── service
│   │   │           │   │       └── GptMeaningEvaluationService.java
│   │   │           │   │
│   │   │           │   ├── problem
│   │   │           │   │   ├── controller
│   │   │           │   │   │   └── ProblemController.java
│   │   │           │   │   │
│   │   │           │   │   ├── dto
│   │   │           │   │   │   ├── AnswerRequest.java
│   │   │           │   │   │   ├── ProblemAnswerResponse.java
│   │   │           │   │   │   ├── ProblemStartRequest.java
│   │   │           │   │   │   └── ProblemStartResponse.java
│   │   │           │   │   │
│   │   │           │   │   ├── entity
│   │   │           │   │   │   ├── ProblemSession.java
│   │   │           │   │   │   ├── ProblemSessionStage.java
│   │   │           │   │   │   └── UserSentenceUsage.java
│   │   │           │   │   │
│   │   │           │   │   ├── repository
│   │   │           │   │   │   ├── ProblemSessionRepository.java
│   │   │           │   │   │   └── UserSentenceUsageRepository.java
│   │   │           │   │   │
│   │   │           │   │   └── service
│   │   │           │   │       └── ProblemService.java
│   │   │           │   │
│   │   │           │   ├── progress
│   │   │           │   │   ├── controller
│   │   │           │   │   │   └── MeProgressController.java
│   │   │           │   │   │
│   │   │           │   │   ├── dto
│   │   │           │   │   │   ├── ProblemHistoryResponse.java
│   │   │           │   │   │   └── ProgressResponse.java
│   │   │           │   │   │
│   │   │           │   │   ├── entity
│   │   │           │   │   │   ├── LearningRank.java
│   │   │           │   │   │   ├── SolvedProblemHistory.java
│   │   │           │   │   │   └── UserProgress.java
│   │   │           │   │   │
│   │   │           │   │   ├── repository
│   │   │           │   │   │   ├── SolvedProblemHistoryRepository.java
│   │   │           │   │   │   └── UserProgressRepository.java
│   │   │           │   │   │
│   │   │           │   │   └── service
│   │   │           │   │       └── ProgressService.java
│   │   │           │   │
│   │   │           │   └── sentence
│   │   │           │       ├── entity
│   │   │           │       │   └── ClassicSentence.java
│   │   │           │       │
│   │   │           │       └── repository
│   │   │           │           └── ClassicSentenceRepository.java
│   │   │           │
│   │   │           └── common
│   │   │               └── exception
│   │   │                   └── ApiExceptionHandler.java
│   │   │
│   │   └── resources
│   │       ├── static
│   │       ├── templates
│   │       └── application.properties
│   │
│   └── test
│
├── build.gradle
├── settings.gradle
└── README.md
```

### 패키지별 역할

| 패키지 | 역할 |
|---|---|
| `auth` | 회원가입, 로그인, 사용자 인증 관련 기능 관리 |
| `auth.config` | Spring Security 설정 및 인증/인가 정책 관리 |
| `auth.jwt` | JWT 토큰 생성, 검증, 인증 필터 처리 |
| `classic.gpt` | GPT 기반 사용자 답안 의미 평가 및 AI 피드백 생성 |
| `classic.problem` | 문제 세션 생성, 단계별 문제 제공, 답안 제출 및 채점 처리 |
| `classic.progress` | 사용자 학습 기록, 풀이 이력, 경험치, 문패 등급 관리 |
| `classic.sentence` | 고전 문장 데이터 엔티티 및 Repository 관리 |
| `common.exception` | 전역 예외 처리 및 API 에러 응답 관리 |
| `resources` | 정적 리소스, 템플릿, 애플리케이션 설정 파일 관리 |

---

## 11. 실행 방법

### 11.1 프로젝트 클론

```bash
git clone https://github.com/사용자명/seonbi-mind.git
cd seonbi-mind
```

---

### 11.2 환경 변수 설정

`application.yml` 또는 `application-prod.yml`에 다음 값을 설정합니다.

```yml
server:
  port: 8080

spring:
  datasource:
    url: jdbc:mysql://localhost:3306/seonbimind
    username: root
    password: password
  jpa:
    hibernate:
      ddl-auto: update
    show-sql: true

app:
  jwt:
    secret: your-jwt-secret-key
    access-token-expiration: 3600000
  cors:
    allowed-origins: http://localhost:3000

openai:
  api-key: your-openai-api-key
```

---

### 11.3 MySQL 데이터베이스 생성

```sql
CREATE DATABASE seonbimind;
```

---

### 11.4 애플리케이션 실행

```bash
./gradlew bootRun
```

또는

```bash
./gradlew build
java -jar build/libs/seonbi-mind.jar
```

---

### 11.5 배포 실행

```bash
chmod +x deploy.sh
./deploy.sh
```

---

## 12. 트러블슈팅

### 12.1 OpenAI API 호출 시 429 insufficient_quota 발생

#### 문제 상황

AI 훈장님 피드백 기능을 테스트하는 과정에서 OpenAI API 요청이 실패하고, 서버에서는 502 응답이 반환되는 문제가 발생했습니다.

```text
OpenAI API request failed.
status=429 TOO_MANY_REQUESTS
code=insufficient_quota
```

#### 원인

백엔드 로직의 오류가 아니라 OpenAI API 계정의 사용량 또는 결제 한도 문제였습니다.

외부 API 의존성이 있는 기능이기 때문에, API 호출 실패 시 전체 문제 풀이 흐름이 중단될 수 있었습니다.

#### 해결 과정

AI API 호출 실패 상황을 예외로 분리하고, 사용자에게 서버 오류가 아닌 피드백 생성 실패로 인식될 수 있도록 처리하였습니다.

또한 기본 해설 데이터를 우선 반환할 수 있는 구조로 개선하여 외부 API 장애가 전체 서비스 장애로 이어지지 않도록 설계하였습니다.

#### 배운 점

외부 API를 사용하는 기능은 반드시 실패 가능성을 고려해야 하며, 핵심 서비스 로직과 외부 연동 로직을 분리해야 안정적인 백엔드 구조를 만들 수 있다는 점을 배웠습니다.

---

### 12.2 CORS 설정 문제

#### 문제 상황

프론트엔드와 백엔드를 분리하여 개발하는 과정에서 브라우저에서 API 요청이 차단되는 문제가 발생했습니다.

#### 원인

백엔드 서버의 CORS 허용 Origin 설정에 프론트엔드 주소가 포함되어 있지 않았습니다.

로컬 개발 환경에서는 `localhost:3000`, 배포 환경에서는 프론트엔드 도메인을 허용해야 했습니다.

#### 해결 과정

`application.yml`에 CORS 허용 Origin을 환경별로 관리하도록 설정하였습니다.

```yml
app:
  cors:
    allowed-origins: http://localhost:3000,https://frontend-domain.com
```

Spring Security 설정에서 CORS를 활성화하고, 배포 환경에서는 프론트엔드 도메인만 허용하도록 구성하였습니다.

#### 배운 점

프론트엔드와 백엔드가 분리된 구조에서는 CORS 설정이 필수이며, 개발 환경과 운영 환경의 Origin을 구분해서 관리해야 한다는 점을 배웠습니다.

---

### 12.3 JWT 인증이 필요한 API에서 401 Unauthorized 발생

#### 문제 상황

내가 푼 문제 조회 API를 호출할 때 `401 Unauthorized` 응답이 발생했습니다.

```http
GET /api/me/problem-history
Authorization: Bearer token
```

#### 원인

Authorization Header의 Bearer Token 형식이 잘못되었거나, Spring Security 필터에서 토큰을 정상적으로 파싱하지 못한 것이 원인이었습니다.

#### 해결 과정

JWT 인증 필터에서 Authorization Header를 확인하고, `Bearer ` 접두어가 있는 경우에만 토큰을 추출하도록 처리하였습니다.

또한 인증이 필요한 API와 인증이 필요 없는 API를 명확히 분리하였습니다.

#### 배운 점

JWT 인증 구조에서는 토큰 발급뿐만 아니라, 요청마다 토큰을 검증하고 SecurityContext에 사용자 정보를 저장하는 흐름이 중요하다는 점을 이해했습니다.

---

### 12.4 데이터베이스 테이블명 및 컬럼명 불일치 문제

#### 문제 상황

고전 문장 데이터를 INSERT하는 과정에서 테이블명 또는 컬럼명이 일치하지 않아 SQL 실행 오류가 발생했습니다.

#### 원인

초기 설계에서는 `classic_sentence`와 같은 단수형 테이블명을 고려했지만, 실제 사용 테이블은 `classic_sentences`로 정리하였습니다.

또한 Java Entity 필드명과 DB 컬럼명이 다를 경우 매핑 문제가 발생할 수 있었습니다.

#### 해결 과정

고전 문장 테이블명을 `classic_sentences`로 통일하고, Entity의 `@Column` 설정과 SQL INSERT 문을 동일한 컬럼명 기준으로 정리하였습니다.

```sql
INSERT INTO classic_sentences
(original_text, reading_text, meaning, used, created_at, updated_at)
VALUES
('詩者原於德性。發於才情。', '시자원어덕성 발어재정', '시란 덕성에 뿌리를 두고 재주와 정에서 피어나는 것이니라.', false, NOW(), NOW());
```

#### 배운 점

DB 설계 초기에 테이블명과 컬럼명 규칙을 정하고, Entity와 SQL 스크립트에서 일관되게 유지하는 것이 중요하다는 점을 배웠습니다.

---

### 12.5 배포 환경에서 8080 포트 충돌 발생

#### 문제 상황

GCP VM에서 Spring Boot 애플리케이션을 실행할 때 8080 포트가 이미 사용 중이라는 오류가 발생했습니다.

#### 원인

기존에 실행 중이던 애플리케이션 프로세스가 종료되지 않아 동일한 포트를 점유하고 있었습니다.

#### 해결 과정

8080 포트를 사용하는 프로세스를 확인하고 종료한 뒤 다시 배포를 진행하였습니다.

```bash
sudo lsof -i :8080
sudo kill -9 {PID}
```

필요한 경우 `application.yml`에서 서버 포트를 변경하여 실행할 수 있도록 구성하였습니다.

```yml
server:
  port: 8081
```

#### 배운 점

배포 환경에서는 애플리케이션 실행 여부와 포트 사용 상태를 반드시 확인해야 하며, 반복 배포를 위해 실행 스크립트에서 기존 프로세스 종료 로직을 포함하는 것이 필요하다는 점을 배웠습니다.

---

## 13. 프로젝트를 통해 배운 점

### 13.1 데이터 기반 서비스 설계

선비마인드는 단순 CRUD 서비스가 아니라 고전 문장 데이터를 기반으로 문제를 생성하고, 사용자의 풀이 기록을 저장하는 학습 서비스입니다.

이를 구현하면서 데이터가 단순히 저장되는 것이 아니라 서비스 흐름 안에서 어떻게 활용되는지 고민할 수 있었습니다.

---

### 13.2 외부 AI API 연동 구조

AI 피드백 기능을 구현하면서 외부 API 호출 구조, 예외 처리, 실패 대응 방식의 중요성을 배웠습니다.

특히 외부 API는 항상 성공한다고 가정하면 안 되며, 장애가 발생하더라도 핵심 서비스가 유지될 수 있도록 설계해야 한다는 점을 경험했습니다.

---

### 13.3 인증이 필요한 사용자 중심 API 설계

내가 푼 문제 조회, 레벨 조회, 학습 기록 저장 기능은 모두 사용자 식별이 필요합니다.

JWT 인증을 기반으로 사용자를 식별하고, 사용자별 데이터를 분리하여 제공하는 구조를 구현하면서 인증과 인가의 역할을 명확히 이해할 수 있었습니다.

---

### 13.4 백엔드 예외 처리의 중요성

AI API 실패, 잘못된 답안 제출, 존재하지 않는 문제 조회, 인증 실패 등 다양한 예외 상황을 처리하면서 백엔드에서 일관된 응답 구조를 제공하는 것이 중요하다는 점을 배웠습니다.

---

### 13.5 배포 환경 구성 경험

로컬 개발 환경을 넘어 GCP VM에 백엔드를 배포하고, CORS, 포트, 환경 변수, 배포 스크립트 등을 설정하면서 실제 서비스 운영에 필요한 기본적인 백엔드 배포 흐름을 경험했습니다.

---

## 14. 향후 개선 방향

### 14.1 문제 추천 기능 고도화

사용자의 오답 기록과 취약한 유형을 분석하여 개인 맞춤형 문제를 추천하는 기능을 추가할 예정입니다.

---

### 14.2 오답 노트 기능 추가

사용자가 틀린 문제를 따로 모아 복습할 수 있도록 오답 노트 기능을 구현할 예정입니다.

---

### 14.3 AI 피드백 품질 개선

사용자의 답변 수준에 따라 더 구체적인 해설을 제공하고, 고전 표현의 실제 활용 예시까지 제공할 수 있도록 AI 피드백 프롬프트를 개선할 예정입니다.

---

### 14.4 관리자용 고전 문장 관리 기능 확장

관리자가 고전 문장을 직접 등록, 수정, 삭제하고 문제 사용 여부를 관리할 수 있는 관리자 기능을 고도화할 예정입니다.

---

### 14.5 랭킹 및 학습 통계 기능 추가

사용자의 누적 학습량, 정답률, 레벨 등을 기반으로 랭킹과 학습 통계를 제공하여 지속적인 학습 동기를 강화할 예정입니다.

---

### 14.6 프론트엔드와의 연동 완성도 향상

프론트엔드 배포 도메인과 백엔드 API 서버를 안정적으로 연동하고, 운영 환경 CORS 및 인증 흐름을 최종적으로 정리할 예정입니다.

---

## 15. 개발자

| 이름 | 역할 |
|---|---|
| 박찬우 | Backend Developer |

### 담당 내용

- Spring Boot 기반 REST API 설계 및 구현
- 고전 문장 데이터베이스 설계
- 문제 조회 및 답안 제출 기능 구현
- AI 훈장님 피드백 연동
- 사용자 학습 기록 조회 API 구현
- JWT 기반 인증 구조 설계
- MySQL 연동 및 JPA Entity 설계
- GCP 기반 백엔드 배포 환경 구성


