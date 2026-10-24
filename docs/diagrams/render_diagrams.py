"""Render the README diagrams with Pillow (Python 3, Pillow, Korean font)."""

from pathlib import Path
import os
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
FONT = os.environ.get("DIAGRAM_FONT", "C:/Windows/Fonts/malgun.ttf")
BOLD = os.environ.get("DIAGRAM_BOLD_FONT", "C:/Windows/Fonts/malgunbd.ttf")
INK, MUTED, BORDER = "#16332D", "#52665E", "#CFDBD5"
GREEN, GOLD = "#26705C", "#9B6B23"


class Canvas:
    def __init__(self, width, height):
        self.im = Image.new("RGB", (width, height), "#F7F8F4")
        self.d = ImageDraw.Draw(self.im)

    def text(self, x, y, text, size=24, fill=INK, bold=False):
        font = ImageFont.truetype(BOLD if bold else FONT, size)
        self.d.text((x, y), text, font=font, fill=fill, anchor="lt")

    def box(self, xy, fill="#FFFFFF", border=BORDER, radius=16):
        self.d.rounded_rectangle(xy, radius, fill, border, 2)

    def line(self, pts, color=GREEN, width=3, arrow=False):
        self.d.line(pts, fill=color, width=width)
        if arrow:
            x, y = pts[-1]
            px, py = pts[-2]
            if x > px:
                tip = [(x, y), (x-12, y-7), (x-12, y+7)]
            elif x < px:
                tip = [(x, y), (x+12, y-7), (x+12, y+7)]
            elif y > py:
                tip = [(x, y), (x-7, y-12), (x+7, y-12)]
            else:
                tip = [(x, y), (x-7, y+12), (x+7, y+12)]
            self.d.polygon(tip, fill=color)

    def save(self, name):
        self.im.save(OUT / name)


def architecture():
    c = Canvas(1600, 960)
    c.text(60, 42, "선비타이핑 · 백엔드 아키텍처", 38, bold=True)
    c.text(60, 102, "공개 저장소의 소스 구조 | 단일 Spring Boot 애플리케이션", 23, MUTED)
    c.box((400, 175, 1110, 835), fill="#EDF3EE")
    c.text(430, 199, "Spring Boot 4.0.5 / Java 17", 28, bold=True)
    c.box((60, 290, 310, 435))
    c.text(85, 318, "웹 클라이언트", 27, bold=True)
    c.text(85, 368, "프론트엔드 영역", 21, MUTED)
    blocks = [
        (275, "Security Filter Chain", "JWT 검증 · 인증 정보 설정 · CORS"),
        (405, "Controller", "AuthController · ProblemController · MeProgressController"),
        (535, "Service", "AuthService · ProblemService · ProgressService"),
        (695, "JPA Repository", "회원 · 문장 · 문제 세션 · 사용 이력 · 진도 · 완료 기록"),
    ]
    for y, title, desc in blocks:
        c.box((430, y, 1080, y+100))
        c.text(452, y+15, title, 26, bold=True)
        c.text(452, y+56, desc, 20, MUTED)
    for start, end in [(375, 405), (505, 535), (635, 695)]:
        c.line([(755, start), (755, end)], arrow=True)
    c.line([(310, 325), (430, 325)], arrow=True)
    c.text(320, 268, "HTTP", 20)
    c.text(64, 472, "보호된 API 요청", 21, MUTED)
    c.text(64, 508, "Authorization:", 20, MUTED)
    c.text(64, 540, "Bearer <accessToken>", 19, MUTED)
    c.box((1200, 680, 1540, 825))
    c.text(1224, 706, "MySQL", 29, bold=True)
    c.text(1224, 754, "6개 테이블 · JPA 매핑", 22, MUTED)
    c.line([(1080, 745), (1200, 745)], arrow=True)
    c.text(1120, 708, "SQL", 20)
    c.box((1200, 365, 1540, 585), fill="#FCF6E9")
    c.text(1224, 392, "OpenAI Responses API", 23, bold=True)
    c.text(1224, 441, "뜻을 보지 않고 쓰기 채점", 22, MUTED)
    c.text(1224, 483, "JSON Schema", 23, bold=True)
    c.text(1224, 526, "correct / reason", 22, MUTED)
    c.line([(1080, 585), (1150, 585), (1150, 475), (1200, 475)], GOLD, arrow=True)
    c.text(1200, 610, "GptMeaningEvaluationService", 19, GOLD)
    c.text(1200, 641, "RestClient 동기 호출", 20, GOLD)
    c.text(60, 880, "화살표는 호출 방향을 나타냅니다. 응답 경로와 배포 인프라는 생략했습니다.", 23, MUTED)
    c.save("architecture.png")


