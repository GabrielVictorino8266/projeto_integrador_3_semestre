import { TripContext } from "@contexts/Trip.context";
import { useContext } from "react";

const useTrip = () => {
  const tripContext = useContext(TripContext);
  return tripContext;
};

export { useTrip };
