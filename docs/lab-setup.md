# My lab setup

The lab is small on purpose. A sample should never reach my main machine, and I should be able to throw the whole thing away.

## Host and guest

I run VMware Workstation on a Windows host, with Kali Linux as a dedicated analysis VM. In the VM settings:

- The network adapter is NAT. I never use Bridged, so the VM stays off my home LAN.
- Shared folders are off.
- Drag and drop and copy/paste between host and guest are off.
- USB and removable devices are disconnected.

Moving files out of a VM with sharing off is a nuisance, but that's the point. Nearly everything I take out is text I wrote myself.

## Packages

```bash
sudo apt update
sudo apt install -y curl wget whois bind9-dnsutils ripgrep mpack ripmime jq \
    python3-venv python3-full pipx uuid-runtime
```

Two things tripped me up. `munpack` is a command, and the package is `mpack`. One wrong package name makes `apt` abort the whole line, so nothing got installed. Also, `uuidgen` comes from `uuid-runtime`. I didn't have it when I generated Sigma rule IDs, so my first IDs were blank. Python's `uuid.uuid4()` works as a fallback.

## Python in a virtual environment

Recent Kali and Debian block system-wide `pip install` (PEP 668). I don't use `--break-system-packages`. I use a venv:

```bash
mkdir -p ~/phishing-email-analysis && cd ~/phishing-email-analysis
python3 -m venv .venv
source .venv/bin/activate
pip install eml-parser iocextract tldextract stix2 requests
pip install sigma-cli pysigma-backend-elasticsearch
```

To check that everything landed:

```bash
which munpack ripmime rg dig whois jq
python -c "import iocextract, stix2, tldextract; print('ok')"
sigma check --help | head -3
```

## Snapshots

A snapshot is a save point. I keep two.

| Snapshot | What it holds | When I use it |
|---|---|---|
| `clean-lab-baseline` | Kali with tools installed and nothing dirty | I never touch it. It is a fresh start when I need one |
| `pre-case-NNN-ready` | Tools, folders and the sample copied in, nothing opened | I revert to it after a case, once the report is out |

My rules:

1. I take the case snapshot after the folders and sample exist. Otherwise a revert wipes my setup too.
2. A revert erases everything since the snapshot, so I copy the report out first.
3. After a revert I check the clock with `date`, because header analysis depends on timestamps.
4. I don't use a revert to fix a frozen VM. I force it off from VMware and then check that my files survived.

## Layout inside the VM

```
phishing-email-analysis/
  cases/case-001-reply-phishing/
    raw/        original sample, read-only, never published
    evidence/   header dump, whois output, enrichment, hash list
    iocs/       iocs.csv
    attack/     mapping.md, Navigator layer
    detections/ Sigma rules, converted searches, behavior ideas
    report/     the written report
  templates/
  tools/
```

`sh tools/newcase.sh` builds this tree for a new case.

## Network use

From the VM I only run `whois` and `dig` against public servers, plus one download of the OpenPhish community feed. I don't visit sample infrastructure from the VM. If I need a sandbox check, I do it from a different machine with a public sample, and I assume anyone can see the task.
