# 🛡️ Dummy-DNS CLI Tool

**Dummy DNS** is a command-line DNS manager tool for Linux. It can manage your DNS servers—store, remove, and reset them using simple commands. It’s easy to use. Currently, it’s in a basic version and not available via `apt`. Installation must be done manually using the install script provided in this repository.

## Why dummy-dns?

You might wonder why it’s called *dummy-dns*—instead of something more straightforward like `dns-mng`, `dns-setter`, `dns-manager`, or any other name that might sound more appropriate.

Well, this name was the result of a dumb decision by an idle programmer (me 😅) who had nothing better to do and decided to build a DNS manager from scratch. I tried several ways to set DNS on my Ubuntu machine, but they didn’t work (maybe you'll have better luck! 😄), so I made this “dumb” decision to create this project(and I like this name and it is a bit related to dumb)—and so, *dummy-dns* was born. It is not totally a dumb package, beacause you can just set and manage your DNS servers on your local machine just by your terminal easily.

## 🚀 Installation

This project is supported on Linux only. Installation is manual via the `install.sh` script (no `apt` support for now). The full source code is available in this repository, so you can inspect it for security or make your own modifications.

To install, run:

```bash
git clone https://github.com/pak-app/dummy-dns-conf.git
cd dummy-dns-conf
pip3 install pyinstaller
chmod +x install.sh
./install.sh
```

## 📚 Usage

Note: This tool requires `sudo` permissions because it reads and writes to the system DNS configuration file (`/etc/resolv.conf`).

Here are the available commands and examples (don’t forget to use `sudo`):

### Basic Usage

```bash
python3 main.py [OPTIONS]
```

---

## ⚙️ Available Options

### 📝 1. Set Custom DNS Configuration

```bash
python3 main.py -cf /path/to/config.json # it will ask you if you want to add the given confiuration to config.json file or not.
```

OR

```bash
python3 main.py --config-file /path/to/config.json
```

- **Purpose:** Sets the DNS configuration using the provided JSON config file.
- **JSON Format:**

```json
{
  "nameserver1": "8.8.8.8",
  "nameserver2": "1.1.1.1"
}
```

- **Default:** If not specified, it will use an empty string.

---

### 🌐 2. Set DNS by DNS Name

```bash
python3 main.py -s google_dns
```

OR

```bash
python3 main.py --set google_dns
```

- **Purpose:** Sets the DNS configuration using the given DNS name.
- **Default:** If the DNS name is not provided, it automatically uses the first DNS configuration found in `/etc/dummy-dns/config.json`.

---

### ❌ 3. Unset the Current DNS

```bash
python3 main.py --unset
```

- **Purpose:** Unsets and removes the current DNS configuration.
- **Action:** No value is required. It’s a `store_true` flag.

---

### 🔄 4. Use Default DNS Configuration

```bash
python3 main.py -d
```

OR

```bash
python3 main.py --default
```

- **Purpose:** Reverts DNS configuration to the default DNS servers.
- **Default:** Uses Shekan DNS as the default DNS.

---

### 🧹 5. Reset DNS to System Default

```bash
python3 main.py --reset
```

- **Purpose:** Resets the DNS configuration to the system’s default settings.
- **Action:** No value required (`store_true` flag).

---

### ⚡ 6. Force Reconfigure Default DNS

```bash
python3 main.py -fr
```

OR

```bash
python3 main.py --force-reset
```

- **Purpose:** Forcefully reconfigures and resets the default DNS settings.
- **⚠️ Warning:** This option **overwrites** the default DNS settings. Use with caution, especially if you're unsure whether the `/etc/resolv.conf` file is in its default state.

---

### 🔎 7. Check if Dummy-DNS is Active

```bash
python3 main.py -cd
```

OR

```bash
python3 main.py --check-dummy
```

- **Purpose:** Checks whether the Dummy-DNS configuration is currently applied or not.
- **Action:** No value required (`store_true` flag).

---

## 🔥 Examples

### Set DNS using a config file

```bash
python3 main.py -cf /etc/dummy-dns/config.json
```

### Set DNS using a name

```bash
python3 main.py -s google_dns
```

### Reset to system default

```bash
python3 main.py --reset
```

### Force reconfigure DNS

```bash
python3 main.py --force-reset
```

### Check if Dummy-DNS is active

```bash
python3 main.py --check-dummy
```

---

## 📝 JSON Configuration Format

Ensure that your configuration file follows this format:

```json
{
  "nameserver1": "8.8.8.8",
  "nameserver2": "1.1.1.1"
}
```

---

## Maintainer

Created and maintained by [Poorya](https://github.com/pak-app/).
