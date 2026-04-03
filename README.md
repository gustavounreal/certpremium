# CertPremium - Security+ Study Platform

[![CI Security Pipeline](https://github.com/gustavounreal/certpremium/actions/workflows/ci.yml/badge.svg)](https://github.com/gustavounreal/certpremium/actions/workflows/ci.yml)
[![Code Scanning](https://img.shields.io/badge/code%20scanning-passing-brightgreen)](https://github.com/gustavounreal/certpremium/security/code-scanning)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> Plataforma de estudos para certificação CompTIA Security+ SY0-701 com foco em arquitetura segura e DevSecOps.

## Objetivo

Este projeto demonstra competências práticas em cibersegurança aplicada:
- Hardening de infraestrutura (VPS Ubuntu 24.04)
- Backend seguro seguindo OWASP Top 10
- Pipeline CI/CD com SAST/DAST
- Threat Modeling (STRIDE)
- Container Security

## Arquitetura

```
┌─────────────┐
│   Flutter   │ (Mobile App - Android/iOS)
└──────┬──────┘
       │ HTTPS
       ▼
┌─────────────┐
│    Nginx    │ (Reverse Proxy + TLS)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Django    │ (REST API + JWT Auth)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ PostgreSQL  │ (Database)
└─────────────┘
```

**Stack:**
- **Backend:** Django 5.0 + DRF + JWT
- **Database:** PostgreSQL 16 (Alpine)
- **Proxy:** Nginx (hardened)
- **Frontend:** Flutter (mobile)
- **Infra:** Docker Compose

## Controles de Segurança Implementados

| Camada | Controle | Ferramenta/Técnica |
|--------|----------|-------------------|
| Infra | VPS Hardening | CIS Benchmark Ubuntu 24.04 |
| Infra | Firewall | UFW (allow 22, 80, 443) |
| Infra | IDS/IPS | CrowdSec |
| Infra | SSH Hardening | Chaves ED25519, fail2ban |
| App | Autenticação | JWT (djangorestframework-simplejwt) |
| App | Anti-IDOR | UUID primary keys |
| App | Input Validation | Django Forms + DRF Serializers |
| App | SQL Injection | Django ORM (parameterized queries) |
| App | XSS Prevention | Django auto-escaping |
| App | HTTPS | TLS 1.3 (Nginx) |
| Container | Non-root user | `certadmin` |
| Container | Vulnerability Scan | Trivy |
| CI/CD | SAST | Semgrep |
| CI/CD | DAST | OWASP ZAP |
| CI/CD | Dependency Check | Safety |

## Estrutura do Projeto

```
certpremium/
├── backend/              # Django REST API
│   ├── core/            # App principal (models, views, serializers)
│   ├── certpremium/     # Settings e configuração Django
│   └── requirements.txt
├── nginx/               # Configuração Nginx (reverse proxy)
├── .github/workflows/   # CI/CD pipelines
└── docker-compose.yml   # Orquestração de containers
```

## Quick Start

### Pré-requisitos
- Docker 24+
- Docker Compose 2.21+
- Git

### 1. Clone o repositório
```bash
git clone https://github.com/gustavounreal/certpremium.git
cd certpremium
```

### 2. Configure as variáveis de ambiente
```bash
cp .env.example .env
# Edite o .env com suas credenciais
```

### 3. Inicie os containers
```bash
docker compose up -d
```

### 4. Execute as migrations
```bash
docker compose exec backend python manage.py migrate
```

### 5. Crie um superusuário
```bash
docker compose exec backend python manage.py createsuperuser
```

### 6. Acesse
- **API:** http://localhost:8000/api/
- **Admin:** http://localhost:8000/admin/

## Testes

```bash
# Rodar testes unitários
docker compose exec backend pytest

# Rodar linting
docker compose exec backend flake8

# Security scan
docker compose exec backend safety check
```

## Competências Demonstradas

Este projeto foi desenvolvido como portfólio técnico para demonstrar:

- Segurança de aplicações web (OWASP Top 10)
- Hardening de infraestrutura (CIS Benchmark)
- DevSecOps (CI/CD com security gates)
- Container Security (Docker hardening)
- Threat Modeling (STRIDE)
- Secure SDLC
- Python/Django
- PostgreSQL
- Git/GitHub Actions

## Licença

MIT License - veja `LICENSE` para detalhes.

## Autor

**Gustavo Macedo**
- LinkedIn: [linkedin.com/in/seu-perfil](https://linkedin.com/in/seu-perfil)
- GitHub: [@gustavounreal](https://github.com/gustavounreal)
