# Behavior-based detection ideas (case-001)

These are ideas only. I haven't tested any of them against real mail logs.

The IOC rules only catch this exact campaign. These look at how the email behaves, so they should still work after the attacker changes domain or mailbox.

## 1. Brand in the display name, sender domain doesn't match

Display name contains "Microsoft" and the From domain isn't one Microsoft owns (the list needs maintaining). ATT&CK: T1684.001. Partner tools that send notices on Microsoft's behalf will trigger it, so I'd allowlist known partner senders.

## 2. Reply-To on a free mail provider, failing authentication

Reply-To is on a free provider, differs from the From domain, and neither SPF nor DKIM passes. ATT&CK: T1598, T1585.002. Small businesses and mailing lists that use personal addresses will trigger it, so I'd limit it to external senders with a security-themed subject.

## 3. Security alert that only has mailto links

Subject matches unusual or suspicious sign-in wording, the body has `mailto:` links and no https link to the claimed brand. ATT&CK: T1598. Real security alerts link to https pages, so false positives should be rare. It needs body inspection, so check that your mail gateway can do that.

## 4. Hidden tracking pixel from a domain nobody has seen

The HTML body has a 1x1 or hidden image pointing at a new domain. No ATT&CK technique, since I only observed it. Marketing mail uses tracking pixels constantly, so I'd combine this with failed SPF and DKIM.

## Limits

The free-provider list and the brand list need regular upkeep. I don't know the false-positive rates until I run these on real mail.
