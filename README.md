# 선비타이핑 🎓

<img width="112" height="68" alt="Image" src="https://github.com/user-attachments/assets/9ca2d32c-fbf8-47dd-a09d-defdc5bd5c00" />

## 개발자 👤

| 이름 | 역할 |
|---|---|
| 박찬우 | Backend Developer |

## 1. 프로젝트 소개 🚀

**선비타이핑**은 고전 문장, 사자성어, 고사성어와 같은 전통 언어 표현을 단계형 퀴즈와 타이핑 학습 방식으로 익힐 수 있는 **AI 기반 고전 언어 학습 백엔드 서비스**입니다.

사용자는 회원가입과 로그인을 통해 JWT 기반 인증을 거친 뒤, 고전 문장을 단계별로 학습합니다. 학습 과정은 단순히 정답을 맞히는 방식이 아니라, 문장의 의미를 이해하고 직접 재구성하며 반복적으로 입력하는 흐름으로 구성되어 있습니다.

백엔드는 사용자 인증, 고전 문장 문제 출제, 문제 세션 관리, 사용자 답안 채점, GPT API 기반 의미 평가, 풀이 기록 저장, 연속 풀이 일수 계산, 문패 등급 관리 기능을 담당합니다.

특히 마지막 단계에서는 사용자의 답변을 단순 문자열 일치로만 판단하지 않고, GPT API를 활용하여 의미가 같은지 평가합니다. 이를 통해 표현이 조금 다르더라도 문장의 핵심 의미가 유지되면 정답으로 인정할 수 있는 유연한 학습 경험을 제공합니다.

사진 넣을 곳

---

## 2. 프로젝트 기획 배경 📌

<table>
  <tr>
    <td align="center">
      <img 
        src="https://github.com/user-attachments/assets/8ceea43b-fdde-493a-80c5-0a6bf5964ec9" 
        alt="프로젝트 이미지" 
        width="100%"
      />
    </td>
  </tr>
</table>

<br />

디지털 환경이 확산되면서 짧고 자극적인 콘텐츠 소비가 증가하고, 줄임말과 신조어 중심의 언어 사용이 일상화되고 있습니다. 이러한 변화 속에서 고전 문장, 사자성어, 고사성어, 전통적인 우리말 표현과 같은 언어 자산은 점차 일상에서 접하기 어려워지고 있습니다.

현재 영어 학습 서비스나 게임형 언어 학습 플랫폼은 다양하게 존재하지만, 우리 고유의 고전 언어 표현을 쉽고 재미있게 학습할 수 있는 디지털 서비스는 상대적으로 부족합니다. 또한 고전 문장은 한자 원문, 독음, 현대어 해석을 함께 이해해야 학습 효과가 높지만, 기존의 단순 암기 방식만으로는 문장 구조와 의미를 오래 기억하기 어렵습니다.

선비타이핑은 이러한 문제를 해결하기 위해 고전 문장을 단계형 학습 콘텐츠로 재구성하였습니다. 사용자는 문장의 해석을 단어 단위로 재배열하고, 보고 타이핑하며, 마지막에는 기억에 의존하여 의미를 직접 입력하는 방식으로 학습합니다.

이를 통해 단순 암기가 아닌 이해 중심의 반복 학습을 제공하고, 고전 언어 표현을 현대적인 웹 기반 학습 서비스로 확장하고자 하였습니다.

### 수혜 대상

| 대상 | 활용 목적 |
|---|---|
| 사회 초년생 및 직장인 | 보고서 작성, 발표, 커뮤니케이션 과정에서 정확하고 품격 있는 표현 학습 |
| 자기계발에 관심 있는 사용자 | 짧은 시간 안에 교양, 어휘력, 표현력, 문해력 향상 |
| 고전 및 전통 언어 관심 사용자 | 고사성어, 사자성어, 고전 문장의 의미와 활용 맥락 학습 |
| 중장년층 사용자 | 옛 우리말과 전통 표현을 디지털 환경에서 다시 접하는 학습 경험 제공 |

### 서비스 활용 목적

- 고전 언어 표현의 현대적 재해석 및 확산
- 사용자 언어 표현력 및 문해력 향상
- 반복 학습을 통한 지속적인 언어 습득
- 고전 우리말의 대중화
- 전통 언어 자산의 문화적 가치 보존

## 3. 성과 및 회고 🏆

사진 넣을 곳

---

## 4. 주요 기능 ✨

### 4.1 사용자 인증 기능

<table>
  <tr>
    <td width="50%" align="center">
      <img 
        src="https://github.com/user-attachments/assets/e34a475b-5af2-4a4a-b0f0-50204874551f" 
        alt="프로젝트 이미지 1" 
        width="100%"
      />
    </td>
    <td width="50%" align="center">
      <img 
        src="https://github.com/user-attachments/assets/ac5e967d-728c-4d6d-9c6a-1b9edd693ed9" 
        alt="프로젝트 이미지 2" 
        width="100%"
      />
    </td>
  </tr>
</table>
<br />

