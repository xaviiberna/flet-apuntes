# Publicar la app: web, APK, Windows y Linux

Todos los formatos se generan con `flet build <plataforma>`. Se ejecuta desde la carpeta del proyecto y con el entorno virtual activado.

```bash
flet build web     --module-name paso8_app_final
flet build apk     --module-name paso8_app_final
flet build windows --module-name paso8_app_final
flet build linux   --module-name paso8_app_final
```

| Código | Qué hace |
|---|---|
| `flet build web` | Genera la versión web (HTML/JS) en `build/web`. |
| `flet build apk` | Genera la app Android (`.apk`) en `build/apk`. |
| `flet build windows` | Genera el ejecutable `.exe` en `build/windows` (solo desde Windows). |
| `flet build linux` | Genera el binario de Linux en `build/linux` (solo desde Linux). |
| `--module-name paso8_app_final` | Qué archivo `.py` es la app, sin la extensión. |

`--module-name` es el nombre del archivo `.py` **sin** la extensión. El resultado aparece en la carpeta `build/<plataforma>/`.

=== "Web"

    ```bash
    flet build web --module-name paso8_app_final
    ```

    | Código | Qué hace |
    |---|---|
    | `flet build web` | Compila la app para navegador. |
    | `--module-name paso8_app_final` | Indica el archivo de la app (`paso8_app_final.py`). |

    Se comprueba sirviendo `build/web` en local y abriendo `http://localhost:8000`.

    ![build web](../assets/img/build-web.png)
    ![web en localhost](../assets/img/web-localhost.png){ width=600 }

=== "Android (APK)"

    ```bash
    flet build apk --module-name paso8_app_final
    ```

    | Código | Qué hace |
    |---|---|
    | `flet build apk` | Compila la app para Android. Si falta el SDK de Android, pregunta si lo instala. |
    | `--module-name paso8_app_final` | Archivo de la app. |

    Si no hay Android SDK, Flet pregunta si lo instala (`y`). Resultado: `build/apk/*.apk`, que se instala en el móvil.

    ![build apk](../assets/img/build-apk.png)
    ![app en Android](../assets/img/apk-android.png){ width=240 }

=== "Windows"

    Requisitos: **Visual Studio Community** (carga de trabajo «Desarrollo para el escritorio con C++») y activar el **Modo desarrollador** de Windows.

    ```powershell
    flet build windows --module-name paso8_app_final
    ```

    | Código | Qué hace |
    |---|---|
    | `flet build windows` | Compila el `.exe`. Necesita Visual Studio (C++) y el modo desarrollador. |
    | `--module-name paso8_app_final` | Archivo de la app. |

    Resultado en `build/windows/`: el `.exe` junto a sus DLL (hay que mantenerlos juntos).

    ![build windows](../assets/img/build-windows.png)
    ![exe](../assets/img/windows-exe.png){ width=600 }

=== "Linux (con Docker desde Windows)"

    Como en Windows no se puede compilar para Linux directamente, se usa un contenedor Ubuntu.

    **1. Abrir el contenedor** montando la carpeta del proyecto en `/app`:

    ```powershell
    docker run -it --rm -v "${PWD}:/app" ubuntu:24.04 bash
    ```

    | Código | Qué hace |
    |---|---|
    | `docker run` | Crea y arranca un contenedor. |
    | `-it` | Modo interactivo con terminal: puedes escribir dentro. |
    | `--rm` | Borra el contenedor al salir. |
    | `-v "${PWD}:/app"` | Monta la carpeta actual de Windows dentro del contenedor en `/app`. |
    | `ubuntu:24.04` | Imagen de Ubuntu 24.04. |
    | `bash` | Abre una terminal bash dentro. |

    **2. Instalar Python y Flet** (dentro del contenedor):

    ```bash
    apt update && apt install -y python3 python3-pip python3-venv curl git unzip xz-utils jq
    python3 -m venv /venv && source /venv/bin/activate
    pip install flet
    ```

    | Código | Qué hace |
    |---|---|
    | `apt update` | Actualiza la lista de paquetes. |
    | `apt install -y python3 python3-pip python3-venv curl git unzip xz-utils jq` | Instala Python, pip, venv y herramientas que usa `flet build`. `-y` = no pregunta. |
    | `python3 -m venv /venv` | Crea un entorno virtual en `/venv`. |
    | `source /venv/bin/activate` | Lo activa. |
    | `pip install flet` | Instala Flet en el entorno. |

    **3. Dependencias de compilación de Linux** (las da el propio Flet):

    ```bash
    LINUX_DEPS="$(flet --version --json | jq -r '.linux_dependencies | join(" ")')"
    apt-get install -y --no-install-recommends $LINUX_DEPS
    ```

    | Código | Qué hace |
    |---|---|
    | `flet --version --json` | Flet muestra su información en JSON, incluida la lista de dependencias para compilar en Linux. |
    | `jq -r '.linux_dependencies | join(" ")'` | `jq` saca esa lista y la une con espacios. |
    | `LINUX_DEPS="$(...)"` | Guarda el resultado en la variable `LINUX_DEPS`. |
    | `apt-get install -y --no-install-recommends $LINUX_DEPS` | Instala esas dependencias, sin paquetes extra recomendados. |

    **4. Compilar:**

    ```bash
    mkdir /work && cp /app/paso8_app_final.py /work/ && cd /work
    flet build linux --module-name paso8_app_final
    ```

    | Código | Qué hace |
    |---|---|
    | `mkdir /work` | Crea una carpeta de trabajo dentro del contenedor. |
    | `cp /app/paso8_app_final.py /work/` | Copia la app desde la carpeta montada. |
    | `cd /work` | Entra en ella. |
    | `flet build linux --module-name paso8_app_final` | Compila el binario de Linux en `/work/build/linux`. |

    Resultado en `/work/build/linux`. Se sube a GitHub (Releases) y se descarga en una máquina Linux para ejecutarlo.

    ![docker run](../assets/img/docker-run.png)
    ![apt](../assets/img/docker-apt.png)
    ![deps](../assets/img/docker-deps.png)
    ![build linux](../assets/img/build-linux.png)
    ![en la VM Linux](../assets/img/linux-vm.png){ width=600 }

!!! info "Entrega"
    Por su tamaño, el APK y los ejecutables no van en el repositorio: se suben como **Release** de GitHub (en esta práctica: `archivos-ejercicio-flet`, tag `v1.0`).
