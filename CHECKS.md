# 검증 기록

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
