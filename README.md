# Basic Keystore

A minimal CLI tool to create Ethereum keystore files from a private key. It encrypts your key with a password and saves it in the standard [Web3 Secret Storage](https://github.com/ethereum/wiki/wiki/Web3-Secret-Storage-Definition) format.

## Features

- **Secure input** — Private key and password are read via `getpass` (no echo, not stored in shell history)
- **Password confirmation** — Reduces risk of typos when setting the keystore password
- **Standard format** — Output is compatible with Geth, MetaMask, and other Ethereum tools

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Installation

With [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

## Usage

Run the keystore manager:

```bash
uv run python main.py
```

You will be prompted for:

1. **Private key** — Your Ethereum private key (input is hidden)
2. **Password** — A password to encrypt the keystore
3. **Password confirmation** — Same password again

On success, an encrypted keystore file is written to `account.keystore.json` in the current directory.

## Output

- **Success:** Keystore saved as `account.keystore.json`
- **Error:** If the two passwords do not match, the program exits with an error and no file is written

## Security

- Never share your private key or keystore file.
- Use a strong, unique password for the keystore.
- Keep `account.keystore.json` (and any backups) in a secure location and out of version control.
- Add `*.keystore.json` to your gitignore.

## Development

- Linting/formatting: [Ruff](https://docs.astral.sh/ruff/) is included as a dependency.
- Run Ruff: `uv run ruff check .` and `uv run ruff format .`

## License

See repository root for license information.
