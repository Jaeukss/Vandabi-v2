# 반다비 AI — Streamlit Native UI

Streamlit 기반으로 구현한 **교통약자 이동지원·생활체육 참여·접근성 점검 보조 UI 프로토타입**입니다.
기존 `bandabi_purple.html` 시안의 화면 흐름을 참고하되, 배포에서는 iframe을 사용하지 않고 `app.py`를 Streamlit native 앱 진입점으로 사용합니다.

본 저장소는 포트폴리오 공개용으로 정리했으며, 실제 API 키·개인정보·내부 URL·원본 민감 데이터는 포함하지 않습니다.
사업계획서의 공개 가능한 문제정의, 서비스 흐름, 공공데이터 활용 방향만 반영했습니다.

## Screenshots

### Title / Branding

![반다비 AI 타이틀](assets/img/title-bandabi-ai.png)

### Navigation Tabs

![반다비 AI 내비게이션 탭](assets/img/nav-tabs.png)

### Logo Asset

![반다비 로고](assets/img/logo-bandabi.png)

## Business Context

사업계획서 기준으로 이 서비스는 장애인 생활체육 참여 문제를 단순한 시설·강좌 정보 부족이 아니라 **이동 가능성의 불확실성**과 **혼자 운동하기 어려운 부담**이 결합된 문제로 정의합니다.

사업계획서에 정리된 문제 근거는 다음과 같습니다.

| 항목 | 사업계획서 기재 내용 | 서비스 시사점 |
|---|---|---|
| 장애인 생활체육 참여율 | 2025년 기준 34.8% | 예약/정보 제공보다 실제 출석과 지속참여 구조 필요 |
| 외출 시 교통수단 이용 어려움 | 2023년 장애인실태조사 기준 35.2% | 체육센터까지 실제로 갈 수 있는지 먼저 판단해야 함 |
| 체육시설 미이용 사유 | “혼자 운동하기 어려워서” 27.8% | 첫 방문 버디, 운동 친구, 센터 도우미 연결 필요 |

위 수치는 사업계획서에 기재된 출처 기반 요약입니다. README에서는 검증된 서비스 성과가 아니라 기획 배경으로만 사용합니다.

## Problem Definition

장애인 생활체육 참여 전후의 병목은 다음 흐름에서 발생합니다.

| 단계 | 이용자 문제 | 기존 방식의 한계 | 반다비 AI 접근 |
|---|---|---|---|
| 정보 탐색 | 내 이동수단과 접근성 필요에 맞는 강습인지 알기 어려움 | 강좌명·시설명 중심 안내 | 이동 가능성을 먼저 분석한 뒤 도착 가능한 강습 추천 |
| 이동 전 | 오늘 실제로 센터까지 갈 수 있을지 불확실함 | 일반 지도 앱은 최단경로 중심 | AI 기반 무장애 이동 경로 추천 |
| 이동 중 | 저상버스, 환승, 보도, 날씨, 진입 동선이 불안정함 | 이동 위험 요소가 분산됨 | 대중교통·도보·날씨·편의시설 통합 분석 |
| 첫 방문 | 접수, 탈의, 강습실 이동이 부담됨 | 첫 방문 지원 기능 부족 | 첫 방문 버디와 센터 도우미 연결 |
| 관계 형성 | 혼자 운동하면 지속하기 어려움 | 단순 예약 앱은 관계 형성 기능 부족 | 같은 시간대·운동목표 기반 피어 매칭 |
| 기관 운영 | 예약 대비 출석률과 이탈 사유 파악이 어려움 | 수기 출석부와 개별 민원 중심 | B2G 운영 대시보드로 출석·이탈·접근성 이슈 기록 |

## Service Concept

반다비 AI는 “시설을 찾는 앱”보다 **오늘 실제로 도착하고, 함께 운동하고, 다시 참여할 수 있는가**를 다루는 서비스 흐름을 목표로 합니다.

핵심 흐름:

```text
AI 무장애 이동 경로 추천
→ 교통약자 이동지원 사전 문의 권장
→ No-stop Care 피어·버디 매칭
→ 도착 가능한 강습/지도자 추천
→ 운동 후 생활체육 리포트
→ 재참여 유도
→ 기관 운영 대시보드 환류
```

## Key AI / Data Features

| 기능 | 설명 | 현재 README 기준 공개 범위 |
|---|---|---|
| Viable Path Scoring AI | 출발지, 목적지, 접근성 지원 유형, 도보 부담, 환승 부담, 날씨 위험, 시설 접근성을 종합해 이동 가능성을 점수화하는 설명가능한 룰 기반 모델 | 기획/프로토타입 구조 공개 |
| No-stop Care 피어·버디 매칭 | 같은 센터, 시간대, 운동 목표, 도움 유형을 기준으로 첫 방문 버디·운동 친구·센터 도우미 연결 | 운영 설계 공개, 실제 개인정보 매칭 데이터 비공개 |
| B2G 운영 대시보드 | 예약 대비 출석률, 이동 실패 사유, 피어 매칭 성공률, 접근성 제보를 기관 운영 지표로 정리 | UI/지표 구조 공개 |
| 접근성 점검 | 사진 업로드 기반 접근성 점검 mock 결과와 관리자 검토용 공문 초안 제공 | 공식 판단이 아닌 참고 UI로 공개 |
| 공공데이터 상태 표시 | API 응답을 `real_api`, `real_api_no_data`, `fallback`, `missing_key` 등으로 구분 | 구현 투명성 기준 공개 |

