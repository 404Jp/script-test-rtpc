import subprocess

# Función para generar combinaciones de URLs RTSP
def generate_urls(ip):
    return [
        f"rtsp://{ip}:554/ch1/main/av_stream",
        f"rtsp://{ip}:554/stream1",
        f"rtsp://{ip}:554/1",
        f"rtsp://{ip}:554/0",
        f"rtsp://{ip}:554/live",
        f"rtsp://{ip}:554/video",
        f"rtsp://{ip}:554/stream"
    ]

# Función para probar una URL usando subprocess (comandos de ffmpeg)
def test_url_subprocess(url):
    try:
        result = subprocess.run(
            ['ffmpeg', '-i', url, '-f', 'null', '-t', '5', '-y', 'null'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10
        )
        if result.returncode == 0:
            print(f"Conexión exitosa: {url}")
        else:
            print(f"Fallo la conexión: {url}")
            print(result.stderr.decode())  # Mostrar más detalles del error
    except subprocess.TimeoutExpired:
        print(f"Fallo por tiempo de espera: {url}")
    except Exception as e:
        print(f"Error inesperado con {url}: {e}")

# Solicitar al usuario la IP de la cámara
def get_camera_ip():
    while True:
        ip = input("Ingresa la IP de la cámara: ").strip()
        if ip:
            return ip
        else:
            print("La IP no puede estar vacía. Por favor, ingresa una IP válida.")

ip = get_camera_ip()

# Generar combinaciones de URLs y probarlas
urls = generate_urls(ip)
for url in urls:
    test_url_subprocess(url)
