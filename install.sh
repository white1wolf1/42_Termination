#!/bin/bash

INSTALL_DIR="$HOME/.termination"
SCRIPT="$INSTALL_DIR/termination.py"
BIN_DIR="$HOME/.local/bin"
BIN="$BIN_DIR/termination"


cmd_install() {
    if [ -d "$INSTALL_DIR" ]; then
        echo "Already installed at $INSTALL_DIR"
        echo "Run 'uninstall' first to reinstall."
        exit 1
    fi

    if ! command -v git &>/dev/null; then
        echo "Error: git not found. Install git and try again."
        exit 1
    fi

    if ! command -v python3 &>/dev/null; then
        echo "Error: python3 not found. Install Python 3 and try again."
        exit 1
    fi

    echo "Cloning into $INSTALL_DIR..."
    git clone --quiet https://github.com/white1wolf1/42_Termination.git "$INSTALL_DIR"

    mkdir -p "$BIN_DIR"
    printf '#!/bin/bash\npython3 "%s" "$@"\n' "$SCRIPT" > "$BIN"
    chmod +x "$BIN"

    # add ~/.local/bin to PATH if not already there
    case ":$PATH:" in
        *":$BIN_DIR:"*) ;;
        *)
            RC="${HOME}/.zshrc"
            [ -n "$BASH_VERSION" ] && RC="${HOME}/.bashrc"
            echo "export PATH=\"\$PATH:$BIN_DIR\"" >> "$RC"
            echo "Added $BIN_DIR to PATH in $RC"
            echo "Run: source $RC  (or open a new terminal)"
            ;;
    esac

    echo "Installed. Type 'termination' to run."
}

cmd_uninstall() {
    if [ -d "$INSTALL_DIR" ]; then
        rm -rf "$INSTALL_DIR"
        echo "Removed $INSTALL_DIR"
    else
        echo "Not installed — nothing to remove."
    fi

    if [ -f "$BIN" ]; then
        rm "$BIN"
        echo "Removed $BIN"
    fi
}


cmd_update() {
    if [ ! -d "$INSTALL_DIR" ]; then
        echo "Not installed."
        exit 1
    fi
    echo "Updating..."
    git -C "$INSTALL_DIR" pull --quiet
    echo "Done."
}

usage() {
    echo "Usage: $0 [install|uninstall|update]"
    echo ""
    echo "  install    Clone repo to $INSTALL_DIR"
    echo "  uninstall  Remove installation"
    echo "  update     Pull latest changes"
    echo ""
    echo "One-liner install:"
    echo "  curl -fsSL https://raw.githubusercontent.com/white1wolf1/42_Termination/main/install.sh | bash -s -- install"
}

case "${1:-usage}" in
    install)   cmd_install ;;
    uninstall) cmd_uninstall ;;
    update)    cmd_update ;;
    *)         usage ;;
esac
