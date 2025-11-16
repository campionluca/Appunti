# Code Policies - Git

> Standard, convenzioni e best practices per l'uso di Git e controllo versione

## 📋 Indice
- [Convenzioni Commit](#convenzioni-commit)
- [Branching Strategy](#branching-strategy)
- [Pull Request](#pull-request)
- [.gitignore](#gitignore)
- [Best Practices](#best-practices)
- [Workflow Comuni](#workflow-comuni)
- [Git Hooks](#git-hooks)
- [Documentazione](#documentazione)

---

## Convenzioni Commit

### Formato Commit Message
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- **feat**: Nuova feature
- **fix**: Bug fix
- **docs**: Solo cambiamenti documentazione
- **style**: Formattazione, mancano punti e virgola, etc (no code change)
- **refactor**: Refactoring (no feat, no fix)
- **perf**: Performance improvements
- **test**: Aggiunta o fix di test
- **chore**: Manutenzione, aggiornamento dipendenze
- **ci**: Modifiche a CI/CD
- **build**: Modifiche al build system
- **revert**: Revert di un commit precedente

### Subject
- Max 50 caratteri
- Imperativo presente: "add" non "added" o "adds"
- Non capitalizzare la prima lettera
- Nessun punto finale

### Body (opzionale)
- Separato dal subject con una riga vuota
- Max 72 caratteri per riga
- Spiega cosa e perché, non come
- Usa bullet points se necessario

### Footer (opzionale)
- Breaking changes: `BREAKING CHANGE: description`
- Issue reference: `Closes #123`, `Fixes #456`, `Related to #789`

### Esempi
```bash
# Esempio semplice
feat: add user authentication

# Esempio con scope
feat(auth): implement JWT token validation

# Esempio completo
feat(user): add profile picture upload

Implement functionality to allow users to upload profile pictures.
The images are resized to 200x200 and stored in S3.

- Add multer middleware for file uploads
- Integrate with AWS S3
- Add image validation and resizing

Closes #123
```

### Conventional Commits Examples
```bash
# Feature
feat: add shopping cart functionality
feat(api): add endpoint for user registration
feat(ui): implement dark mode toggle

# Bug fix
fix: resolve memory leak in data processor
fix(auth): correct token expiration logic
fix(deps): update vulnerable package

# Documentation
docs: update API documentation
docs(readme): add installation instructions

# Refactoring
refactor: simplify user validation logic
refactor(db): optimize query performance

# Performance
perf: improve image loading time
perf(api): cache frequently accessed data

# Breaking change
feat(api): change authentication endpoint

BREAKING CHANGE: The /auth endpoint now requires API key in header
instead of query parameter. Update all API clients accordingly.
```

---

## Branching Strategy

### Git Flow
```
main (production)
├── develop (integration)
│   ├── feature/user-authentication
│   ├── feature/shopping-cart
│   ├── bugfix/login-error
│   └── hotfix/critical-security-fix
└── release/v1.2.0
```

### Branch Naming Conventions
```bash
# Feature branches
feature/short-description
feature/123-issue-title
feat/user-profile-page

# Bug fix branches
bugfix/short-description
fix/123-memory-leak
bugfix/login-validation

# Hotfix branches
hotfix/critical-issue
hotfix/security-patch

# Release branches
release/v1.2.0
release/2025.01

# Experimental branches
experiment/new-architecture
spike/performance-optimization
```

### GitHub Flow (Simplified)
```
main (production)
├── feature/add-payment
├── fix/checkout-bug
└── docs/update-readme
```

### Trunk-Based Development
```
main (trunk)
├── short-lived-feature-branch-1
└── short-lived-feature-branch-2
```

---

## Pull Request

### PR Title
- Segue le stesse convenzioni dei commit messages
- Chiaro e descrittivo
```
feat(auth): implement OAuth2 login
fix(api): resolve rate limiting issue
docs: update contribution guidelines
```

### PR Description Template
```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Related Issues
Closes #123
Related to #456

## Changes Made
- Change 1
- Change 2
- Change 3

## How Has This Been Tested?
- [ ] Unit tests
- [ ] Integration tests
- [ ] Manual testing

## Screenshots (if applicable)
[Add screenshots here]

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published

## Additional Notes
Any additional information or context
```

### Code Review Guidelines
```markdown
# For Reviewers:
- Be constructive and specific
- Focus on the code, not the person
- Ask questions instead of making demands
- Approve if minor changes needed
- Request changes if significant issues

# For Authors:
- Respond to all comments
- Don't take feedback personally
- Ask for clarification if needed
- Mark conversations as resolved
- Update PR description if scope changes
```

---

## .gitignore

### Template Base
```gitignore
# ===================================
# Operating System Files
# ===================================

# macOS
.DS_Store
.AppleDouble
.LSOverride
._*

# Windows
Thumbs.db
ehthumbs.db
Desktop.ini
$RECYCLE.BIN/

# Linux
*~
.directory

# ===================================
# IDE and Editor Files
# ===================================

# Visual Studio Code
.vscode/
*.code-workspace

# JetBrains IDEs (IntelliJ, PyCharm, etc.)
.idea/
*.iml
*.ipr
*.iws

# Vim
*.swp
*.swo
*~

# Sublime Text
*.sublime-project
*.sublime-workspace

# ===================================
# Language Specific
# ===================================

# Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*
.npm
.eslintcache

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.venv
pip-log.txt
.pytest_cache/
.coverage
htmlcov/

# Java
*.class
*.jar
*.war
*.ear
target/
.gradle/
build/

# C/C++
*.o
*.exe
*.out
*.a
*.so

# ===================================
# Environment and Secrets
# ===================================

.env
.env.local
.env.*.local
*.key
*.pem
secrets.yml
credentials.json

# ===================================
# Build and Distribution
# ===================================

dist/
build/
*.egg-info/
*.egg

# ===================================
# Logs and Databases
# ===================================

*.log
*.sql
*.sqlite
*.db

# ===================================
# Temporary Files
# ===================================

tmp/
temp/
*.tmp
*.bak
*.swp

# ===================================
# Project Specific
# ===================================

# Add your project-specific ignores here
```

### Global gitignore
```bash
# Create global gitignore
git config --global core.excludesfile ~/.gitignore_global

# Add to ~/.gitignore_global
cat << 'EOF' > ~/.gitignore_global
.DS_Store
.vscode/
.idea/
*.swp
EOF
```

---

## Best Practices

### Commit Best Practices
```bash
# ✅ DO: Commit early and often
git commit -m "feat: add user model"
git commit -m "feat: add user controller"
git commit -m "feat: add user routes"

# ❌ DON'T: One massive commit
git commit -m "add entire user feature"  # Too big!

# ✅ DO: Atomic commits (one logical change)
git commit -m "fix: correct email validation regex"

# ❌ DON'T: Multiple unrelated changes
git commit -m "fix email validation and add dark mode and update dependencies"

# ✅ DO: Use imperative mood
git commit -m "add feature"
git commit -m "fix bug"

# ❌ DON'T: Past tense or present continuous
git commit -m "added feature"
git commit -m "adding feature"
```

### Branch Best Practices
```bash
# Always work on a branch (not main)
git checkout -b feature/new-feature

# Keep branches short-lived (max 2-3 days)
# Merge or delete after PR is merged

# Sync with main frequently
git checkout main
git pull origin main
git checkout feature/my-feature
git merge main  # or rebase

# Delete merged branches
git branch -d feature/old-feature
git push origin --delete feature/old-feature
```

### Rebase vs Merge
```bash
# Merge: Preserva history completa
git merge feature-branch
# Creates merge commit

# Rebase: Linear history
git rebase main
# Replays commits on top of main

# When to use:
# - Merge: Per feature branches in main (preserva context)
# - Rebase: Per sync feature con main (clean history)

# Interactive rebase per cleanup
git rebase -i HEAD~3
# Squash, reorder, edit commits
```

### Stashing
```bash
# Save work in progress
git stash save "WIP: working on feature"

# List stashes
git stash list

# Apply stash
git stash apply stash@{0}
git stash pop  # Apply and remove

# Drop stash
git stash drop stash@{0}

# Stash including untracked files
git stash -u
```

---

## Workflow Comuni

### Feature Development Workflow
```bash
# 1. Create feature branch from main
git checkout main
git pull origin main
git checkout -b feature/new-feature

# 2. Make changes and commit
git add .
git commit -m "feat: implement feature part 1"
git commit -m "feat: implement feature part 2"

# 3. Sync with main
git checkout main
git pull origin main
git checkout feature/new-feature
git rebase main

# 4. Push and create PR
git push origin feature/new-feature
# Create PR on GitHub/GitLab

# 5. After PR approved and merged
git checkout main
git pull origin main
git branch -d feature/new-feature
```

### Hotfix Workflow
```bash
# 1. Create hotfix from main
git checkout main
git pull origin main
git checkout -b hotfix/critical-bug

# 2. Fix and commit
git add .
git commit -m "fix: resolve critical security issue"

# 3. Push and merge immediately
git push origin hotfix/critical-bug
# Fast-track review and merge

# 4. Tag release
git tag -a v1.2.1 -m "Hotfix release 1.2.1"
git push origin v1.2.1
```

### Fixing Mistakes
```bash
# Amend last commit
git commit --amend -m "fix: corrected commit message"

# Undo last commit (keep changes)
git reset HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Revert commit (create new commit that undoes)
git revert <commit-hash>

# Reset to specific commit
git reset --hard <commit-hash>

# Recover deleted commit
git reflog
git cherry-pick <commit-hash>
```

---

## Git Hooks

### Pre-commit Hook
```bash
#!/bin/bash
# .git/hooks/pre-commit

# Run linter
npm run lint
if [ $? -ne 0 ]; then
    echo "Linting failed. Commit aborted."
    exit 1
fi

# Run formatter
npm run format
git add -u

# Run tests
npm test
if [ $? -ne 0 ]; then
    echo "Tests failed. Commit aborted."
    exit 1
fi

exit 0
```

### Commit-msg Hook
```bash
#!/bin/bash
# .git/hooks/commit-msg

commit_msg=$(cat "$1")

# Check commit message format (Conventional Commits)
pattern="^(feat|fix|docs|style|refactor|perf|test|chore|ci|build|revert)(\(.+\))?: .{1,50}"

if ! echo "$commit_msg" | grep -qE "$pattern"; then
    echo "ERROR: Commit message doesn't follow Conventional Commits format"
    echo "Format: <type>(<scope>): <subject>"
    echo "Example: feat(auth): add login functionality"
    exit 1
fi

exit 0
```

### Using Husky (Node.js)
```json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged",
      "commit-msg": "commitlint -E HUSKY_GIT_PARAMS"
    }
  },
  "lint-staged": {
    "*.js": ["eslint --fix", "git add"],
    "*.{json,md}": ["prettier --write", "git add"]
  }
}
```

---

## Documentazione

### README.md Essentials
```markdown
# Project Name

Brief description of the project

## Installation

\`\`\`bash
npm install
\`\`\`

## Usage

\`\`\`bash
npm start
\`\`\`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT
```

### CONTRIBUTING.md
```markdown
# Contributing Guidelines

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a feature branch
4. Make changes
5. Submit a pull request

## Commit Message Format

Follow [Conventional Commits](https://www.conventionalcommits.org/)

## Code Style

- Run `npm run lint` before committing
- Follow existing code patterns

## Testing

- Add tests for new features
- Ensure all tests pass: `npm test`

## Pull Request Process

1. Update documentation
2. Add tests
3. Request review
4. Wait for approval
```

### Tags and Releases
```bash
# Create annotated tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push tags
git push origin v1.0.0
git push origin --tags

# Semantic Versioning
# MAJOR.MINOR.PATCH
# 1.0.0 -> 1.0.1 (patch: bug fixes)
# 1.0.1 -> 1.1.0 (minor: new features, backward compatible)
# 1.1.0 -> 2.0.0 (major: breaking changes)
```

---

## Note Aggiuntive

### Git Configuration
```bash
# User identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Default editor
git config --global core.editor "code --wait"

# Default branch name
git config --global init.defaultBranch main

# Aliases
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.lg "log --graph --oneline --decorate --all"

# Pull rebase by default
git config --global pull.rebase true

# Auto-correct typos
git config --global help.autocorrect 1
```

### Useful Git Commands
```bash
# Beautiful log
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit

# Show changed files
git diff --stat

# Search in commits
git log --grep="search term"

# Find who changed a line
git blame file.txt

# Show file history
git log -p -- file.txt

# Cherry-pick specific commit
git cherry-pick <commit-hash>

# Clean untracked files
git clean -fd
```

### Riferimenti
- Pro Git Book (git-scm.com)
- Conventional Commits (conventionalcommits.org)
- Git Flow (nvie.com/posts/a-successful-git-branching-model)
- Semantic Versioning (semver.org)

---

**Ultima revisione**: 2025-11-16
**Versione**: 1.0.0
