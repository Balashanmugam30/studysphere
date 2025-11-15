# StudySphere - Your Conversational AI Study Partner

A modern, clean web application built with React that helps students interact with an AI study assistant. Upload PDF notes, chat with AI, and generate quiz questions to test your knowledge.

## Features

- 📚 **PDF Upload**: Simulated PDF upload with file name display
- 💬 **AI Chat Interface**: Full conversational chat with AI assistant
- 🧪 **Test Me**: Generate 3 multiple-choice quiz questions from your notes
- 🎨 **Modern UI**: Clean blue and white academic design with Poppins font
- ⚡ **Real-time Responses**: Instant backend communication with error handling
- 📱 **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

- **Frontend**: React + Create React App
- **Styling**: CSS with custom design system
- **UI Components**: Shadcn/UI components
- **HTTP Client**: Axios
- **Notifications**: Sonner toast notifications
- **Icons**: Lucide React

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
