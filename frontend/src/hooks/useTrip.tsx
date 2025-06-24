import { TripContext } from "@contexts/trip.context";
import { useContext } from "react";

const useTrip = () => {
  const tripContext = useContext(TripContext);
  return tripContext;
};

export { useTrip };
