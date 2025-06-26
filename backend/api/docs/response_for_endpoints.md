# Documentação das Respostas da API

Este documento descreve a estrutura das respostas retornadas pelos endpoints da API.

## Autenticação

### 1. Login
**Endpoint:** `POST /api/login/`

**Resposta de Sucesso (200 OK):**
```json
{
  "access_token": "string",
  "refresh_token": "string",
  "user": {
    "id": "string",
    "name": "string",
    "cpf": "string",
    "type": "string"
  }
}
```

**Resposta de Erro (400 Bad Request):**
```json
{
  "detail": "CPF e Senha são necessários para a requisição"
}
```

**Resposta de Erro (401 Unauthorized):**
```json
{
  "detail": "CPF ou Senha não são válidos, verifique os e tente novamente."
}
```

### 2. Refresh Token
**Endpoint:** `POST /api/refresh/`

**Resposta de Sucesso (200 OK):**
```json
{
  "access_token": "string"
}
```

**Resposta de Erro (400 Bad Request):**
```json
{
  "detail": "Refresh Token é necessário, verifique-o e envie novamente."
}
```

**Resposta de Erro (401 Unauthorized):**
```json
{
  "detail": "Refresh Token é inválido ou está expirado, verifique-o e tente novamente."
}
```

### 3. Logout
**Endpoint:** `POST /api/logout/`

**Resposta de Sucesso (200 OK):**
```json
{
  "detail": "Logout realizado com sucesso."
}
```

### 4. Perfil do Usuário
**Endpoint:** `GET /api/profile/`

**Resposta de Sucesso (200 OK):**
```json
{
  "id": "string",
  "name": "string",
  "cpf": "string",
  "type": "string"
}
```

**Resposta de Erro (401 Unauthorized):**
```json
{
  "detail": "Credenciais de Autenticação não foram providenciadas."
}
```

## Motoristas

### 1. Listar Motoristas
**Endpoint:** `GET /api/drivers/`

**Resposta de Sucesso (200 OK):**
```json
[
  {
    "id": "string",
    "cpf": "string",
    "name": "string",
    "birthYear": "number",
    "phone": "string",
    "licenseType": "string",
    "licenseNumber": "string",
    "performance": "number",
    "incidents": "number",
    "isActive": "boolean",
    "type": "string"
  }
]
```

### 2. Detalhes do Motorista
**Endpoint:** `GET /api/drivers/{id}/`

**Resposta de Sucesso (200 OK):**
```json
{
  "id": "string",
  "cpf": "string",
  "name": "string",
  "birthYear": "number",
  "phone": "string",
  "licenseType": "string",
  "licenseNumber": "string",
  "performance": "number",
  "incidents": "number",
  "isActive": "boolean",
  "type": "string"
}
```

**Resposta de Erro (404 Not Found):**
```json
{
  "detail": "Usuário não encontrado ao tentar recuperar o user_profile."
}
```

## Viagens

### 1. Listar Viagens
**Endpoint:** `GET /api/trips/`

**Resposta de Sucesso (200 OK):**
```json
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": "string",
      "driver": "string",
      "vehicle": "string",
      "startLocation": "string",
      "endLocation": "string",
      "startTime": "string",
      "endTime": "string",
      "status": "string"
    }
  ]
}
```

## Veículos

### 1. Listar Veículos
**Endpoint:** `GET /api/vehicles/`

**Resposta de Sucesso (200 OK):**
```json
[
  {
    "id": "string",
    "plate": "string",
    "model": "string",
    "year": "number",
    "capacity": "number",
    "status": "string",
    "maintenanceDate": "string"
  }
]
```

## Códigos de Status HTTP

- **200 OK**: Requisição bem-sucedida
- **201 Created**: Recurso criado com sucesso
- **400 Bad Request**: Dados inválidos fornecidos
- **401 Unauthorized**: Autenticação necessária
- **403 Forbidden**: Acesso negado
- **404 Not Found**: Recurso não encontrado
- **500 Internal Server Error**: Erro interno do servidor
