# Evidence for Case 001

These are screenshots from my lab while I worked the case, in the order I did the work. I left the raw sample, raw header dump and raw WHOIS output out of the repo. The screenshots are the proof of what I saw.

Two things to know when you look at them:
- The early screenshots show a folder called `case-001-credential-harvest`. That was my first guess at the case, and I renamed it to `case-001-reply-phishing` once the evidence showed there was no login page.
- Screenshots 04 and 05 show the wrong sample (`sample-10020.eml`, the Dutch spam message). That mistake is written up in [docs/lessons-learned.md](../../../docs/lessons-learned.md). The real sample is `sample-1001.eml`.

## Lab

| File | What it shows |
|---|---|
| [01-lab-pep668-pip-blocked](screenshots/01-lab-pep668-pip-blocked.png) | Kali refusing a system-wide `pip install` (PEP 668), which is why I use a venv |
| [02-lab-tools-check](screenshots/02-lab-tools-check.png) | The tools and Python packages installed in the venv |
| [03-lab-snapshot-manager](screenshots/03-lab-snapshot-manager.png) | VMware snapshots and the revert prompt |

## Mistakes

| File | What it shows |
|---|---|
| [04-mistake-wrong-sample-headers](screenshots/04-mistake-wrong-sample-headers.png) | Headers of the wrong sample, a Dutch spam message instead of the Microsoft alert |
| [05-mistake-empty-file-hash](screenshots/05-mistake-empty-file-hash.png) | The hash `e3b0c442...b855` of an empty file, after the VM froze |

## Email and headers

| File | What it shows |
|---|---|
| [06-sample-subject-sender-confirmed](screenshots/06-sample-subject-sender-confirmed.png) | Subject and From of `sample-1001.eml`, read again from the copy |
| [07-headers-key-fields](screenshots/07-headers-key-fields.png) | From, Return-Path, Reply-To, Message-ID, and `spf=none` for `nonkfrgr.co.uk` |
| [08-headers-received-chain](screenshots/08-headers-received-chain.png) | The Received chain and Authentication-Results |

## Body

| File | What it shows |
|---|---|
| [09-body-anchor-and-pixel-search](screenshots/09-body-anchor-and-pixel-search.png) | The hidden 1x1 image from `thebandalisty[.]com` found with the message glued into one line |
| [10-body-mailto-anchors-and-dig](screenshots/10-body-mailto-anchors-and-dig.png) | Both buttons are `mailto:` links to the Gmail address, and `dig` returns NXDOMAIN for the pixel domain |
| [11-body-readable-message](screenshots/11-body-readable-message.png) | The message as a person would read it |

## Infrastructure and reputation

| File | What it shows |
|---|---|
| [12-whois-access-accsecurity](screenshots/12-whois-access-accsecurity.png) | WHOIS: no match for the From domain |
| [13-whois-ip-block](screenshots/13-whois-ip-block.png) | WHOIS for the first-hop IP, with a block record created in 2025 |
| [14-whois-dig-thebandalisty](screenshots/14-whois-dig-thebandalisty.png) | WHOIS and DNS for the pixel domain |
| [15-virustotal-summary](screenshots/15-virustotal-summary.png) | VirusTotal: 10 of 91 vendors flag `http://thebandalisty.com/` |
| [16-virustotal-detection](screenshots/16-virustotal-detection.png) | Which vendors flagged it |
| [17-sandbox-browser-unreachable](screenshots/17-sandbox-browser-unreachable.png) | A public sandbox could not reach the domain |
| [18-sandbox-dns-requests](screenshots/18-sandbox-dns-requests.png) | The sandbox DNS requests for the domain, with no IP address found |
| [19-openphish-302-redirect-page](screenshots/19-openphish-302-redirect-page.png) | My first OpenPhish download: an HTTP 302 and a 7-line page, so the "0 matches" meant nothing |
| [20-openphish-300-line-feed](screenshots/20-openphish-300-line-feed.png) | After following the redirect: HTTP 200 and 300 lines |

## Indicators

| File | What it shows |
|---|---|
| [21-hash-match-and-iocs](screenshots/21-hash-match-and-iocs.png) | My copy's SHA256 matches the source, and the IOC table |

## ATT&CK checks on attack.mitre.org

| File | What it shows |
|---|---|
| [22-attack-t1583-001](screenshots/22-attack-t1583-001.png) | T1583.001 Acquire Infrastructure: Domains |
| [23-attack-t1585-002](screenshots/23-attack-t1585-002.png) | T1585.002 Establish Accounts: Email Accounts |
| [24-attack-t1598](screenshots/24-attack-t1598.png) | T1598 Phishing for Information |
| [25-attack-t1684-001](screenshots/25-attack-t1684-001.png) | T1684.001 Social Engineering: Impersonation (Stealth) |
| [26-attack-t1684-002-considered](screenshots/26-attack-t1684-002-considered.png) | T1684.002 Email Spoofing, which I considered and left out |

## Detections

| File | What it shows |
|---|---|
| [27-sigma-check-pass](screenshots/27-sigma-check-pass.png) | `sigma check` passes on both rules |
| [28-sigma-convert-needs-pipeline](screenshots/28-sigma-convert-needs-pipeline.png) | `sigma convert` refusing to run without a processing pipeline |
| [29-sigma-ecs-pipeline-and-convert](screenshots/29-sigma-ecs-pipeline-and-convert.png) | The ECS pipeline and the converted Lucene searches |
| [30-sigma-check-and-convert](screenshots/30-sigma-check-and-convert.png) | The check and both conversions run together |

The ATT&CK Navigator layer is in [../attack/](../attack).
