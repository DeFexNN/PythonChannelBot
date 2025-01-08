import subprocess
import sys

def install_dependencies():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "python-telegram-bot==20.0a0"])
        print("Зависимости успешно установлены.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при установке зависимостей: {e}")

if __name__ == "__main__":
    install_dependencies()
