# 반다비 AI — Streamlit Native UI

Streamlit 기반으로 구현한 **교통약자 이동지원·생활체육 참여·접근성 점검 보조 UI 프로토타입**입니다.
기존 `bandabi_purple.html` 시안의 화면 흐름을 참고하되, 배포에서는 iframe을 사용하지 않고 `app.py`를 Streamlit native 앱 진입점으로 사용합니다.

본 저장소는 포트폴리오 공개용으로 정리했으며, 실제 API 키·개인정보·내부 URL·원본 민감 데이터는 포함하지 않습니다.

## Screenshots

### Title / Branding

![반다비 AI 타이틀](assets/img/title-bandabi-ai.png)

### Navigation Tabs

![반다비 AI 내비게이션 탭](assets/img/nav-tabs.png)

### Logo Asset

![반다비 로고](assets/img/logo-bandabi.png)

## Overview

이 프로젝트는 장애인 생활체육 서비스 이용자가 이동, 프로그램 참여, 접근성 확인 과정에서 필요한 정보를 한 화면 흐름으로 확인할 수 있도록 구성한 UI 중심 MVP입니다.

주요 사용 흐름은 다음과 같습니다.

1. 사용자 또는 관리자 역할로 진입
2. 출발지/목적지와 지원 필요 유형 입력
3. 경로 분석 및 이동지원 후보 확인
4. 생활체육 프로그램/지도자 추천 흐름 확인
5. 사진 업로드 기반 접근성 점검 mock 결과 확인
6. 기관 담당자용 운영 대시보드와 공문 초안 확인

## Key Features

| 구분 | 구현 내용 |
|---|---|
| 로그인/회원가입 | Streamlit dialog와 `st.session_state` 기반 User/Admin 역할 흐름 |
| 사용자 시작 화면 | 출발지, 목적지, 알림 설정, AI 추천 시작 UI |
| 경로 분석 | mock 경로 카드, 접근성 참고 점수, AI 소견 표시 |
| 버디/센터 정보 | 이동지원 후보, 센터, 보호자 공유 카드 구성 |
| Program AI | 생활체육 프로그램 및 지도자 추천 UI |
| 리포트 | 성취도, 가이드, BT 포인트, 보호자 공유 흐름 |
| 일정 추천 | 선호 조건 기반 추천 시간 3개 표시 |
| 접근성 점검 | 사진 업로드, mock 검토 결과, 공문 초안, SendGrid payload 미리보기 |
| 기관 대시보드 | KPI mock, 공공데이터/CSV/RAG/API 설정 상태 표시 |

## Tech Stack

| 분류 | 사용 기술 |
|---|---|
| Language | Python |
| Web UI | Streamlit |
| State | `st.session_state` |
| Data | pandas, numpy |
| API Client | requests |
| RAG | rank_bm25 |
| Env | python-dotenv, Streamlit Secrets |
| Email | SendGrid, 기본 발송 비활성 |
| AI API | OpenRouter/OpenAI 연동 구조, key 미설정 시 fallback |

## Project Structure

```text
.
├── app.py                  # Streamlit native 진입점
├── app_engine_tabs.py       # 탭형 엔진 흐름
├── engine_bridge.py         # mock/engine 연결부
├── components/              # 테마, 앱 셸, mock UI, route engine
├── views/                   # 탭별 화면 구성
├── modules/                 # API client, RAG, LLM, email, safety, vision, voice
├── docs/                    # RAG 참고 문서
├── assets/img/              # README와 UI에 사용하는 이미지 asset
├── scripts/                 # config/smoke check
├── requirements.txt
└── README.md
```

## Local Run

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

API 설정 확인과 smoke test는 아래 명령으로 분리해 실행할 수 있습니다.

```bash
python -m scripts.check_config
python -m scripts.smoke_external_apis
```

## Environment Variables

실제 값은 GitHub에 올리지 않습니다. 로컬에서는 `.env.example`을 복사해 `.env`를 만들고 값을 채웁니다.

| 이름 | 용도 | 공개 처리 |
|---|---|---|
| `VWORLD_API_KEY` | VWorld 장소/주소 좌표 검색 | 값 비공개 |
| `DATA_GO_KR_SERVICE_KEY` | 기상청, TAGO, 공공데이터 API | 값 비공개 |
| `OPENROUTER_API_KEY` | OpenRouter 텍스트/비전 모델 호출 | 값 비공개 |
| `OPENROUTER_MODEL` | 텍스트 답변 모델명 | 설정명만 공개 |
| `VISION_MODEL` | 이미지 검토 모델명 | 설정명만 공개 |
| `SENDGRID_API_KEY` | SendGrid 발송 키 | 값 비공개 |
| `EMAIL_ADDRESS` | SendGrid 인증 발신 주소 | 값 비공개 |
| `ENABLE_SENDGRID_SEND` | 실제 발송 허용 여부 | 기본값 `false` |

## Security / Privacy

- `.env`, `.streamlit/secrets.toml`, 실제 API key는 commit하지 않습니다.
- README, 로그, UI에 실제 key 값, key 길이, 전체 요청 URL, raw response를 출력하지 않습니다.
- SendGrid 실제 발송은 기본 비활성 상태로 둡니다.
- 공공데이터 또는 외부 API가 실패해도 fallback 상태를 표시해 앱 흐름이 중단되지 않도록 구성했습니다.
- 접근성 점검 결과는 공식 행정 판단이 아니라 관리자 확인 전 참고 정보로 취급합니다.

## Portfolio Notes

이 프로젝트에서 확인되는 구현 역량은 다음과 같습니다.

- Streamlit native UI로 복수 화면 흐름을 구성하는 능력
- 사용자/관리자 역할별 화면 분리와 상태 관리
- 공공데이터, VWorld, SendGrid, OpenRouter 등 외부 서비스 연동 구조 설계
- API key 미설정, API 실패, 데이터 없음 상태를 구분하는 fallback-first 설계
- 포트폴리오 공개를 고려한 secrets 비노출, 민감정보 제외, 안전 고지 문서화

## Limits

- 현재 버전은 UI/프로토타입 중심입니다.
- 실제 이동지원 확정, 배차 확정, 공식 민원 접수, 의료 판단 기능은 제공하지 않습니다.
- API 연동 기능은 설정값과 실행 환경에 따라 fallback으로 동작할 수 있습니다.
- 배포 URL은 확인된 경우에만 별도로 추가합니다.
