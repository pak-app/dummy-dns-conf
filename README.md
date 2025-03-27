# DNS Manager

Dummy DNS is a DNS manager CLI tool for Linux. It can manage your DNS servers, store, remove, and reset them with commands. It is easy to use. Currently, it is in its simple version and not listed on `apt`. Installation is manual, by building and installing manually with the install script in this repository.

## Why dummy-dns?

You may wonder why we call it better. dns-mng, dns-setter, dns-manager, or any other names you think are more related and suitable for this app, and why this name set?

So I should say that this is a dummy decision of an idle programmer without anything to do, and decide this dummy decision to build a DNS manager from scratch. I tried many ways to set DNS on my Ubuntu but it failed (you can do it instead of me :grin:), so I made this dummy decision to build and name this project dummy-dns.

## Installation

It is supported on Linux and the installation is manual with `install.sh` script (no `apt`). The codes and all things are available on this repository, and you can check its security. Do these commands to install:

```bash
git clone https://github.com/pak-app/dummy-dns-conf.git
cd dummy-dns-conf
chmod +x install.sh
./install.sh
```

## Usage

First of all, this package needs sudo to use it, because writing and reading the DNS configuration file 
