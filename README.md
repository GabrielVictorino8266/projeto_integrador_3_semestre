# Projeto Integrador - 3º Semestre

Uma aplicação Django desenvolvida como parte do Projeto Integrador do 3º semestre. Este projeto visa [descreva brevemente o propósito ou objetivo principal da aplicação, por exemplo: "gerenciar tarefas acadêmicas", "automatizar processos de matrícula", etc.].

---

## 🚀 Começando

### Pré-requisitos

- [Docker](https://www.docker.com/get-started) (versão 20.10 ou superior)
- [Docker Compose](https://docs.docker.com/compose/install/) (versão 2.0 ou superior)
- Python 3.11+ (opcional, apenas para desenvolvimento fora do container)

---

## 📥 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```

---

## 🐳 Execução com Docker

### ▶️ Iniciar o Backend

#### Configuração para Desenvolvimento

Se desejar iniciar o desenvolvimento, siga estes passos:

1. Acesse `backend/docker-compose.yml`
    - Comente a linha: `command: python api/manage.py runserver 0.0.0.0:8000`
    - Descomente a linha: `# command: tail -f /dev/null`
2. Acesse `backend/Dockerfile`
    - Comente a linha: `CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]`
    - Descomente a linha: `# CMD ["tail", "-f", "/dev/null"]`

#### Build e Inicialização dos Containers

Execute o comando abaixo para construir as imagens e iniciar os containers:

```bash
docker-compose up --build
```

---

## 📚 Documentação

- [Documentação oficial do Django](https://docs.djangoproject.com/pt-br/4.0/)
- [Documentação do Docker](https://docs.docker.com/)

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---