| 기능 | 설명 |
|---|---|
| 회원가입 | 이름, 로그인 ID, 비밀번호를 입력받아 사용자를 생성합니다. |
| 로그인 | 로그인 ID와 비밀번호를 검증하고 JWT Access Token과 Refresh Token을 발급합니다. |
| 로그아웃 | Refresh Token 쿠키를 만료시켜 로그아웃 처리를 수행합니다. |
| 내 정보 조회 | 사용자 이름, 로그인 ID, 풀이 수, 연속 풀이 일수, 등급, 오늘의 문장을 조회합니다. |

사용자별 학습 기록과 진행도를 관리해야 하므로 JWT 기반 인증 구조를 적용하였습니다. 인증된 사용자는 문제 풀이, 풀이 기록 조회, 진행도 확인 기능을 사용할 수 있습니다.

---

### 4.2 단계형 고전 문장 학습 기능

선비타이핑은 고전 문장을 한 번에 암기하는 방식이 아니라, 단계적으로 이해하고 입력하는 방식으로 학습 흐름을 구성하였습니다.

| 단계 | 기능 | 설명 |
|---|---|---|
| 1단계 | 단어 순서 맞추기 | 해석 문장을 단어 단위로 섞어 제공하고, 사용자가 올바른 순서로 조합합니다. |
| 2단계 | 보고 타이핑 | 해석 문장을 보면서 그대로 입력하고 문자열 비교 방식으로 채점합니다. |
| 3단계 | 안 보고 타이핑 | 문장을 보지 않고 기억한 내용을 입력하며, GPT API를 통해 의미 일치 여부를 평가합니다. |

이 구조를 통해 사용자는 문장의 의미를 단순히 읽고 넘기는 것이 아니라, 직접 재구성하고 입력하면서 자연스럽게 고전 표현을 익힐 수 있습니다.

사진 넣을 곳

---

### 4.3 문제 시작 및 세션 관리 기능

문제 시작 기능은 사용자의 학습 상태에 따라 새 문제 출제, 진행 중 문제 재개, 완료 문제 복습을 구분하여 처리합니다.

| 기능 | 설명 |
|---|---|
| 새 문제 출제 | 사용자가 아직 풀지 않은 고전 문장을 기준으로 새로운 문제 세션을 생성합니다. |
| 진행 중 문제 재개 | 사용자가 문제를 풀다가 중단한 경우 기존 문제 세션을 이어서 제공합니다. |
| 완료 문제 복습 | 이미 완료한 문제는 기록 기반으로 다시 확인할 수 있도록 처리합니다. |
| 오늘의 문장 | 사용자가 당일 처음 시작한 문제를 오늘의 문장으로 표시합니다. |

문제 세션과 풀이 기록을 분리하여 관리함으로써, 사용자가 학습 도중 이탈하더라도 기존 진행 상태를 유지할 수 있도록 구현하였습니다.

사진 넣을 곳

---

### 4.4 AI 훈장님 피드백 기능

마지막 단계인 안 보고 타이핑에서는 사용자의 답변과 정답 문장을 GPT API로 비교하여 의미 일치 여부를 평가합니다.

단순 문자열 비교 방식은 띄어쓰기나 표현 차이에 민감하지만, GPT 기반 의미 평가는 사용자의 답변이 정답과 같은 의미를 가지는지 판단할 수 있습니다.

| 기능 | 설명 |
|---|---|
| 의미 기반 채점 | 사용자의 답변과 정답 해석의 의미가 일치하는지 평가합니다. |
| 정답 피드백 | 정답인 경우 긍정적인 피드백과 함께 문장의 의미를 다시 설명합니다. |
| 오답 피드백 | 오답인 경우 사용자가 놓친 의미를 중심으로 해설을 제공합니다. |
| 훈장님 말투 적용 | 서비스 콘셉트에 맞게 서당 훈장님 스타일의 피드백을 제공합니다. |

이를 통해 사용자는 단순히 맞고 틀림만 확인하는 것이 아니라, 자신의 답변이 어떤 부분에서 정확했는지 또는 부족했는지 이해할 수 있습니다.

사진 넣을 곳

---

### 4.5 고전 표현 해설 기능

문제 풀이 후에는 고전 문장의 원문, 독음, 현대어 의미, 해설을 함께 제공합니다.

| 제공 정보 | 설명 |
|---|---|
| 원문 | 고전 문장의 한자 또는 원문 표현 |
| 독음 | 사용자가 읽을 수 있도록 제공되는 발음 정보 |
| 현대어 뜻 | 고전 문장의 현대적 해석 |
| 해설 | 문장의 의미와 학습 맥락 설명 |

이를 통해 사용자는 고전 표현을 단순 암기하는 것이 아니라, 표현의 뜻과 활용 맥락까지 함께 이해할 수 있습니다.

사진 넣을 곳

---

### 4.6 학습 기록 저장 기능

사용자가 완료한 문제는 풀이 기록으로 저장됩니다.

| 기능 | 설명 |
|---|---|
| 풀이 기록 저장 | 사용자가 완료한 문제의 원문, 독음, 뜻, 답안, 해설을 저장합니다. |
| 풀이 기록 조회 | 사용자가 이전에 푼 문제 목록을 다시 확인할 수 있습니다. |
| 정답 여부 저장 | 사용자의 답변이 정답인지 오답인지 저장합니다. |
| 학습 데이터 누적 | 향후 오답 노트, 복습 추천, 개인화 학습 기능으로 확장할 수 있습니다. |

