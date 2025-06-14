

# Como Executar e Criar Migrações no MongoDB

Este projeto utiliza o pacote [`mongodb-migrations`](https://pypi.org/project/mongodb-migrations/) para gerenciar as migrações do banco de dados **MongoDB** de forma semelhante às migrações do Django.

## Executar Migrações

Para aplicar todas as migrações pendentes no MongoDB, utilize o comando abaixo:

```bash
python manage.py migrate_mongo
```

Esse comando busca os arquivos de migração no diretório padrão (`database/migrations`), verifica o que já foi aplicado e executa apenas as migrações novas ou pendentes.

> Certifique-se de que as variáveis `MONGO_URI` e `MONGO_DB_NAME` estão corretamente configuradas no seu arquivo de ambiente ou nas configurações do Django.

---

## Criar uma Nova Migração

Para criar um novo arquivo de migração, use o seguinte comando, passando uma **descrição resumida** da migração como argumento:

```bash
python manage.py create_migration nome_da_migration
```

* O argumento `nome_da_migration` será usado no nome do arquivo da migração.
* O arquivo será criado automaticamente no diretório `database/migrations` com um nome no formato:

```
<timestamp>_nome_da_migration.py
```

* Dentro do arquivo gerado, você encontrará a estrutura básica com os métodos `upgrade()` e `downgrade()`, que você deve preencher com a lógica necessária para aplicar ou reverter a migração.

### Exemplo de arquivo gerado:

```python
from mongodb_migrations.base import BaseMigration

class Migration(BaseMigration):
    def upgrade(self):
        # Adicione aqui a lógica para aplicar a migração
        pass

    def downgrade(self):
        # Adicione aqui a lógica para reverter a migração
        pass
```
