import { createContext } from "react";
import type { IVehicle } from "@interfaces/vehicles.interface";

export interface IVehicleContextProps {
    getVehicleList(): Promise<void>;
    vehicleList: IVehicle[];
    vehicleQuantity: number;
    vehicleActive: number;
    vehicleInactive: number;
}

export const VehicleContext = createContext<IVehicleContextProps>({
  getVehicleList: async () => {
    throw new Error("Function not implemented.");
  },
  vehicleList: [],
  vehicleQuantity: 0,
  vehicleActive: 0,
  vehicleInactive: 0,
});