풀이 결과를 단순 응답으로 끝내지 않고 데이터베이스에 저장하여, 사용자별 학습 흐름을 지속적으로 관리할 수 있도록 설계하였습니다.

사진 넣을 곳

---

### 4.7 레벨 기반 성장 시스템

사용자의 지속적인 학습 참여를 유도하기 위해 전통 관직 명칭을 활용한 문패 등급 시스템을 적용하였습니다.

| 레벨 | 등급 |
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

사용자는 문제 풀이를 통해 학습 경험을 쌓고, 총 풀이 수와 진행도에 따라 단계별로 승급합니다. 이 등급 구조는 사용자의 학습 성과를 직관적으로 보여주는 지표로 작용하며, 지속적인 서비스 이용을 유도합니다.

사진 넣을 곳

---

### 4.8 학습 진행도 관리 기능

선비타이핑은 사용자의 학습 활동을 기반으로 진행도를 계산합니다.

| 기능 | 설명 |
|---|---|
| 전체 풀이 수 | 사용자가 최종 완료한 문제 수를 누적 저장합니다. |
| 연속 풀이 일수 | 한국 시간 기준으로 매일 1문제 이상 풀었는지 계산합니다. |
| 등급 계산 | 총 풀이 수에 따라 현재 문패 등급을 계산합니다. |
| 오늘의 문장 조회 | 당일 학습한 문장을 사용자 정보와 함께 제공합니다. |

이를 통해 사용자는 자신의 학습 성과를 확인할 수 있으며, 서비스는 사용자별 학습 상태를 기반으로 향후 맞춤형 복습 기능으로 확장할 수 있습니다.

사진 넣을 곳

## 5. 기술 스택 🛠️

| 구분 | 기술 |
|---|---|
| Language | Java 17 |
| Framework | Spring Boot 4.0.5 |
| Web | Spring Web MVC |
| Security | Spring Security |
| Authentication | JWT |
| ORM | Spring Data JPA |
| Database | MySQL |
| Build Tool | Gradle |
| Library | Lombok |
| External API | OpenAI Responses API |
| Test | JUnit Platform, Spring Boot Test Dependencies |

## 6. 시스템 구조 🧩

사진 넣을 곳

선비타이핑은 Controller, Service, Repository, Entity를 기준으로 계층을 분리한 구조입니다. Controller는 HTTP 요청과 응답을 담당하고, Service는 인증된 사용자 기준의 비즈니스 로직을 처리하며, Repository는 Spring Data JPA를 통해 데이터베이스에 접근합니다.

```text
Client
  ↓
Controller
  ↓
Service
  ↓
Repository
  ↓
Database
```

인증 흐름은 JWT 기반으로 구성되어 있습니다. 로그인 또는 회원가입 성공 시 Access Token은 응답 body로 내려주고, Refresh Token은 `HttpOnly` 쿠키로 내려줍니다. 이후 인증이 필요한 API는 `Authorization: Bearer {accessToken}` 헤더를 통해 호출합니다.

```text
Client Request
  ↓
JwtAuthenticationFilter
  ↓
JwtTokenProvider
  ↓
SecurityContext 인증 정보 저장
  ↓
Controller 진입
```

`SecurityConfig`에서는 CSRF, Form Login, HTTP Basic, 기본 Logout을 비활성화하고, 세션 정책을 `STATELESS`로 설정했습니다. `/api/auth/signup`, `/api/auth/login`, `/api/auth/logout`, `/error`, `OPTIONS /**` 요청은 허용하고, 그 외 API는 인증을 요구합니다.

## 7. 백엔드 핵심 구현 내용 🔥

### JWT 기반 인증/인가 구조

JWT 인증은 `JwtTokenProvider`와 `JwtAuthenticationFilter`로 분리했습니다. `JwtTokenProvider`는 HMAC SHA-256 방식으로 Access Token과 Refresh Token을 생성하고, 토큰 payload에는 사용자 ID, 로그인 ID, 이름, 토큰 타입, 발급 시각, 만료 시각을 포함합니다.

`JwtAuthenticationFilter`는 모든 요청에서 `Authorization` 헤더를 확인하고, 유효한 Access Token이면 로그인 ID로 회원을 조회한 뒤 `SecurityContextHolder`에 인증 객체를 저장합니다. 이 구조를 통해 Controller나 Service에서 request body로 사용자 ID를 받지 않고도 현재 로그인한 사용자를 안전하게 식별할 수 있습니다.

### 회원가입/로그인 구조

회원가입은 이름, 로그인 ID, 비밀번호를 입력받아 처리합니다. 비밀번호는 `BCryptPasswordEncoder`로 암호화하여 저장하고, 로그인 ID는 DB unique 제약 조건과 서비스 레벨 중복 검사로 보호합니다.