def erd():
    c = Canvas(1680, 1120)
    c.text(60, 40, "선비타이핑 · ERD", 38, bold=True)
    c.text(60, 99, "JPA 엔티티 기준 · 핵심 컬럼만 표기 · PK: 기본키 / FK: 외래키 / UQ: 유니크 제약", 22, MUTED)
    c.box((60, 160, 690, 300))
    c.text(82, 178, "members", 28, GREEN, True)
    c.text(82, 225, "id PK   ·   login_id UQ   ·   name   ·   password", 23)
    c.box((990, 160, 1620, 300))
    c.text(1012, 178, "classic_sentences", 28, GOLD, True)
    c.text(1012, 225, "id PK   ·   original_text   ·   reading_text", 23)
    c.text(1012, 261, "meaning   ·   used", 23)
    c.line([(375, 300), (375, 335), (125, 335), (1295, 335)], GREEN)
    c.line([(1305, 300), (1305, 380), (745, 380), (1525, 380)], GOLD)
    c.text(390, 302, "1", 22, GREEN, True)
    c.text(1320, 301, "1", 22, GOLD, True)
    tables = [
        (60, "user_progress", "회원별 진도", ["id  PK", "member_id  FK · UQ", "total_solved_count", "current_streak", "last_solved_date", "updated_at"], "member_id", "0..1"),
        (450, "problem_sessions", "진행 중인 문제와 답안", ["id  PK", "member_id  FK", "sentence_id  FK", "history_id  NULL 허용", "stage / completed", "shuffled_words", "user_*_answer", "gpt_correct / gpt_reason", "completed_at"], "member_id, history_id", "0..N"),
        (840, "solved_problem_histories", "완료 기록과 내용 스냅샷", ["id  PK", "member_id  FK", "sentence_id  FK", "history_id  NULL 허용", "problem_session_id *", "original_text / reading_text", "meaning / shuffled_words", "user_*_answer", "gpt_correct / gpt_reason", "explanation / solved_at"], "member_id, history_id", "0..N"),
        (1230, "user_sentence_usages", "회원별 완료 문장", ["id  PK", "member_id  FK", "sentence_id  FK", "used_at"], "member_id, sentence_id", "0..N"),
    ]
    for x, name, label, fields, uq, count in tables:
        c.line([(x+65, 335), (x+65, 450)], GREEN)
        c.text(x+18, 411, count, 20, GREEN, True)
        if name != "user_progress":
            c.line([(x+295, 380), (x+295, 450)], GOLD)
            c.text(x+302, 411, "0..N", 18, GOLD, True)
        c.box((x, 450, x+350, 940))
        c.text(x+18, 471, name, 21, bold=True)
        c.text(x+18, 510, label, 22, MUTED)
        c.line([(x+18, 550), (x+332, 550)], BORDER, 2)
        for i, f in enumerate(fields):
            c.text(x+18, 572+i*30, f, 20)
        c.text(x+18, 889, "UQ: " + uq, 17, GREEN)
    c.text(60, 977, "초록선: members.id → member_id    황갈색선: classic_sentences.id → sentence_id", 23, MUTED)
    c.text(60, 1022, "* problem_session_id는 일반 Long 컬럼입니다. 세션 테이블과의 FK 관계는 선언되어 있지 않습니다.", 23, MUTED)
    c.text(60, 1064, "진도는 첫 완료 시 생성되며, 나머지 하위 테이블은 회원 또는 문장마다 0개 이상의 행을 가집니다.", 22, MUTED)
    c.save("erd.png")


if __name__ == "__main__":
    architecture()
    erd()
