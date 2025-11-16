# Code Policies - Linux & Bash

> Standard, convenzioni e politiche per scripting Bash e amministrazione Linux

## 📋 Indice
- [Standard di Scrittura](#standard-di-scrittura)
- [Convenzioni di Nomenclatura](#convenzioni-di-nomenclatura)
- [Template di Script](#template-di-script)
- [Best Practices](#best-practices)
- [Pattern di Programmazione](#pattern-di-programmazione)
- [Gestione Errori](#gestione-errori)
- [Sicurezza](#sicurezza)
- [Commenti e Documentazione](#commenti-e-documentazione)

---

## Standard di Scrittura

### Formattazione
- **Indentazione**: 2 o 4 spazi (no tab)
- **Lunghezza linea**: max 80 caratteri
- **Encoding**: UTF-8
- **Fine riga**: LF (Unix)
- **Shebang**: `#!/usr/bin/env bash` (portable) o `#!/bin/bash`

### Stile del Codice
```bash
#!/usr/bin/env bash
#
# Script description here
#
# Usage: script.sh [options] <arguments>

set -euo pipefail  # Exit on error, undefined vars, pipe failures
IFS=$'\n\t'        # Set Internal Field Separator

# === CONSTANTS ===
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly SCRIPT_NAME="$(basename "${BASH_SOURCE[0]}")"
readonly LOG_FILE="/var/log/script.log"

# === VARIABLES ===
verbose=0
dry_run=0

# === FUNCTIONS ===

# Print error message and exit
# Arguments:
#   $1 - Error message
# Returns:
#   Exits with code 1
error() {
    echo "[ERROR] $*" >&2
    exit 1
}

# Print log message
# Arguments:
#   $1 - Log message
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*"
}

# Print usage information
usage() {
    cat << EOF
Usage: ${SCRIPT_NAME} [OPTIONS] <input_file>

Description:
    Brief description of what the script does

Options:
    -h, --help        Show this help message
    -v, --verbose     Enable verbose output
    -n, --dry-run     Perform dry run
    -o, --output FILE Specify output file

Examples:
    ${SCRIPT_NAME} input.txt
    ${SCRIPT_NAME} -v -o output.txt input.txt

EOF
    exit 0
}

# === MAIN LOGIC ===

main() {
    # Parse arguments
    local input_file=""
    local output_file=""

    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                usage
                ;;
            -v|--verbose)
                verbose=1
                shift
                ;;
            -n|--dry-run)
                dry_run=1
                shift
                ;;
            -o|--output)
                output_file="$2"
                shift 2
                ;;
            -*)
                error "Unknown option: $1"
                ;;
            *)
                input_file="$1"
                shift
                ;;
        esac
    done

    # Validate arguments
    [[ -z "${input_file}" ]] && error "Input file required"
    [[ ! -f "${input_file}" ]] && error "File not found: ${input_file}"

    # Main script logic
    log "Processing ${input_file}..."

    # Do work here
    if [[ ${dry_run} -eq 1 ]]; then
        log "Dry run mode - no changes made"
    else
        # Actual processing
        :
    fi

    log "Done"
}

# Run main function if script is executed (not sourced)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
```

### Regole Generali
- [ ] Sempre usare `set -euo pipefail`
- [ ] Quote tutte le variabili: `"${var}"`
- [ ] Usare `readonly` per costanti
- [ ] Usare `local` per variabili in funzioni
- [ ] Preferire `[[` a `[` per test

---

## Convenzioni di Nomenclatura

### Variabili
- **Variabili locali**: `snake_case` - Esempio: `file_name`, `user_input`
- **Variabili globali**: `UPPER_SNAKE_CASE` - Esempio: `CONFIG_FILE`, `LOG_DIR`
- **Costanti**: `readonly` + `UPPER_SNAKE_CASE` - Esempio: `readonly MAX_RETRIES=3`
- **Environment vars**: `UPPER_SNAKE_CASE` - Esempio: `PATH`, `HOME`

### Funzioni
- **Funzioni**: `snake_case` - Esempio: `process_file()`, `validate_input()`
- **Private functions**: `_snake_case` - Esempio: `_internal_helper()`
- **Verbi per azioni**: `create_`, `delete_`, `check_`, `validate_`

### Files
- **Script files**: `kebab-case.sh` - Esempio: `backup-database.sh`
- **Config files**: `kebab-case.conf` - Esempio: `app-config.conf`
- **Evitare estensioni**: Per executable in PATH: `mycommand` invece di `mycommand.sh`

---

## Template di Script

### Script Base
```bash
#!/usr/bin/env bash
#
# Script Name: script-name.sh
# Description: Brief description of what this script does
# Author: Nome Autore
# Date: 2025-11-16
# Version: 1.0.0
#
# Usage: ./script-name.sh [OPTIONS] <arguments>
#
# Requirements:
#   - bash 4.0+
#   - jq (for JSON parsing)
#   - curl
#

# === STRICT MODE ===
set -euo pipefail
IFS=$'\n\t'

# === CONSTANTS ===
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly SCRIPT_NAME="$(basename "${BASH_SOURCE[0]}")"
readonly VERSION="1.0.0"

# === CONFIGURATION ===
readonly CONFIG_FILE="${SCRIPT_DIR}/config.conf"
readonly LOG_DIR="/var/log"
readonly TMP_DIR="/tmp"

# === GLOBAL VARIABLES ===
VERBOSE=0
DEBUG=0

# === COLORS ===
if [[ -t 1 ]]; then
    readonly RED='\033[0;31m'
    readonly GREEN='\033[0;32m'
    readonly YELLOW='\033[1;33m'
    readonly NC='\033[0m' # No Color
else
    readonly RED=''
    readonly GREEN=''
    readonly YELLOW=''
    readonly NC=''
fi

# === UTILITY FUNCTIONS ===

# Print colored message
# Arguments:
#   $1 - Color code
#   $@ - Message
_print_colored() {
    local color="$1"
    shift
    echo -e "${color}$*${NC}"
}

# Print error message and exit
# Arguments:
#   $@ - Error message
error() {
    _print_colored "${RED}" "[ERROR] $*" >&2
    exit 1
}

# Print warning message
# Arguments:
#   $@ - Warning message
warn() {
    _print_colored "${YELLOW}" "[WARN] $*" >&2
}

# Print info message
# Arguments:
#   $@ - Info message
info() {
    _print_colored "${GREEN}" "[INFO] $*"
}

# Print debug message if DEBUG is enabled
# Arguments:
#   $@ - Debug message
debug() {
    if [[ ${DEBUG} -eq 1 ]]; then
        echo "[DEBUG] $*" >&2
    fi
}

# Check if command exists
# Arguments:
#   $1 - Command name
# Returns:
#   0 if command exists, 1 otherwise
command_exists() {
    command -v "$1" &> /dev/null
}

# Check required commands
check_requirements() {
    local missing=()

    for cmd in jq curl; do
        if ! command_exists "${cmd}"; then
            missing+=("${cmd}")
        fi
    done

    if [[ ${#missing[@]} -gt 0 ]]; then
        error "Missing required commands: ${missing[*]}"
    fi
}

# Cleanup function (called on exit)
cleanup() {
    local exit_code=$?
    debug "Cleanup with exit code: ${exit_code}"
    # Add cleanup tasks here
    exit "${exit_code}"
}

# Print usage information
usage() {
    cat << EOF
${SCRIPT_NAME} - Description

Usage:
    ${SCRIPT_NAME} [OPTIONS] <arguments>

Options:
    -h, --help          Show this help message
    -v, --verbose       Enable verbose output
    -d, --debug         Enable debug output
    -V, --version       Show version
    -c, --config FILE   Use custom config file

Arguments:
    <input>             Input file or value

Examples:
    ${SCRIPT_NAME} -v input.txt
    ${SCRIPT_NAME} --config custom.conf data.json

EOF
}

# === MAIN FUNCTIONS ===

# Main logic goes here
process() {
    info "Starting processing..."

    # Your code here

    info "Processing complete"
}

# === ARGUMENT PARSING ===

parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                usage
                exit 0
                ;;
            -v|--verbose)
                VERBOSE=1
                shift
                ;;
            -d|--debug)
                DEBUG=1
                shift
                ;;
            -V|--version)
                echo "${SCRIPT_NAME} version ${VERSION}"
                exit 0
                ;;
            -c|--config)
                CONFIG_FILE="$2"
                shift 2
                ;;
            -*)
                error "Unknown option: $1"
                ;;
            *)
                # Positional arguments
                shift
                ;;
        esac
    done
}

# === MAIN ===

main() {
    # Setup cleanup trap
    trap cleanup EXIT INT TERM

    # Parse arguments
    parse_args "$@"

    # Check requirements
    check_requirements

    # Run main logic
    process
}

# Execute main if script is run (not sourced)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
```

### Function Template
```bash
# Function description
#
# Globals:
#   GLOBAL_VAR - Description of global used
#
# Arguments:
#   $1 - First argument description
#   $2 - Second argument description (optional)
#
# Outputs:
#   Writes progress to stdout
#
# Returns:
#   0 on success, non-zero on error
#
# Example:
#   my_function "value1" "value2"
my_function() {
    local arg1="${1:?Missing required argument 1}"
    local arg2="${2:-default_value}"

    # Validation
    if [[ ! -f "${arg1}" ]]; then
        echo "File not found: ${arg1}" >&2
        return 1
    fi

    # Processing
    echo "Processing ${arg1}..."

    # Return success
    return 0
}
```

---

## Best Practices

### Safety First
```bash
# Sempre usare strict mode
set -euo pipefail

# -e: Exit on error
# -u: Treat unset variables as error
# -o pipefail: Return error if any command in pipe fails

# Quote tutte le variabili
echo "${variable}"           # ✅ CORRETTO
echo $variable               # ❌ SBAGLIATO (word splitting)

# Usare [[ ]] invece di [ ]
if [[ "${var}" == "value" ]]; then    # ✅ CORRETTO
    echo "match"
fi

if [ "$var" = "value" ]; then         # ❌ Vecchio stile
    echo "match"
fi

# Controllare esistenza variabili
echo "${var:?Variable not set}"       # Exit se non definita
echo "${var:-default}"                # Usa default se vuota
echo "${var:=default}"                # Assegna default se vuota
```

### File Operations
```bash
# Check file exists
if [[ -f "${file}" ]]; then
    echo "File exists"
fi

# Check directory exists
if [[ -d "${dir}" ]]; then
    echo "Directory exists"
fi

# Check file readable/writable/executable
[[ -r "${file}" ]] && echo "Readable"
[[ -w "${file}" ]] && echo "Writable"
[[ -x "${file}" ]] && echo "Executable"

# Safe file creation with temp file
tmpfile=$(mktemp)
trap 'rm -f "${tmpfile}"' EXIT

# Do work with tmpfile
echo "data" > "${tmpfile}"

# Atomic file operation
mv "${tmpfile}" "${destination}"
```

### Process Management
```bash
# Run command in background
my_command &
pid=$!

# Wait for specific process
wait "${pid}"

# Check if process is running
if kill -0 "${pid}" 2>/dev/null; then
    echo "Process ${pid} is running"
fi

# Timeout for command
timeout 30s long_running_command || echo "Timed out"
```

---

## Pattern di Programmazione

### Pattern 1: Argument Parsing
```bash
parse_arguments() {
    local positional_args=()

    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                usage
                exit 0
                ;;
            -v|--verbose)
                VERBOSE=1
                shift
                ;;
            --option-with-value)
                OPTION_VALUE="$2"
                shift 2
                ;;
            --)
                shift
                positional_args+=("$@")
                break
                ;;
            -*|--*)
                echo "Unknown option: $1" >&2
                exit 1
                ;;
            *)
                positional_args+=("$1")
                shift
                ;;
        esac
    done

    # Restore positional parameters
    set -- "${positional_args[@]}"
}
```

### Pattern 2: Retry Logic
```bash
retry() {
    local max_attempts="${1}"
    local delay="${2}"
    local command="${3}"
    local attempt=1

    while [[ ${attempt} -le ${max_attempts} ]]; do
        if eval "${command}"; then
            return 0
        fi

        warn "Attempt ${attempt}/${max_attempts} failed. Retrying in ${delay}s..."
        sleep "${delay}"
        ((attempt++))
    done

    error "Command failed after ${max_attempts} attempts"
    return 1
}

# Usage
retry 3 5 "curl -f https://example.com"
```

### Pattern 3: Parallel Execution
```bash
parallel_execute() {
    local max_jobs="${1}"
    shift
    local commands=("$@")

    for cmd in "${commands[@]}"; do
        # Wait if we have max_jobs running
        while [[ $(jobs -r | wc -l) -ge ${max_jobs} ]]; do
            sleep 0.1
        done

        # Execute command in background
        eval "${cmd}" &
    done

    # Wait for all background jobs
    wait
}

# Usage
parallel_execute 4 "task1" "task2" "task3" "task4" "task5"
```

### Pattern 4: Configuration Loading
```bash
load_config() {
    local config_file="${1}"

    if [[ ! -f "${config_file}" ]]; then
        warn "Config file not found: ${config_file}"
        return 1
    fi

    # Source config file in subshell to avoid polluting namespace
    # shellcheck source=/dev/null
    source "${config_file}"

    # Or parse specific values
    # DB_HOST=$(grep "^DB_HOST=" "${config_file}" | cut -d'=' -f2)
}
```

---

## Gestione Errori

### Error Handling Patterns
```bash
# Simple error check
if ! command_that_might_fail; then
    error "Command failed"
fi

# Check exit code
command_that_might_fail
exit_code=$?
if [[ ${exit_code} -ne 0 ]]; then
    error "Command failed with code: ${exit_code}"
fi

# Try-catch equivalent
if ! output=$(risky_command 2>&1); then
    error "Command failed: ${output}"
fi

# Trap errors
error_handler() {
    local line_number="$1"
    error "Script failed at line ${line_number}"
}

trap 'error_handler ${LINENO}' ERR
```

### Logging
```bash
# Simple logging to file
log() {
    local level="$1"
    shift
    local message="$*"
    local timestamp
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')

    echo "[${timestamp}] [${level}] ${message}" | tee -a "${LOG_FILE}"
}

# Usage
log "INFO" "Starting process"
log "ERROR" "Process failed"

# Rotate logs
rotate_logs() {
    local log_file="$1"
    local max_size=$((10 * 1024 * 1024))  # 10 MB

    if [[ -f "${log_file}" ]]; then
        local file_size
        file_size=$(stat -f%z "${log_file}" 2>/dev/null || stat -c%s "${log_file}")

        if [[ ${file_size} -gt ${max_size} ]]; then
            mv "${log_file}" "${log_file}.old"
            touch "${log_file}"
        fi
    fi
}
```

---

## Sicurezza

### Secure Coding
```bash
# ❌ INSECURE: Command injection
user_input="$1"
eval "echo ${user_input}"  # PERICOLOSO!

# ✅ SECURE: Quote e validate input
if [[ "${user_input}" =~ ^[a-zA-Z0-9_-]+$ ]]; then
    echo "${user_input}"
else
    error "Invalid input"
fi

# ❌ INSECURE: Temporary file in /tmp
tmpfile="/tmp/myfile.$$"

# ✅ SECURE: Use mktemp
tmpfile=$(mktemp)
trap 'rm -f "${tmpfile}"' EXIT

# Secure file permissions
umask 077  # Created files will be -rw-------

# Check for world-writable files
find /path -type f -perm -002 -ls
```

### Input Validation
```bash
validate_email() {
    local email="$1"
    local regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if [[ "${email}" =~ ${regex} ]]; then
        return 0
    else
        return 1
    fi
}

validate_ip() {
    local ip="$1"
    local regex='^([0-9]{1,3}\.){3}[0-9]{1,3}$'

    if [[ "${ip}" =~ ${regex} ]]; then
        return 0
    else
        return 1
    fi
}

sanitize_filename() {
    local filename="$1"
    # Remove dangerous characters
    echo "${filename}" | tr -cd '[:alnum:]._-'
}
```

---

## Commenti e Documentazione

### Script Header
```bash
#!/usr/bin/env bash
#
# Script Name: backup-database.sh
# Description: Automated database backup with compression and rotation
#
# Usage: backup-database.sh [OPTIONS]
#
# Options:
#   -h, --help          Show help message
#   -d, --database DB   Database name
#   -o, --output DIR    Output directory
#
# Requirements:
#   - bash 4.0+
#   - mysqldump
#   - gzip
#
# Author: Nome Autore
# Email: author@example.com
# Date: 2025-11-16
# Version: 1.0.0
#
# License: MIT
#
# Examples:
#   # Basic backup
#   ./backup-database.sh -d mydb
#
#   # Custom output directory
#   ./backup-database.sh -d mydb -o /backup/custom
#
# Exit Codes:
#   0 - Success
#   1 - General error
#   2 - Missing requirements
#   3 - Invalid arguments
#
```

### Inline Comments
```bash
# TODO: Add support for PostgreSQL
# FIXME: Handle spaces in filenames
# NOTE: This function assumes UTC timezone
# HACK: Workaround for bug in bash 4.2

# Commenta il "perché", non il "cosa"
# ✅ BUONO:
# We retry 3 times because the API has intermittent failures
readonly MAX_RETRIES=3

# ❌ CATTIVO:
# Set MAX_RETRIES to 3
readonly MAX_RETRIES=3
```

---

## Note Aggiuntive

### Shell Check
```bash
# Use shellcheck for linting
# Install: apt-get install shellcheck
# Run: shellcheck script.sh

# Disable specific warnings
# shellcheck disable=SC2086
echo $variable

# Ignore file
# shellcheck source=/dev/null
source "${CONFIG_FILE}"
```

### Debugging
```bash
# Enable debug mode
set -x  # Print each command before executing
set +x  # Disable debug mode

# Debug specific section
(
    set -x
    # Commands to debug
    command1
    command2
)

# Trace with PS4
export PS4='+(${BASH_SOURCE}:${LINENO}): ${FUNCNAME[0]:+${FUNCNAME[0]}(): }'
set -x
```

### Riferimenti
- Bash Reference Manual
- Google Shell Style Guide
- ShellCheck wiki
- Advanced Bash-Scripting Guide

---

**Ultima revisione**: 2025-11-16
**Versione**: 1.0.0
