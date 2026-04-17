# CertPremium - Secure Security+ Study Platform

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
- Dependency Security (Dependabot)
- SAST (Semgrep) + upload SARIF (GitHub Code Scanning)
- Dependency & Container Scanning (Trivy)
- Code Scanning (CodeQL)

---

CI/CD SECURITY EVIDENCE

Esta seção demonstra a implementação de um **Security Pipeline** integrado ao fluxo de CI/CD, com foco em detecção de vulnerabilidades, automação de segurança e validação contínua do código e da infraestrutura.

1. Dependency Security (Dependabot)

O projeto utiliza Dependabot para automação de atualização de dependências e monitoramento contínuo de vulnerabilidades conhecidas (CVEs).

- Atualizações automáticas de pacotes Python (requirements em `backend/`)
- Atualizações de GitHub Actions
- Atualizações relacionadas a Docker/Dockerfile no `backend/`

Evidência:
- Configuração em `.github/dependabot.yml`
- PRs automáticos com labels `dependencies`/`security`

2. SAST (Static Application Security Testing) — Semgrep

O SAST roda no pipeline de CI para detectar padrões inseguros em Python/Django sem executar a aplicação.

Evidência:
- Workflow `.github/workflows/ci.yml` (job `sast`)
- Geração de `semgrep.sarif` e upload via `github/codeql-action/upload-sarif` para a aba **Security → Code scanning**

3. Dependency & Container Scanning — Trivy

O pipeline utiliza Trivy para analisar vulnerabilidades em dependências e em imagens Docker.

Evidência:
- Workflow `.github/workflows/ci.yml` (jobs `dependency-scan` e `docker-scan`)
- Pipeline configurado para falhar em achados `HIGH/CRITICAL` (exit-code 1)

4. Code Scanning (CodeQL + GitHub Security)

Integração com GitHub CodeQL para análise semântica avançada do código.

Evidência:
- Workflow `.github/workflows/codeql.yml`
- Resultados visíveis na aba **Security → Code scanning**

5. Security Automation Pipeline (CI/CD Enforcement)

O pipeline funciona como um **security gate**:

Fluxo:
- Commit/PR → GitHub Actions
- Lint/Checks
- SAST (Semgrep + SARIF)
- Scans de dependências e containers (Trivy)
- Code scanning (CodeQL)

Resultado:
- Detecção automática de vulnerabilidades
- Evidências auditáveis (logs e SARIF)
- Base para práticas contínuas de DevSecOps

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

