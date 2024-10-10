---
created: 2024-10-10T10:31:15 (UTC +01:00)
tags: []
source: https://console.groq.com/docs/rate-limits
author: 
---

# GroqCloud

> ## Excerpt
> Experience the fastest inference in the world

---
Rate limits act as control measures to regulate how frequently a user or application can make requests within a given timeframe.

You can view the current rate limits for chat completions in your organization [settings](https://console.groq.com/settings/limits)

The team is working on introducing paid tiers with stable and increased rate limits in the near future.

We set the following `x-ratelimit` headers to inform you on current rate limits applicable to the API key and associated organization.

HeaderValueNotes`retry-after``2`In seconds`x-ratelimit-limit-requests``14400`Always refers to Requests Per Day (RPD)`x-ratelimit-limit-tokens``18000`Always refers to Tokens Per Minute (TPM)`x-ratelimit-remaining-requests``14370`Always refers to Requests Per Day (RPD)`x-ratelimit-remaining-tokens``17997`Always refers to Tokens Per Minute (TPM)`x-ratelimit-reset-requests``2m59.56s`Always refers to Requests Per Day (RPD)`x-ratelimit-reset-tokens``7.66s`Always refers to Tokens Per Minute (TPM)

When the rate limit is reached we return a `429` Too Many Requests HTTP status code.

Note, `retry-after` is only set if you hit the rate limit and status code 429 is returned. The other headers are always included.
