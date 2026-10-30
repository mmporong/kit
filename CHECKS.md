# 검증 기록

## 2026-10-31 — 전체 스킬의 한 줄 호출 절차 보강

- 기준 버전: 공개 `main`의 `52e4c613ccc1c533774fffbca3fa4aa0df84b9b6`. 작업 전 변경이 없는 상태와 원격 일치를 확인했습니다.
- 범위: 기존 스킬 5개의 description·자료 확보·처리·출력·완료·실패·생략 기준, KIT.md, README, 개발용 테스트. 설치기·스킬 이름·참고자료·설치 경로·의존성은 유지했습니다.
- 각 스킬이 목표 한 줄을 받아 과제 지침·README·관련 자료·기존 코드와 실행 방법을 찾도록 작성했습니다. 담당자 질문은 업무 정의에 한정하고 실제 답변·실행 증거·추론·미확인을 구분하며 유효한 기존 결과를 재사용합니다.
- 환경: 로컬 Windows, Python 3.14.0, 설치된 Git Bash. 실제 응시 플랫폼이 아닙니다. 테스트 보조 코드가 Windows에서 Git Bash와 UTF-8을 명시하고 링크 생성 권한 부재를 skip으로 보고합니다. 사용자 설정이나 설치기는 변경하지 않습니다.
- `bash -n install.sh`: 설치된 Git Bash로 실행, 종료코드 0.
- 첫 회귀검사: 기존 18개 중 통과 16개·skip 2개, 실패 0·오류 0, 종료코드 0. 전체 설치 내용·기존 설정 보존과 한글 경로 검사를 추가한 뒤 다시 실행했습니다.
- 최종 `python -m unittest discover -s tests -v`: 20개 중 통과 18개·skip 2개, 실패 0·오류 0, 종료코드 0. `Ran 20 tests in 14.206s / OK (skipped=2)`.
- skip은 `test_agents_symlink_rejected`, `test_source_link_rejected`이며 Windows 심볼릭 링크 생성 권한이 없어 해당 동작은 이번 실행에서 미확인입니다. 전체 20개 통과로 해석하지 않습니다.
- 검사는 새 설치·동일 재설치·충돌 전 중단·원본과 기존 설정 보존, 전체 스킬 및 참고자료의 바이트 일치·공백/한글 경로, 실제 테스트 러너의 0개·전부 skip·실패를 숨긴 종료코드 사례를 포함합니다. 마지막 세 사례는 AI 판정 동작을 검증하는 테스트가 아닙니다.
- skill-creator의 `quick_validate.py`: 기존 설치 도구로 5개 모두 통과. 문서 상대 링크 25개·README 목차 앵커 8개·펼치기 5개·코드 블록 짝도 확인했습니다. `git diff --check` 통과.
- 작성 후 별도 code-reviewer가 변경과 시험 제한 보존을 검토해 승인했습니다. 금지 단계 중단, 외부 전송·Push 금지, Codex 업데이트·브라우저 자동 조작 금지를 유지했습니다.
- 개인 자료·실제 문제·제출물·자격증명은 추가하지 않았습니다. 실제 플랫폼 자동 인식, 모델의 한 줄 호출 수행 품질, 점수·속도 향상, 다른 운영체제의 실행은 미검증입니다.

## 2026-10-31 — 검증 판정·모델 평가 사용법 보강

- 기준 버전: `3684130e4b1c9c3c2b6057ea78eafee69fbad3e4`의 `main`. 변경한 문서는 이 항목을 포함한 5개이며 설치기와 테스트 소스는 기준 버전과 바이트가 같습니다.
- 환경: 로컬 Windows, Python 3.14, Git Bash 5.2.26. 실제 응시 플랫폼이 아닙니다.
- 실행 시점: 2026-10-31 08:17~08:19 KST. 변경한 스킬·참고문서·README를 대상으로 검사했습니다.
- `bash -n install.sh`: 종료코드 0. `git diff --check`: 종료코드 0. 다섯 스킬 이름과 README 상대 링크의 대상 존재를 별도로 확인했습니다.
- 최초 `python -m unittest discover -s tests -v`: 18개 실행, 실패 4개·오류 2개. Windows 기본 Bash 선택과 출력 인코딩 문제, 심볼릭 링크 생성 권한 오류를 관찰했습니다. 통과로 처리하지 않았습니다.
- 재검증은 `PYTHONUTF8=1`을 Python 시작 전에 지정하고, 일회성 실행기에서 테스트의 `bash` 호출을 Git Bash 절대경로로 연결하며 인수의 경로 구분자를 변환했습니다. 저장소의 설치기·테스트 코드는 수정하지 않았습니다.
- 재검증 결과: 16개 실행·16개 통과·실패 0·오류 0·러너 skip 0, 종료코드 0, `Ran 16 tests in 29.427s / OK`. 설치·재설치·충돌 보존·참고문서 바이트 동일 배치와 0개/전부 skip/실패를 숨긴 종료코드의 합성 사례를 포함합니다.
- `test_agents_symlink_rejected`, `test_source_link_rejected`는 Windows 심볼릭 링크 생성 권한이 없어 재검증 선택에서 제외했습니다. 러너의 skip 집계와 별개인 미확인 2개이며, 전체 18개 통과를 뜻하지 않습니다. 로컬 WSL 실행도 연결 오류·시간 초과로 사용할 수 없었습니다.
- 변경 diff를 별도 검토했습니다. 공개 범용 지침만 보강했으며 개인 접속 링크·자격증명·시험 문제·제출물은 추가하지 않았습니다. 모델 평가 실행이나 실제 플랫폼 지침 준수·점수 향상은 검증하지 않았습니다.

