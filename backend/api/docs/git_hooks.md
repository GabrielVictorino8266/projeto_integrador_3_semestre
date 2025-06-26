# Git Hooks - Verificação de Configuração Docker

Este projeto utiliza um hook do Git para garantir que as configurações do Docker estejam corretas antes de fazer commits.

## O que é um Git Hook?

Um Git Hook é um script que o Git executa automaticamente em determinados momentos do fluxo de trabalho. Neste caso, estamos usando um `pre-commit` hook que é executado antes de cada commit.

## O que este Hook faz?

O hook verifica se as configurações do Docker estão corretas em dois arquivos importantes:

1. `docker-compose.yml`
2. `Dockerfile`

### Verificações no docker-compose.yml:
- O comando automático deve estar descomentado:
  ```yaml
  command: >
    sh -c "python api/manage.py migrate_mongo && python api/manage.py runserver 0.0.0.0:8000"
  ```
- O comando manual deve estar comentado:
  ```yaml
  # command: >
  #   sh -c "python api/manage.py migrate_mongo && tail -f /dev/null"
  ```

### Verificações no Dockerfile:
- O comando automático deve estar descomentado:
  ```dockerfile
  CMD ["sh", "-c", "python api/manage.py migrate_mongo && python api/manage.py runserver 0.0.0.0:8000"]
  ```
- O comando manual deve estar comentado:
  ```dockerfile
  # CMD ["sh", "-c", "python api/manage.py migrate_mongo && python api/manage.py runserver 0.0.0.0:8000"]
  ```

## Como fazer commit agora?

1. Faça as alterações normais no seu código
2. Adicione os arquivos ao staging:
   ```bash
   git add .
   ```
3. Tente fazer o commit:
   ```bash
   git commit -m "sua mensagem de commit"
   ```

## O que acontece se a configuração estiver incorreta?

Se as configurações do Docker estiverem incorretas, o commit será interrompido e você verá uma mensagem de erro indicando exatamente qual arquivo está com problema.

Por exemplo:
- "❌ Erro: O comando automático está comentado ou não existe no docker-compose.yml"
- "❌ Erro: As linhas manuais não estão comentadas no Dockerfile"

## Como corrigir?

1. Verifique a mensagem de erro para saber qual arquivo está com problema
2. Corrija a configuração de acordo com as especificações acima
3. Tente fazer o commit novamente

## Dicas

- Sempre mantenha as configurações consistentes entre docker-compose.yml e Dockerfile
- Use o comando manual apenas para desenvolvimento local
- O comando automático deve ser usado para produção

## Desativando temporariamente o hook

Se precisar desativar temporariamente o hook:
```bash
# Desativar
mv .git/hooks/pre-commit .git/hooks/pre-commit.disabled

# Reativar
mv .git/hooks/pre-commit.disabled .git/hooks/pre-commit
```
