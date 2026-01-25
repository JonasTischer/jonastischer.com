Title: Setting Up My Personal AI Assistant with Clawdbot
Date: 2026-01-25 06:38
Category: blog

I've been fascinated by the idea of having a personal AI assistant that I can talk to anytime, anywhere — not just through a web interface, but through WhatsApp, voice messages, or any other channel I use daily. Today, I finally set it up, and I want to share my experience.

# Why Clawdbot?

There are many AI assistants out there, but most of them live behind a web UI or require you to open an app. What I wanted was something different: an AI that feels like a **real assistant** — one I can message on WhatsApp at 2am with a voice note, and it just... works.

[Clawdbot](https://github.com/clawdbot/clawdbot) is exactly that. It's a gateway that connects Claude (my AI of choice) to various messaging platforms. But more importantly, it gives the AI **agency** — it can read files, run commands, access my GitHub repos, create calendar events, and much more.

# The Setup Journey

Getting Clawdbot running on my VPS was surprisingly smooth, though I learned a few things along the way.

**The basics were easy**: SSH into the server, run `clawdbot doctor` to check the state, and start the gateway. Where it got interesting was making it accessible from anywhere while keeping it **secure**.

I didn't want to expose my AI assistant to the public internet with just a password. Instead, I used **Tailscale** to create a private network between my devices. The clever trick? I pointed my custom domain to the Tailscale IP instead of the public IP. This means only devices on my personal VPN can reach it — everyone else gets nothing.

For SSL, I used **Caddy** which handles Let's Encrypt certificates automatically. No more messing with certbot renewals or nginx configs. Just point and shoot.

# What Blew My Mind

Once everything was connected, I started testing features and honestly got a bit carried away.

**Voice messages just work.** I can send a WhatsApp voice note, and Clawdbot transcribes it using Groq's Whisper API (which is insanely fast — we're talking sub-second transcription). The AI then responds like it's a normal conversation.

**It can write to my blog.** I asked it to create a test post, and within seconds, it committed a new markdown file to my GitHub repo. This very post you're reading? Drafted entirely through a WhatsApp conversation.

**Linear integration.** I gave it my Linear API key, and now it can see my tasks, create issues, and help me stay organized. No more context-switching between apps.

# Lessons Learned

A few things I'd do differently or want to highlight:

1. **DNS propagation takes time** — I spent 20 minutes debugging SSL issues before realizing my DNS changes just hadn't propagated yet. Patience is a virtue.

2. **Tailscale for private access is genius** — Pointing your domain to a Tailscale IP instead of a public IP is such an elegant solution. You get custom domain + SSL + private access without complex authentication.

3. **Caddy simplifies everything** — If you're still manually managing SSL certificates, stop. Caddy handles it automatically.

4. **Persistent services matter** — Creating proper systemd units ensures everything survives reboots. I learned this the hard way after my gateway died and I didn't notice for hours.

# What's Next?

This is just the beginning. Here's what I'm planning to set up:

- **Password manager integration** — Let Clawdbot help me manage credentials securely
- **Security hardening** — Rate limiting, better logging, maybe some intrusion detection
- **Dedicated Gmail account** — Give my AI its own email address so it can send messages on my behalf
- **Burner credit card** — For when I want it to make purchases or sign up for services
- **Browser access** — Let it browse the web, fill forms, and interact with websites I use

The goal is to build something that feels less like a chatbot and more like a **digital extension of myself** — one that can handle the tedious stuff while I focus on what matters.

# Conclusion

Setting up Clawdbot took me about a day, but the result feels like a glimpse into the future of personal computing. Having an AI that's always available, understands context, and can actually *do things* in the real world changes how I think about productivity.

If you're technical enough to run a VPS and curious about AI assistants, I'd highly recommend giving it a try. The setup docs are solid, and the community on Discord is helpful.

Now if you'll excuse me, I need to go do some yoga. My AI has been reminding me for the past hour. 🧘

---

*This post was drafted collaboratively with Clawdbot via WhatsApp.*
