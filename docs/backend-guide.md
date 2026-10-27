# 백엔드 개발 가이드

[프로젝트 소개와 주요 설계](../README.md)

## API

보호된 API는 `Authorization: Bearer <accessToken>`으로 인증합니다. 로그인·회원가입 응답에는 Access Token을 담고, Refresh Token은 HttpOnly 쿠키로 발급합니다. 현재 재발급 API는 없으며 로그아웃은 해당 쿠키를 만료시키는 방식입니다.

| Method | 경로 | 기능 | 인증 |
| --- | --- | --- | --- |
| POST | `/api/auth/signup` | 회원가입 | 불필요 |
| POST | `/api/auth/login` | 로그인 | 불필요 |
| POST | `/api/auth/logout` | Refresh Token 쿠키 만료 | 불필요 |
| GET | `/api/auth/me` | 내 정보·진도·오늘의 문장 조회 | 필요 |
| POST | `/api/problems/start` | 문제 시작·이어하기·복습 | 필요 |
| POST | `/api/problems/order-answer/{problemId}` | 단어 순서 답안 제출 | 필요 |
| POST | `/api/problems/copy-typing/{problemId}` | 따라 쓰기 답안 제출 | 필요 |
| POST | `/api/problems/blind-typing/{problemId}` | 뜻을 보지 않고 쓰기 답안 제출 | 필요 |
| GET | `/api/me/problem-history` | 완료 기록을 최근 순으로 조회 | 필요 |

문제 시작 요청은 `{"historyId": 1}`, 각 단계의 답안 요청은 `{"answer": "사용자가 입력한 문장"}` 형태입니다. 시작 응답의 `problemId`를 이후 답안 제출에 사용합니다. 관리자용 문장 CRUD API는 현재 제공하지 않습니다.

### 인증 요청 예시

회원가입 · `POST /api/auth/signup`

```json
{
  "name": "학습자",
  "loginId": "seonbi-demo",
  "password": "example-password"
}
```

로그인 · `POST /api/auth/login`

```json
{
  "loginId": "seonbi-demo",
  "password": "example-password"
}
```

위 값은 요청 형식 설명용이며, 미리 생성된 계정이 아닙니다. 두 요청은 `Content-Type: application/json`으로 전송합니다. `loginId` 대신 `id`도 받을 수 있지만, 둘 다 전달되면 비어 있지 않은 `loginId`를 우선 사용합니다.

로그인·회원가입 응답의 `accessToken`은 이후 보호된 API의 요청 헤더에 넣습니다.

```http
Authorization: Bearer <accessToken>
```

### 응답과 기록 범위

- 진행 중인 세션은 재사용하지만, 문제 시작 응답에는 현재 단계와 이전 답안 필드가 없습니다.
- 각 단계의 답안은 제출할 때마다 덮어쓰며, 완료 기록에는 단계별 최종 답안을 저장합니다. 모든 오답 시도의 이력을 별도로 보존하지는 않습니다.
- `ResponseStatusException`은 `timestamp`, `status`, `error`, `message`, `path` 형식으로 응답합니다. Spring Security가 인증되지 않은 요청을 차단할 때는 401과 `{"message":"인증이 필요합니다."}`를 반환하므로, 모든 오류 응답의 구조가 동일하지는 않습니다.

관련 코드: [SignupRequest](../src/main/java/youngju/seonbimind/auth/dto/SignupRequest.java) · [LoginRequest](../src/main/java/youngju/seonbimind/auth/dto/LoginRequest.java) · [ApiExceptionHandler](../src/main/java/youngju/seonbimind/common/exception/ApiExceptionHandler.java)

## 실행 방법

Java 17과 MySQL을 준비한 뒤 DB 스키마와 접속 계정을 생성합니다. 서버는 기본적으로 8080 포트에서 실행됩니다. 별도 Docker 구성은 필요하지 않습니다.

| 환경변수 | 설정 |
| --- | --- |
| `DB_URL` | 기본값 `jdbc:mysql://localhost:3306/seonbimind?serverTimezone=Asia/Seoul&characterEncoding=UTF-8` |
| `DB_USERNAME` | DB 계정 · 기본값 `seonbi` |
| `DB_PASSWORD` | DB 비밀번호 · 필수 |
| `JWT_SECRET` | 토큰 서명용 비밀값 · 필수 |
| `OPENAI_API_KEY` | 환경변수 등록 필수 · 마지막 단계의 정상 채점에는 유효한 키 필요 |
| `OPENAI_MODEL` | 사용할 모델 ID · 사용 가능한 모델에 맞게 설정 |
| `CORS_ALLOWED_ORIGINS` | 허용할 프론트엔드 주소 · 기본값 `http://localhost:5173` |
| `JPA_DDL_AUTO` | 기본값 `update` · 실행 시 스키마 변경 가능 |

프론트엔드를 로컬 3000 포트에서 실행한다면 `CORS_ALLOWED_ORIGINS=http://localhost:3000`으로 설정합니다. 환경변수는 실행 터미널 또는 IDE 실행 구성에 등록합니다. 현재 저장소에는 `.env` 자동 로딩 설정이 없습니다.

```bash
./gradlew bootRun
```

Windows PowerShell에서는 `./gradlew.bat bootRun`을 사용합니다. 출제에는 `classic_sentences` 데이터가 필요합니다. 저장소에 초기 문장 적재 스크립트가 포함되어 있지 않으므로 원문·독음·뜻과 필수 컬럼을 준비해야 합니다. 문장이 없으면 문제 시작 API는 404를 반환합니다.

설정 상세: [application.properties](../src/main/resources/application.properties)

## 검증 범위와 개선 과제

공개 코드 [2f1f2a5](https://github.com/ParkChanWoo0321/Seonbi-Typing/commit/2f1f2a56c87b38af150348e1b020a03483337091)를 기준으로 소스·테스트 소스 컴파일과 실행 JAR 생성을 확인했습니다.

```bash
./gradlew compileJava compileTestJava bootJar
```

현재 테스트 소스는 `@SpringBootTest`의 컨텍스트 로딩 테스트 1개입니다. 위 확인에는 테스트 실행, 실제 MySQL 연결, OpenAI 호출이 포함되지 않습니다. 처리량이나 응답 시간에 대한 부하 테스트 수치는 없습니다.

| 개선 항목 | 후속 작업 |
| --- | --- |
| 동시 요청 | 동시 시작·최종 답안 중복 제출 테스트를 추가하고, 잠금 또는 멱등성 처리 방식 검토 |
| 인증 수명주기 | Refresh Token 재발급·폐기 구현, 로그아웃 후 Access Token 처리 정책 정리, 직접 구현한 JWT의 시간 클레임을 표준 초 단위로 정비 |
| 외부 채점 | 명시적 시간 제한과 오류 응답 정리, 외부 응답 본문 노출 제한, 채점 호출과 DB 트랜잭션 경계 개선 |
| 조회·출제 | 완료 기록 페이지네이션, 전체 미완료 문장을 메모리에 읽어 섞는 출제 방식 개선 |
| 자동 검증 | 단계 건너뛰기, 다른 회원의 문제 접근, 날짜 경계, 실패 시 롤백에 대한 테스트 추가 |
