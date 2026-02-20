# 🚀 BragBoard – Internal Recognition & Shoutout Platform

BragBoard is a full-stack web application designed to promote peer recognition within organizations. Employees can give shoutouts, react, comment, and view department-based leaderboards.

---

## 🌐 Live Demo

Frontend: (Coming Soon)  
Backend API: (Coming Soon)

---

## 🛠 Tech Stack

### Frontend
- React (Vite)
- Tailwind CSS
- Axios / Fetch API

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication

### Deployment
- Frontend: Vercel
- Backend: Render
- Database: Render PostgreSQL

---

## ✨ Features

- 🔐 User Authentication (JWT based)
- 🏢 Department-based feed
- 👏 Multi-user shoutouts
- 💬 Comment system
- ⭐ Reaction system
- 🏆 Leaderboard
- 👤 Profile page
- 🔔 Notifications
- 🛡 Admin Dashboard
- 🚩 Report & moderation system

---

## 📂 Project Structure
bragboard/
│
├── backend/ # FastAPI Backend
│ ├── main.py
│ ├── models/
│ ├── routers/
│ ├── schemas/
│ ├── database.py
│ └── requirements.txt
│
├── bragfront/ # React Frontend
│ ├── src/
│ │ ├── components/
│ │ ├── pages/
│ │ └── main.jsx
│ ├── package.json
│ └── tailwind.config.js
│
├── .gitignore
└── README.md


---

## ⚙️ Local Development Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/bragboard.git
cd bragboard

🖥 Backend Setup (FastAPI)
Step 1: Create Virtual Environment
cd backend
python -m venv venv

Activate environment:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
Step 2: Install Dependencies
pip install -r requirements.txt
Step 3: Create Environment Variables

Create a .env file inside backend/:

DATABASE_URL=postgresql://user:password@localhost:5432/bragboard
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
Step 4: Run Backend Server
uvicorn main:app --reload

Backend runs at:

http://localhost:8000

Swagger Docs:

http://localhost:8000/docs
🌐 Frontend Setup (React + Vite)
Step 1: Install Dependencies
cd bragfront
npm install
Step 2: Configure Environment Variable

Create a .env file inside bragfront/:

VITE_API_BASE_URL=http://localhost:8000
Step 3: Run Development Server
npm run dev

Frontend runs at:

http://localhost:5173
🚀 Production Deployment Architecture
Frontend (Vercel)
        ↓
Backend API (Render)
        ↓
PostgreSQL Database (Render Managed DB)
Environment Variables in Production

Backend (Render):

DATABASE_URL

SECRET_KEY

ALGORITHM

ACCESS_TOKEN_EXPIRE_MINUTES

Frontend (Vercel):

VITE_API_BASE_URL

🔒 Security Considerations

JWT-based authentication

Password hashing

Environment variable configuration

No hardcoded secrets

Role-based route protection

Secure database connection (production)

📈 Future Improvements

Docker containerization

CI/CD pipeline

Redis caching

Email notifications

File upload support

WebSocket-based real-time notifications

Advanced analytics dashboard

Unit and integration testing

📊 Project Purpose

This project demonstrates:

Full-stack architecture design

RESTful API development

Secure authentication system

Database modeling & relationships

Admin moderation workflows

Production deployment strategy

Clean frontend component structuring

👨‍💻 Author

Suthan
Full Stack Developer

📜 License

This project is built for educational and portfolio purposes.


---

# ✅ Next Step

After adding this README:

1. Commit it:
```bash
git add README.md
git commit -m "Added professional README"
git push