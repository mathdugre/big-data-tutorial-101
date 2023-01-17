# Recommended Development Environment

## pyenv

## pipx

## hatch

## zsh Profile

```bash
# Python
export PIP_REQUIRE_VIRTUALENV=true
alias py=python
## pyenv
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
## pipx
export PATH=$HOME/.local/bin:$PATH
export PIPX_DEFAULT_PYTHON=python
## hatch
source ~/.zsh/completion/hatch-complete.zsh
```