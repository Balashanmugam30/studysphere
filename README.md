# StudySphere - Your Conversational AI Study Partner

**HackFest GDG New Delhi - LA-01 Smart Study Partner Track**

A modern, intelligent web application built with React that helps students interact with an AI study assistant using voice and text. Features Agora Conversational AI integration for real-time voice interactions.

## Features

- 🎤 **Agora Voice Mode**: Real-time voice conversations with AI using Agora RTC SDK
- 🗣️ **Speech-to-Text**: Web Speech API integration for accurate voice recognition
- 📚 **PDF Upload**: Simulated PDF upload with file name display
- 💬 **AI Chat Interface**: Full conversational chat with AI assistant
- 🧪 **Test Me**: Generate 3 multiple-choice quiz questions from your notes
- 🎨 **Modern UI**: Clean blue and white academic design with Poppins font
- ⚡ **Real-time Responses**: Instant backend communication with error handling
- 📱 **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

- **Frontend**: React + Create React App
- **Voice Integration**: Agora RTC SDK (Web)
- **Speech Recognition**: Web Speech API (browser-native)
- **Styling**: CSS with custom design system
- **UI Components**: Shadcn/UI components
- **HTTP Client**: Axios
- **Notifications**: Sonner toast notifications
- **Icons**: Lucide React

## Agora Conversational AI Integration

### Voice Mode Features
- **Real-time Voice Capture**: Uses Agora RTC SDK for high-quality audio capture
- **Speech-to-Text**: Converts spoken words to text using Web Speech API
- **Voice Messages**: Voice input appears as chat bubbles with 🎤 indicator
- **Visual Feedback**: Recording indicator with animated red dot
- **Seamless Integration**: Voice messages sent to same backend as text messages

### How Voice Mode Works
1. Click "🎤 Voice Mode (Agora)" button in left panel
2. Grant microphone permissions when prompted
3. Click "Start Recording" to begin speaking
4. Speak your question clearly
5. Speech is automatically converted to text and sent to AI
6. AI response appears in chat interface
7. Click "Stop Voice Mode" when finished

### Agora SDK Integration
- **SDK**: AgoraRTC_N.js loaded via CDN
- **Mode**: RTC (Real-Time Communication)
- **Codec**: VP8
- **Audio**: Microphone capture enabled
- **Fallback**: Graceful degradation if SDK unavailable

## Installation & Setup

### Prerequisites
- Node.js (v16 or higher)
- yarn package manager

### Install Dependencies

```bash
cd /app/frontend
yarn install
```

### Run Development Server

```bash
yarn start
```

The app will be available at `http://localhost:3000`

## Backend Integration

The app sends all chat messages to:
```
https://studysphere-c3jet4vgr4gooj9g8vq5tm.streamlit.app
```

### API Format

All requests are POST requests with JSON body:
```json
{
  "question": "Your message or question here"
}
```

### Test Me Feature

When clicking "Test Me", the app sends:
```json
{
  "question": "Generate 3 multiple-choice quiz questions from my notes."
}
```

## Build for Production

```bash
cd /app/frontend
yarn build
```

The optimized build will be in the `build/` directory.

## Design System

### Colors
- **Primary Blue**: #2563eb, #3b82f6
- **White**: #ffffff
- **Light Gray**: #f5f7fa, #f8fafc
- **Text**: #1e293b (dark), #64748b (muted)

### Typography
- **Font Family**: Poppins (Google Fonts)
- **Weights**: 300, 400, 500, 600, 700

## File Structure

```
/app/frontend/
├── src/
│   ├── App.js              # Main application component
│   ├── App.css             # Application styles
│   ├── index.js            # React entry point
│   └── components/ui/      # Shadcn UI components
├── public/
│   └── index.html          # HTML template
└── package.json            # Dependencies
```

## Features Verification

✅ Left panel with PDF upload and Test Me button
✅ Right panel with full chat interface
✅ POST requests to Streamlit backend
✅ Blue and white academic UI design
✅ Poppins font from Google Fonts
✅ Rounded cards and soft shadows
✅ Smooth chat bubbles with animations
✅ Error handling with friendly messages
✅ No missing imports or build errors
✅ Successful compilation
