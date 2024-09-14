import subprocess

# Función para generar combinaciones de URLs RTSP para cámaras Hipcam
def generate_urls(ip):
    return [
        f"rtsp://admin:admin@{ip}:554/11",
        f"rtsp://admin:admin@{ip}:10554/11",
        f"rtsp://admin:admin@{ip}:5544/11",
        f"rtsp://admin:admin@{ip}:554/h264_stream",
        f"rtsp://admin:admin@{ip}:554/user=admin_password=Y5eIMz3C_channel=1_stream=0.sdp",
        f"rtsp://admin:admin@{ip}:554/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp"
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
