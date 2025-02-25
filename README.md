# Chatbot Setup Guide

Welcome! Follow this guide to set up and run the chatbot on your computer. No coding experience needed! 😊

## **1. What You Need**
Before you start, make sure you have:
- **Docker** → [Download Docker](https://www.docker.com/get-started/)
- **Git** (to clone the project) → [Download Git](https://git-scm.com/downloads)

## **2. Install the Chatbot**
### **Option 1: Download the Code (Recommended)**
Open a terminal or command prompt and run:
```sh
# Clone the chatbot repository
git clone https://github.com/Paink64/Chatbot.git
cd Chatbot
```

### **Option 2: Download as a ZIP (Alternative)**
1. Go to the [GitHub Repository](https://github.com/Paink64/Chatbot)
2. Click **"Code" → "Download ZIP"**
3. Extract the ZIP file and open the extracted folder in a terminal or command prompt.

## **3. Set Up Environment Variables**
We use a `.env` file to store secrets (like API keys). Create a new file called `.env` inside the project folder and add:
```
GROQ_API_KEY=(your-api-key-here)
```

If you don’t have API keys, leave the values empty.

## **4. Build and Run the Chatbot with Docker**
Since Docker is required, you need to build and run the chatbot using Docker commands.

### **Enable execute permissions for the setup script:**
```sh
chmod u+x run_chatbot.sh
```

### **Build and Run the Docker Image:**
```sh
./run_chatbot.sh
```

Now, open your browser and go to:
```
http://localhost:8501
```

## **5. Troubleshooting**
- If you get a permission error, try running the commands with `sudo` on Mac/Linux.
- If the chatbot doesn’t start, ensure Docker is running on your system.
- For Windows users, ensure Docker Desktop is installed and running.

Enjoy chatting with your AI bot! 🚀

