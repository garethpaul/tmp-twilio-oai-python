#!/usr/bin/env sh
set -eu
PATH=/usr/bin:/bin
export PATH
ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && /bin/pwd -P)
TEMP_ROOT=$(mktemp -d "${TMPDIR:-/tmp}/twilio-make-root-control-XXXXXX")
trap 'rm -rf "$TEMP_ROOT"' EXIT HUP INT TERM
unset MAKEFILES MAKEFILE_LIST MAKEFLAGS MFLAGS MAKEOVERRIDES ROOT SHELL
CONTROL_DIR="$TEMP_ROOT/control"; CHECKOUT="$TEMP_ROOT/twilio's [gate] \"quoted\" \`touch TWILIO_BACKTICK_MARKER\`"; ATTACKER_ROOT="$TEMP_ROOT/attacker"; LOG="$TEMP_ROOT/commands.log"; SHELL_LOG="$TEMP_ROOT/shell.log"
mkdir -p "$CONTROL_DIR" "$CHECKOUT/scripts" "$ATTACKER_ROOT"; CONTROL_DIR=$(CDPATH= cd -- "$CONTROL_DIR" && /bin/pwd -P); CHECKOUT=$(CDPATH= cd -- "$CHECKOUT" && /bin/pwd -P); MAKEFILE="$CHECKOUT/Makefile"; cp "$ROOT_DIR/Makefile" "$MAKEFILE"
FAKE_PYTHON="$TEMP_ROOT/trusted python's \"quoted\" \`touch TWILIO_PYTHON_MARKER\` \$literal"; cat >"$FAKE_PYTHON" <<'TOOL'
#!/bin/sh
printf '%s|%s|%s\n' "$PWD" "$0" "$*" >> "$TWILIO_COMMAND_LOG"
TOOL
chmod +x "$FAKE_PYTHON"
cat >"$CHECKOUT/scripts/test-makefile-root.sh" <<'SCRIPT'
#!/bin/sh
printf '%s|%s|root-test\n' "$PWD" "$0" >> "$TWILIO_COMMAND_LOG"
SCRIPT
chmod +x "$CHECKOUT/scripts/test-makefile-root.sh"
FAKE_SHELL="$TEMP_ROOT/fake-shell"; printf '#!/bin/sh\nprintf invoked >> %s\nexec /bin/sh "$@"\n' "'$SHELL_LOG'" >"$FAKE_SHELL"; chmod +x "$FAKE_SHELL"
reset_sentinels(){ rm -rf "$ATTACKER_ROOT"; mkdir -p "$ATTACKER_ROOT/build" "$ATTACKER_ROOT/dist" "$ATTACKER_ROOT/hostile.egg-info"; : >"$ATTACKER_ROOT/build/sentinel"; : >"$ATTACKER_ROOT/dist/sentinel"; : >"$ATTACKER_ROOT/hostile.egg-info/sentinel"; }
assert_sentinels(){ test -f "$ATTACKER_ROOT/build/sentinel"; test -f "$ATTACKER_ROOT/dist/sentinel"; test -f "$ATTACKER_ROOT/hostile.egg-info/sentinel"; }
run_case(){ target=$1 mode=$2; rm -f "$LOG" "$SHELL_LOG"; reset_sentinels; set +e; case "$mode" in default) (cd "$CONTROL_DIR"&&TWILIO_COMMAND_LOG="$LOG" /usr/bin/make --no-print-directory -f "$MAKEFILE" PYTHON="$FAKE_PYTHON" "$target") >/dev/null 2>&1;; command-root) (cd "$CONTROL_DIR"&&TWILIO_COMMAND_LOG="$LOG" /usr/bin/make --no-print-directory -f "$MAKEFILE" ROOT="$ATTACKER_ROOT" PYTHON="$FAKE_PYTHON" "$target") >/dev/null 2>&1;; environment-root) (cd "$CONTROL_DIR"&&ROOT="$ATTACKER_ROOT" TWILIO_COMMAND_LOG="$LOG" /usr/bin/make --no-print-directory -f "$MAKEFILE" PYTHON="$FAKE_PYTHON" "$target") >/dev/null 2>&1;; command-shell) (cd "$CONTROL_DIR"&&TWILIO_COMMAND_LOG="$LOG" /usr/bin/make --no-print-directory -f "$MAKEFILE" SHELL="$FAKE_SHELL" PYTHON="$FAKE_PYTHON" "$target") >/dev/null 2>&1;; environment-shell) (cd "$CONTROL_DIR"&&SHELL="$FAKE_SHELL" TWILIO_COMMAND_LOG="$LOG" /usr/bin/make --no-print-directory -f "$MAKEFILE" PYTHON="$FAKE_PYTHON" "$target") >/dev/null 2>&1;; esac; status=$?; set -e; [ "$status" -eq 0 ]||exit "$status"; [ ! -e "$SHELL_LOG" ]; grep -Fq "$CHECKOUT" "$LOG"; assert_sentinels; }
executed=0; for target in build check lint package-smoke root-test test verify; do for mode in default command-root environment-root command-shell environment-shell; do run_case "$target" "$mode"; executed=$((executed+1)); done; done; [ "$executed" -eq 35 ]
rm -f "$LOG"; (cd "$CONTROL_DIR"&&TWILIO_COMMAND_LOG="$LOG" /usr/bin/make --no-print-directory -f "$MAKEFILE" PYTHON="$FAKE_PYTHON" check) >/dev/null 2>&1; grep -Fq "$FAKE_PYTHON" "$LOG"
MARK="$TEMP_ROOT/make-syntax"; BAD="\$(shell /usr/bin/touch '$MARK')"; if (cd "$CONTROL_DIR"&&/usr/bin/make --no-print-directory -f "$MAKEFILE" "PYTHON=$BAD" check) >/dev/null 2>&1; then exit 1; fi; [ ! -e "$MARK" ]
if (cd "$CONTROL_DIR"&&/usr/bin/make --no-print-directory -f "$MAKEFILE" MAKEFILE_LIST=/tmp/x check) >"$TEMP_ROOT/list" 2>&1; then exit 1; fi; grep -Fq 'MAKEFILE_LIST must not be overridden' "$TEMP_ROOT/list"
if (cd "$CONTROL_DIR"&&MAKEFILE_LIST=/tmp/x /usr/bin/make --environment-overrides --no-print-directory -f "$MAKEFILE" check) >"$TEMP_ROOT/list2" 2>&1; then exit 1; fi; grep -Fq 'MAKEFILE_LIST must not be overridden' "$TEMP_ROOT/list2"
PRE="$TEMP_ROOT/pre.mk"; PRE_MARKER="$TEMP_ROOT/pre-ran"; printf '%s\n' "\$(shell /usr/bin/touch '$PRE_MARKER')" >"$PRE"; if (cd "$CONTROL_DIR"&&MAKEFILES="$PRE" /usr/bin/make --no-print-directory -f "$MAKEFILE" check) >"$TEMP_ROOT/pre" 2>&1; then exit 1; fi; grep -Fq 'MAKEFILES must be empty' "$TEMP_ROOT/pre"; [ -e "$PRE_MARKER" ]
EARLY="$TEMP_ROOT/early.mk"; EARLY_MARKER="$TEMP_ROOT/early-ran"; printf '%s\n' "\$(shell /usr/bin/touch '$EARLY_MARKER')" >"$EARLY"; if (cd "$CONTROL_DIR"&&/usr/bin/make --no-print-directory -f "$EARLY" -f "$MAKEFILE" check) >"$TEMP_ROOT/early" 2>&1; then exit 1; fi; [ -e "$EARLY_MARKER" ]
if (cd "$CONTROL_DIR"&&/usr/bin/make --no-print-directory -f "$MAKEFILE" MAKEFLAGS=-n check) >"$TEMP_ROOT/makeflags" 2>&1; then exit 1; fi; grep -Fq 'MAKEFLAGS must not be overridden' "$TEMP_ROOT/makeflags"
for flag in -n --just-print --dry-run --recon -t --touch -q --question -i --ignore-errors; do if (cd "$CONTROL_DIR"&&/usr/bin/make "$flag" --no-print-directory -f "$MAKEFILE" check) >"$TEMP_ROOT/flag" 2>&1; then exit 1; fi; grep -Fq 'non-executing or error-ignoring MAKEFLAGS are not supported' "$TEMP_ROOT/flag"; done
printf '%s\n' 'Makefile root tests passed: 35 target/authority cleanup cases, 1 literal-dollar tool case, 1 raw tool Make-syntax rejection, 2 MAKEFILE_LIST rejections, 2 contained startup-boundary cases, 1 caller MAKEFLAGS rejection, and 10 mode-flag rejections'
