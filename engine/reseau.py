# -*- coding: utf-8 -*-
"""Contexte SSL robuste : certifi si présent, sinon bundle système, sinon défaut.

Certains Python (python.org sans « Install Certificates.command », ou un venv
minimal) n'ont pas de magasin de certificats utilisable — les flux RSS et les
appels API échouent alors en CERTIFICATE_VERIFY_FAILED. Ce module règle ça
une fois pour toutes, en local comme dans GitHub Actions.
"""
import os
import ssl


def contexte():
    try:
        import certifi  # noqa: WPS433
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        pass
    for chemin in ("/etc/ssl/cert.pem",
                   "/etc/pki/tls/certs/ca-bundle.crt",
                   "/etc/ssl/certs/ca-certificates.crt"):
        if os.path.exists(chemin):
            try:
                return ssl.create_default_context(cafile=chemin)
            except Exception:
                continue
    return ssl.create_default_context()
