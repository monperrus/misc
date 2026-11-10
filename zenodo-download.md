# Downloading data from Zenodo (with coding agents)

## The agentic use case

In research, we routinely ask a coding agent (Claude Code, Codex, ...) to fetch a reproduction package from Zenodo and analyze it, e.g.

> download the data at https://zenodo.org/records/23414101 and report

When such a download fails with HTTP 403, agents tend to escalate to browser impersonation
(`curl_cffi`, Playwright, ...). This is unnecessary: Zenodo's block is a **User-Agent blocklist**,
not TLS fingerprinting. `curl_cffi` with `impersonate="chrome"` only works because it sends an allowed User-Agent.
Plain `curl` with a descriptive User-Agent is enough.

## The 403 and its causes

The 403 page says *"Access to this resource has been restricted due to unusual traffic from your network."*
Measured on 2026-11-10 (the list is opaque and may change):

* blocked: no User-Agent, empty User-Agent, bare `Mozilla/5.0`, some browser strings popular with scrapers (e.g. Chrome 80–95, 115, 120; Firefox 60);
* allowed: `curl/x`, `python-requests/x`, `Wget/x`, recent browser strings, and descriptive strings like `mytool/1.0 (+mailto:me@example.org)`;
* the TLS fingerprint does not matter: plain `curl` with an allowed User-Agent gets the same answer as `curl_cffi` impersonating Chrome.

Other causes of 403 and failures:

* `/api/records/<id>/files/<key>/container` is 403 for `.zip` files; use `/files/<key>/content` instead.
* restricted records are 403 without an access token.
* rate limit: 133 requests/minute (see the `x-ratelimit-*` response headers).
* on hosts with broken IPv6, Python `requests` stalls ~30 s per address before falling back to IPv4, which looks like a Zenodo problem but isn't (`curl` falls back instantly; or use `curl -4`).

## Recipe

Download all files of a record and verify their checksums (needs `curl` and `jq`):

```bash
UA="zenodo-download/1.0 (+mailto:you@example.org)"
REC=23414101
curl -sf -A "$UA" https://zenodo.org/api/records/$REC \
  | jq -r '.files[] | "\(.links.self) \(.key) \(.checksum|ltrimstr("md5:"))"' \
  | while read url key md5; do
      curl -sfL -A "$UA" --retry 5 -o "$key" "$url"
      echo "$md5  $key" | md5sum -c
    done
```

Split archives (`data.tar.gz.part_aa`, `..._ab`, ...): `cat data.tar.gz.part_* | tar -xz`.

## Prompt snippet for agents

Add this to the task prompt or to your `CLAUDE.md` / `AGENTS.md`:

```
To download from Zenodo, use plain curl with a descriptive User-Agent
(curl -A "zenodo-download/1.0 (+mailto:you@example.org)"), list files via
https://zenodo.org/api/records/<id>, fetch each files[].links.self, and verify
files[].checksum (md5). A 403 "unusual traffic" means a blocked User-Agent:
fix the User-Agent, do not reach for browser impersonation (curl_cffi, Playwright).
Do not use the /container endpoint. Stay under 133 requests/minute.
```
