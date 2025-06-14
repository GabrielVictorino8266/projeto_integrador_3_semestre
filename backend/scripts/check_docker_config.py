import re
import sys

def check_docker_config():
    # Verifica docker-compose.yml
    with open('docker-compose.yml', 'r') as f:
        content = f.read()
        
        # Verifica se as linhas automáticas estão descomentadas
        automatic_command = re.search(r'command:\s*>\s*sh -c "python api/manage.py migrate_mongo && python api/manage.py runserver 0\.0\.0\.0:8000"', content)
        
        # Verifica se as linhas manuais estão comentadas
        manual_command = re.search(r'#\s*command:\s*>\s*sh -c "python api/manage.py migrate_mongo && tail -f /dev/null"', content)
        manual_command2 = re.search(r'#\s*Command to run Django development server manually', content)
        
        if not automatic_command:
            print("❌ Erro: O comando automático está comentado ou não existe no docker-compose.yml")
            return False
            
        if not manual_command or not manual_command2:
            print("❌ Erro: As linhas manuais não estão comentadas no docker-compose.yml")
            return False

    # Verifica Dockerfile
    with open('Dockerfile', 'r') as f:
        content = f.read()
        
        # Verifica se as linhas automáticas estão descomentadas
        automatic_command = re.search(r'CMD \["sh", "-c", "python api/manage.py migrate_mongo && python api/manage.py runserver 0\.0\.0\.0:8000"\]', content)
        
        # Verifica se as linhas manuais estão comentadas
        manual_command = re.search(r'#\s*CMD \["sh", "-c", "python api/manage.py migrate_mongo && python api/manage.py runserver 0\.0\.0\.0:8000"\]', content)
        
        if not automatic_command:
            print("❌ Erro: O comando automático está comentado ou não existe no Dockerfile")
            return False
            
        if not manual_command:
            print("❌ Erro: As linhas manuais não estão comentadas no Dockerfile")
            return False
            
    print("✅ Configuração do Docker está correta em ambos os arquivos")
    return True

if __name__ == '__main__':
    if not check_docker_config():
        sys.exit(1)
