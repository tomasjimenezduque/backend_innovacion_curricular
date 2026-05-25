import requests

class ApiService:
    BASE_URL = "http://127.0.0.1:8000/api"

    def listar(self, tabla, limite=None, **kwargs):
        try:
            params = {}

            if limite is not None:
                params["limite"] = limite

            params.update(kwargs)

            response = requests.get(
                f"{self.BASE_URL}/{tabla}/",
                params=params,
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            if isinstance(data, dict):

                if "datos" in data:
                    return data["datos"]

                if "data" in data:
                    return data["data"]

                if "results" in data:
                    return data["results"]

                if "items" in data:
                    return data["items"]

            return data

        except Exception as e:
            print(f"Error listar {tabla}: {e}")
            return []

    def obtener(self, tabla, id, **kwargs):
        try:
            r = requests.get(
                f"{self.BASE_URL}/{tabla}/{id}",
                params=kwargs
            )
            r.raise_for_status()
            return r.json()
        except Exception:
            return None

    def crear(self, tabla, data):
        try:
            return requests.post(
                f"{self.BASE_URL}/{tabla}/",
                json=data
            ).json()
        except Exception:
            return None

    def actualizar(self, tabla, id, data):
        try:
            return requests.put(
                f"{self.BASE_URL}/{tabla}/{id}",
                json=data
            ).json()
        except Exception:
            return None

    def eliminar(self, tabla, id):
        try:
            return requests.delete(
                f"{self.BASE_URL}/{tabla}/{id}"
            ).ok
        except Exception:
            return False
