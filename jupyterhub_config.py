# Configuration file for JupyterHub
import os
from jupyterhub.spawner import SimpleLocalProcessSpawner

c = get_config()  # noqa: F821

# ✅ Use simple spawner for local testing (no Docker/Podman)
c.JupyterHub.spawner_class = SimpleLocalProcessSpawner

# ✅ Set the working directory inside the spawned server
notebook_dir = os.environ.get("DOCKER_NOTEBOOK_DIR", "/home/{username}/work")
c.Spawner.notebook_dir = notebook_dir

# ✅ Enable debug logs (optional)
c.Spawner.debug = True

# ✅ Hub configuration
c.JupyterHub.hub_ip = "127.0.0.1"
c.JupyterHub.hub_port = 8080

# ✅ Persist data
c.JupyterHub.cookie_secret_file = "/data/jupyterhub_cookie_secret"
c.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"

# ✅ Authentication setup
c.Authenticator.allow_all = True
c.JupyterHub.authenticator_class = "nativeauthenticator.NativeAuthenticator"
c.NativeAuthenticator.open_signup = True

# ✅ Admin setup (optional)
admin = os.environ.get("JUPYTERHUB_ADMIN")
if admin:
    c.Authenticator.admin_users = [admin]