## Public Data Plan

사업계획서와 코드 구조에서 확인되는 데이터 활용 방향입니다.

| 데이터/API | 활용 목적 |
|---|---|
| VWorld API | 장소명/주소 좌표 변환 |
| TAGO 버스노선·도착 정보 | 대중교통 경로와 도착 정보 참고 |
| 기상청 단기예보 API | 비, 눈, 폭염, 한파, 강풍 등 이동 위험 보정 |
| 장애인편의시설 데이터 | 승강기, 장애인화장실, 주출입구 등 접근성 참고 |
| 교통약자 이동지원 정보 | 대체 이동수단 사전 문의 권장 |
| 장애인 생활체육조사/장애인실태조사 | 문제정의와 서비스 필요성 근거 |
| 향후 스마트도시 데이터허브 | 도시 단위 접근성 취약구간 분석과 SaaS 확장 검토 |

## MVP Scope

현재 공개 저장소의 범위는 **UI/프로토타입 중심**입니다.

구현/정리된 범위:

- Streamlit native UI 진입점
- User/Admin 역할 흐름
- 경로 분석 mock 카드
- Program AI/버디/리포트/일정 추천 화면
- 접근성 점검 mock 결과
- 기관 대시보드 mock
- RAG, API client, email, safety, vision, voice 모듈 구조
- API key 비노출 원칙과 fallback 상태 표시

포함하지 않는 범위:

- 실제 예약 확정
- 실제 배차 확정
- 실제 동행 매칭 확정
- 공식 민원 접수
- 의료 진단, 치료, 처방
- 운영기관 승인 없는 실제 공문 발송
- 개인정보 기반 매칭 데이터

## Expected Impact

사업계획서 기준 기대효과는 다음과 같이 정리됩니다.

| 대상 | 기대효과 |
|---|---|
| 장애인 이용자 | 이동 불안 완화, 첫 방문 부담 감소, 운동 친구 형성, 생활체육 참여 기회 확대 |
| 체육센터 | 예약자 수뿐 아니라 실제 출석률, 이동 실패 사유, 첫 방문 이탈, 지속참여율을 관리할 수 있음 |
| 지자체 | 접근성 취약구간, 교통약자 이동지원 수요, 시설 개선 우선순위 판단 근거 확보 |
| 스마트도시 확장 | 공공체육시설, 복지시설, 문화시설까지 확장 가능한 무장애 이동 경로 추천 SaaS 모델 검토 |

사업계획서의 실증 검증 KPI 후보:

| KPI | 성격 |
|---|---|
| 예약 대비 실제 출석률 향상 | 실증 목표 |
| 신규 이용자 첫 방문 완료율 향상 | 실증 목표 |
| 첫 방문 버디 매칭률 | 실증 목표 |
| 이동 실패 사유 파악률 | 실증 목표 |
| 4주 지속참여율 향상 | 실증 목표 |

위 항목은 달성 결과가 아니라 사업계획서에 정리된 검증 목표입니다.

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
- 피어·버디 매칭은 실명/연락처 직접 노출 제한, 관리자 승인, 상호 동의, 신고/차단 등 안전장치를 전제로 설계했습니다.

## Portfolio Notes

이 프로젝트에서 확인되는 구현 역량은 다음과 같습니다.

- Streamlit native UI로 복수 화면 흐름을 구성하는 능력
- 사용자/관리자 역할별 화면 분리와 상태 관리
- 공공데이터, VWorld, SendGrid, OpenRouter 등 외부 서비스 연동 구조 설계
- API key 미설정, API 실패, 데이터 없음 상태를 구분하는 fallback-first 설계
- 장애인 생활체육 참여 문제를 이동 가능성, 첫 방문 부담, 관계 형성, 지속참여 관점으로 구조화한 서비스 기획
- 포트폴리오 공개를 고려한 secrets 비노출, 민감정보 제외, 안전 고지 문서화

## Limits

- 현재 버전은 UI/프로토타입 중심입니다.
- 실제 이동지원 확정, 배차 확정, 공식 민원 접수, 의료 판단 기능은 제공하지 않습니다.
- API 연동 기능은 설정값과 실행 환경에 따라 fallback으로 동작할 수 있습니다.
- 사업계획서의 KPI는 실증 목표이며, 현재 README에서는 달성 성과로 표현하지 않습니다.
- 배포 URL은 접근 가능 여부가 별도로 확인된 경우에만 추가합니다.
