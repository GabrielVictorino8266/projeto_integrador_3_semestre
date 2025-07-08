import type { driverRegisterFormSchema } from '@schemas/driverRegisterSchema';
import type { driverUpdateFormSchema } from '@schemas/driverUpdateSchema';
import type { z } from 'zod';

export interface IDriver {
  id: string;
  cpf: string;
  email: string;
  name: string;
  birthYear: string;
  phone: string;
  licenseType: string;
  licenseNumber: string;
  performance: number;
  incidents: {
    id: string;
    type: string;
    date: string;
    description: string;
  }[];
  isActive: boolean;
  type: string;
}

export interface IGetDriversResponse {
  total: number;
  per_page: number;
  current_page: number;
  last_page: number;
  first_page_url: string;
  last_page_url: string;
  next_page_url: string | null;
  prev_page_url: string | null;
  path: string;
  from: number;
  to: number;
  items: Array<IDriver>;
}

export interface ICreateDriverResponse {
  id: string;
  cpf: string;
  name: string;
  birthYear: string;
  phone: string;
  licenseType: string;
  licenseNumber: string;
  performance: number;
  incidents: {
    id: string;
    type: string;
    date: string;
    description: string;
  }[];
  isActive: boolean;
  type: 'Motorista' | 'Administrador';
}

export type ICreateDriverData = z.output<typeof driverRegisterFormSchema>;

export type IUpdateDriverData = z.output<typeof driverUpdateFormSchema>;

export interface IDriverContextProps {
  handleCreateDriver: (newDriverData: ICreateDriverData) => Promise<void>;
  getDriverList: ({
    isActive,
    limit,
    driverName,
    page
  }: IGetDriveParams) => Promise<void>;
  driverList: Array<IDriver>;
  driverQuantity: number;
  driverActive: number;
  driverInactive: number;
  getDriverByID: (id: string) => Promise<void>;
  driverUnderEdition: IDriver | null;
  setDriverUnderEdition: React.Dispatch<React.SetStateAction<IDriver | null>>;
  updateDriver: (id: string, driverData: IUpdateDriverData) => Promise<void>;
  deleteDriver: (id: string) => Promise<void>;
  totalPages: number;
  setTotalPages: React.Dispatch<React.SetStateAction<number>>;
  apiPage: number;
  setApiPage: React.Dispatch<React.SetStateAction<number>>;
  driverName: string;
  setDriverName: React.Dispatch<React.SetStateAction<string>>;
}

export interface IGetDriveParams {
  page?: number;
  limit?: number;
  isActive?: string;
  driverName?: string;
}

export interface IDriverChildrenProps {
  children: React.ReactNode;
}
