/* eslint-disable @typescript-eslint/no-unused-vars */
import type {
  ICreateTripRequest,
  ITripContextProps,
} from "@interfaces/trips.interface";
import { createContext } from "react";

const TripContext = createContext<ITripContextProps>({
  createTrip: function (_createTripData: ICreateTripRequest): Promise<void> {
    throw new Error("Function not implemented.");
  },
});

export { TripContext };
