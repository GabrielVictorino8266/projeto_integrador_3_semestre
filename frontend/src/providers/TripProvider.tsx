import { TripContext } from "@contexts/trip.context";
import type { IDefaultChildrenProp } from "@interfaces/default.interface";
import type {
  ICreateTripRequest,
  ICreateTripResponse,
} from "@interfaces/trips.interface";
import { api } from "@services/api";
import type { AxiosResponse } from "axios";
import { toast } from "react-toastify";

const TripProvider = ({ children }: IDefaultChildrenProp) => {
  const createTrip = async (createTripData: ICreateTripRequest) => {
    try {
      const createTripResponse: AxiosResponse<ICreateTripResponse> =
        await api.post("/trips/create", createTripData);

      if (createTripResponse.status === 201) {
        toast.success("Viagem criada com sucesso!");
      }
    } catch (error) {
      toast.error("Erro ao criar viagem");
      console.log(error);
    }
  };
  return (
    <TripContext.Provider value={{ createTrip }}>
      {children}
    </TripContext.Provider>
  );
};

export { TripProvider };
