# 🔐 PyPassGen - Password Generator

A command-line and web-based password generator built with **Python**, **Flask**, and **TailwindCSS**. Deployed using **Docker** on **Render**.

## 🌍 Live Demo

👉 [https://pypassgen.onrender.com](https://pypassgen.onrender.com), Might dhout down due to free plan

## 🛠 Tech Stack

- Python
- Flask
- TailwindCSS（CDN）
- Docker
- Render (for cloud deployment)

## ✨ Features

- 🔢 Customize password length
- 🔐 Choose complexity (digits, special characters)
- 📜 Web interface with password generation history
- 🧪 CLI mode for quick password generation
- 🐳 Dockerized and ready for deployment

## 🚀 Local Development

1. Clone the repo:
   ```bash
   git clone path
   cd pypassgen
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

## 🐳 Docker Usage

1. Build the Docker image:
   ```bash
   docker build -t pypassgen .
   ```

2. Run the container:
   ```bash
   docker run -d -p 5000:5000 pypassgen
   ```

Then open your browser to: [http://localhost:5000](http://localhost:5000)

## ☁️ Deploying on Render

1. Push your repo to GitHub.
2. Go to [Render.com](https://render.com) and create a new **Web Service**.
3. Select “docker”.
4. Connect your repo and deploy.

Deployed URL: [https://pypassgen.onrender.com](https://pypassgen.onrender.com), Might shut down because it is a free plan

## 🧠 Password Generator Logic

```python
def generate_password(length=12, use_digits=True, use_specials=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_specials:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))
```

- `length`: desired password length (default is 12)
- `use_digits`: whether to include numbers
- `use_specials`: whether to include special characters

## 📁 Project Structure

```
pypassgen/
├── app.py              # Main Flask app
├── templates/          # HTML templates
├── generator.py             # generation logic
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker config
└── README.md
```

## 📄 License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

---

Feel free to fork, modify, and deploy your own version! 🔧🧪🚀
```