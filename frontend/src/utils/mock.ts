const driversMockList = [
  {
    id: "drv_001",
    password: "SenhaForte!1",
    cpf: "123.456.789-00",
    email: "joao.silva@email.com",
    name: "João da Silva",
    birthYear: "1985-07-14",
    phone: "+55 11 91234-5678",
    licenseType: "B",
    licenseNumber: "ABC1234567",
    performance: 88,
    incidents: [],
    isActive: true,
    type: "driver",
    createdAt: "2022-10-01T12:00:00Z",
    updatedAt: "2025-06-09T09:30:00Z"
  },
  {
    id: "drv_002",
    password: "Segura123!",
    cpf: "987.654.321-00",
    email: "maria.lima@email.com",
    name: "Maria Lima",
    birthYear: "1990-05-22",
    phone: "+55 21 98765-4321",
    licenseType: "C",
    licenseNumber: "XYZ9876543",
    performance: 92,
    incidents: [
      {
        id: "inc_001",
        type: "infração",
        date: "2023-08-10T14:00:00Z",
        description: "Estacionamento irregular"
      }
    ],
    isActive: true,
    type: "driver",
    createdAt: "2023-01-15T09:00:00Z",
    updatedAt: "2025-06-08T15:45:00Z"
  },
  {
    id: "drv_003",
    password: "Abc#123456",
    cpf: "321.654.987-00",
    email: "carlos.pereira@email.com",
    name: "Carlos Pereira",
    birthYear: "1980-03-30",
    phone: "+55 31 99876-5432",
    licenseType: "D",
    licenseNumber: "LMN3217890",
    performance: 79,
    incidents: [],
    isActive: false,
    type: "driver",
    createdAt: "2021-07-19T10:30:00Z",
    updatedAt: "2024-12-01T11:20:00Z"
  },
  {
    id: "drv_004",
    password: "Senha@123",
    cpf: "456.123.789-00",
    email: "ana.souza@email.com",
    name: "Ana Souza",
    birthYear: "1995-11-11",
    phone: "+55 41 92345-6789",
    licenseType: "B",
    licenseNumber: "BCD4561239",
    performance: 85,
    incidents: [
      {
        id: "inc_002",
        type: "acidente",
        date: "2022-12-05T18:15:00Z",
        description: "Batida em via expressa"
      }
    ],
    isActive: true,
    type: "driver",
    createdAt: "2022-04-22T08:00:00Z",
    updatedAt: "2025-04-10T14:30:00Z"
  },
  {
    id: "drv_005",
    password: "123Senha!",
    cpf: "654.321.987-00",
    email: "roberto.melo@email.com",
    name: "Roberto Melo",
    birthYear: "1975-09-08",
    phone: "+55 51 93456-7810",
    licenseType: "E",
    licenseNumber: "EFG7654321",
    performance: 93,
    incidents: [],
    isActive: true,
    type: "driver",
    createdAt: "2020-02-14T11:45:00Z",
    updatedAt: "2025-05-09T16:10:00Z"
  },
  {
    id: "drv_006",
    password: "Senha123@",
    cpf: "789.123.456-00",
    email: "juliana.oliveira@email.com",
    name: "Juliana Oliveira",
    birthYear: "1993-06-17",
    phone: "+55 61 95678-4321",
    licenseType: "C",
    licenseNumber: "HIJ4321567",
    performance: 87,
    incidents: [
      {
        id: "inc_003",
        type: "infração",
        date: "2024-03-21T09:30:00Z",
        description: "Uso de celular ao volante"
      }
    ],
    isActive: true,
    type: "driver",
    createdAt: "2023-05-01T10:10:00Z",
    updatedAt: "2025-06-01T12:00:00Z"
  },
  {
    id: "drv_007",
    password: "Drive@2024",
    cpf: "147.258.369-00",
    email: "fernando.alves@email.com",
    name: "Fernando Alves",
    birthYear: "1988-12-05",
    phone: "+55 62 96789-1234",
    licenseType: "D",
    licenseNumber: "JKL6547893",
    performance: 90,
    incidents: [],
    isActive: false,
    type: "driver",
    createdAt: "2021-09-30T13:20:00Z",
    updatedAt: "2025-01-01T10:00:00Z"
  },
  {
    id: "drv_008",
    password: "SenhaSegura@!",
    cpf: "852.963.741-00",
    email: "camila.santos@email.com",
    name: "Camila Santos",
    birthYear: "1992-02-14",
    phone: "+55 71 97890-6543",
    licenseType: "B",
    licenseNumber: "MNO5678432",
    performance: 95,
    incidents: [],
    isActive: true,
    type: "driver",
    createdAt: "2023-03-12T15:00:00Z",
    updatedAt: "2025-06-05T17:30:00Z"
  },
  {
    id: "drv_009",
    password: "Teste@123",
    cpf: "963.852.741-00",
    email: "lucas.ferreira@email.com",
    name: "Lucas Ferreira",
    birthYear: "1997-10-09",
    phone: "+55 81 91234-8765",
    licenseType: "C",
    licenseNumber: "PQR9081723",
    performance: 82,
    incidents: [
      {
        id: "inc_004",
        type: "acidente",
        date: "2023-09-12T07:45:00Z",
        description: "Colisão com ciclista"
      }
    ],
    isActive: true,
    type: "driver",
    createdAt: "2023-07-20T08:45:00Z",
    updatedAt: "2025-06-09T11:00:00Z"
  },
  {
    id: "drv_010",
    password: "SuperSenha!2",
    cpf: "741.852.963-00",
    email: "renata.costa@email.com",
    name: "Renata Costa",
    birthYear: "1983-04-01",
    phone: "+55 91 97654-3210",
    licenseType: "D",
    licenseNumber: "STU1234569",
    performance: 89,
    incidents: [],
    isActive: false,
    type: "driver",
    createdAt: "2020-11-05T16:10:00Z",
    updatedAt: "2024-12-20T13:50:00Z"
  }
];

export {driversMockList}