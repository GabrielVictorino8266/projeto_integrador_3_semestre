import type { driverRegisterFormSchema } from "@schemas/driverRegisterSchema";
import type { z } from "zod";

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
  password: string; // REMOVER APÓS A RETIRADA DO CAMPO NO RETORNO DA API
  cpf: string;
  email: string; // REMOVER APÓS A RETIRADA DO CAMPO NO RETORNO DA API
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
  type: "Motorista" | "Administrador";
}

export type ICreateDriverData = z.output<typeof driverRegisterFormSchema>;

export interface IDriverContextProps {
  handleCreateDriver: (newDriverData: ICreateDriverData) => Promise<void>;
  getDriverList: () => void;
  driverList: Array<IDriver>;
  driverQuantity: number;
  driverActive: number;
  driverInactive: number;
  getDriverByID: (id: string) => Promise<void>;
  driverUnderEdition: IDriver | null;
  setDriverUnderEdition: React.Dispatch<React.SetStateAction<IDriver | null>>;
  deleteDriver: (id: string) => Promise<void>;
}

export interface IDriverChildrenProps {
  children: React.ReactNode;
}
