# 참고 출처와 작성 범위

이 묶음의 지침·설치기는 일반적인 개발·검증 원리를 바탕으로 새로 작성했습니다.
타인의 Skill 본문, 설치 스크립트, 개인 지침, 실제 시험 문제를 복사해 포함하지 않았습니다.
공개 저장소에 있었다는 사실만으로 재배포 권한이 생기지는 않습니다.

## 형식·활용 참고
- OpenAI Skills: https://developers.openai.com/codex/skills
- OpenAI Customization: https://learn.chatgpt.com/docs/customization/overview
- OpenAI AGENTS.md: https://developers.openai.com/codex/guides/agents-md
- NIST 공정능력: https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm
- scikit-learn 데이터 누수: https://scikit-learn.org/stable/common_pitfalls.html

## 앞선 준비 과정에서 비교한 공개 설계
- https://github.com/hanjin8387-alt/hynix-round2-kit (작업 단계 분리 참고, 원문 미포함)
- https://github.com/aiopshwang/data-analysis-ml-agent-skills (데이터 의미·평가 경계 참고, 원문 미포함)
- https://github.com/openai/plugins/tree/main/plugins/superpowers (검증·디버깅 절차 비교, 원문 미포함)

현행 플랫폼의 지원 버전과 허용 범위를 따릅니다. 이 문서는 공식 승인 증거가 아닙니다.
개인 메일·첨부 원본·접속 링크·토큰은 이 공개 패키지에 포함하지 않았습니다.

## 2026-11-05 공개 설계 재비교

아래는 공개 파일을 읽고 기존 kit와 비교한 범위입니다. 모든 참가자 저장소를 망라한 조사나 참가 이력 확인이 아닙니다. 본문·코드·설치기는 가져오지 않고 필요한 일반 원칙만 새로 작성했습니다. 실제 과제나 비공개 자료는 포함하지 않습니다.

| 저장소와 확인 버전 | 비교한 부분 | kit 반영 판단 |
|---|---|---|
| [hanjin8387-alt/hynix-round2-kit](https://github.com/hanjin8387-alt/hynix-round2-kit/tree/7b35870687e4ba5ab39a87d2db7e0effaecaa8c6) | README, hynix-build·hynix-verify, 파일 목록 | 저장 후 별도 조회와 고정 성공 표시 검사를 보강. 별도 build 스킬·기존 시험 고정 시각·시작 스크립트는 추가하지 않음. 확인한 트리에 라이선스 파일이 없어 복제하지 않음. |
| [aiopshwang/data-analysis-ml-agent-skills](https://github.com/aiopshwang/data-analysis-ml-agent-skills/tree/82a1dc2c7a9f40a052b20f32dcb805d86132f29b) | README, shipping-reproducible-results | 입력·처리·산출물 연결과 재현 경계 비교. 기존 데이터·모델 평가 지침과 겹쳐 전체 묶음은 추가하지 않음. README에 MIT 표기. |
| [openai/plugins의 superpowers](https://github.com/openai/plugins/tree/b767f8fa3be1a22b093127dd59956c91ecffca9d/plugins/superpowers) | verification-before-completion·systematic-debugging, 파일 목록 | 실행 증거·원인 재현은 기존 kit-verify·kit-debug와 중복. 새 설치·의존 스킬 호출을 추가하지 않음. |
| [AgenticLab-SH/sh-workflows](https://github.com/AgenticLab-SH/sh-workflows/tree/798f02fd518c01f72ee69bf89dc584b303ce1a06) | optimization-modeling·saved-file-reconciliation, LICENSE | 조건부 최적화 점검과 버퍼·디스크·실행 상태 구분을 짧게 반영. 도구·알고리즘 묶음은 추가하지 않음. MIT 확인. |
| [JINwonLEE/cofa-codex-harness](https://github.com/JINwonLEE/cofa-codex-harness/tree/171a8f37d5a87be6618eb5fdc8316b92cc82faaa) | hx-wrap, LICENSE | 필수 제출 파일·실행·저장 확인을 보강. 자동 커밋·별도 기록 양식은 추가하지 않음. MIT 확인. |
| [ripplelover/cofa-ready-kit](https://github.com/ripplelover/cofa-ready-kit/tree/d6745cbe30097ce2a5ccb5215ab2eb59387d30ed) | cofa-triage, LICENSE | 기존 계약 보존과 부분 답변의 미해결 상태 유지를 반영. 기존 요구 분석과 중복되는 단계는 추가하지 않음. MIT 확인. |
| [allsleep7610/hynix-hackathon-workflow](https://github.com/allsleep7610/hynix-hackathon-workflow/tree/1e4a2636514df5bc2d1a78f5459f9c698bf3eb0d) | my-session-save, 파일 목록 | 필요한 시점에만 기존 기록에 복구 체크포인트를 남기도록 보강. Hook·Node·세션 프레임워크는 추가하지 않음. 확인한 트리에 라이선스 파일이 없어 복제하지 않음. |

저장소의 규칙 설명은 주최 측 공식 안내의 대체 자료가 아닙니다. 이번 로컬 수정에서는 최신 공식 첨부 원문을 확인하지 못했으므로 시각·문항 수·용량·허용 도구를 새 규칙으로 고정하지 않았습니다. 현재 공식 안내를 읽어 확인하도록 유지합니다.
