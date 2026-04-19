<img width="1374" height="418" alt="logo3" src="https://github.com/user-attachments/assets/b8692bb9-38ba-4fa0-9727-4f497d72a4b4" /># CERTPREMIUM - SECURE SECURITY+ STUDY PLATFORM

[![CI Security Pipeline](https://github.com/gustavounreal/certpremium/actions/workflows/ci.yml/badge.svg)](https://github.com/gustavounreal/certpremium/actions/workflows/ci.yml)
[![CodeQL](https://github.com/gustavounreal/certpremium/actions/workflows/codeql.yml/badge.svg)](https://github.com/gustavounreal/certpremium/actions/workflows/codeql.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![OWASP Top 10](https://img.shields.io/badge/OWASP-Top%2010-blue)
![DevSecOps](https://img.shields.io/badge/DevSecOps-CI%2FCD%20Security-blue)
![Threat Model STRIDE](https://img.shields.io/badge/Threat%20Model-STRIDE-blue)

Plataforma de estudos para certificação CompTIA Security+ (SY0-701) com foco em cibersegurança aplicada, DevSecOps e detecção de ameaças.

---

SOBRE O PROJETO

Esse projeto prático foi desenvolvido para demonstrar competencias reais em ciberseguranca moderna, incluindo:

- Protecao de aplicacoes web (OWASP Top 10)
- Hardening de infraestrutura Linux
- Monitoramento e analise de eventos de seguranca (SOC-like)
- Pipeline DevSecOps com validacoes automatizadas (CI/CD Security)

O projeto funciona como um laboratorio de seguranca aplicado, integrando desenvolvimento seguro e praticas de seguranca ofensiva e defensiva.

---

VISAO GERAL E SCREENSHOTS

O CertPremium foi concebido como uma plataforma multi-certificação, utilizando o exame CompTIA Security+ (SY0-701) como projeto piloto para demonstrar um ecossistema completo de aprendizado e segurança aplicada.
Abaixo estão os principais fluxos visuais do projeto:
1. Experiência de Aprendizado (Mobile App)
A interface móvel, desenvolvida em Flutter, foi projetada para ser limpa e direta, facilitando o consumo de conteúdo técnico denso.

<p align="center">
  <img src="https://github.com/user-attachments/assets/3f5745e4-92fc-41bd-8d15-c22e291f6883" alt="Dashboard Principal" width="280"  /> 
   &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/cf836f0a-05e9-48ad-b9ea-2427f9d25c90" alt="Visão do Domínio" width="280"  />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/a7c9d6bb-a6f3-440d-8b5f-48215defb1d0" alt="Aulas do Tópico"  width="280" />
  

</p>


  * Dashboard Intuitivo: Exibe o status do exame, progresso e acesso rápido a estudos e simulados.    
  * Organização por Domínios: O conteúdo é categorizado de acordo com os domínios oficiais da CompTIA SY0-701.    
  * Fluxo de Tópicos: Navegação hierárquica clara de domínios para tópicos e aulas individuais.    

  <img src="https://github.com/user-attachments/assets/6cd7d83f-0afd-45ae-83dc-fcd35e54ada3" alt="Seções da Aula" width="280" />



ARQUITETURA

Flutter (Mobile)
↓ HTTPS
Nginx (Reverse Proxy + TLS 1.3)
↓
Django (REST API + Authentication JWT)
↓
PostgreSQL

Stack tecnologica:

- Backend: Django + Django REST Framework + JWT
- Database: PostgreSQL
- Proxy: Nginx (hardened)
- Infraestrutura: Docker Compose
- Mobile: Flutter

---

SEGURANCA IMPLEMENTADA

INFRAESTRUTURA (HARDENING)

- Ubuntu 24.04 com baseline CIS
- Firewall UFW configurado
- Fail2ban para protecao contra brute force
- CrowdSec como IDS/IPS
- SSH com autenticacao por chave ED25519 (password disabled)

SEGURANCA NA APLICACAO (OWASP TOP 10)

- Protecao contra SQL Injection utilizando ORM
- Protecao contra Cross-Site Scripting (XSS)
- Controle de acesso baseado em JWT
- Prevencao de IDOR (Insecure Direct Object Reference)
- Validacao de entrada em todas as APIs

COMUNICACAO SEGURA

- HTTPS obrigatorio
- TLS 1.3 habilitado
- Reverse proxy com Nginx hardening

CONTEINERES

- Execucao com usuario nao-root
- Boas praticas de seguranca em Docker
- Scan de imagens com Trivy

---

DEVSECOPS PIPELINE (CI/CD SECURITY)

O projeto implementa um pipeline de seguranca integrado ao CI/CD, funcionando como um security gate automatizado.

FLUXO DO PIPELINE (RESUMO)

Commit / Pull Request
↓
GitHub Actions CI
↓
SAST (Semgrep)
↓
Dependency Scan (Trivy)
↓
Container Scan (Trivy)
↓
Code Scanning (CodeQL)
↓
Relatorios e evidencias de seguranca

CONTROLES E EVIDENCIAS (O QUE EXISTE NO REPO)

1. Dependency Security (Dependabot)

- Atualizacao automatica de dependencias (pip, Docker, GitHub Actions)
- PRs automaticos com labels de dependencias/seguranca

Evidencia:

- `.github/dependabot.yml`

2. SAST (Semgrep)

- Analise estatica de codigo em Python/Django
- Gera relatorio SARIF e publica no GitHub Security (Code scanning)

Evidencia:

- `.github/workflows/ci.yml` (job `sast`)

Observacao:

- O Semgrep atualmente publica evidencias (SARIF) e nao bloqueia o pipeline em achados (configurado com `|| true`).

3. Dependency e Container Scanning (Trivy)

- Scan de vulnerabilidades no filesystem do repo e na imagem Docker
- Pipeline configurado para falhar em achados `HIGH/CRITICAL` nos scans principais

Evidencia:

- `.github/workflows/ci.yml` (jobs `dependency-scan` e `docker-scan`)

4. Code Scanning (CodeQL)

- Analise semantica do codigo e publicacao na aba Security

Evidencia:

- `.github/workflows/codeql.yml`

---

THREAT MODEL (STRIDE)

- Spoofing: autenticacao JWT
- Tampering: validacao de dados
- Repudiation: logging estruturado
- Information Disclosure: criptografia e TLS
- Denial of Service: rate limiting e Fail2ban
- Elevation of Privilege: controle de acesso e RBAC

---

MONITORAMENTO (SOC-LIKE)

- Coleta centralizada de logs
- Deteccao de acessos suspeitos
- Analise de eventos de seguranca
- Base inicial para SIEM
- Identificacao de IPs e padroes de acesso

---

ESTRUTURA DO PROJETO

- `backend/`
- `nginx/`
- `.github/workflows/`
- `docker-compose.yml`
- `README.md`

---

QUICK START

```bash
git clone https://github.com/gustavounreal/certpremium.git
cd certpremium

cp .env.example .env
docker compose up -d

docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
```

---

ACESSO

- API: http://localhost:8000/api/
- Admin: http://localhost:8000/admin/

---

TESTES

No CI, o job de validacao executa `python manage.py check` e lint com Flake8.

---

ROADMAP

- Integracao com SIEM (ELK / Wazuh)
- Alertas automatizados
- Deteccao de anomalias baseada em comportamento
- RBAC avancado
- Simulacao de ataques (red team / blue team scenario)

---

COMPETENCIAS DEMONSTRADAS

- OWASP Top 10
- Secure SDLC
- DevSecOps (CI/CD Security)
- Linux Hardening (CIS baseline)
- Threat Modeling (STRIDE)
- Log Analysis e fundamentos de SOC
- Container Security

---

OBJETIVO

Projeto desenvolvido como portfolio para atuacao nas areas:

- SOC Analyst
- Security Engineer Junior
- DevSecOps Engineer Junior

---

AUTOR

Gustavo Macedo

- GitHub: https://github.com/gustavounreal
- LinkedIn: https://linkedin.com/in/gustavo-r-macedo-225a636a

---

LICENCA

MIT License
