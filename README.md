<img width="2200" height="464" alt="logo final" src="https://github.com/user-attachments/assets/4c7ec459-2086-4cbf-8f10-b3aa588366bb" />
 # CERTPREMIUM | Portfólio Prático de Cibersegurança

## Qualidade e Segurança

[![CI Security Pipeline](https://github.com/gustavounreal/certpremium/actions/workflows/ci.yml/badge.svg)](https://github.com/gustavounreal/certpremium/actions/workflows/ci.yml)
[![CodeQL](https://github.com/gustavounreal/certpremium/actions/workflows/codeql.yml/badge.svg)](https://github.com/gustavounreal/certpremium/actions/workflows/codeql.yml)

## Licença

![License](https://img.shields.io/badge/License-Source%20Available-orange)

## Boas Práticas e Metodologias

![OWASP Top 10](https://img.shields.io/badge/OWASP-Top%2010-blue)
![DevSecOps](https://img.shields.io/badge/DevSecOps-CI%2FCD%20Security-blue)
![Threat Modeling STRIDE](https://img.shields.io/badge/Threat%20Model-STRIDE-blue)

Projeto autoral focado em segurança aplicada, arquitetura real e pipeline DevSecOps.

## Portfólio técnico criado para demonstrar competências reais em AppSec, DevSecOps e monitoramento de segurança.

## Navegação

- Highlights
- Competências
- Arquitetura Técnica
- Segurança Implementada
- Pipeline
- CertMonitor 360
- Interface do Aplicativo
- Como Executar
- Roadmap
- Sobre o Autor
  
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

---

## CertMonitor 360

O CertMonitor 360 é um painel administrativo interno desenvolvido para demonstrar competências em monitoramento de segurança, observabilidade e análise operacional. A proposta é simular uma visão inicial de SOC (Security Operations Center), utilizando sinais gerados pelo próprio backend.

### Objetivos do Painel

- Centralizar indicadores técnicos e eventos relevantes de segurança.
- Fornecer visibilidade rápida sobre a saúde da aplicação.
- Apoiar identificação inicial de comportamentos anômalos.
- Demonstrar capacidade de logging, métricas e monitoramento aplicado.

### Recursos Implementados

- Status geral da infraestrutura e serviços.
- Registro e contagem de falhas de login.
- Identificação de spikes de requisições.
- Top IPs e principais eventos registrados.
- Leitura de IPs bloqueados (integração best-effort).
- Pontuação heurística de anomalia (0 a 100).
- Logs estruturados em JSON para análise posterior.

### Controles de Acesso

- Acesso restrito a usuários administrativos (staff).
- Rotas protegidas no backend.
- Painel voltado exclusivamente para uso interno.

### Valor Técnico Demonstrado

- Incident Monitoring
- Threat Detection
- Operational Visibility
- Security Logging
- Dashboarding
- Security Analytics

### Demonstração Visual

<p align="center">
  <img src="https://github.com/user-attachments/assets/09404fad-9ef6-464b-abaa-1a82f050075f" alt="Painel CertMonitor 360" width="1020"/>
</p>

### Contexto Profissional

Este módulo foi criado para representar, em escala de portfólio, conceitos utilizados em ambientes de monitoramento de segurança, SIEM e operações SOC.

---

## Interface do Aplicativo

O frontend mobile do CertPremium foi desenvolvido em Flutter com foco em usabilidade, organização de conteúdo técnico e integração com APIs seguras. A proposta é oferecer uma experiência objetiva de estudo, demonstrando também competências práticas em desenvolvimento cross-platform.

### Objetivos da Interface

- Facilitar o consumo de conteúdo técnico denso.
- Organizar trilhas de estudo de forma clara e escalável.
- Integrar autenticação e consumo seguro de APIs.
- Demonstrar arquitetura moderna de frontend mobile.

### Competências Técnicas Demonstradas

- Desenvolvimento Mobile com Flutter / Dart
- Integração com APIs REST
- Navegação estruturada entre módulos
- Interface responsiva
- Componentização de telas
- Estrutura preparada para múltiplas certificações

### Principais Fluxos Visuais

### Dashboard Intuitivo

Exibe progresso de estudos, status do exame e atalhos rápidos para módulos principais.

<p align="center">
  <img src="https://github.com/user-attachments/assets/3f5745e4-92fc-41bd-8d15-c22e291f6883" alt="Dashboard Principal" width="240"/>
</p>

---

### Organização por Domínios

Conteúdo categorizado conforme os domínios oficiais da CompTIA Security+ (SY0-701).

<p align="center">
  <img src="https://github.com/user-attachments/assets/cf836f0a-05e9-48ad-b9ea-2427f9d25c90" alt="Visão por Domínios" width="240"/>
</p>

---

### Fluxo de Tópicos

Navegação hierárquica entre domínios, tópicos e conteúdos específicos.

<p align="center">
  <img src="https://github.com/user-attachments/assets/f05552ad-6385-457d-a7a1-88e4b0925a3c" alt="Fluxo de Tópicos" width="240"/>
</p>

---

### Conteúdo Estruturado

Aulas organizadas em blocos objetivos para acelerar revisão e retenção.

<p align="center">
  <img src="https://github.com/user-attachments/assets/6cd7d83f-0afd-45ae-83dc-fcd35e54ada3" alt="Conteúdo Estruturado" width="240"/>
</p>

---

### Estratégias de Prova e Armadilhas

Seções voltadas para raciocínio prático, pegadinhas comuns e tomada de decisão em prova.

<p align="center">
  <img src="https://github.com/user-attachments/assets/a7c9d6bb-a6f3-440d-8b5f-48215defb1d0" alt="Estratégias de Prova" width="240"/>
</p>

### Valor Estratégico do Projeto

Além da camada de segurança, o frontend demonstra capacidade de entrega completa de produto, integrando experiência do usuário, backend seguro e arquitetura escalável.

---

## Como Executar o Projeto

O CertPremium pode ser executado localmente utilizando Docker Compose, replicando a arquitetura principal do ambiente de desenvolvimento com backend Django, banco PostgreSQL e reverse proxy.

### Pré-requisitos

- Docker instalado
- Docker Compose habilitado
- Git instalado

### 1. Clonar o Repositório

```
git clone https://github.com/gustavounreal/certpremium.git
cd certpremium
```
### 2. Subir os Containers

```
docker compose up --build
```
Esse comando irá iniciar os principais serviços:

- db → PostgreSQL
- backend → Django + Gunicorn
- nginx → Reverse Proxy

### 3. Aplicar Migrações

Em outro terminal:

```
docker compose exec backend python manage.py migrate
```
### 4. Criar Usuário Administrativo

```
docker compose exec backend python manage.py createsuperuser
```
### 5. Acessar o Ambiente

Após a inicialização, os principais endpoints estarão disponíveis:

- Aplicação Web / Proxy: http://localhost
- Django Admin: http://localhost/admin
- CertMonitor 360: http://localhost/api/v1/dashboard/

### Comandos Úteis

Parar containers

```
docker compose down
```

### Reconstruir ambiente

```
docker compose up --build --force-recreate
```

### Ver logs em tempo real

```
docker compose logs -f
```
### Observações Técnicas
- O projeto utiliza containers independentes para aplicação, banco e proxy.
- Volumes persistentes são utilizados para retenção de dados.
- Variáveis de ambiente podem ser ajustadas conforme necessidade local.
- O CertMonitor 360 requer usuário com privilégios administrativos.

  ---

  ## Estrutura do Repositório

O projeto foi organizado de forma modular para separar responsabilidades entre aplicação, infraestrutura, automação e documentação técnica.

```text

certpremium/
├── backend/                 # Backend Django + Django REST Framework
│   ├── certpremium/         # Configurações principais do projeto
│   ├── core/                # Views, APIs, templates e lógica principal
│   ├── manage.py
│   └── Dockerfile
│
├── nginx/                   # Dados e volumes do Nginx Proxy Manager
│
├── .github/
│   └── workflows/           # Pipelines CI/CD e Code Scanning
│       ├── ci.yml
│       └── codeql.yml
│
├── docker-compose.yml       # Orquestração dos serviços
├── requirements.txt         # Dependências Python (quando aplicável)
├── README.md                # Documentação principal
└── LICENSE                  # Termos de uso e licença
```
### Organização por Camadas

 - Aplicação: Backend Django/DRF e frontend mobile (Flutter em evolução/integrado separadamente).
 - Infraestrutura: Docker Compose, PostgreSQL e reverse proxy Nginx.
 - Segurança: Pipelines automatizados, scanners e controles de acesso.
 - Observabilidade: CertMonitor 360, logs estruturados e sinais operacionais.
 - Documentação: README e materiais técnicos de apoio.
   
### Benefícios da Estrutura

 - Separação clara de responsabilidades.
 - Facilidade de manutenção e escalabilidade.
 - Evolução incremental por módulos.
 - Ambiente preparado para práticas profissionais de desenvolvimento seguro.

---

## Roadmap

O CertPremium segue uma evolução contínua orientada a segurança aplicada, qualidade de software e maturidade operacional.

### Curto Prazo

- Ampliação da integração entre frontend Flutter e backend Django REST Framework.
- Refinamento visual e funcional do CertMonitor 360.
- Melhoria da cobertura de logs e eventos operacionais.
- Otimizações de performance e usabilidade da aplicação.

### Segurança e DevSecOps

- Evolução das políticas de security gates no CI/CD.
- Expansão das regras SAST e quality checks.
- Testes automatizados integrados ao pipeline.
- Hardening adicional dos ambientes de execução.
- Melhor gestão de segredos e variáveis sensíveis.

### Monitoramento e Observabilidade

- Novos indicadores operacionais no CertMonitor 360.
- Health checks dedicados para serviços críticos.
- Alertas baseados em comportamento anômalo.
- Métricas históricas e tendências de eventos.

### Produto e Escalabilidade

- Estrutura preparada para múltiplas certificações além da Security+.
- Evolução da arquitetura para novos módulos educacionais.
- Escalabilidade para novos usuários e novos conteúdos.
- Melhorias contínuas na experiência mobile.

### Visão de Longo Prazo

- Consolidar o projeto como portfólio técnico de referência em cibersegurança aplicada.
- Evoluir para plataforma comercial de educação em segurança digital.
- Demonstrar competências reais em AppSec, SOC e DevSecOps em ambiente público.

---

## Lições Técnicas / Desafios Resolvidos

Durante o desenvolvimento do CertPremium, diversos desafios reais de arquitetura, segurança e operação foram tratados na prática, contribuindo para a evolução técnica do projeto.

### Arquitetura e Infraestrutura

- Estruturação de ambiente containerizado com múltiplos serviços integrados.
- Comunicação entre containers de aplicação, banco de dados e proxy reverso.
- Persistência de dados com volumes dedicados.
- Padronização de ambiente para desenvolvimento e execução local.

### Backend e Segurança

- Implementação de autenticação segura com JWT.
- Aplicação de rate limiting para mitigação de abuso de requisições.
- Restrição de acesso a rotas administrativas.
- Organização do backend para crescimento modular e manutenção contínua.

### Monitoramento e Observabilidade

- Criação de logging estruturado em JSON para rastreabilidade.
- Captura de falhas de login e eventos relevantes.
- Identificação de spikes de requisições e padrões suspeitos.
- Construção do CertMonitor 360 como painel interno de visibilidade operacional.

### DevSecOps

- Integração de pipeline CI/CD com validações automáticas.
- Uso combinado de Semgrep, Trivy e CodeQL.
- Geração de evidências de segurança no GitHub Security Tab.
- Automação de verificações repetitivas para reduzir risco operacional.

### Aprendizados Estratégicos

- Segurança deve ser incorporada desde o início do projeto.
- Observabilidade reduz tempo de diagnóstico e resposta.
- Automação aumenta consistência e confiabilidade.
- Documentação clara acelera manutenção e evolução técnica.
- Projetos públicos podem funcionar como prova prática de competência profissional.

---


## Sobre o Autor

Profissional de TI com foco em cibersegurança aplicada, desenvolvimento seguro e automação.

### Contato Profissional

Gustavo R Macedo

- GitHub: https://github.com/gustavounreal
- LinkedIn: https://linkedin.com/in/gustavo-r-macedo-225a636a

---

## Licença

Copyright © 2026 Gustavo Ribeiro. Todos os direitos reservados.

Este repositório é disponibilizado publicamente para fins de portfólio, demonstração técnica, estudo individual e avaliação profissional.

É permitido:

- Visualizar o código-fonte publicamente no GitHub.
- Clonar e executar localmente para testes, aprendizado e análise técnica.
- Utilizar como referência educacional sem redistribuição.

Não é permitido:

- Copiar integral ou parcialmente este projeto para fins comerciais.
- Revender, sublicenciar ou redistribuir o código-fonte.
- Publicar versões derivadas como produto próprio.
- Utilizar marca, identidade visual, nome CertPremium ou materiais relacionados.
- Hospedar versões públicas ou privadas com finalidade comercial.

Para parcerias, licenciamento ou uso autorizado, entre em contato.

