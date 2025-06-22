/* eslint-disable @typescript-eslint/no-unused-vars */
import type { ITripContextProps } from "@interfaces/trips.interface";
import { createContext, type SetStateAction } from "react";

const TripContext = createContext<ITripContextProps>({
  createTrip: function (): Promise<void> {
    throw new Error("Function not implemented.");
  },
});

export { TripContext };