로그인은 로그인 ID로 사용자를 조회한 뒤 BCrypt로 비밀번호를 검증합니다. 인증에 성공하면 Access Token과 Refresh Token을 발급하고, Refresh Token은 `HttpOnly` 쿠키에 담아 내려줍니다. 이 방식은 프론트엔드가 Access Token을 활용해 API를 호출하면서도 Refresh Token을 JavaScript에서 직접 다루지 않도록 구성한 것입니다.

### 주요 도메인 설계

문제 풀이 도메인은 `ClassicSentence`, `ProblemSession`, `SolvedProblemHistory`, `UserProgress`, `UserSentenceUsage`로 나누어 설계했습니다.

`ClassicSentence`는 고전 문장 원본 데이터입니다. `ProblemSession`은 사용자가 현재 풀고 있는 문제 상태를 저장합니다. 사용자가 문제를 시작하면 세션이 생성되고, 단어 순서 맞추기, 보고 타이핑, 안 보고 타이핑 단계를 거치며 `stage` 값이 변경됩니다.

최종 완료된 문제는 `SolvedProblemHistory`에 별도로 저장합니다. 진행 중인 세션과 완료 기록을 분리했기 때문에, 중간에 실패하거나 이탈한 문제는 완료 기록으로 처리되지 않습니다. 또한 `UserProgress`는 총 풀이 수와 연속 풀이 일수를 관리하고, `UserSentenceUsage`는 사용자별로 이미 사용한 문장을 기록하여 여러 사용자가 독립적으로 문제를 풀 수 있도록 했습니다.

### 문제 시작과 복습 흐름 설계

문제 시작 API는 `historyId`를 요청 body로 받습니다. 이 값은 DB PK가 아니라 사용자 기준 몇 번째 문제인지를 의미합니다.

이미 완료한 `historyId`를 요청하면 새 문제를 출제하지 않고 기존 풀이 기록을 반환합니다. 다음으로 풀어야 할 `historyId`를 요청하면 진행 중 문제가 있는지 먼저 확인하고, 없을 때만 새 문제를 뽑습니다. 아직 접근할 수 없는 미래 번호를 요청하면 400 에러를 반환합니다.

이 설계는 같은 사용자가 같은 문제 번호를 여러 번 요청해도 중복 데이터가 생기지 않도록 하고, 프론트엔드에서 “1번 문제, 2번 문제, 3번 문제”처럼 사용자 기준 학습 순서를 안정적으로 다룰 수 있게 합니다.

### 3단계 문제 풀이 구조

문제 풀이는 `ORDER`, `COPY_TYPING`, `BLIND_TYPING`, `COMPLETED` 단계로 관리됩니다. 각 단계는 이전 단계를 성공해야 다음 단계로 이동할 수 있습니다.

1단계에서는 해석 문장을 단어 단위로 섞어 제공하고, 사용자가 조합한 문장을 정답 해석과 비교합니다. 2단계에서는 해석 문장을 보고 그대로 타이핑하며 문자열 비교를 수행합니다. 3단계에서는 사용자가 문장을 보지 않고 입력한 답안을 GPT API로 평가합니다.

문제를 완료한 것으로 인정되는 시점은 GPT 의미 채점까지 성공한 경우입니다. 이때만 문장 사용 처리, 사용자별 문장 사용 기록 저장, 총 풀이 수 증가, 연속 풀이 일수 갱신, 풀이 기록 저장이 수행됩니다.

### GPT API 기반 의미 채점

`GptMeaningEvaluationService`는 OpenAI Responses API 호출을 담당합니다. API Key, 모델명, 호출 URL은 `application.properties`와 환경 변수를 통해 주입받으며, 코드에 직접 하드코딩하지 않았습니다.

GPT 응답은 JSON Schema 형식으로 제한하여 `correct`와 `reason` 값을 받도록 구성했습니다. `reason`은 한국어 훈장님 말투로 간결하고 따뜻하게 작성하도록 프롬프트를 구성했습니다. 문자열이 완전히 같지 않아도 의미가 유지되면 정답으로 처리할 수 있어, 고전 문장 학습에 더 적합한 채점 방식을 제공합니다.

### 사용자 진행도와 등급 계산

`UserProgress`는 사용자의 총 풀이 수, 현재 연속 풀이 일수, 마지막 풀이 날짜를 저장합니다. 날짜 계산은 `Asia/Seoul` 기준으로 수행합니다.

총 풀이 수는 절대 초기화되지 않고, 최종 완료된 문제 수만 누적됩니다. 등급은 `LearningRank` enum에서 총 풀이 수 기준으로 계산하며, 도사부터 영의정까지 단계적으로 상승합니다. `api/auth/me` 응답에는 현재 등급, 다음 등급, 다음 등급까지 남은 문제 수가 포함됩니다.

### 예외 처리 구조

비즈니스 예외는 `ResponseStatusException`을 사용하고, `ApiExceptionHandler`에서 공통 JSON 응답으로 변환합니다. 응답에는 timestamp, status, error, message, path가 포함됩니다.

이를 통해 API 실패 시 프론트엔드가 일관된 구조로 에러 메시지를 처리할 수 있습니다. 인증 실패는 Spring Security의 `authenticationEntryPoint`에서 별도의 JSON 메시지로 처리합니다.

