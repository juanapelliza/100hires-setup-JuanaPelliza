# 100hires-setup-JuanaPelliza
## Tools Installed
- **Cursor IDE**: Main development environment.
- **Claude Code**: AI assistant extension.
- **Codex**: AI autocomplete extension.

## Steps Completed
1. Downloaded and installed the Cursor IDE.
2. Configured the required extensions (Claude Code and Codex).
3. Created a public GitHub repository.
4. Cloned the repository locally and documented the process in this README file.

## Issues and Solutions
- **Initial concern**: I was worried about the software being too heavy for my computer or hard to uninstall. 
- **Solution**: I researched the requirements and realized it's a lightweight environment based on VS Code, and uninstallation is straightforward, so I proceeded with the setup.
**Navigation Challenge**: When I first opened Cursor, the interface was "clean" (the Activity Bar was hidden), and I couldn't find where to search for extensions.
- **Solution**: I used AI assistance to identify the correct menu settings (`View > Appearance > Activity Bar`) and keyboard shortcuts (`Command + Shift + X`) to access the Extensions marketplace.


# B2B SaaS Research Project: LinkedIn Organic Content Strategy

## Project Overview
This repository contains a high-signal research project focused on **LinkedIn Organic Content Strategy for B2B SaaS**. The goal is to identify and deconstruct the methods used by top industry experts to drive awareness, trust, and revenue through organic social content.

## Chosen Topic
**LinkedIn Organic Content Strategy for B2B SaaS**
* **Why this topic?** In the current B2B landscape, "Dark Social" and organic presence are becoming more effective than traditional paid ads. Understanding how to build a personal brand that drives SaaS demos is a critical skill for 2026.

## Research Structure
The project is organized into three main areas:
- `/research/sources.md`: A curated list of 10 industry experts with annotations.
- `/research/youtube-transcripts/`: Deep dives into interviews and masterclasses using API-extracted transcripts.
- `/research/linkedin-posts/`: Real-world examples of high-performing posts organized by author.
- `/research/other/`: Technical proofs and additional materials.

## Featured Expert: Justin Welsh
The first phase of this research focuses on **Justin Welsh**, a pioneer in "Content Operating Systems."
- **Selection Criteria:** Former VP of Sales at PatientPop (SaaS). His strategies aren't just for "influencers"; they are rooted in B2B sales cycles and scalable systems.
- **Key Contribution:** The "Creator Funnel" (Awareness > Trust > Relationship > Monetization).

## Technical Implementation
To ensure high-quality data collection, I utilized:
- **YouTube API tools:** Extracted full transcripts from long-form interviews to identify strategic pillars.
- **AI-Assisted Curation (Claude 3.5):** Used to summarize key insights, categorize content with tags, and ensure the information is "scannable" for stakeholders.
- **Manual Scraping:** Collected specific LinkedIn posts to analyze formatting and hooks.

## Featured Expert: Sam Dunning


- **Technical Issue**: Initial API call failed due to specific video restrictions (`VideoUnavailable`).
- **Solution**: I collaborated with Claude to refactor the Python script, adding a "fallback mode" that allows custom URLs.
- **Result**: Successfully extracted the transcript for Sam Dunning's video using the new script, fulfilling the API-usage requirement.
---
*This project is part of the 100hires technical assessment.*