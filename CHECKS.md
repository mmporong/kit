# 검증 기록

## 2026-11-05 — 서술형 답안 완결성 검토 보강

- written-review.md에 질문의 세부 요구와 답안의 대응 확인, 협업 결정의 제안·근거·판단·구현 영향·검증 연결, 정적 증명과 실측의 구분을 추가했습니다. 없는 의사결정 기록이나 측정값을 만들지 않는 원칙은 유지합니다.
- 동일 로컬 Windows/Python 3.14/Git Bash의 `PYTHONUTF8=1 python -m unittest discover -s tests -v`: 20개 중 통과 18개·skip 2개·실패 0·오류 0. `Ran 20 tests in 10.362s / OK (skipped=2)`, 종료코드 0. skip은 기존 Windows 링크 생성 권한 제한입니다.
- kit-explain의 기존 quick_validate.py와 `git diff --check`는 종료코드 0입니다. 합성 과제와 독립 생성·검토 결과는 공개 kit 밖의 격리 폴더에서 관리합니다. 실제 플랫폼 성과나 사용자 이해를 검증한 것은 아닙니다.
- 동일 원자료의 독립 재생성본도 기본 10문항을 유지했습니다. 격리된 합성 입력족 2건의 후속 실행과 정적 도출을 대조했고, 최초·재생성본과 원자료 해시를 보존했습니다. 자료 밖의 측정·협업 경위는 미확인으로 남겼습니다. 단일 합성 프로젝트의 관찰이며 일반적인 품질 향상 수치로 해석하지 않습니다.

## 2026-11-05 — kit-explain 심화 서술형 복습

- 기존 로컬 개선을 보존하고 kit-explain 본문·written-review 참고문서와 README 사용 설명을 보강했습니다. 실제 코드의 작동 원리·데이터 사용·보장 범위·취약 조건과 기록으로 확인되는 협업 판단을 묻도록 했습니다. 설명 답안·근거·꼬리 질문·보조 암기 단서를 제공하며 기본 연습 10개와 AI 금지 단계 중단 원칙을 유지했습니다.
- 비공개 소재·문항·세부 사실·원문·합성 재현 예시는 파일에 포함하지 않았습니다. 일반화된 작성 방법만 반영했습니다. 새 의존성·도구·모델 설정·자동화·원격 push는 없습니다.
- 기존 skill-creator의 quick_validate.py로 kit-explain 검사: `Skill is valid!`, 종료코드 0. 상대 링크 29개와 수정한 두 explain 문서의 코드 블록 짝, `git diff --check`를 확인했습니다.
- 로컬 Windows/Python 3.14/Git Bash에서 `PYTHONUTF8=1`로 `python -m unittest discover -s tests -v`: 20개 중 통과 18개·skip 2개·실패 0·오류 0. `Ran 20 tests in 11.455s / OK (skipped=2)`, 종료코드 0. `bash -n install.sh` 종료코드 0. skip은 기존 Windows 링크 생성 권한 제한 2개입니다.
- 검사 범위는 메타데이터·문서 연결·설치 payload와 기존 회귀 사례입니다. 실제 과제의 질문·답안 생성 품질, 사용자의 이해, 시험 플랫폼·평가 성과를 검증한 것은 아닙니다.

## 2026-11-05 — 공개 설계 비교와 실제 동작 확인

- 기준: 공개 main `b103ed5632abe4ebc679d7a029fca6cb37b06567`을 새 작업 폴더에 복제했고 수정 전 변경이 없었습니다. 원격 push·Codex 업데이트·전역 설정 변경은 수행하지 않았습니다.
- 변경: 저장 후 별도 조회·입력 대비·가짜 성공 감지 참고문서와 호출 연결, 기존 API 계약·부분 답변·저장 충돌 확인, 조건부 최적화 점검, 선택형 복구 체크포인트, 제출 파일·현재 한도 확인, 버전 충돌 설명. 공개 설계 7개의 확인 범위·버전·반영 판단은 SOURCES.md에 있습니다. 설치기와 스킬 이름 5개는 유지했습니다.
- 환경: 로컬 Windows, Python 3.14, 기존 Git Bash. 최초 샌드박스 실행은 임시 폴더 권한과 Bash 하위 프로세스 오류로 `Ran 20 tests / FAILED (errors=33)`이었습니다. 성공으로 취급하지 않았습니다.
- 같은 로컬 검사를 실행 권한 승인 후 다시 수행했습니다. `PYTHONUTF8=1`로 `python -m unittest discover -s tests -v`: 20개 중 통과 18개·skip 2개·실패 0·오류 0, 종료코드 0. 최종 회귀 실행은 `Ran 20 tests in 7.695s / OK (skipped=2)`입니다. 새 참고문서의 설치 바이트 일치, 전체 payload·기존 설정 보존, 충돌 선검사와 링크 경로 검사를 포함합니다.
- skip은 `test_agents_symlink_rejected`, `test_source_link_rejected`이며 Windows 심볼릭 링크 생성 권한 제한으로 두 동작은 미확인입니다.
- 기존 Git Bash의 `bash -n install.sh`와 `git diff --check`는 종료코드 0입니다. 설치기 변경은 없습니다. 테스트는 파일 배치·기존 합성 러너 사례를 확인하며 새 지침을 AI가 수행하는 품질을 증명하지 않습니다.
- 최신 공식 첨부 원문·실제 플랫폼 인식·허용 도구와 제한·점수·시간 개선은 미확인입니다. 과제 내용·개인 자료·접속 정보는 추가하지 않았습니다.

