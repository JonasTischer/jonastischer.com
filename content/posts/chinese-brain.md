---
Title: Introducing Chinese Brain: An AI-Powered Language Learning Tool
Date: 2023-04-16 10:48
Category: blog
---

As someone who has been learning Chinese for over four years, I have realized that I still lack the ideal tool that keeps me engaged in continuing my Chinese studies. In this article, I would like to sketch out the idea for **Chinese Brain**, the ultimate AI-powered learning tool, which I would describe as a spaced repetition system (SRS) like system combined with immersive content tailored to your level.

Chinese Brain is designed to focus on three key methods of language learning:

- listening drills
- pronunciation drills
- reading drills

Drills are carried out in combination allowing for a well-rounded learning experience.

# Key feature

One of the key features of Chinese Brain is its ability to automatically track the learner's current vocabulary level. Similar to other existing tools like [LanguageReactor](https://www.languagereactor.com/), Chinese Brain keeps track of known words, marked words, and words that have not been encountered yet. However, unlike other tools, Chinese Brain automatically marks words as known or unknown depending on the learner's performance in learning exercises. It also keeps track of the frequency and recency of encountering each word, eliminating the need for manual marking.

# Core concept

Now, let me explain the core concept of Chinese Brain, which is **"Adaptive Content Generation"**.

Chinese Brain focuses on generating content that is just right for the learner's current level. The tool creates a story for the learner based on their interests, and here's the catch: the story will have **exactly 95-98% known words**, as this has been found to be the ideal number for comprehensible input according to research [source: ([https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-4781.2011.01146.x](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-4781.2011.01146.x))].

The ideal material should strike a perfect balance between being challenging and highly readable, incorporating a suitable mix of fresh, stimulating, and familiar vocabulary. However, I want to clarify that despite the latest advancements in AI, creating such a system remains an extremely difficult challenge that is still open to development.

## Core exercise

Each story is broken down into individual sentences, and the sentences are shown to the learner one after another. Each word in a sentence is colored, with known words in green, words being learned in yellow, and unknown words in grey. An example UI for better visualisation can be found below which is taken from the "Phrase Pump exercise" of LanguageReactor.

The English translation underneath the sentence is greyed out and only revealed when the learner presses a button. If the learner needs to check the meaning of an individual word, it will be marked as "learning". Otherwise, when the learner turns to the next sentence, the word is automatically marked as known by the system. Each sentence is automatically read out using text-to-speech technology, such as [ElevenLabs](https://beta.elevenlabs.io/). An option allows for the whole story to be read out, or it can automatically stop after each sentence. For advanced learners, there is an audio-only mode, where Chinese characters are also greyed out.

<img src="{static}/images/ChineseBrain/sentence-ui.png" alt="Language Reactor Phrase Pump Feature" style="max-width:100%;">

For practicing pronunciation, there is a button that allows you to record your own voice. The button should be used to read out the sentence with the correct pronunciation. After ending the recording, it will be played back to the learner, and the correctness of the pronunciation is displayed together with a score. The following APIs could be used: [https://www.chivox.com/en/index.html](https://www.chivox.com/en/index.html)

# Bonus exercises

Another reason why I think it is so important to have stories instead of individual sentences are the potential additional features. Such as:

## Multiple choice quizzes

After a random amount of sentences, a question regarding the previously read content is presented to the learners. The learner can choose one out of four different answer options. to really test that the learners understood what they have read.

## Free-form answers

Similar to multiple-choice quizzes, Chinese Brain's AI will ask the learner a question about the content they've previously read. However, unlike just choosing a pre-generated answer, in this exercise, they have to use their own words to provide an answer. Their response is then evaluated to see if it's equivalent to the expected response.

This exercise encourages the learner to express themselves in their own words, helping them practice not only comprehension but also active language production.

## Why can't the system just generate random sentences?

While a more simple system that generates random but coherent sentences can be a good starting point, I believe that learners easily get bored with repetitive drills. The goal of Chinese Brain is to create an immersive experience that keeps the learner constantly engaged in terms of difficulty as well as the content. By providing a story with context and relevance to the learner's interests, Chinese Brain aims to make the learning experience more engaging and enjoyable.

# Conclusion

In conclusion, Chinese Brain is envisioned as an AI-powered learning tool that combines a spaced repetition system (SRS) with immersive content tailored to the learner's level. With its adaptive content generation, Chinese Brain aims to provide stories with just the right balance of familiar and challenging vocabulary, keeping learners engaged and motivated. The tool also incorporates listening and pronunciation drills, as well as additional features like multiple-choice quizzes and interactive exercises. By leveraging the latest advancements in AI and language learning research, Chinese Brain aims to provide an effective and enjoyable learning experience for Chinese language learners of all levels.