## 2026-10-31 — README 상세 사용 설명 보강

- 환경: 작업 컨테이너의 Linux/Bash/Python. 실제 응시 플랫폼이 아닙니다.
- 수정 전 GitHub `main`의 파일 16개와 로컬 파일의 Git blob SHA-1이 모두 일치함을 확인했습니다.
- 변경 범위: `README.md`, `CHECKS.md`. 설치기·스킬 본문·참고자료·테스트 코드는 변경하지 않았습니다.
- README에 빠른 시작, 파일 구성, 상황별 흐름, 스킬 5개의 입력·처리·출력·사용 예시·생략 조건, 한계와 문제 대응을 추가했습니다.
- 상세 사용 예시는 자체 합성 예시이며 실제 시험 문제·모델 실행 로그·성능 개선 실측이 아닙니다.
- `bash -n install.sh`: 통과.
- `python3 -m unittest discover -s tests -v`: 12개 통과. 실행 출력은 아래와 같습니다.
- 별도 문서 검사: 상대 링크 20개와 목차 앵커 8개, 스킬 상세 펼치기 5개, 코드 블록 짝이 정상임을 확인했습니다.
- README가 실제 스킬 이름·경로와 일치하고, 공개 전 안내 문구와 개인 접속 링크·계정 비밀값이 포함되지 않았는지 점검했습니다. 이 점검은 완전한 보안 감사를 의미하지 않습니다.
- 공개 `mmporong/kit` 저장소와 준비 파일의 존재를 GitHub 연결로 확인했습니다.

## 실행 출력

```text
test_agents_symlink_rejected (test_install.InstallTests.test_agents_symlink_rejected) ... ok
test_conflict_is_detected_before_writing (test_install.InstallTests.test_conflict_is_detected_before_writing) ... ok
test_conflicting_kit_md_preserved (test_install.InstallTests.test_conflicting_kit_md_preserved) ... ok
test_forbidden_side_effects_absent_from_installer (test_install.InstallTests.test_forbidden_side_effects_absent_from_installer) ... ok
test_fresh_install_preserves_existing_files (test_install.InstallTests.test_fresh_install_preserves_existing_files) ... ok
test_identical_install_is_idempotent (test_install.InstallTests.test_identical_install_is_idempotent) ... ok
test_install_into_source_rejected (test_install.InstallTests.test_install_into_source_rejected) ... ok
test_missing_source_leaves_target_unchanged (test_install.InstallTests.test_missing_source_leaves_target_unchanged) ... ok
test_missing_target_rejected (test_install.InstallTests.test_missing_target_rejected) ... ok
test_non_directory_agents_rejected (test_install.InstallTests.test_non_directory_agents_rejected) ... ok
test_skill_metadata_and_names (test_install.InstallTests.test_skill_metadata_and_names) ... ok
test_source_link_rejected (test_install.InstallTests.test_source_link_rejected) ... ok

----------------------------------------------------------------------
Ran 12 tests in 0.361s

OK
```

## 검증 범위와 한계

검사는 기존 파일 보존, 동일 내용 재설치, 충돌 선검사, 링크 차단, 잘못된 경로 차단,
Skill 기본 메타데이터와 설치기의 특정 금지 명령 문자열 부재를 확인합니다.
명령 문자열 검사는 완전한 동작 분석이나 네트워크 감시를 대체하지 않습니다.

설치 중 다른 프로세스가 같은 경로를 변경하지 않는 단일 실행을 전제로 합니다.
시스템 장애·동시 쓰기에 대한 완전한 트랜잭션 또는 자동 복구 보장은 하지 않습니다.

미확인 사항은 실제 코파의 설치 허용/경로와 자동 인식, 모델별 지침 준수,
스킬 사용 전후의 정확도·시간·토큰·점수 개선, 모든 운영체제 호환성입니다.
테스트 통과를 이러한 항목의 통과로 해석하지 않습니다.
