# Case 001: reply-phishing

The email claims to be a Microsoft alert about unusual sign-in activity. There is no fake login page. Two buttons open a reply to a Gmail address, so the victim has to write to the attacker first.

| Item | Value |
|---|---|
| Source | Public phishing corpus (phishing_pot), sample-1001.eml |
| SHA256 of the original | `a28a794537f537758b69ba34835090f5ee0e76380bff07101811ab85a3fd84cf` |
| Verdict | Phishing, reply-based, low effort |
| ATT&CK (v20) | T1583.001, T1585.002, T1684.001, T1598 |
| Web link to trace | None. One hidden 1x1 pixel and two `mailto:` buttons |

## Files

- [report/case-001-report.md](report/case-001-report.md) is the full write-up.
- [iocs/iocs.csv](iocs/iocs.csv) has 10 defanged indicators.
- [attack/mapping.md](attack/mapping.md) has the ATT&CK table and my verification notes.
- [detections/](detections) has two Sigma rules, an ECS pipeline, the converted Lucene searches and some untested behavior ideas.

I haven't published the raw sample, the raw WHOIS output or the header dump. The sample is public in its source corpus, so you can compare your own copy against the hash above.