### CORS/Security 설정

CORS 허용 Origin은 `app.cors.allowed-origins` 설정값으로 관리합니다. 기본값은 `http://localhost:5173`이며, 쉼표로 여러 Origin을 설정할 수 있습니다.

프론트엔드 연동을 고려하여 `Authorization` 헤더를 노출하고, 쿠키 기반 Refresh Token 처리를 위해 credentials를 허용했습니다. 인증이 필요한 API는 JWT 필터를 거쳐야 하며, 회원가입과 로그인 API만 인증 없이 호출할 수 있습니다.

## 8. API 명세 📡

| 기능 | Method | URL | 인증 필요 여부 | 설명 |
|---|---|---|---|---|
| 회원가입 | POST | `/api/auth/signup` | 불필요 | 이름, 로그인 ID, 비밀번호로 회원가입합니다. |
| 로그인 | POST | `/api/auth/login` | 불필요 | 로그인 ID와 비밀번호를 검증하고 토큰을 발급합니다. |
| 로그아웃 | POST | `/api/auth/logout` | 불필요 | Refresh Token 쿠키를 만료합니다. |
| 내 정보 조회 | GET | `/api/auth/me` | 필요 | 사용자 정보, 진행도, 등급, 오늘의 문장을 조회합니다. |
| 문제 시작 | POST | `/api/problems/start` | 필요 | `historyId` 기준으로 새 문제, 진행 중 문제, 복습 문제를 반환합니다. |
| 단어 순서 제출 | POST | `/api/problems/order-answer/{problemId}` | 필요 | 단어 순서 맞추기 답안을 제출합니다. |
| 보고 타이핑 제출 | POST | `/api/problems/copy-typing/{problemId}` | 필요 | 보고 타이핑 답안을 제출합니다. |
| 안 보고 타이핑 제출 | POST | `/api/problems/blind-typing/{problemId}` | 필요 | 안 보고 타이핑 답안을 제출하고 GPT 의미 채점을 수행합니다. |
| 풀이 기록 조회 | GET | `/api/me/problem-history` | 필요 | 사용자가 완료한 문제 기록을 조회합니다. |

## 9. API 요청/응답 예시 🧾

### 회원가입

Request

```json
{
  "name": "박찬우",
  "loginId": "seonbi",
  "password": "password1234"
}
```

Response

```json
{
  "name": "박찬우",
  "accessToken": "access-token-value",
  "loginId": "seonbi",
  "totalSolvedCount": 0,
  "currentStreak": 0,
  "currentRank": "도사",
  "nextRank": "정랑",
  "remainingToNextRank": 1,
  "todaySentence": null
}
```

### 로그인

Request

```json
{
  "loginId": "seonbi",
  "password": "password1234"
}
```

Response

```json
{
  "name": "박찬우",
  "accessToken": "access-token-value",
  "loginId": "seonbi",
  "totalSolvedCount": 7,
  "currentStreak": 3,
  "currentRank": "사인",
  "nextRank": "집의",
  "remainingToNextRank": 3,
  "todaySentence": {
    "sentenceId": 10,
    "originalText": "天地元無酒後愁",
    "readingText": "천지원무주후수",
    "meaning": "천지에는 본래 술 뒤의 근심이 없다"
  }
}
```

### 내 정보 조회

Request

```http
GET /api/auth/me
Authorization: Bearer access-token-value
```

Response

```json
{
  "name": "박찬우",
  "accessToken": "access-token-value",
  "loginId": "seonbi",
  "totalSolvedCount": 7,
  "currentStreak": 3,
  "currentRank": "사인",
  "nextRank": "집의",
  "remainingToNextRank": 3,
  "todaySentence": null
}
```

### 문제 시작

Request

```json
{
  "historyId": 1
}
```

Response

```json
{
  "historyId": 1,
  "problemId": 10,
  "sentenceId": 25,
  "isTodaySentence": true,
  "completed": false,
  "reviewMode": false,
  "inProgress": true,
  "originalText": "天地元無酒後愁",
  "readingText": "천지원무주후수",
  "meaning": "천지에는 본래 술 뒤의 근심이 없다",
  "shuffledWords": ["술", "없다", "천지에는", "근심이", "본래", "뒤의"]
}
```

### 단어 순서 제출

Request

```json
{
  "answer": "천지에는 본래 술 뒤의 근심이 없다"
}
```

Response

```json
{
  "problemId": 10,
  "correct": true,
  "nextStep": "COPY_TYPING",
  "completed": false,
  "gptCorrect": null,
  "gptReason": null
}
```

### 보고 타이핑 제출

Request

```json
{
  "answer": "천지에는 본래 술 뒤의 근심이 없다"
}
```

Response

```json
{
  "problemId": 10,
  "correct": true,
  "nextStep": "BLIND_TYPING",
  "completed": false,
  "gptCorrect": null,
  "gptReason": null
}
```

### 안 보고 타이핑 제출

Request

```json
{
  "answer": "천지에는 원래 술 뒤의 근심이 없다"
}
```

Response

