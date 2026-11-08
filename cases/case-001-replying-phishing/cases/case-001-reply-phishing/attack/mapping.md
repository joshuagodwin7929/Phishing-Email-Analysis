# ATT&CK Mapping (IDs verified on attack.mitre.org)

ATT&CK version: v20 (confirmed on attack.mitre.org Versions page)

| Tactic | Technique | Evidence | Confidence |
|---|---|---|---|
| Resource Development | T1583.001 Acquire Infrastructure: Domains | Three throwaway domains used; none registered today, creation dates unknown | Medium (inferred) |
| Resource Development | T1585.002 Establish Accounts: Email Accounts | Gmail address used as reply mailbox (Reply-To and both mailto buttons) | Medium (could be a compromised account) |
| Stealth | T1684.001 Social Engineering: Impersonation | "Microsoft account team" display name and fake sign-in alert | High |
| Reconnaissance | T1598 Phishing for Information | Buttons push the reader to email the attacker | Medium (assessed) |

## Observed but not mapped
- Hidden 1x1 tracking pixel
- Hidden filler text in a style block (filter evasion)

## Deliberately not mapped
- T1566.001 (no attachment)
- T1566.002 (no web link; only mailto buttons and an invisible image)
- T1204 (no user execution)
- T1056, T1539, T1111 (no fake login page or credential capture seen)

## Verification log (attack.mitre.org, v20 banner)
- T1585.002 Establish Accounts: Email Accounts, tactic Resource Development: confirmed
- T1684.001 Social Engineering: Impersonation, tactic Stealth: confirmed (T1656 was an outdated ID)
- T1598 Phishing for Information, tactic Reconnaissance: confirmed
- T1583.001 Acquire Infrastructure: Domains, tactic Resource Development: confirmed
- T1684.002 Social Engineering: Email Spoofing, tactic Stealth: reviewed, not mapped (see note below)

## Considered and not mapped
- T1684.002 Social Engineering: Email Spoofing (Stealth): the From address uses the attacker's own domain (access-accsecurity[.]com). No real Microsoft domain was forged and no legitimate-domain header manipulation was observed. Only the display name is fake, which T1684.001 covers.

## Note on T1583.001 confidence
Strongest for thebandalisty[.]com (it served the tracking pixel, so it was live). Weaker for access-accsecurity[.]com, which only appeared in the From header and did not need to be registered to send this email. Creation dates could not be verified because the domains are no longer registered.
