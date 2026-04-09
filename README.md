# CertPremium - Secure Security+ Study Platform

[![CI Security Pipeline](https://github.com/gustavounreal/certpremium/actions/workflows/ci.yml/badge.svg)](https://github.com/gustavounreal/certpremium/actions/workflows/ci.yml)
[![Code Scanning](https://img.shields.io/badge/code%20scanning-passing-brightgreen)](https://github.com/gustavounreal/certpremium/security/code-scanning)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Plataforma de estudos para certificação CompTIA Security+ (SY0-701) com foco em segurança aplicada, DevSecOps e detecção de ameaças.

---

VISÃO GERAL

O CertPremium é um projeto prático desenvolvido para demonstrar competências reais em cibersegurança, incluindo:

- Proteção de aplicações web (OWASP Top 10)
- Hardening de infraestrutura Linux
- Monitoramento e análise de eventos de segurança
- Pipeline DevSecOps com validações automatizadas

Mais do que uma plataforma de estudos, este projeto funciona como um laboratório de segurança aplicado.

---

ARQUITETURA

Flutter (Mobile)
   ↓ HTTPS
Nginx (Reverse Proxy + TLS)
   ↓
Django (REST API + Auth)
   ↓
PostgreSQL

Stack:
- Backend: Django + DRF + JWT
- Database: PostgreSQL
- Proxy: Nginx (hardened)
- Infra: Docker Compose
- Mobile: Flutter

---

SEGURANÇA IMPLEMENTADA

Infraestrutura:
- Hardening de VPS (Ubuntu 24.04 - CIS Benchmark)
- Firewall (UFW)
- Proteção contra brute force (Fail2ban)
- IDS/IPS com CrowdSec
- SSH com chaves ED25519

Aplicação (OWASP Top 10):
- Proteção contra SQL Injection (ORM)
- Proteção contra XSS
- Controle de acesso com JWT
- Prevenção de IDOR
- Validação de entrada

Comunicação:
- HTTPS obrigatório (TLS 1.3)

Containers:
- Execução com usuário não-root
- Scan com Trivy

DevSecOps:
- SAST (Semgrep)
- DAST (OWASP ZAP)
- Dependency Scan (Safety)
- CI/CD com validações de segurança

---

THREAT MODEL (STRIDE)

- Spoofing → autenticação JWT
- Tampering → validação de dados
- Repudiation → logs
- Information Disclosure → criptografia
- DoS → rate limiting / Fail2ban
- Privilege Escalation → controle de acesso

---

MONITORAMENTO (SOC)

- Coleta de logs
- Detecção de acessos suspeitos
- Base para SIEM
- Análise inicial de eventos

---

ESTRUTURA

certpremium/
- backend/
- nginx/
- .github/workflows/
- docker-compose.yml

---

QUICK START

git clone https://github.com/gustavounreal/certpremium.git
cd certpremium

cp .env.example .env
docker compose up -d

docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser

---

ACESSO

API: http://localhost:8000/api/
Admin: http://localhost:8000/admin/

---

TESTES

pytest
flake8
safety check

---

ROADMAP

- Integração com SIEM
- Alertas automatizados
- Dashboard de segurança
- Detecção de anomalias
- RBAC avançado

---

COMPETÊNCIAS

- OWASP
- Hardening Linux
- Logs e monitoramento
- DevSecOps
- Threat Modeling
- Secure SDLC

---

OBJETIVO

Projeto desenvolvido como portfólio para atuação em:

- SOC
- Security Analyst
- DevSecOps

---

AUTOR

Gustavo Macedo
GitHub: https://github.com/gustavounreal
LinkedIn: https://linkedin.com/in/gustavo-r-macedo-225a636a

---

LICENÇA

MIT

