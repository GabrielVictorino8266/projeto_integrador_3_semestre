/* eslint-disable @typescript-eslint/no-unused-vars */
import type {
  ICreateTripRequest,
  IGetTripResponse,
  ITripContextProps,
} from "@interfaces/trips.interface";
import { createContext, type SetStateAction } from "react";

const TripContext = createContext<ITripContextProps>({
  createTrip: function (_createTripData: ICreateTripRequest): Promise<void> {
    throw new Error("Function not implemented.");
  },

  getTripByID: function (_id: string): Promise<void> {
    throw new Error("Function not implemented.");
  },

  tripUnderEdition: null,

  setTripUnderEdition: function (
    _value: SetStateAction<IGetTripResponse | null>
  ): void {
    throw new Error("Function not implemented.");
  },
  updateTrip: function (
    _id: string,
    _updateTripData: ICreateTripRequest
  ): Promise<void> {
    throw new Error("Function not implemented.");
  },
});

export { TripContext };
