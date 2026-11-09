# How I analyse a phishing email

This is the order I follow on every case, and it matches the sections of my reports. Replace `sample.eml` with your file name.

PhishTank and OpenPhish list URLs, not emails, so they can't give you headers. I pair an email corpus for headers and body with the feeds for verification and enrichment.

## 0. Safety

- I work in an isolated VM with snapshots, NAT or host-only networking and no shared folders.
- I read the sample as text. I don't double-click an `.eml` or paste its links into a browser.
- I defang every indicator in notes and reports, like `hxxps://bad[.]example` and `user[@]bad[.]example`.
- I only use public samples or my own mail. A public sandbox is only for public samples, because free tasks are visible to everyone.
- I run `sync` after writing evidence files. A frozen VM can lose data that was still in memory.

## 1. Intake and integrity

```bash
sha256sum sample.eml | tee evidence/sample.sha256
sync
chmod a-w raw/sample.eml
```

I record the case ID, source, date, hash and a first verdict. After copying a sample into the case folder, I hash the copy and compare it with the source. A hash of `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` means the file is empty.

I also re-read the subject and sender of the copy, to be sure it's the email I meant to pick.

## 2. Headers

```bash
tr -d '\r' < raw/sample.eml | sed -n '1,/^$/p' > evidence/headers.txt
rg -i '^(From|To|Subject|Date|Reply-To|Return-Path|Message-ID|Received|Authentication-Results|Received-SPF|DKIM-Signature|X-Originating-IP|X-Mailer)' evidence/headers.txt
```

The `tr -d '\r'` matters. Some samples use Windows line endings, and without it the `sed` range doesn't stop at the first blank line, so body text leaks into the header file.

I check these in order:

1. The Received chain, read bottom to top. The lowest hop is closest to the origin.
2. From, Return-Path and Reply-To. A mismatch means spoofing or reply hijacking.
3. SPF, DKIM and DMARC in `Authentication-Results`, and whether they align with the visible From domain.
4. The Message-ID, whose domain can show the real sending platform.
5. Dates: the send time against the first hop, and the gaps between hops.
6. The display name against the real address.

## 3. Body and attachments

I read the HTML as text and list every element that can carry a destination: anchor tags, `mailto:` links, images and forms.

```bash
tr -d '\r\n' < raw/sample.eml | grep -oiE '<a [^>]{0,300}>' | head -20
tr -d '\r\n' < raw/sample.eml | grep -oiE '<img [^>]{0,300}>' | head -20
```

"Are there any http links?" is the wrong question. A pixel is an `<img>`, not an `<a>`, and a `mailto:` is a link that opens no website. To read only what a person would see, I strip style and script blocks and tags with a short Python script.

## 4. URLs and redirects

If the message has real web links, I trace them from headers only and use a sandbox for anything beyond that. If it has none, I say so and explain why. "No redirect chain" is still a finding.

## 5. Infrastructure

```bash
whois example.com
dig example.com @1.1.1.1 | grep -E 'status|ANSWER SECTION'
whois 203.0.113.7
```

For domains I record the registrar and creation date, and for IPs the network name, owner and ASN. I check dates before drawing conclusions. If a registry record was created after the email was sent, it shows who holds the address now, not who held it then. For dead domains, a WHOIS `No match` and a DNS `NXDOMAIN` are results worth reporting, along with the fact that the creation dates are unknown.

Reputation checks (VirusTotal, OpenPhish, PhishTank) tell me about the domain today. They don't record what it served on the day of the email.

## 6. IOCs

I keep one table with type, defanged value, context, confidence, first seen and source, in both CSV and JSON. I state what each confidence level means.

## 7. MITRE ATT&CK

I map only what I observed and cite the evidence for each technique. I check every ID and tactic name on attack.mitre.org for the version I'm using, because they change between versions. I also list the techniques I considered and rejected, with the reason.

## 8. Detections

- Sigma rules for the sender, reply mailbox and domains.
- Behavior ideas that survive a change of domain or mailbox, clearly marked as untested.
- I run `sigma check` on every rule, then convert it. Some backends need a processing pipeline that maps generic field names (for example `query`) to the SIEM's names (for example `dns.question.name`).
- A passing check means the rule is well formed. It doesn't mean your logs contain those fields.

## 9. Report

The report has eleven sections: executive summary, scope and method, email overview, technical findings, infrastructure, IOC appendix, ATT&CK mapping, detection and response, confidence and limitations, timeline and evidence index. I lead with the conclusion and put the evidence behind it, and I keep observed, concluded and assumed apart. The skeleton is in [templates/report-template.md](../templates/report-template.md).

## 10. Before I publish

- Every indicator is defanged, except in rule files where a defanged value would never match.
- Every ATT&CK technique has evidence and a verified ID.
- The numbers in the report match the evidence files, and the hash list is current.
- No local paths, usernames, hostnames, personal names or sandbox links remain.
- The limitations section says specific things.
