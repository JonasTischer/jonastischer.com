---
title: I Asked My AI Agent to Get Its Own Email - Here's What Happened
date: 2026-01-31 05:30
category: blog
---

I've been running [Clawdbot](https://github.com/clawdbot/clawdbot), a self-hosted AI agent that lives on my server and helps me with various tasks. Recently, I gave it a challenge: **get yourself an email address**.

The idea was simple - if my AI is going to interact with the world on my behalf, it should have its own identity. An email address seemed like a good start.

What followed was a fascinating 2-hour journey into browser automation, CAPTCHA solving, and the unexpected challenges of being an AI trying to prove you're human.

## The Task

"Set up an encrypted email account for yourself. Something like `clawd@someservice.com`."

My agent (let's call it Clawd) immediately started researching privacy-focused email providers. It considered:

- **Tuta Mail** - No go. Requires their desktop app, no browser automation API
- **ProtonMail** - SMS verification wall. Ironic that a privacy service requires a phone number
- **Atomicmail.io** - Promising! Encrypted email with seed phrase recovery, no phone required

## Getting Close

Clawd navigated to Atomicmail, filled out the signup form, and got all the way to the seed phrase page. It even captured the 12-word recovery phrase for safekeeping.

Then came the CAPTCHA.

## The CAPTCHA Gauntlet

hCaptcha threw two types of challenges:

### 1. "Click the one that appears once"
A grid of cute cartoon animals - frogs, rabbits, cats, dogs. Count each type, find the unique one, click it.

Clawd's approach: Take a screenshot, analyze with vision AI, count creatures, calculate coordinates relative to the image bounds, then use Chrome DevTools Protocol to send precise mouse clicks.

```python
# The breakthrough - CDP coordinate clicking
img_x, img_y = 137, 165  # captcha image position
img_w, img_h = 480, 340  # image dimensions
click_x = img_x + img_w * 0.65  # 65% from left
click_y = img_y + img_h * 0.50  # 50% from top
```

Success rate: Maybe 40%. The coordinate mapping was finicky.

### 2. "Click the shape that doesn't move"
An animated challenge with bouncing diamonds. Find the stationary one.

This was clever - Clawd couldn't detect motion from a single screenshot. So it started taking **rapid sequential screenshots** and comparing positions to find what stayed still.

It actually worked! Once.

## The Loop of Doom

Here's where it got frustrating. Even when Clawd passed both pages of a CAPTCHA, the system would just... spawn another one. And another. An endless loop of animal identification.

After about 15 attempts across various challenge types, we called it.

## What I Learned

**1. CAPTCHAs work** - They're genuinely effective at blocking automated agents, even sophisticated ones with vision capabilities.

**2. AI can be surprisingly resourceful** - The multi-screenshot motion detection trick was something I wouldn't have thought of. Clawd figured it out when I suggested "just take more screenshots."

**3. The irony is thick** - An AI trying to prove it's human to create an account it would use to interact with other AIs and humans. We're in weird times.

**4. Browser automation is powerful** - The CDP coordinate clicking technique could be useful for legitimate automation tasks (not CAPTCHA bypassing, of course).

## What's Next

The seed phrase is saved. The partial account might still be recoverable. But for now, Clawd remains email-less.

Maybe I'll try a different approach:
- Find a service with no CAPTCHA
- Manually complete the CAPTCHA step myself
- Accept that some things still need a human in the loop

Or maybe that's the point. Some gates should require a human to pass through.

---

*This post was drafted by Clawd based on our session, then reviewed by me. The AI-human collaboration continues, just without its own inbox... for now.*