```json
{
  "problemId": 10,
  "correct": true,
  "nextStep": "COMPLETED",
  "completed": true,
  "gptCorrect": true,
  "gptReason": "잘하였네. 표현은 조금 다르지만 본래 술 뒤의 근심이 없다는 뜻을 온전히 담고 있구나."
}
```

### 풀이 기록 조회

Request

```http
GET /api/me/problem-history
Authorization: Bearer access-token-value
```

Response

```json
[
  {
    "historyId": 1,
    "originalText": "天地元無酒後愁",
    "readingText": "천지원무주후수",
    "meaning": "천지에는 본래 술 뒤의 근심이 없다",
    "userAnswer": "천지에는 원래 술 뒤의 근심이 없다",
    "correct": true,
    "explanation": "잘하였네. 표현은 조금 다르지만 본래 술 뒤의 근심이 없다는 뜻을 온전히 담고 있구나.",
    "solvedAt": "2026-04-29T09:59:02.670601"
  }
]
```

### 에러 응답

```json
{
  "timestamp": "2026-05-08T12:00:00",
  "status": 400,
  "error": "Bad Request",
  "message": "historyId is required.",
  "path": "/api/problems/start"
}
```

## 10. 데이터베이스 설계 🗄️

### 주요 테이블 요약

| 테이블 | 설명 |
|---|---|
| `members` | 서비스 사용자 정보를 저장합니다. |
| `classic_sentences` | 고전 문장 원문, 독음, 해석, 사용 여부를 저장합니다. |
| `problem_sessions` | 사용자가 진행 중이거나 완료한 문제 세션 상태를 저장합니다. |
| `user_sentence_usages` | 사용자별로 이미 사용한 문장을 저장합니다. |
| `user_progress` | 사용자별 총 풀이 수, 연속 풀이 일수, 마지막 풀이 날짜를 저장합니다. |
| `solved_problem_histories` | 최종 완료된 문제 풀이 기록을 저장합니다. |

### members

| 컬럼 | 설명 |
|---|---|
| `id` | 사용자 PK |
| `name` | 사용자 이름 |
| `login_id` | 로그인 ID, unique 제약 조건 적용 |
| `password` | BCrypt로 암호화된 비밀번호 |

### classic_sentences

| 컬럼 | 설명 |
|---|---|
| `id` | 고전 문장 PK |
| `original_text` | 한자 원문 |
| `reading_text` | 한글 독음 |
| `meaning` | 해석 문장 |
| `used` | 문장이 문제로 사용되었는지 여부 |
| `created_at` | 생성 시각 |
| `updated_at` | 수정 시각 |

### problem_sessions

| 컬럼 | 설명 |
|---|---|
| `id` | 문제 세션 PK |
| `member_id` | 사용자 FK |
| `sentence_id` | 고전 문장 FK |
| `history_id` | 사용자 기준 풀이 순번 |
| `today_sentence` | 오늘의 문장 여부 |
| `shuffled_words` | 섞인 단어 목록을 문자열로 저장 |
| `stage` | 현재 단계: `ORDER`, `COPY_TYPING`, `BLIND_TYPING`, `COMPLETED` |
| `user_ordered_answer` | 단어 순서 맞추기 답안 |
| `user_copy_typing_answer` | 보고 타이핑 답안 |
| `user_blind_typing_answer` | 안 보고 타이핑 답안 |
| `gpt_correct` | GPT 의미 채점 결과 |
| `gpt_reason` | GPT 채점 사유 |
| `correct` | 최종 정답 여부 |
| `completed` | 최종 완료 여부 |
| `created_at` | 생성 시각 |
| `updated_at` | 수정 시각 |
| `completed_at` | 완료 시각 |

`problem_sessions`는 `member_id`와 `history_id` 조합에 unique 제약 조건을 두어, 같은 사용자가 같은 풀이 순번으로 중복 세션을 만들지 않도록 설계했습니다.

### user_sentence_usages

| 컬럼 | 설명 |
|---|---|
| `id` | 사용자별 문장 사용 기록 PK |
| `member_id` | 사용자 FK |
| `sentence_id` | 고전 문장 FK |
| `used_at` | 사용 처리 시각 |

`user_sentence_usages`는 `member_id`, `sentence_id` 조합에 unique 제약 조건을 두어 사용자별 문장 중복 풀이를 방지합니다.

### user_progress

| 컬럼 | 설명 |
|---|---|
| `id` | 사용자 진행도 PK |
| `member_id` | 사용자 FK, unique 제약 조건 적용 |
| `total_solved_count` | 최종 완료한 총 문제 수 |
| `current_streak` | 현재 연속 풀이 일수 |
| `last_solved_date` | 마지막 풀이 날짜 |
| `updated_at` | 수정 시각 |

### solved_problem_histories

