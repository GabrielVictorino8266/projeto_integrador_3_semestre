import re
import sys
import io

# Configurar a saída para UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def check_docker_config():
    try:
        # Verifica docker-compose.yml
        with open('docker-compose.yml', 'r') as f:
            content = f.read()
            
            # Verifica se o comando de produção está descomentado
            production_command = re.search(r'^\s*command:\s*>\s*\n\s*sh -c \"python api/manage.py migrate_mongo &&\s*\n\s*python api/manage.py runserver 0\.0\.0\.0:8000\"', content, re.MULTILINE)
            
            # Verifica se o comando de desenvolvimento está comentado
            dev_command = re.search(r'^\s*#\s*command:\s*>\s*\n\s*#\s*sh -c \"python api/manage.py migrate_mongo && tail -f /dev/null\"', content, re.MULTILINE)
            
            if not production_command:
                print("[ERRO] O comando de produção não está configurado corretamente no docker-compose.yml")
                print("  - Verifique se está descomentado e formatado corretamente")
                return False
                
            if not dev_command:
                print("[ERRO] O comando de desenvolvimento não está comentado corretamente no docker-compose.yml")
                print("  - Certifique-se de que a linha 'command:' e o comando 'sh -c...' estão comentados")
                return False

        # Verifica Dockerfile
        with open('Dockerfile', 'r') as f:
            content = f.read()
            
            # Verifica se o comando de produção está descomentado
            production_command = re.search(r'^\s*CMD \["sh", "-c", "python api/manage.py migrate_mongo && python api/manage.py runserver 0\.0\.0\.0:8000"\]', content, re.MULTILINE)
            
            # Verifica se o comando de desenvolvimento está comentado
            dev_command = re.search(r'^\s*#\s*CMD \["sh", "-c", "python api/manage.py migrate_mongo && tail -f /dev/null"\]', content, re.MULTILINE)
            
            if not production_command:
                print("[ERRO] O comando de produção não está configurado corretamente no Dockerfile")
                print("  - Verifique se está descomentado e formatado corretamente")
                return False
                
            if not dev_command:
                print("[ERRO] O comando de desenvolvimento não está comentado corretamente no Dockerfile")
                print("  - Certifique-se de que a linha CMD está comentada")
                return False
                
        print("[OK] Configuração do Docker está correta em ambos os arquivos")
        return True
        
    except FileNotFoundError as e:
        print(f"[ERRO] Arquivo não encontrado - {e}")
        return False
    except Exception as e:
        print(f"[ERRO] Erro ao verificar configurações do Docker: {e}")
        return False

if __name__ == '__main__':
    if not check_docker_config():
        sys.exit(1)
