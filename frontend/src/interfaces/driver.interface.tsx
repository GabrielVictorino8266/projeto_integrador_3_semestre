import type { IDriverRegisterData } from "@schemas/driverRegisterSchema";

export interface IDriverChildrenProps {
  children: React.ReactNode;
}

export interface IDriverContextProps {
  handleCreateDriver: (newDriverData: IDriverRegisterData) => Promise<void>;
  getDriverList: () => void;
  driverList: IDriverListResponse | [];
  driverQuantity: number;
  driverActive: number;
  driverInactive: number;
}

export interface IDriverList {
  id: string;
  password: string;
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
  createdAt: string;
  updatedAt: string;
}

export type IDriverListResponse = Array<IDriverList>;
