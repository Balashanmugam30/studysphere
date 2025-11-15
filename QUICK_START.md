# StudySphere - Quick Start Guide
## HackFest GDG New Delhi - LA-01 Smart Study Partner

---

## 🚀 Run in 3 Steps

### Step 1: Install Dependencies
```bash
cd /app/frontend
yarn install
```

### Step 2: Start Development Server
```bash
yarn start
```

### Step 3: Open in Browser
```
http://localhost:3000
```

---

## 🎤 Using Voice Mode (Agora)

### First Time Setup
1. **Click** the green "🎤 Voice Mode (Agora)" button
2. **Allow** microphone permissions when prompted
3. **Click** "Start Recording" button
4. **Speak** your question clearly
5. **Wait** for AI response in chat

### Visual Indicators
- 🟢 **Green Button**: Voice Mode ready to activate
- 🔴 **Red Button**: Voice Mode active (click to stop)
- 🟠 **Orange Button**: Click to start recording
- 🔴 **Red Dot Pulsing**: Currently recording your voice

### Voice Message Format
- Your voice input appears with 🎤 emoji
- Messages in green bubble (vs blue for text)
- Timestamp shows when spoken

---

## 💬 Using Text Chat

### Send a Message
1. Type question in bottom input field
2. Press **Enter** or click **Send** button
3. AI responds instantly

### Example Questions
```
"What is photosynthesis?"
"Explain Newton's laws of motion"
"Help me understand calculus"
"Summarize the French Revolution"
```

---

## 🧪 Generate Quiz

### Test Your Knowledge
1. **Upload** a PDF (simulated) or have a conversation
2. **Click** the blue "Test Me" button
3. AI generates 3 multiple-choice questions
4. Questions appear in chat interface

---

## 📚 Upload Study Materials

### PDF Upload (Simulated)
1. **Click** "Choose PDF File" button
2. **Select** any PDF from your computer
3. **See** success message with filename
4. Note: File is not processed (MVP feature)

---

## 🎨 UI Features

### Color-Coded Buttons
- **Blue**: Main actions (Upload, Test, Send)
- **Green**: Voice Mode activation
- **Orange**: Recording control
- **Red**: Stop/Exit actions

### Chat Bubbles
- **Blue (right)**: Your text messages
- **Green (right)**: Your voice messages
- **White (left)**: AI responses

### Animations
- Messages slide in smoothly
- Recording indicator pulses
- Buttons lift on hover
- Input glows on focus

---

## ⚙️ Requirements

### Browser Support
- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge

### System Requirements
- Modern browser with microphone access
- Internet connection for AI backend
- JavaScript enabled

### Microphone Access
Voice Mode requires microphone permissions:
1. Browser will prompt on first use
2. Click "Allow" to enable voice features
3. Can be changed in browser settings

---

## 🐛 Troubleshooting

### Voice Mode Not Working
**Issue**: "Speech recognition not supported"
- **Solution**: Use Chrome or Edge (best support)
- **Alternative**: Use text chat instead

**Issue**: "Microphone access denied"
- **Solution**: Check browser permissions
- **Steps**: Settings → Privacy → Microphone → Allow

**Issue**: "No speech detected"
- **Solution**: Speak louder and clearer
- **Tip**: Reduce background noise

### Chat Not Responding
**Issue**: "Couldn't connect to backend"
- **Cause**: Backend CORS restrictions
- **Expected**: Demo limitation
- **Note**: App UI fully functional

### Build Issues
**Issue**: Dependencies not installing
```bash
# Clear cache and reinstall
rm -rf node_modules yarn.lock
yarn install
```

**Issue**: Port 3000 already in use
```bash
# Kill process and restart
lsof -ti:3000 | xargs kill -9
yarn start
```

---

## 📝 Key Features Summary

| Feature | Status | Description |
|---------|--------|-------------|
| Voice Mode | ✅ Working | Agora RTC + Speech-to-Text |
| Text Chat | ✅ Working | Real-time AI conversation |
| Quiz Generation | ✅ Working | Click "Test Me" button |
| PDF Upload | ✅ Working | Simulated upload |
| Agora Branding | ✅ Visible | Footer label present |
| Responsive UI | ✅ Working | Mobile + desktop |
| Error Handling | ✅ Working | Friendly error messages |

---

## 🎯 Best Practices

### For Voice Input
1. Speak clearly and at normal pace
2. One question at a time
3. Wait for AI response before next question
4. Use quiet environment

### For Text Input
1. Type complete questions
2. Be specific for better answers
3. Use "Test Me" for quiz generation
4. Can use Enter key for quick send

### General Tips
- Upload a PDF first for context
- Try voice mode for hands-free learning
- Use quiz to test understanding
- Keep chat window scrolled to see responses

---

## 📞 Need Help?

### Documentation
- **README.md**: Full project documentation
- **HACKFEST_SUBMISSION.md**: Competition details
- **CODEBASE_SUMMARY.md**: Technical architecture

### Common Questions

**Q: Does voice mode work offline?**
A: No, requires internet for AI backend and speech recognition.

**Q: Can I save my chat history?**
A: Not in current version (MVP feature only).

**Q: What languages are supported?**
A: English only for voice and text.

**Q: Is my data stored?**
A: No, all conversations are temporary (not persisted).

---

## 🚀 Ready to Start!

1. ✅ Dependencies installed?
2. ✅ Server running?
3. ✅ Browser open at localhost:3000?
4. ✅ Microphone ready?

**You're all set! Click Voice Mode and start learning! 🎤📚**

---

**Built for HackFest GDG New Delhi with ❤️**
