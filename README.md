# Projeto Integrador - 3º Semestre

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
git clone git@github.com:GabrielVictorino8266/projeto_integrador_3_semestre.git
cd projeto_integrador_3_semestre
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


## ▶️ Iniciar o Frontend

Siga os passos abaixo para rodar a aplicação localmente. 

### ✅ Pré-requisitos

- [Node.js](https://nodejs.org/) instalado

### 📁 Passo a passo

### 1. Navegue até a pasta do frontend
```bash
cd projeto_integrador_3_semestre/frontend
```

### 2. Instale as dependências
```bash
npm install
```

### 3. Inicie o servidor de desenvolvimento
```bash
npm run dev
```

---

## 📚 Documentação

- [Documentação oficial do Django](https://docs.djangoproject.com/pt-br/4.0/)
- [Documentação do Docker](https://docs.docker.com/)

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---


