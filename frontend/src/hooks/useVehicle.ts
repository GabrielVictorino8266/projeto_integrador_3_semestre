import { useContext } from "react";
import { VehicleContext } from "@contexts/vehicles.context";

export const useVehicle = () => useContext(VehicleContext);
