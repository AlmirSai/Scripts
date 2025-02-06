# Git Tutorial - Essential Commands and Best Practices

## Table of Contents
1. [Repository Setup](#repository-setup)
2. [Basic Operations](#basic-operations)
3. [Branching and Merging](#branching-and-merging)
4. [Remote Operations](#remote-operations)
5. [Advanced Features](#advanced-features)
6. [Configuration](#configuration)
7. [Best Practices](#best-practices)
8. [Git Workflows](#git-workflows)
9. [Troubleshooting](#troubleshooting)
10. [Security Guidelines](#security-guidelines)

## Repository Setup

### Initialize a New Repository
```bash
git init
```
Creates a new Git repository in the current directory

### Clone an Existing Repository
```bash
git clone <repository-url>
```
Downloads a copy of a remote repository

## Basic Operations

### Check Status
```bash
git status
```
Shows the working tree status

### Stage Changes
```bash
git add <file-name>    # Stage specific file
git add .              # Stage all changes
git add -p             # Stage changes interactively
```

### Commit Changes
```bash
git commit -m "commit message"    # Commit with message
git commit -am "commit message"   # Stage tracked files and commit
```

### View History
```bash
git log                 # View commit history
git log --oneline       # Compact view
git log --graph         # Graphical view
```

## Branching and Merging

### Branch Management
```bash
git branch                  # List branches
git branch <branch-name>    # Create new branch
git checkout <branch-name>  # Switch to branch
git checkout -b <branch-name>  # Create and switch to new branch
git branch -d <branch-name>    # Delete branch
```

### Merging
```bash
git merge <branch-name>    # Merge branch into current branch
git merge --abort          # Abort merge in case of conflicts
```

### Handling Conflicts
```bash
git diff                   # Show conflicts
git mergetool              # Use configured merge tool
```

## Remote Operations

### Remote Repository Management
```bash
git remote -v                          # List remote repositories
git remote add <name> <url>            # Add remote repository
git remote remove <name>               # Remove remote
```

### Syncing with Remote
```bash
git fetch                  # Download objects and refs
git pull                   # Fetch and merge changes
git push                   # Upload local changes
git push -u origin <branch>  # Set upstream branch
```

## Advanced Features

### Stashing Changes
```bash
git stash                  # Stash changes
git stash list             # List stashes
git stash pop              # Apply and remove stash
git stash apply            # Apply but keep stash
```

### History Modification
```bash
git commit --amend         # Modify last commit
git rebase -i HEAD~n       # Interactive rebase
git reset --hard HEAD~1    # Undo last commit and changes
git reset --soft HEAD~1    # Undo last commit only
```

### Tags
```bash
git tag                    # List tags
git tag -a v1.0 -m "message"  # Create annotated tag
git push --tags            # Push tags to remote
```

## Configuration

### User Configuration
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Aliases
```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.st status
```

## Best Practices

1. **Commit Messages**
   - Write clear, concise commit messages
   - Use present tense ("Add feature" not "Added feature")
   - First line should be under 50 characters
   - Include detailed description if needed

2. **Branching Strategy**
   - Keep `main/master` branch stable
   - Create feature branches for new work
   - Delete merged branches
   - Use descriptive branch names

3. **Commits**
   - Make atomic commits (one logical change per commit)
   - Commit early and often
   - Don't commit broken code

4. **Pull Requests**
   - Keep PRs small and focused
   - Review code before merging
   - Update branch with main before merging

5. **General Tips**
   - Use `.gitignore` for project-specific files
   - Don't commit sensitive information
   - Regularly fetch and pull from remote
   - Back up your repositories

## Git Workflows

### GitFlow
A robust workflow for managing feature development, releases, and hotfixes.

```bash
# Initialize GitFlow
git flow init

# Start a new feature
git flow feature start feature_name

# Finish a feature
git flow feature finish feature_name

# Start a release
git flow release start v1.0.0

# Finish a release
git flow release finish v1.0.0
```

### Trunk-Based Development
A streamlined workflow focusing on small, frequent changes to the main branch.

1. Create short-lived feature branches
2. Merge frequently (at least daily)
3. Use feature flags for incomplete features
4. Maintain high test coverage

## Troubleshooting

### Common Issues and Solutions

1. **Detached HEAD State**
```bash
git checkout main    # Return to main branch
git pull origin main # Update with remote
```

2. **Undo Last Commit (Keep Changes)**
```bash
git reset --soft HEAD~1
```

3. **Remove Untracked Files**
```bash
git clean -n    # Dry run
git clean -fd   # Force delete
```

4. **Fix Wrong Commit Message**
```bash
git commit --amend -m "New message"
```

5. **Recover Deleted Branch**
```bash
git reflog               # Find the SHA
git checkout -b branch_name SHA
```

## Security Guidelines

1. **Repository Security**
   - Use `.gitignore` for sensitive files
   - Implement Git hooks for pre-commit checks
   - Regular security audits with `git secrets`

2. **Credential Management**
```bash
# Use credential helper
git config --global credential.helper cache

# Set cache timeout (in seconds)
git config --global credential.helper 'cache --timeout=3600'
```

3. **Signing Commits**
```bash
# Configure GPG key
git config --global user.signingkey <key-id>

# Sign commits automatically
git config --global commit.gpgsign true

# Sign a commit
git commit -S -m "Signed commit"
```

4. **Access Control**
   - Use SSH keys instead of passwords
   - Implement branch protection rules
   - Regular access review

## Repository Backup and Recovery

### Local Backup Strategies
```bash
# Create a bare backup
git clone --bare /path/to/repo /path/to/backup.git

# Create a mirror backup
git clone --mirror /path/to/repo /path/to/backup.git

# Update mirror backup
cd /path/to/backup.git
git remote update
```

### Disaster Recovery Procedures
1. **Corrupted Repository Recovery**
```bash
# Check repository integrity
git fsck --full

# Repair corrupted objects
git gc --aggressive

# Recover lost commits
git reflog expire --expire=now --all
git gc --prune=now
```

2. **Lost Changes Recovery**
```bash
# Find lost commits
git fsck --lost-found

# Examine dangling commits
git show <SHA>

# Recover specific commit
git cherry-pick <SHA>
```

## Advanced Git Operations

### Git Hooks
```bash
# Common hook locations
.git/hooks/pre-commit
.git/hooks/pre-push
.git/hooks/commit-msg

# Example pre-commit hook
#!/bin/sh
if git diff --cached | grep -i "TODO"; then
    echo "Warning: TODOs found in staged changes"
    exit 1
fi
```

### Git Submodules
```bash
# Add submodule
git submodule add <repository-url> <path>

# Initialize submodules
git submodule init
git submodule update

# Update all submodules
git submodule update --remote --merge
```

### Git LFS (Large File Storage)
```bash
# Install Git LFS
git lfs install

# Track large files
git lfs track "*.psd"

# Verify tracked files
git lfs ls-files
```

### Continuous Integration Practices
1. **Pre-push Checks**
```bash
#!/bin/sh
# .git/hooks/pre-push

# Run tests
npm test

# Check code style
lint-staged
```

2. **Branch Protection**
- Require status checks to pass
- Enforce signed commits
- Require linear history

3. **Automated Workflows**
```yaml
# Example GitHub Actions workflow
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: |
          npm install
          npm test
```

## Git Internals and Performance

### Git Object Model
```bash
# View Git object contents
git cat-file -p <hash>    # Show object contents
git cat-file -t <hash>    # Show object type

# List all objects
git rev-list --objects --all
```

### Repository Optimization
```bash
# Optimize repository
git gc                    # Run garbage collection
git gc --aggressive       # Aggressive optimization
git prune                # Remove unreachable objects

# Pack repository
git repack -a -d         # Repack all objects
git count-objects -v     # View repository size
```

### Custom Git Commands
```bash
# Create custom command in ~/.gitconfig
[alias]
    changelog = log --pretty=format:"%h - %an, %ar : %s"
    graph = log --graph --oneline --decorate
    cleanup = !git branch --merged | grep -v "\*" | xargs -n 1 git branch -d
```

## Git Server Administration

### Server Setup
```bash
# Initialize bare repository
git init --bare /path/to/repo.git

# Configure Git daemon
git daemon --reuseaddr --base-path=/path/to/git/repos/

# Set up Git over SSH
git config --system receive.fsckObjects true
```

### Repository Maintenance
```bash
# Check repository health
git fsck --full          # Check all objects
git verify-pack -v .git/objects/pack/*.idx  # Verify packed objects

# Configure reflog expiry
git config gc.reflogExpire 90
git config gc.reflogExpireUnreachable 30
```

### Advanced Collaboration Strategies

1. **Feature Flags**
   - Use environment variables
   - Implement feature toggles
   - Manage long-running features

2. **Code Review Workflow**
   ```bash
   # Create review branch
   git checkout -b review/feature-name
   
   # Prepare patch series
   git format-patch -M origin/main
   
   # Apply review comments
   git commit --fixup=SHA
   git rebase -i --autosquash main
   ```

3. **CI/CD Integration**
   ```yaml
   # Advanced GitHub Actions workflow
   name: Advanced CI/CD
   on:
     push:
       branches: [ main, develop ]
     pull_request:
       branches: [ main ]
   
   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
           with:
             fetch-depth: 0
         
         - name: Lint commits
           run: |
             npx @commitlint/cli --from=${{ github.event.pull_request.base.sha }}
         
         - name: Run tests
           run: |
             npm install
             npm test
         
         - name: Check coverage
           run: npm run coverage
   ```

## Backend Development Git Practices

### Database Migration Management
```bash
# Create feature branch for migrations
git checkout -b feature/add-user-table

# Commit migration files separately
git add db/migrations/20231215_create_users.sql
git commit -m "feat(db): add users table migration"

# Keep schema changes in separate commits
git add db/schema.sql
git commit -m "chore(db): update schema with users table"
```

### Configuration Management
1. **Environment-Specific Files**
   ```bash
   # Add template to version control
   git add config/database.template.yml
   
   # Ignore environment-specific configs
   echo "config/*.yml" >> .gitignore
   echo "!config/*.template.yml" >> .gitignore
   ```

2. **Sensitive Data Protection**
   ```bash
   # Use git-crypt for encrypted files
   git-crypt init
   git-crypt add-gpg-user USER_ID
   
   # Specify files to encrypt
   echo "secrets.yml filter=git-crypt diff=git-crypt" >> .gitattributes
   ```

### Deployment Workflow
1. **Feature Branch Deployment**
   ```bash
   # Create deployment branch
   git checkout -b deploy/feature-name
   
   # Merge feature with deployment configs
   git merge feature/new-api
   git add deployment/
   git commit -m "deploy: configure feature-name for staging"
   ```

2. **Hotfix Process**
   ```bash
   # Create hotfix branch from production
   git checkout -b hotfix/fix-api-timeout production
   
   # Apply fix and tag
   git commit -am "fix: increase API timeout threshold"
   git tag -a v1.2.1 -m "Hotfix: API timeout fix"
   
   # Merge to both production and development
   git checkout production
   git merge hotfix/fix-api-timeout
   git checkout development
   git merge hotfix/fix-api-timeout
   ```

### Backend-Specific .gitignore
```bash
# Dependencies
node_modules/
venv/
.env

# Logs
logs/
*.log

# Database
*.sqlite
*.db
dump.sql

# Cache
.cache/
__pycache__/
.pytest_cache/

# IDE
.idea/
.vscode/
```

### Microservices Version Control
1. **Service Repository Structure**
   ```bash
   # Clone service repository
   git clone git@github.com:org/user-service.git
   
   # Set up upstream for shared libraries
   git remote add shared-lib git@github.com:org/shared-lib.git
   git subtree add --prefix=lib/shared shared-lib main
   ```

2. **Cross-Service Changes**
   ```bash
   # Create branch for cross-service feature
   git checkout -b feature/auth-upgrade
   
   # Update shared library
   git subtree pull --prefix=lib/shared shared-lib feature/auth-v2
   
   # Commit service-specific changes
   git commit -am "feat: implement new auth protocol"
   ```

### CI/CD Pipeline Management
1. **Pipeline Configuration**
   ```bash
   # Version control CI/CD configs
   git add .github/workflows/
   git commit -m "ci: update deployment pipeline"
   
   # Create branch for pipeline testing
   git checkout -b ci/test-new-pipeline
   ```

2. **Environment Management**
   ```bash
   # Store environment templates
   git add deploy/env.template.json
   
   # Ignore environment-specific files
   echo "deploy/env.*.json" >> .gitignore
   echo "!deploy/env.template.json" >> .gitignore
   ```

This section provides backend-specific Git practices and workflows, focusing on database management, configuration handling, and deployment strategies commonly used in backend development.

This comprehensive guide covers Git commands, workflows, best practices, and advanced topics. For more detailed information, consult the [official Git documentation](https://git-scm.com/doc).