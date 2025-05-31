# DynamicHumanAuth

**DynamicHumanAuth** is a dynamic, real-time human authentication system developed using Python and OpenCV. It employs facial recognition techniques—specifically the Local Binary Patterns Histogram (LBPH) algorithm—to accurately detect and authenticate individuals using live camera feeds. This system is designed to provide an additional layer of security for workplaces, academic institutions, and other access-controlled environments by only allowing pre-registered users to gain access while alerting security personnel when unauthorized individuals are detected.

---

## 📌 Project Objective

The core objective of DynamicHumanAuth is to replace or supplement traditional physical authentication methods (such as ID cards or biometrics) with an intelligent, real-time facial recognition system. The solution aims to:
- Reduce unauthorized physical access.
- Improve response time in case of intrusion attempts.
- Automate attendance logging and monitoring.
- Create a lightweight and scalable model for deployment across various environments.

---

## 🧠 Core Concept

At its heart, DynamicHumanAuth is built on a simple but effective idea:  
> "Let a machine recognize faces just like a human would—quickly and reliably."

### Workflow:
1. **Capture images of known (authorized) individuals.**
2. **Train a facial recognition model using those images.**
3. **Continuously analyze live camera feeds.**
4. **Compare detected faces in real-time with the trained data.**
5. **Trigger alerts if an unrecognized individual is found.**

This system simulates the process of securing access to restricted zones such as server rooms, research labs, or entrance gates in real time.

---

## 🛠️ Technologies Used

| Component               | Role                                              |
|------------------------|---------------------------------------------------|
| **Python 3**           | Core programming language                         |
| **OpenCV**             | For face detection, recognition, and image I/O    |
| **LBPH Algorithm**     | For training and recognizing facial features      |
| **IP/USB Cameras**     | For capturing live feeds                          |
| **Tkinter (optional)** | For GUI components (if extended)                  |
| **NumPy & OS Modules** | For data handling and directory operations        |

---

## 🔍 Detailed Features

### 🔐 Face Registration
- Run `Register.py` to enroll new users.
- Captures 100+ facial images per user to ensure model accuracy.
- Stores user images in an organized dataset directory, labeled by ID.

### 🧠 Model Training
- Uses the Local Binary Patterns Histogram (LBPH) model for its balance between accuracy and efficiency.
- Face recognizer is trained on grayscale versions of captured images.
- The model is serialized and saved to disk as `classifier.xml`.

### 🎥 Camera Configuration
- `Camera_select.py` allows the user to configure IP camera or webcam sources.
- This ensures flexibility and portability across environments.

### 🧾 Real-Time Authentication
- `Home_page.py` acts as the main interface.
- Continuously monitors the camera feed.
- Matches faces from the feed against the trained dataset.
- If an unauthorized individual is detected, alerts can be sent or logged.

---

## 🖥️ Installation & Setup

### ✅ Prerequisites

- Python 3.x
- A working webcam or IP camera
- `pip` package manager

### 📦 Installation Steps

1. **Clone the repository**

bash
git clone https://github.com/saikiranbheemagani/SecureVision-FaceAccessSystem.git
cd DynamicHumanAuth

Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Start with face registration

bash
Copy
Edit
python Register.py
Configure your camera

bash
Copy
Edit
python Camera_select.py
Run the main interface

bash
Copy
Edit
python Home_page.py
🧪 How It Works
Data Collection
The system captures multiple face images for each individual.

These are stored in folders labeled by user ID.

Training
The LBPH algorithm converts faces into feature vectors.

The trained model maps each vector to its corresponding ID.

Recognition
At runtime, the system captures a frame from the video feed.

Face detection is performed using Haar cascades.

The LBPH recognizer predicts the ID (or flags unknown).

Alerts (Optional Extension)
If an unknown face is detected, logs can be generated.

Extensions like email alerts, SMS, or GUI alerts can be added.

📷 Screenshots (optional placeholders)
You can include screenshots or GIFs like:

📸 Face registration

🎦 Real-time authentication window

⚠️ Unauthorized person alert

(If you need help creating or embedding those, let me know and I’ll help generate them.)

🧩 Project Structure
bash
Copy
Edit
DynamicHumanAuth/
│
├── dataset/               # Contains captured face images per user
├── classifier.xml         # Trained LBPH model
├── Register.py            # For face image registration
├── Camera_select.py       # Camera configuration and testing
├── Home_page.py           # Real-time recognition interface
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
🔮 Future Improvements
Add database integration (SQLite/MySQL) for storing logs.

Integrate with hardware access control systems (e.g., smart doors).

Deploy GUI dashboard for managing users and access logs.

Add support for multiple camera inputs.

Cloud-based face recognition using REST APIs.

Integrate with attendance systems.

🙋‍♂️ Author
This project was developed by Sai Kiran Bheemagani, as part of an academic initiative to demonstrate the application of computer vision in real-time security systems.

GitHub Profile →

📄 License
This project is licensed under the MIT License.
Feel free to use, modify, and share under the terms of this license.

“Security is not just a feature—it's a necessity. With DynamicHumanAuth, we bring intelligent surveillance closer to the real world.”