| 컬럼 | 설명 |
|---|---|
| `id` | 풀이 기록 DB PK |
| `member_id` | 사용자 FK |
| `sentence_id` | 고전 문장 FK |
| `history_id` | 사용자 기준 풀이 순번 |
| `problem_session_id` | 연결된 문제 세션 ID |
| `today_sentence` | 오늘의 문장 여부 |
| `original_text` | 풀이 당시 한자 원문 |
| `reading_text` | 풀이 당시 독음 |
| `meaning` | 풀이 당시 해석 |
| `shuffled_words` | 풀이 당시 섞인 단어 목록 |
| `user_ordered_answer` | 단어 순서 맞추기 답안 |
| `user_copy_typing_answer` | 보고 타이핑 답안 |
| `user_blind_typing_answer` | 안 보고 타이핑 답안 |
| `gpt_correct` | GPT 의미 채점 결과 |
| `gpt_reason` | GPT 채점 사유 |
| `correct` | 최종 정답 여부 |
| `explanation` | 풀이 해설 |
| `solved_at` | 풀이 완료 시각 |

### Entity 관계

| 관계 | 설명 |
|---|---|
| `members` 1 : N `problem_sessions` | 한 사용자는 여러 문제 세션을 가질 수 있습니다. |
| `classic_sentences` 1 : N `problem_sessions` | 하나의 문장은 여러 문제 세션에서 참조될 수 있습니다. |
| `members` 1 : N `solved_problem_histories` | 한 사용자는 여러 완료 기록을 가질 수 있습니다. |
| `classic_sentences` 1 : N `solved_problem_histories` | 하나의 문장은 여러 완료 기록에서 참조될 수 있습니다. |
| `members` 1 : 1 `user_progress` | 사용자별 진행도는 하나만 존재합니다. |
| `members` 1 : N `user_sentence_usages` | 사용자별 문장 사용 여부를 독립적으로 기록합니다. |

## 11. 프로젝트 구조 📁

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

## 12. 트러블슈팅 🧯

### JWT 인증 실패

**문제 상황**  
인증이 필요한 API를 호출했을 때 401 응답이 발생하고, 서버에서 인증된 사용자를 찾을 수 없는 문제가 발생할 수 있습니다.

**원인**  
`Authorization` 헤더가 없거나 `Bearer ` 접두사가 빠진 경우, Access Token이 만료된 경우, 또는 `jwt.secret` 값이 토큰 생성 시점과 검증 시점에 다르면 JWT 검증에 실패합니다.

**해결 방법**  
클라이언트에서 `Authorization: Bearer {accessToken}` 형식으로 헤더를 전달하도록 하고, 서버 실행 환경의 `JWT_SECRET` 값을 일관되게 설정합니다. 인증 필터에서는 Access Token 타입과 만료 시간을 검증한 뒤에만 `SecurityContextHolder`에 인증 정보를 저장하도록 구성했습니다.

**결과**  
인증이 필요한 문제 풀이 API와 내 정보 조회 API에서 request body로 사용자 ID를 받지 않고도 현재 로그인 사용자를 안정적으로 식별할 수 있게 되었습니다.

### DB 연동 오류

**문제 상황**  
서버 실행 시 DataSource 설정 오류가 발생하거나 MySQL 연결에 실패할 수 있습니다.

**원인**  
`DB_URL`, `DB_USERNAME`, `DB_PASSWORD` 환경 변수가 올바르게 설정되지 않았거나, MySQL 데이터베이스가 생성되지 않은 상태에서 애플리케이션을 실행하면 연결에 실패합니다.

**해결 방법**  
`application.properties`에서 MySQL 드라이버와 datasource 설정을 명확히 지정하고, 환경 변수로 DB 접속 정보를 주입하도록 구성했습니다. 로컬 실행 전 `seonbimind` 데이터베이스를 생성하고 계정 권한을 확인해야 합니다.

**결과**  
환경별 DB 접속 정보를 코드에 직접 작성하지 않고 분리할 수 있어, 로컬 개발 환경과 배포 환경에서 설정을 유연하게 변경할 수 있습니다.

### GPT API 키 누락 또는 외부 API 호출 실패

**문제 상황**  
안 보고 타이핑 단계에서 GPT 의미 채점을 수행할 때 503 또는 502 응답이 발생할 수 있습니다.

**원인**  
`OPENAI_API_KEY`가 설정되지 않으면 서비스는 503 응답을 반환합니다. API Key가 설정되어 있어도 OpenAI API에서 quota, 인증, 네트워크 오류가 발생하면 502 응답으로 변환됩니다.

**해결 방법**  
`GptMeaningEvaluationService`에서 API Key가 비어 있는 경우를 먼저 검사하고, OpenAI API 호출 실패는 `ResponseStatusException`으로 감싸 공통 예외 응답 구조로 내려주도록 처리했습니다. API Key와 모델명은 환경 변수 기반 설정으로 분리했습니다.

**결과**  
GPT 채점 실패 상황을 프론트엔드에서 일관된 에러 응답으로 처리할 수 있고, 민감한 API Key를 코드에 하드코딩하지 않게 되었습니다.

### 문제 중복 출제와 진행 중 문제 재시작 문제

**문제 상황**  
사용자가 같은 문제 번호로 여러 번 문제 시작 API를 호출하면 새 문제가 중복으로 출제될 수 있습니다.

**원인**  
문제 시작 API가 단순히 호출될 때마다 새 문장을 뽑는 방식이면, 사용자의 풀이 순번과 진행 중 세션을 구분하기 어렵습니다.

