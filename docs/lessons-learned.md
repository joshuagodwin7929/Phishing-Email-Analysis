# What I got wrong on Case 001

I'm keeping this public. Most of analysis is catching your own mistakes, so here are mine, how I found them and what I do differently now.

## I opened the wrong email

I listed the subjects and senders of the first 40 samples and picked one by its subject line. The listing printed each file name before its own subject, so I paired my subject with the neighbouring file. When I dumped the headers, I got a Dutch dating-style spam message instead of the Microsoft alert.

I noticed because the subject in my header screenshot didn't match the one I'd picked. Now I re-read the subject and sender from the copied file before doing anything else. I parked the Dutch sample for a later case.

## A VM freeze emptied my evidence copy

The VM froze after a big package upgrade and I had to force it off. When it came back, my sample file was there but had zero bytes, and the hash file I'd written just before the freeze was gone.

The new hash was `e3b0c442...b855`, the well-known SHA256 of an empty file, and it no longer matched my old one. Now I hash every copy against its source, run `sync` after writing evidence, and keep the original in the public repo it came from so I can re-copy it. The incident is also in the report's limitations, because it touches the evidence chain.

## I assumed it was a credential-harvesting phish

I named the folder `case-001-credential-harvest` because "unusual sign-in activity" lures nearly always lead to a fake login page. My first link search found nothing, and instead of questioning my guess I decided the search was wrong.

What fixed it was gluing the whole message into one line and reading the text around the only domain I could find. It was a hidden 1x1 `<img>`, not a link. A second search for anchor tags showed that both buttons were `mailto:` links to a Gmail address. There was no login page at all.

Now I list every element that can carry a destination (anchor, image, form, mailto) before deciding what the lure does, and I name the case after what the evidence shows. I renamed the folder to `case-001-reply-phishing`.

## My first redirect plan was for the wrong thing

Since I thought the one URL was a tracking link, I planned to trace its redirect chain. It was a pixel, so there was nothing to trace. A missing redirect chain is a finding, and the report says why.

## I used an outdated ATT&CK technique

From memory I mapped the fake brand name to T1656 (Impersonation) under Defense Evasion. On the current site that technique had moved and the tactic had been split, so the right entry is T1684.001 under Stealth.

I caught it by opening each technique page on attack.mitre.org and comparing the title, ID and tactic with my table. Now I check every ID for the version I'm citing and keep a verification log in the mapping file. I also considered T1684.002 (Email Spoofing) and left it out, with the reason written down.

## Smaller slips

- I read a count badge in a sandbox tab as a number of matches. It changed when I changed the filter, so now I only quote what the rows show.
- My first header command leaked body text into the header file because the sample used Windows line endings. Adding `tr -d '\r'` fixed it, and I noticed because the file was far longer than a header should be.
- My first OpenPhish download was a 302 redirect page, not the feed. Searching a 7-line page and finding zero matches proved nothing. I re-ran it with `curl -L` and checked the line count before trusting the result.
- I first described the SPF result as proof the sender was unauthorised. "None" only means the domain publishes no policy, which is weaker than "fail", and the report says so.

## Screenshots

The screenshots for these slips are in [the case evidence folder](../cases/case-001-reply-phishing/evidence/README.md): the [wrong sample](../cases/case-001-reply-phishing/evidence/screenshots/04-mistake-wrong-sample-headers.png), the [empty-file hash](../cases/case-001-reply-phishing/evidence/screenshots/05-mistake-empty-file-hash.png), the [OpenPhish redirect page](../cases/case-001-reply-phishing/evidence/screenshots/19-openphish-302-redirect-page.png) and the [fixed download](../cases/case-001-reply-phishing/evidence/screenshots/20-openphish-300-line-feed.png), and the [ATT&CK checks](../cases/case-001-reply-phishing/evidence/screenshots/26-attack-t1684-002-considered.png).

## What I take from this

1. Check the thing you're about to analyse before you analyse it.
2. A negative result from a broken search tells you nothing.
3. A hash only fingerprints the file you hold, so compare it with the source after every copy.
4. Map what you can show, and write down what you looked at and rejected.
5. Put the limits in the report. I trust an analyst more when they say what they couldn't verify.
