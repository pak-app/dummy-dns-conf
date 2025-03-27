# DNS Manager

**Dummy DNS** is a command-line DNS manager tool for Linux. It can manage your DNS servers—store, remove, and reset them using simple commands. It’s easy to use. Currently, it’s in a basic version and not available via `apt`. Installation must be done manually using the install script provided in this repository.

## Why dummy-dns?

You might wonder why it’s called *dummy-dns*—instead of something more straightforward like `dns-mng`, `dns-setter`, `dns-manager`, or any other name that might sound more appropriate.

Well, this name was the result of a dumb decision by an idle programmer (me 😅) who had nothing better to do and decided to build a DNS manager from scratch. I tried several ways to set DNS on my Ubuntu machine, but they didn’t work (maybe you'll have better luck! 😄), so I made this “dumb” decision to create this project(and I like this name and it is a bit related to dumb)—and so, *dummy-dns* was born. It is not totally a dumb package, beacause you can just set your DNS servers on your local machine just by entering and managing them easily.

## Installation

This project is supported on Linux only. Installation is manual via the `install.sh` script (no `apt` support for now). The full source code is available in this repository, so you can inspect it for security or make your own modifications.

To install, run:

```bash
git clone https://github.com/pak-app/dummy-dns-conf.git
cd dummy-dns-conf
pip3 install pyinstaller
chmod +x install.sh
./install.sh
```

## Usage

Note: This tool requires `sudo` permissions because it reads and writes to the system DNS configuration file (`/etc/resolv.conf`).

Here are the available commands and examples (don’t forget to use sudo):

```bash
dummy-dns --reset # revert system default DNS settings
# Caution: To use this command be carefull what you gonna do, use dummy-dns --help for more information.
dummy-dns --force-reset # saves current system DNS settings as default settings for dummy-dns

dummy-dns --config-file ./config.json # set DNS servers on config.json file

dummy-dns --check-dummy # Check DNS settings is set or not

dummy-dns --default # set default and built-in configuration(currently Shecan DNS is supported (https://shecan.ir/).

dummy-dns --unset # Set system default configuration
```

## Maintainer

Created and maintained by [Poorya](https://github.com/pak-app/).