**해결 방법**  
`historyId`를 사용자 기준 풀이 순번으로 사용하고, `problem_sessions`에 `member_id`, `history_id` unique 제약 조건을 적용했습니다. 문제 시작 시 이미 완료한 번호는 복습 모드로 반환하고, 진행 중인 번호는 기존 세션을 재사용하며, 다음 번호일 때만 새 문제를 출제하도록 분기했습니다.

**결과**  
프론트엔드가 같은 문제 번호를 다시 요청해도 중복 데이터가 생성되지 않고, 사용자는 진행 중이던 문제를 안정적으로 이어서 풀 수 있습니다.

### 사용자별 풀이 기록 순번 문제

**문제 상황**  
DB PK를 그대로 `historyId`로 응답하면 여러 사용자가 함께 사용할 때 사용자별 1번, 2번, 3번 문제 구조가 깨질 수 있습니다.

**원인**  
DB PK는 전체 테이블 기준으로 증가하므로, A 사용자의 두 번째 풀이 기록 ID가 다른 사용자의 기록 때문에 3 또는 4가 될 수 있습니다.

**해결 방법**  
`SolvedProblemHistory`에 DB PK와 별개로 사용자 기준 `historyId`를 추가하고, `member_id`, `history_id` 조합을 unique로 관리했습니다. 기존 기록 중 `historyId`가 비어 있는 경우에는 사용자별 풀이 완료 시각 기준으로 순번을 보정하도록 구현했습니다.

**결과**  
각 사용자가 자신의 풀이 기록을 1번부터 순차적으로 조회할 수 있게 되었고, 문제 복습 API에서도 사용자 기준 순번을 안정적으로 사용할 수 있습니다.

## 13. 프로젝트를 통해 배운 점 🌱

이 프로젝트를 구현하면서 계층형 아키텍처의 역할 분리가 왜 중요한지 직접 경험했습니다. Controller는 요청과 응답을 처리하고, Service는 인증된 사용자 기준의 비즈니스 흐름을 담당하며, Repository는 JPA 쿼리와 데이터 접근에 집중하도록 나누었습니다. 그 결과 문제 풀이, 진행도, 인증 로직이 서로 섞이지 않고 유지보수하기 쉬운 구조가 되었습니다.

JWT 인증을 직접 구현하면서 Access Token과 Refresh Token의 역할을 분리하고, Security Filter에서 인증 객체를 구성하는 흐름을 이해할 수 있었습니다. 특히 인증된 사용자 정보를 request body로 받지 않고 토큰에서 가져오는 구조를 적용하면서, API 보안과 데이터 신뢰성을 함께 고려하는 경험을 했습니다.

JPA Entity 설계에서는 진행 중인 문제와 완료된 풀이 기록을 분리하는 방식이 중요했습니다. 문제를 시작했다고 바로 완료 기록을 만들지 않고, 최종 GPT 의미 채점까지 성공했을 때만 기록과 진행도를 갱신하도록 설계했습니다. 이를 통해 실제 서비스에서 사용자의 중간 이탈, 재시도, 복습 흐름을 더 안정적으로 처리할 수 있었습니다.

또한 프론트엔드 연동을 고려해 DTO를 분리하고, 응답에 `completed`, `reviewMode`, `inProgress`, `historyId` 같은 상태 정보를 포함했습니다. 이 과정에서 백엔드 API가 단순 데이터 제공을 넘어 프론트엔드 화면 흐름을 안정적으로 이끌 수 있어야 한다는 점을 배웠습니다.

## 14. 향후 개선 방향 🔧

| 개선 방향 | 설명 |
|---|---|
| 테스트 코드 작성 | 인증, 문제 풀이 단계, GPT 채점 실패, 진행 중 문제 재개 등 핵심 흐름에 대한 단위 테스트와 통합 테스트를 추가할 수 있습니다. |
| Swagger API 문서화 | 현재 README와 코드 기준으로 정리된 API를 Swagger/OpenAPI로 문서화하면 프론트엔드와 협업 효율을 높일 수 있습니다. |
| Refresh Token 저장소 개선 | 현재 Refresh Token은 쿠키로 내려주지만 서버 저장소는 없습니다. Redis 또는 DB 기반 저장소를 추가하면 재발급과 강제 로그아웃 처리를 더 안전하게 구현할 수 있습니다. |
| 예외 응답 구조 통일 | Spring Security 인증 실패 응답과 `ApiExceptionHandler` 응답 구조를 더 통일하면 클라이언트 에러 처리가 쉬워집니다. |
| 로그 관리 | 문제 풀이 실패, GPT API 호출 실패, 인증 실패 등에 대한 로그를 체계적으로 남기면 운영 환경에서 원인 분석이 쉬워집니다. |
| 관리자 기능 확장 | 현재 관리자 API는 없으므로, 고전 문장 등록·수정·삭제 기능을 별도 권한 기반으로 확장할 수 있습니다. |
| 보안 설정 강화 | 운영 환경에서는 Refresh Token 쿠키의 `secure` 옵션을 true로 설정하고, CORS 허용 Origin을 배포 도메인으로 제한할 수 있습니다. |
