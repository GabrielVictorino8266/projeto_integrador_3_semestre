# Conexão com MongoDB via MongoDB Compass

## Configurações do Docker Compose

No arquivo `docker-compose.yml`, o MongoDB está configurado para expor a porta **27018**:

```yaml
mongodb:
  image: mongo:latest
  ports:
    - "27018:27017"
```

## Conectando via MongoDB Compass

1. Abra o **MongoDB Compass**.
2. No campo de conexão, use:
   - **Host**: `localhost`
   - **Porta**: `27018`
   - **URL completa**: `mongodb://localhost:27018`
3. Clique em **"Connect"**.

## Verificando a Conexão

Após a conexão, você verá:

- O banco de dados configurado na variável `MONGO_DB_NAME`.
- As coleções criadas pelo sistema:
  - `users`
  - `refresh_tokens`
  - `token_blacklist`
  - `vehicle`

## Dicas de Uso

- Para ver os dados dos usuários, acesse a coleção `users`.
- Para visualizar os dados em formato mais amigável, use o recurso **"View as Table"**.
- Para fazer buscas específicas, utilize o campo de **filtro** no topo da coleção.

## Problemas Comuns

Se encontrar problemas de conexão:

- Verifique se o container do MongoDB está rodando.
- Confirme se o MongoDB Compass está usando a **porta correta (27018)**.
- Certifique-se de que **nenhum outro serviço** está usando a porta 27018.

## Comandos Úteis

Para verificar o status dos containers:

```bash
docker compose ps
```

Para reiniciar o MongoDB:

```bash
docker compose restart mongodb
```

Para ver os logs do MongoDB:

```bash
docker compose logs mongodb
```

---

> Este guia assume que você está usando o MongoDB Compass para visualizar os dados do MongoDB rodando dentro do Docker.  
> Versão do MongoDB Compass: 1.46.3
> O MongoDB Compass é uma ferramenta gráfica que facilita a visualização e manipulação de dados do MongoDB.
