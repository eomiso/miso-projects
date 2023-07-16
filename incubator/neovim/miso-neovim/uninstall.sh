#!/usr/bin/sh


# ANSI escape sequence for colors
GREEN="\033[0;32m"
UNDERLINE='\033[4m'
RESET="\033[0m"
BOLD="\033[1m"

echo -e "${BOLD}${UNDERLINE}Deleting the XDG files${RESET}"

set -x
set -e

rm -rf $HOME/.local/state/nvim
rm -rf $HOME/.local/share/nvim
rm -rf $HOME/.config/nvim

echo -e "${GREEN}${BOLD}DONE${RESET}"
