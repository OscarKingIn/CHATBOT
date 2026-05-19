ChatBot Application

A full-stack AI-powered chatbot application with real-time messaging, persistent storage, and scalable cloud deployment.

---

## 🧱 Tech Stack

### Frontend

- React / Next.js
- Tailwind CSS

### Backend

- Node.js / Express (or FastAPI if Python)
- REST API / WebSockets

### Database

- PostgreSQL (Neon)

### Cache / Queue

- Redis (Upstash)

### Deployment

- Frontend → Vercel
- Backend → Render / Railway

---

## 📁 Project Structure

/frontend → UI (React / Next.js)
/backend → API server
/config → Environment configs

---

## ⚙️ Environment Variables

Create `.env` files:

### Backend

DATABASE_URL=
REDIS_URL=
PORT=5000
OPENAI_API_KEY=

### Frontend

NEXT_PUBLIC_API_URL=

---

## 🧪 Local Development

### 1. Clone Repo

git clone https://github.com/OscarKingIn/CHATBOT.git
cd CHATBOT

### 2. Install Dependencies

Frontend:

cd frontend
npm install

Backend:

cd backend
npm install

### 3. Run App

Backend:

npm run dev

Frontend:

npm run dev

---

## 🚀 Production Deployment

| Service  | Platform         |
| -------- | ---------------- |
| Frontend | Vercel           |
| Backend  | Render / Railway |
| DB       | Neon PostgreSQL  |
| Cache    | Upstash Redis    |

---

## 🔐 Security Notes

- Never commit `.env`
- Use environment variables in production
- Enable HTTPS

---

## 📦 Features

- Real-time chat
- AI responses
- Persistent conversations
- Scalable architecture

---

## 👨‍💻 Author

Oscar
