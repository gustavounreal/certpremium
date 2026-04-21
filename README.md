<img width="2200" height="464" alt="logo final" src="https://github.com/user-attachments/assets/4c7ec459-2086-4cbf-8f10-b3aa588366bb" />
 # CERTPREMIUM | Portfólio Prático de Cibersegurança

## Qualidade e Segurança

[![CI Security Pipeline](https://github.com/gustavounreal/certpremium/actions/workflows/ci.yml/badge.svg)](https://github.com/gustavounreal/certpremium/actions/workflows/ci.yml)
[![CodeQL](https://github.com/gustavounreal/certpremium/actions/workflows/codeql.yml/badge.svg)](https://github.com/gustavounreal/certpremium/actions/workflows/codeql.yml)

## Licença

![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-red)

## Boas Práticas e Metodologias

![OWASP Top 10](https://img.shields.io/badge/OWASP-Top%2010-blue)
![DevSecOps](https://img.shields.io/badge/DevSecOps-CI%2FCD%20Security-blue)
![Threat Modeling STRIDE](https://img.shields.io/badge/Threat%20Model-STRIDE-blue)

Projeto autoral focado em segurança aplicada, arquitetura real e pipeline DevSecOps.

## Portfólio técnico criado para demonstrar competências reais em AppSec, DevSecOps e monitoramento de segurança.

---

## Highlights

- Backend seguro em Django REST Framework com autenticação JWT e rate limiting.
- Pipeline DevSecOps com Semgrep, Trivy, CodeQL e Dependabot.
- CertMonitor 360: painel interno estilo mini-SIEM com logs e sinais de segurança.
- Logging estruturado em JSON para análise operacional e eventos suspeitos.
- Infraestrutura containerizada com Docker Compose, PostgreSQL e reverse proxy Nginx.
- Proteções alinhadas ao OWASP Top 10 aplicadas ao backend.
- Projeto de portfólio voltado a vagas de SOC, DevSecOps e Segurança da Informação.

---

## Competências Demonstradas

- Detecção de Ameaças
- Gestão de Vulnerabilidades
- Secure SDLC
- Monitoramento de Incidentes
- Automação DevSecOps
- Infraestrutura Segura
  
---

## Sobre o Projeto

Este projeto prático foi desenvolvido para demonstrar competências reais em cibersegurança aplicada, utilizando um ambiente full stack com Django REST Framework, Docker e pipeline CI/CD.

Principais áreas demonstradas:

- Segurança de aplicações web com práticas alinhadas ao OWASP Top 10
- Autenticação segura com JWT e controles de rate limiting
- Monitoramento de eventos e logs estruturados com painel interno CertMonitor 360
- DevSecOps com validações automatizadas (Semgrep, Trivy e CodeQL)
- Infraestrutura containerizada com PostgreSQL, Gunicorn e reverse proxy Nginx

O projeto funciona como um laboratório aplicado de segurança, integrando desenvolvimento seguro, visibilidade operacional e automação de controles.

---

## Arquitetura Técnica

O CertPremium foi estruturado em uma arquitetura modular, simulando componentes comuns de ambientes reais de produção, com separação entre aplicação, banco de dados, proxy reverso e controles de segurança.

### Componentes Principais

- **Frontend Mobile:** Aplicativo em Flutter para consumo de conteúdo técnico e integração com APIs seguras.
- **Backend API:** Django + Django REST Framework com autenticação JWT, rate limiting e rotas administrativas protegidas.
- **Banco de Dados:** PostgreSQL 16 com volume persistente para integridade e continuidade dos dados.
- **Application Server:** Gunicorn para execução do backend em ambiente produtivo.
- **Reverse Proxy:** Nginx Proxy Manager para publicação segura, roteamento e gestão de certificados TLS.
- **Containerização:** Docker Compose para orquestração local e padronização de deploy.

### Fluxo da Arquitetura


<img src="https://github.com/user-attachments/assets/b8868e1d-2bfe-483c-8816-b815ecc6890d" alt="Fluxo da Arquitetura" width="1536" />


### Controles Técnicos Aplicados

- Separação de serviços por containers
- Persistência segura de dados via volumes Docker
- Proxy reverso entre cliente e aplicação
- Rotas administrativas restritas
- Estrutura preparada para logs centralizados
- Base escalável para evolução futura em nuvem

## Tecnologias Utilizadas

* Flutter / Dart
* Python
* Django
* Django REST Framework
* PostgreSQL
* Gunicorn
* Docker Compose
* Nginx Proxy Manager
  
---

## Segurança Implementada

O CertPremium foi desenvolvido com foco em controles reais de segurança aplicados ao ciclo de vida da aplicação, combinando proteção preventiva, monitoramento e validações automatizadas.

### Controles de Aplicação (AppSec)

- Autenticação baseada em JWT utilizando SimpleJWT.
- Rotação de refresh tokens para maior segurança de sessão.
- Rate limiting (throttling) para usuários autenticados e anônimos.
- Rotas administrativas com acesso restrito.
- Serializers e validações no backend para integridade de dados.
- Proteções alinhadas às boas práticas do OWASP Top 10.

### Segurança de Infraestrutura

- Reverse proxy com Nginx Proxy Manager.
- Publicação segura com suporte a TLS/SSL.
- Isolamento de serviços via containers Docker.
- Persistência segregada por volumes dedicados.
- Estrutura preparada para hardening em ambiente Linux.

### Monitoramento e Auditoria

- Logging estruturado em JSON para rastreabilidade.
- Registro de falhas de login via signals do Django.
- Monitoramento de requisições via middleware.
- Identificação de spikes de tráfego e eventos suspeitos.
- Painel interno CertMonitor 360 para visibilidade operacional.

### Segurança no Desenvolvimento (DevSecOps)

- SAST automatizado com Semgrep.
- Code Scanning com CodeQL.
- Scans de dependências e containers com Trivy.
- Dependabot para atualização contínua de dependências.
- Pipeline CI/CD com validações de segurança a cada alteração.

### Abordagem de Segurança

- Segurança integrada desde o desenvolvimento (Shift Left Security).
- Defesa em camadas (Defense in Depth).
- Automação de controles preventivos e detectivos.
- Base preparada para evolução contínua.
  
---

## DevSecOps Pipeline

O CertPremium utiliza um pipeline de integração contínua orientado à segurança, com validações automatizadas a cada commit ou Pull Request. O objetivo é identificar vulnerabilidades cedo no ciclo de desenvolvimento e reduzir riscos antes do deploy.

### Fluxo do Pipeline


<img src="https://github.com/user-attachments/assets/6b05b1bf-84a5-4ddd-ad78-4c097b6fc5a9" alt="Fluxo do Pipeline"  width="1536" />


## VISAO GERAL E SCREENSHOTS

O CertPremium foi concebido como uma plataforma multi-certificação, utilizando o exame CompTIA Security+ (SY0-701) como projeto piloto para demonstrar um ecossistema completo de aprendizado e segurança aplicada.
Abaixo estão os principais fluxos visuais do projeto:
## 1. EXPERIÊNCIA DE APRENDIZADO (Mobile App)

A interface móvel, desenvolvida em Flutter, foi projetada para ser limpa, objetiva e eficiente, facilitando o consumo de conteúdo técnico denso.

---

### Dashboard Intuitivo

Exibe o status do exame, progresso e acesso rápido a estudos e simulados.

<p align="center">
  <img src="https://github.com/user-attachments/assets/3f5745e4-92fc-41bd-8d15-c22e291f6883" alt="Dashboard Principal" width="240"/>
</p>

---

### Organização por Domínios

O conteúdo é categorizado de acordo com os domínios oficiais da CompTIA SY0-701.

<p align="center">
  <img src="https://github.com/user-attachments/assets/cf836f0a-05e9-48ad-b9ea-2427f9d25c90" alt="Visão do Domínio" width="240"/>
</p>

---

### Fluxo de Tópicos

Navegação hierárquica clara de domínios para tópicos e aulas individuais.

<p align="center">
  <img src="https://github.com/user-attachments/assets/f05552ad-6385-457d-a7a1-88e4b0925a3c" alt="Conceitos Gerais" width="240"/>
</p>

---

### Conteúdo Estruturado

As aulas utilizam cards e seções expansíveis ("Tese Central", "Definição Operacional", "Matriz de Decisão") para organizar o conhecimento de forma didática.

<p align="center">
  <img src="https://github.com/user-attachments/assets/6cd7d83f-0afd-45ae-83dc-fcd35e54ada3" alt="Seções da Aula" width="240"/>
</p>

---

### Heurísticas Mentais & Armadilhas

Seções focadas em estratégias de prova e erros comuns, cruciais para a certificação.

<p align="center">
  <img src="https://github.com/user-attachments/assets/a7c9d6bb-a6f3-440d-8b5f-48215defb1d0" alt="Aulas do Tópico" width="240"/>
</p>


## 2. CERTMONITOR 360 (Painel Administrativo / Security Dashboard)

O CertMonitor 360 é o painel administrativo que demonstra competências de defesa, observabilidade e monitoramento de segurança.

Ele fornece uma visão em tempo real da saúde da infraestrutura e dos eventos gerados pelo backend (Nginx + Django).

<p align="center">
  <img src="https://github.com/user-attachments/assets/09404fad-9ef6-464b-abaa-1a82f050075f" alt="Painel CertMonitor 360" width="1020"/>
</p>

---

### Status do Sistema

Monitoramento contínuo de:

- CPU  
- RAM  
- Swap (estado de atenção)  
- Disco  

---

### Alertas Ativos

Notificações em tempo real relacionadas a:

- Anomalias de hardware  
- Uso excessivo de recursos  
- Eventos suspeitos de segurança  

---

### Últimos Eventos & Resumo SIEM

Centralização e análise de logs do ambiente, incluindo:

- Requisições HTTP via Nginx  
- Tentativas de acesso  
- Origem de IPs  
- Eventos relevantes do sistema  

---

### Laboratório de Segurança Aplicado

A integração entre o app de aprendizado e o painel operacional cria um ambiente prático de segurança.

Enquanto o usuário estuda conceitos como:

- CIA Triad  
- Controles de Segurança  
- Hardening  
- Threat Detection  
- Monitoring  

O sistema opera simultaneamente com controles reais de proteção, observabilidade e análise de eventos.

---

==========================
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
### Licença

![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-red)
