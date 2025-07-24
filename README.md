# SceneScribe

*AI-Powered Interactive System for Descriptive Audio Narration of Visual Content for the Visually Impaired*

---

## Overview

**SceneScribe** is an interactive assistive technology platform that leverages advanced deep learning to provide real-time, context-aware audio descriptions of images and videos for visually impaired users. It features multimodal input processing, robust natural language support, and a fully audio-based command-line interface.

---

## Key Features

- **Multi-Modal Media Support:** Analyze static images (JPEG, PNG) and videos (MP4) with specialized deep learning models.
- **Descriptive Audio Narration:** Generate semantically rich and contextually precise audio descriptions.
- **Voice Interaction:** Navigate and interact using a multilingual speech interface (supports 9 languages and local dialects).
- **Real-Time Processing:** Latency <2.5secs for 90% of queries.
- **Robust Error Handling:** Automated retries, fallback strategies, persistent session state, and operational continuity under network disruptions.
- **Privacy-First:** Local, on-device audio processing safeguards user data privacy.

---

**Main Pipeline Stages:**

1. **Media Acquisition & Validation**
   - Console interface for choosing images/videos
   - File format checking, extension whitelisting, and path normalization
2. **Content Analysis & Captioning**
   - Images: Vision-language transformer model (BLIP2) generates captions
   - Videos: Temporal-aware model (VideoLLaMA2) analyzes keyframes and fuses visual/audio features
3. **Language Configuration**
   - Voice-guided multilingual selection using text-to-speech and speech-to-text
4. **Interactive Dialogue**
   - Context-managed Q&A with realtime audio capture, intent extraction, and context fusion
5. **Response Generation**
   - Locale-specific formatting; speech synthesis with dynamic leveling and sample rate control
6. **Error Recovery**
   - Real-time monitoring, failovers, session state carry-over, feedback mechanisms

---

## Methodology in Brief

- **Multi-Modal Input Processing:** Custom deep learning for image and video, using attention and temporal-awareness.
- **Speech & Language Interface:** Acoustic and cloud speech recognition, noise suppression, and full multi-language adaptability.
- **Context Management:** Pipeline design with session-based prompt engineering, context carry-over, and consistent language generation.
- **System Integration:** Hardware abstraction for audio playback, strict file operations, and session-based output management.
- **Fault Tolerance:** Immediate retries, smart fallbacks, session recovery, and proactive feedback.

---

## Technical Stack
  
| Component        | Technology                           |
|------------------|----------------------------------------|
| **Vision Transformer Models**         | **BLIP2** (Images), **VideoLLaMA2** (Videos) |
| **Speech Recognition** | On-device & Cloud APIs |
| **Audio Synthesis** | ext-to-speech engine with noise cancellation & sample rate control |
| **Languages Supported**       | 9+ (extensible to local dialects)  |
| **Platforms**     | Cross-platform (console-based interface)   |


---

## Results and Validation

- **Operational Efficiency:** Handles heterogeneous media with adaptive, hybrid processing (cloud + local).
- **Robustness:** Three-level error tolerance—automatic API retries, intelligent failure detection, and dynamic processing fallbacks.
- **Accessibility Testing:** Successfully validated with visually impaired participants for audio-only navigation and feedback.
- **Privacy:** On-device processing ensures personal audio data is not stored or sent to the cloud.
- **Use Cases:** Proven in educational and multilingual communication settings; scalable and adaptable.

---

## Getting Started

### Prerequisites

- Python 3.8+
- PyTorch (for DL models)
- Compatible device with microphone & speaker
- [Optional] Cloud API keys for BLIP2, VideoLLaMA2

### Installation

git clone https://github.com/your-org/SceneScribe.git

cd SceneScribe

pip install -r requirements.txt

--- 

*Designed to make rich media accessible—empowering visually impaired users everywhere.*
