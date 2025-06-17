export interface IVehicle {
  id: string;
  vehicleNumber: string;
  licensePlate: string;
  vehicleType: string;
  manufacturingYear: number;
  brand: string;
  currentKm: number;
  warningKmLimit: number;
  deletedAt?: string | null;
  status: VehicleStatus;
}

export interface IGetVehiclesResponse {
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
  items: IVehicle[];
}

export type VehicleStatus = ""| "active" | "indisponivel" | "maintenance";
