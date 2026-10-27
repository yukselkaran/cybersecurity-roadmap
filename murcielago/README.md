# Murciélago 🦇

**Murciélago** is a subnet calculator and network scanner written in pure Python.
It computes network information from CIDR notation and discovers live hosts on a subnet using three different methods.

---

## Features

- **Subnet calculation** — network, broadcast, subnet mask, host range, and host count (`/31` and `/32` special cases per RFC 3021).
- **Three scanning methods:**

  | Method | Description | Root required? |
  |--------|-------------|:--------------:|
  | `subprocess` | Calls the system `ping` command, multi-threaded (ThreadPoolExecutor) | No |
  | `icmp` | Hand-crafted ICMP echo packets over raw sockets | Yes |
  | `arp` | L2 ARP scan via Scapy (MAC addresses) | Yes |

- **Platform-independent** `ping` invocation (correct flags for macOS / Linux / Windows).
- **Adjustable concurrency** — `max_workers` and `timeout` parameters.

---

## Requirements

- Python 3.8+
- [scapy](https://scapy.net/) (only for the `arp` scan)

```bash
pip install scapy
```

---

## Usage

```bash
python main.py --cidr <CIDR> [--scan <method>]
```

| Argument | Required | Description |
|----------|:--------:|-------------|
| `--cidr` | Yes | CIDR notation, e.g. `192.168.1.0/24` |
| `--scan` | No | Scan method: `subprocess`, `icmp`, or `arp` |

### Examples

Compute subnet information only:
```bash
python main.py --cidr 192.168.1.0/24
```

Scan with subprocess ping (no root required):
```bash
python main.py --cidr 192.168.1.0/28 --scan subprocess
```

Raw ICMP or ARP scan (root/sudo required):
```bash
sudo python main.py --cidr 192.168.1.0/28 --scan icmp
sudo python main.py --cidr 192.168.1.0/28 --scan arp
```

> The `icmp` and `arp` methods use raw sockets and therefore require root privileges.
> Without them, the program exits with a clear error message.

---

## Project Structure

| File | Role |
|------|------|
| `main.py` | CLI interface (argparse) |
| `subnet_calc.py` | CIDR / IP calculations (pure functions) |
| `ping_sweep.py` | Subprocess- and ICMP-based host scanning |
| `icmp_ping.py` | ICMP packet generation, checksum, and reply capture |
| `arp_scan.py` | ARP scan via Scapy |
| `benchmark.py` | Concurrency (worker count) performance test |

---

## Benchmark

### Concurrency Test — 2026-08-08

A local `/28` subnet was scanned using `subprocess`-based ping with a fixed 200 ms timeout.
As the worker count increased, scan time dropped significantly up to about 25 workers.

| Workers | Scan Time | Hosts Found |
|:-------:|:---------:|:-----------:|
| 1 | 15.826 s | 1 |
| 5 | 3.651 s | 2 |
| 10 | 2.440 s | 2 |
| 25 | **1.223 s** | 2 |
| 50 | 1.235 s | 2 |

**Finding:** Raising the worker count from 1 to 25 reduced scan time by about 92.3% (~12.9x speedup).
Going from 25 to 50 provided no additional benefit, and was even marginally (~1%) slower. In this test
environment, performance plateaued at around 25 concurrent workers.

> **Note:** These results are environment-dependent and should not be interpreted as a universal
> "optimal worker count." The test used a `/28` subnet and a 200 ms timeout; larger subnets and
> different network conditions may produce different results.

Run the benchmark yourself:
```bash
python benchmark.py
```

---

## Legal Notice

This tool should only be used on networks you own or have explicit permission to scan.
Unauthorized network scanning is illegal in many jurisdictions. The user assumes all responsibility.
