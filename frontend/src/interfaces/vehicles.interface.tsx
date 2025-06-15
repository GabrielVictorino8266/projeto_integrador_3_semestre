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
  status: string;
}

export interface IGetVehiclesResponse {
    items: IVehicle[]
}