#!/usr/bin/sh

rm -rf "$HOME/.config/nvim"

mkdir -p "$HOME/.config/nvim"

stow --restow --target="$HOME"/.config/nvim .
