---
name: How to build Python from source on Ubuntu
---

1. Obligatory `sudo apt update`
2. Install dependencies `sudo apt install build-essential zlib1g-dev libssl-dev` (first two are needed for compilation, libssl-dev is needed for pip)
3. Download source from https://www.python.org
4. Extract it
5. cd into that folder
6. Run `./configure --enable-optimizations`
7. Run `make`
8. Run `sudo make install`
9. **Optional**: Run `python3 -m pip install --upgrade pip`, so that python won't nag you about updating pip every time you install something (for now)
10. **Optional**: Make `python` an alias for `python3`

You're done :)