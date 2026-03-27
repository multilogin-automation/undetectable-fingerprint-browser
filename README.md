# <!-- Maintainer: @multilogin-automation - Modernized Fork -->

# 🕵️‍♂️ Undetectable Fingerprint Browser  

[中文介绍](https://github.com/itbrowser-net/undetectable-fingerprint-browser/blob/main/README_zh.md)

**Open Source · Modular · Programmable Anti-Detection Browser**

**Undetectable Fingerprint Browser** is a **highly customizable, realistically emulated, automation-friendly** anti-detection browser, specifically designed to counter modern websites' advanced fingerprinting and detection systems.

Whether you're engaged in **anti-anti-scraping research, marketing analytics, multi-account management**, or need to build a **fully controllable browser automation environment**, this project is your ultimate choice.

![fingerprints](usage/fingerprints_en.png)



### download [prebuild release browser](https://github.com/itbrowser-net/undetectable-fingerprint-browser/releases/download/v1.0.0/fingerprint_browser_v1.0.7z) 



---

## 🚀 Key Highlights

### 🧠 1. Comprehensive Fingerprint Spoofing

> Not just spoofing more — but spoofing better and more realistically, with global consistency.

| Fingerprint Type         | Feature Description |
|--------------------------|---------------------|
| **Canvas Fingerprint**   | Precision spoofing, random noise, custom rendering results |
| **WebGL & WebGL2**       | Fake GPU models, render returns, renderer strings, antialias settings |
| **AudioContext Fingerprint** | Alters audio behavior to return stable spoofed results |
| **ClientRects / DOMRect** | Emulates browser-specific rendering differences |
| **Font Fingerprint**     | Controls font detection responses to block OS font probing |
| **Timezone / Language**  | Global override of `navigator`, `Intl API`, `Date` outputs |
| **Hardware Concurrency** | Custom CPU core count |
| **Device Memory**        | Spoof `navigator.deviceMemory` values |
| **Screen Resolution & Color Depth** | Simulates different screen sizes and color depths |
| **Touch / Mobile Indicators** | Emulates mobile device indicators: touch events, UA, media queries |

👉 **Exclusive Feature: Consistency Analysis Engine** ensures all spoofing fields align logically and do not conflict, eliminating detection signals at the root.

---

### 🧩 2. Fully Supported & Built-in Modules

We’ve integrated a complete anti-leak system — no extra installation required for:

- ✅ WebRTC leak prevention  
- ✅ Auto-adaptive Canvas/WebGL spoofing  
- ✅ Automation module (Puppeteer / Playwright compatible)  
- ✅ Built-in proxy injection (SOCKS5, HTTP, TLS proxy)  
- ✅ GPS & sensor data emulation  
- ✅ Local JS injection with CSP bypass support  

---

### 🤖 3. Automation-Ready

Seamlessly integrate this browser into any automation pipeline, or fully control it programmatically.

#### 🤝 Full Framework Compatibility:

- Just add a startup parameter — no need to modify code.
- Puppeteer: Works by pointing to custom Chromium binary  
- Playwright: Fully compatible with Chromium engine  
- DevTools Protocol and WebSocket control support  
- JavaScript API and CLI tools for advanced tuning and scripting



---

## 🌍 Real-World Use Cases

| Use Case               | Description |
|------------------------|-------------|
| ✅ Anti-bot Environment | Bypass bot detection, captchas and verification scripts |
| ✅ SEO & Ad Verification | Simulate access from various device and geo profiles |
| ✅ Multi-account Login | Avoid being linked by fingerprint, storage, or cookies |
| ✅ Data Extraction Research | Test and defeat site-level fingerprint traps |
| ✅ Security Research | Validate fingerprint-based defenses and study tracking vectors |

---

## 📊 Comparison with Mainstream Solutions

| Feature / Solution        | Puppeteer Stealth | Playwright Stealth | Undetectable-Fingerprint-Browser |
|--------------------------|-------------------|--------------------|----------------------------------|
| Multi-dimensional spoofing | Partial support   | Partial support    | ✅ Full fingerprint coverage      |
| Plugin system             | ❌ None           | ❌ None             | ✅ Complete plugin architecture   |
| Behavioral consistency    | ❌ May conflict    | ❌ May conflict     | ✅ Adaptive consistency management |
| Customizability           | Medium            | Medium             | ✅ Highly configurable             |
| Isolation & sandboxing    | Medium            | Medium             | ✅ Deep sandbox support            |
| Automation integration    | ✅ Supported       | ✅ Supported        | ✅ Fully supported                 |

---

## 🔧 Quick Start  
# Install Pre-Compiled Version  
Download and extract the pre-built package: [Compiled Binary Release](https://github.com/itbrowser-net/undetectable-fingerprint-browser/releases/download/v1.0.0/fingerprint_browser_v1.0.7z).  

**Generate a Fingerprint via Command Line**  
```bash  
./itbrowser_fingerprint.exe  
```

**Launch the Browser with a Specified Fingerprint**  
```bash  
chrome --itbrowser=myfingerprint.json  
```

**For Automation Use:**  
```bash  
chrome.exe --user-data-dir=data1 --itbrowser="D:\Program Files\chrome\1.json" --proxy-server="socks5://someuser:password@host:port" --remote-debugging-port=9222  
```


# build the project from source
git clone https://github.com/itbrowser-net/undetectable-fingerprint-browser.git
merge the code with chromium source code.

---

## ⚠️ Legal Disclaimer

This project is intended for **legal and ethical use only**, such as for security research, automation testing, or development environment simulation.

**Any use of this tool for illegal scraping, ad fraud, account hijacking, or malicious activity is strictly prohibited.**  
The authors are not liable for any misuse of this software.

---

## 📫 Contact Us

- Feel free to open an issue on GitHub for questions or feature requests.  
- For enterprise-level support or custom development, contact us via email:  
  **`javaflashproject@gmail.com`**
- [https://discord.gg/AhW2RaHCs6](https://discord.gg/AhW2RaHCs6)
---

> ⭐ If you find this project useful, please give us a star on GitHub! If you think it's worth starting, please star it to avoid forgetting. I will gradually upload the project source code.

---
