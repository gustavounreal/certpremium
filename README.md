<img width="2210" height="464" alt="logoColorido" src="https://github.com/user-attachments/assets/41ec751b-389f-4e1d-a3c0-806ac0ca4670" />

 ### CERTPREMIUM | Portfólio Prático de Cibersegurança
 Disponível para oportunidades em Cybersecurity | AppSec | DevSecOps | SOC

Projeto autoral focado em:

- AppSec
- DevSecOps
- Monitoramento
- APIs Seguras
- Docker Infrastructure

### Qualidade e Segurança
[![CI Security Pipeline](https://github.com/gustavounreal/certpremium/actions/workflows/ci.yml/badge.svg)](https://github.com/gustavounreal/certpremium/actions/workflows/ci.yml)
[![CodeQL](https://github.com/gustavounreal/certpremium/actions/workflows/codeql.yml/badge.svg)](https://github.com/gustavounreal/certpremium/actions/workflows/codeql.yml)
### Boas Práticas e Metodologias
![OWASP Top 10](https://img.shields.io/badge/OWASP-Top%2010-blue)
![DevSecOps](https://img.shields.io/badge/DevSecOps-CI%2FCD%20Security-blue)
![Threat Modeling STRIDE](https://img.shields.io/badge/Threat%20Model-STRIDE-blue)
### Licença
![License](https://img.shields.io/badge/License-Source%20Available-orange)


### Portfólio técnico criado para demonstrar competências em AppSec, DevSecOps e monitoramento de segurança.

<p align="center">
<img src="https://github.com/user-attachments/assets/70dc5313-f9cf-48b8-a71b-74a18facfa8c"  alt="mobile+certmonitor" width="720"/>
</p>

### Navegação

- [Highlights](#highlights)
- [Competências Demonstradas](#competencias-demonstradas)
- [Arquitetura Técnica](#arquitetura-tecnica)
- [Segurança Implementada](#seguranca-implementada)
- [DevSecOps Pipeline](#devsecops-pipeline)
- [CertMonitor 360](#certmonitor-360)
- [Interface do Aplicativo](#interface-do-aplicativo)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Roadmap](#roadmap)
- [Sobre o Autor](#sobre-o-autor)

---

## Highlights

- API segura em Django REST Framework com JWT, permissões e rate limiting.
- Pipeline CI/CD com validações de segurança automatizadas.
- Dashboard interno de monitoramento e eventos (CertMonitor 360).
- Logging estruturado para auditoria e análise operacional.
- Ambiente real com Docker, PostgreSQL e reverse proxy Nginx.
- Práticas alinhadas ao OWASP Top 10 e Secure SDLC.
- Portfólio técnico voltado a AppSec, SOC e DevSecOps.

  
## Competências Demonstradas

- Application Security (AppSec)
- DevSecOps
- Gestão de Vulnerabilidades
- Monitoramento de Segurança
- Incident Response Fundamentals
- Secure SDLC
- Infraestrutura Segura
- APIs REST Seguras
  
---

### Sobre o Projeto

O CertPremium é um laboratório prático de cibersegurança aplicado a um ambiente realista de desenvolvimento.

O projeto integra:

- API segura em Django REST Framework
- Pipeline CI/CD com scanners automatizados
- Monitoramento interno com CertMonitor 360
- Infraestrutura containerizada com Docker e PostgreSQL

Objetivo: demonstrar capacidade técnica em AppSec, DevSecOps e operações de segurança.

---
## Arquitetura Técnica

O CertPremium utiliza arquitetura modular baseada em múltiplos serviços, separando aplicação, banco de dados, proxy reverso e controles de segurança.

<p align="center">
  <img src="https://github.com/user-attachments/assets/b8868e1d-2bfe-483c-8816-b815ecc6890d" alt="Fluxo da Arquitetura" width="1536" />
</p>

### Componentes Principais

- **Frontend Mobile:** Aplicativo Flutter integrado a APIs seguras.
- **Backend API:** Django REST Framework com JWT, permissões e rate limiting.
- **Banco de Dados:** PostgreSQL 16 com persistência em volume dedicado.
- **Application Server:** Gunicorn para execução em ambiente produtivo.
- **Reverse Proxy:** Nginx Proxy Manager com roteamento e TLS.
- **Containerização:** Docker Compose para padronização e orquestração local.

### Security by Design (STRIDE)

Controles aplicados com base em modelagem de ameaças:

- **Spoofing:** autenticação JWT e rotas protegidas
- **Tampering:** validações backend e serializers
- **Repudiation:** logs estruturados e trilhas de eventos
- **Information Disclosure:** segregação de acesso administrativo
- **Denial of Service:** throttling e rate limiting
- **Elevation of Privilege:** permissões restritas e áreas staff-only

### Controles Técnicos Aplicados

- Separação de serviços por containers
- Persistência segura de dados via volumes Docker
- Proxy reverso entre cliente e aplicação
- Rotas administrativas restritas
- Estrutura preparada para logs centralizados
- Base escalável para evolução futura em nuvem

## Tecnologias Utilizadas

**Backend**
- Python
- Django
- Django REST Framework

**Frontend**
- Flutter / Dart

**Infraestrutura**
- PostgreSQL
- Gunicorn
- Docker Compose
- Nginx Proxy Manager

**Segurança**
- JWT
- Semgrep
- Trivy
- CodeQL
---
## DevSecOps Pipeline

O CertPremium possui pipeline CI/CD orientado à segurança, executando validações automáticas a cada commit ou Pull Request.

Objetivo: detectar riscos cedo no ciclo de desenvolvimento e reduzir exposição antes do deploy.

### Security Checks Automatizados

- SAST com Semgrep
- Code Scanning com CodeQL
- Scan de dependências com Trivy
- Scan de containers com Trivy
- Dependabot para atualização contínua

### Fluxo do Pipeline

<p align="center">
  <img src="https://github.com/user-attachments/assets/6b05b1bf-84a5-4ddd-ad78-4c097b6fc5a9" alt="Fluxo do Pipeline" width="1536" />
</p>

### Evidências de Execução

<p align="center">
 <img src="https://github.com/user-attachments/assets/3b88bb40-6d06-4ef6-a728-89133a428fe8"  alt="Evidências do Pipeline" width="1536"  />
</p>

### Benefícios Demonstrados

- Automação de controles de segurança
- Validação contínua de código
- Redução de falhas manuais
- Segurança integrada ao CI/CD
- Maior maturidade de desenvolvimento seguro

## CertMonitor 360

O CertMonitor 360 é um painel administrativo interno criado para demonstrar competências em monitoramento de segurança, observabilidade e análise operacional.

Inspirado em conceitos utilizados em ambientes SOC, o módulo consolida sinais gerados pelo backend e oferece visão rápida da saúde da aplicação.

### Demonstração Visual

<p align="center">
  <img src="https://github.com/user-attachments/assets/09404fad-9ef6-464b-abaa-1a82f050075f" alt="Painel CertMonitor 360" width="1020"/>
</p>

### Objetivos

- Centralizar indicadores técnicos e eventos relevantes
- Fornecer visibilidade operacional rápida
- Apoiar identificação inicial de comportamentos anômalos
- Demonstrar logging, métricas e monitoramento aplicado

### Recursos Implementados

- Status geral da infraestrutura e serviços
- Contagem de falhas de login
- Identificação de spikes de requisições
- Top IPs e eventos registrados
- Consulta de IPs bloqueados
- Pontuação heurística de anomalia (0 a 100)
- Logs estruturados em JSON

### Controles de Acesso

- Acesso restrito a usuários administrativos
- Rotas protegidas no backend
- Uso exclusivamente interno

### Competências Demonstradas

- Incident Monitoring
- Threat Detection
- Security Logging
- Operational Visibility
- Dashboarding
- Security Analytics

## Interface do Aplicativo

O frontend mobile foi desenvolvido em Flutter, integrando experiência do usuário, organização de conteúdo técnico e consumo seguro de APIs.

Demonstra capacidade de entrega full stack, conectando aplicação mobile a backend seguro.

### Competências Demonstradas

- Flutter / Dart
- Integração com APIs REST
- Autenticação e consumo seguro de endpoints
- Navegação estruturada
- Interface responsiva
- Componentização de telas

### Visão Geral

<p align="center">
  <img  src="https://github.com/user-attachments/assets/d4bbe300-225e-4335-b64c-79792870d6ab" alt="Interface do Aplicativo CertPremium" width="620" />
</p>


### Funcionalidades Principais

- Dashboard com progresso e atalhos rápidos
- Navegação por domínios da certificação
- Conteúdo organizado por tópicos
- Trilhas objetivas de revisão
- Estrutura preparada para expansão futura


## Como Executar

Execute localmente com Docker Compose.

### Pré-requisitos

* Docker
* Docker Compose
* Git

### 1. Clonar repositório

```bash
git clone https://github.com/gustavounreal/certpremium.git
cd certpremium
```

### 2. Iniciar ambiente

```bash
docker compose up --build
```

Serviços iniciados:

* db → PostgreSQL
* backend → Django + Gunicorn
* nginx → Reverse Proxy

### 3. Aplicar migrações

```bash
docker compose exec backend python manage.py migrate
```

### 4. Criar usuário administrador

```bash
docker compose exec backend python manage.py createsuperuser
```

### 5. Acessar

* Aplicação: http://localhost
* Admin: http://localhost/admin
* CertMonitor 360: http://localhost/api/v1/dashboard/

### Comandos úteis

Parar ambiente:

```bash
docker compose down
```

Recriar containers:

```bash
docker compose up --build --force-recreate
```

Ver logs:

```bash
docker compose logs -f
```

### Observações

* O dashboard requer usuário administrador.
* Dados persistem em volumes Docker.
* Variáveis de ambiente podem ser ajustadas localmente.

---

## Estrutura do Repositório

```text
certpremium/
├── backend/              # Django + DRF
├── nginx/                # Proxy reverso
├── .github/workflows/    # CI/CD e Code Scanning
├── docker-compose.yml
├── README.md
└── LICENSE
```

### Organização

* Aplicação: backend Django/DRF e frontend mobile
* Infraestrutura: Docker, PostgreSQL e Nginx
* Segurança: scanners, pipelines e controles de acesso
* Observabilidade: CertMonitor 360 e logs estruturados

---

## Roadmap

* Evoluir integração Flutter + backend
* Expandir regras de segurança no CI/CD
* Melhorar métricas e alertas no CertMonitor 360
* Aumentar cobertura de testes
* Hardening adicional da infraestrutura
* Escalar para novos módulos e conteúdos

---

## Lições Técnicas

* Segurança integrada desde o início do projeto
* Automação reduz falhas operacionais
* Observabilidade acelera diagnóstico
* Arquitetura modular facilita evolução
* Projeto público como prova prática de competência

---

## Sobre o Autor

Gustavo R Macedo
---
Profissional de TI com foco em cibersegurança aplicada, desenvolvimento seguro e automação.

* GitHub: https://github.com/gustavounreal
* LinkedIn: https://linkedin.com/in/gustavo-r-macedo-225a636a

---

## Licença

Copyright © 2026 Gustavo Ribeiro.

Uso permitido para estudo, análise técnica e portfólio.
Redistribuição comercial ou reutilização integral do projeto não autorizadas.

---

Se este projeto foi útil, considere deixar uma estrela no repositório.