## 2026-10-31 — 모델·에포트 기본값 제거

- 사용자 요청에 따라 스킬 5개와 KIT.md·README의 모델·에포트 기본값, 배정표, 전환·상향 조건을 제거했습니다. 과거 실행 기록은 보존했습니다.
- 스킬 이름은 kit-brief·kit-data·kit-verify·kit-debug·kit-explain으로 유지합니다. 요약·암기 단서는 kit-explain의 출력이며 별도 스킬이 아닙니다. 프로젝트 요약과 서술형 연습 10문항·답안·근거 기능은 유지했습니다.
- `PYTHONUTF8=1`로 `python -m unittest discover -s tests -v` 실행: 20개 중 통과 18개·skip 2개·실패 0·오류 0, 종료코드 0. `Ran 20 tests in 17.270s / OK (skipped=2)`.
- skip 2개는 기존 Windows 심볼릭 링크 생성 권한 제한으로 미확인입니다. 전체 통과로 해석하지 않습니다.
- 별도 검토에서 활성 문서의 배정값·제거된 표 참조 부재, 상대 링크, 영어 스킬명 5개, 서술형 복습 유지, 설치기 바이트 보존과 `git diff --check`를 확인했습니다. 실제 응시 환경에서의 지침 수행은 미검증입니다.

## 2026-10-31 — 모델 배정과 현재 프로젝트 서술형 복습

- 기준: `c0aaf8a8a0a5386bff0859b482af78cdec9576f9`의 main. 작업 전 원격·로컬 SHA 일치와 변경 없는 상태를 확인했습니다.
- 변경: 스킬 5개의 모델·에포트 권장값, KIT.md의 허용된 선택·대체 원칙과 제출 전 마무리, kit-explain의 전체 요약·연습 10문항·답안·근거·암기 단서 및 선택형 참고문서, README 사용법. 설치기·스킬 이름·기존 테스트 소스는 유지했습니다.
- 지정 모델은 6.1 Sol·5.6 Terra·6.0 Luna입니다. 로컬 제공 모델 목록에서 지정 세 모델과 low·medium·high 지원을 확인했습니다. 실제 Cofa 제공·선택 제어·전환 성공은 확인하지 않았으며 자동 라우터나 설정 변경 코드를 추가하지 않았습니다.
- 하이닉스 공식 대회·Talent Hub, Cofa 공식 안내와 공개 Cofathon 참가 후기 두 건을 확인했습니다. 공식 평가 설명·참가자 질문 사례·자체 연습 설계를 구분했습니다. 실제 하이닉스 문항 수·배점·기출 전체는 미확인입니다. 출처와 한계는 written-review 참고문서에 있습니다.
- 최종 실행: 2026-10-31 09:03 KST, 로컬 Windows/Python 3.14/Git Bash. `PYTHONUTF8=1`로 `python -m unittest discover -s tests -v` 실행. 수집 20개·통과 18개·skip 2개·실패 0·오류 0, 종료코드 0. `Ran 20 tests in 15.391s / OK (skipped=2)`.
- skip은 Windows 링크 생성 권한 부족에 따른 `test_agents_symlink_rejected`, `test_source_link_rejected`입니다. 두 동작은 미확인으로 남기며 전체 20개 통과로 보고하지 않습니다.
- Git Bash의 `bash -n install.sh`, `git diff --check` 통과. 스킬 기본 검증기 5개 통과. 상대 링크 28개·코드 블록 짝·10개 질문 관점을 확인하고, 설치기 바이트와 다섯 스킬 이름을 기준 버전과 대조했습니다. 전체 설치 payload 테스트에서 새 참고문서도 배치 대상에 포함됩니다.
- 향후 생길 해커톤 프로젝트를 아직 읽거나 평가한 것은 아닙니다. 실제 답안 생성 품질·모델 전환·응시 환경 인식·점수·시간 개선은 미검증입니다. 개인 프로젝트 코드·답안·접속 정보·비밀값은 추가하지 않았습니다.
- 별도 code-reviewer가 모델 제어·시험 경계·출처 구분·현재 프로젝트 연결과 문서 충돌을 읽기 검토해 수정 요구 없이 승인했습니다. 리뷰어 환경의 테스트 재실행은 임시 폴더 권한 문제로 실패했으며, 위 테스트 결과는 주 작업 환경에서 실행한 기록입니다.

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
