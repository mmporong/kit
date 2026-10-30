#!/usr/bin/env bash
# ! New: only add selected project-local documentation; never alter agent settings.
set -euo pipefail
fail() { printf '설치 중단: %s\n' "$*" >&2; exit 1; }
for tool in cp cmp diff find mkdir; do
  command -v "$tool" >/dev/null 2>&1 || fail "$tool 명령이 필요합니다."
done
[[ $# -eq 1 ]] || fail '사용법: bash install.sh 실제_과제_폴더'
kit=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
[[ -d "$1" && ! -L "$1" ]] || fail '실제 과제 폴더를 지정하세요. 심볼릭 링크는 사용하지 않습니다.'
project=$(cd -- "$1" && pwd -P)
[[ "$project" != / && "$project" != "$kit" ]] || fail '시스템 루트나 준비 키트 자체에는 설치하지 않습니다.'
if [[ -n "${HOME:-}" && -d "$HOME" ]]; then
  home_path=$(cd -- "$HOME" && pwd -P)
  [[ "$project" != "$home_path" ]] || fail '개인 홈 루트에는 설치하지 않습니다.'
fi
names=(kit-brief kit-data kit-verify kit-debug kit-explain)

# ! Preflight every source and destination before writing any files.
[[ -f "$kit/KIT.md" && ! -L "$kit/KIT.md" ]] || fail 'KIT.md가 없거나 링크입니다.'
[[ -d "$kit/skills" && ! -L "$kit/skills" ]] || fail 'skills 경로가 없거나 링크입니다.'
for name in "${names[@]}"; do
  src="$kit/skills/$name"
  [[ -d "$src" && ! -L "$src" && -f "$src/SKILL.md" ]] || fail "Skill 파일 누락: $name"
  [[ -z "$(find "$src" ! -type d ! -type f -print -quit)" ]] || fail "특수 파일/링크가 포함돼 있습니다: $name"
done
for path in "$project/.agents" "$project/.agents/skills"; do
  [[ ! -L "$path" ]] || fail "기존 링크를 변경하지 않습니다: $path"
  [[ ! -e "$path" || -d "$path" ]] || fail "기존 파일과 충돌합니다: $path"
done
if [[ -e "$project/KIT.md" || -L "$project/KIT.md" ]]; then
  [[ -f "$project/KIT.md" && ! -L "$project/KIT.md" ]] || fail '기존 KIT.md 경로와 충돌합니다.'
  cmp -s -- "$kit/KIT.md" "$project/KIT.md" || fail '기존 KIT.md 내용이 다릅니다. 기존 파일을 보존했습니다.'
fi
for name in "${names[@]}"; do
  dst="$project/.agents/skills/$name"
  if [[ -e "$dst" || -L "$dst" ]]; then
    [[ -d "$dst" && ! -L "$dst" ]] || fail "기존 경로와 충돌합니다: $name"
    [[ -z "$(find "$dst" ! -type d ! -type f -print -quit)" ]] || fail "기존 Skill에 링크/특수 파일이 있습니다: $name"
    diff -qr -- "$kit/skills/$name" "$dst" >/dev/null || fail "기존 Skill 내용이 다릅니다: $name"
  fi
done

# ! No overwrite. Do not run another installer/editor concurrently.
mkdir -p -- "$project/.agents/skills"
for name in "${names[@]}"; do
  dst="$project/.agents/skills/$name"
  if [[ ! -e "$dst" ]]; then
    mkdir -- "$dst"
    cp -R -n -- "$kit/skills/$name/." "$dst/"
  fi
  diff -qr -- "$kit/skills/$name" "$dst" >/dev/null || fail "복사 확인 실패: $name"
done
if [[ ! -e "$project/KIT.md" ]]; then
  (set -o noclobber; cat -- "$kit/KIT.md" > "$project/KIT.md") || fail 'KIT.md 추가 실패. 기존 파일을 확인하세요.'
fi
cmp -s -- "$kit/KIT.md" "$project/KIT.md" || fail 'KIT.md 내용 확인 실패.'
printf '%s\n' '파일 배치 완료: Skill 5개 + KIT.md' \
  '기존 AGENTS.md·과제 코드·전역 설정은 변경하지 않았습니다.' \
  'Codex 자동 인식은 별도로 확인하세요. 버전 업데이트나 제한 우회는 하지 마세요.' \
  '현재 대화에서 KIT.md와 .agents/skills/kit-brief/SKILL.md를 읽도록 요청하세요.'
