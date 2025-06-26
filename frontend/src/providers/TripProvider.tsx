import { TripContext } from "@contexts/trip.context";
import type { IDefaultChildrenProp } from "@interfaces/default.interface";
import type {
  ICreateTripRequest,
  ICreateTripResponse,
  IGetTripResponse,
} from "@interfaces/trips.interface";
import { api } from "@services/api";
import type { AxiosResponse } from "axios";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";

const TripProvider = ({ children }: IDefaultChildrenProp) => {
  const navigate = useNavigate();

  const [tripUnderEdition, setTripUnderEdition] =
    useState<IGetTripResponse | null>(null);

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

  const getTripByID = async (id: string) => {
    try {
      const getTripResponse: AxiosResponse<IGetTripResponse> = await api.get(
        `/trips/list/${id}`
      );

      if (getTripResponse.status === 200) {
        const tripFound: IGetTripResponse = getTripResponse.data;
        // toast.success("Viagem encontrada!");
        setTripUnderEdition(tripFound);
      }
    } catch (error) {
      toast.error("Viagem não encontrada");
      console.log(error);
      navigate("/dashboard/viagens");
    }
  };

  const updateTrip = async (id: string, updateTripData: ICreateTripRequest) => {
    try {
      const updateTripResponse: AxiosResponse<ICreateTripResponse> =
        await api.put(`/trips/update/${id}`, updateTripData);

      if (updateTripResponse.status === 200) {
        toast.success("Viagem atualizada com sucesso!");
        navigate("/dashboard/viagens");
      }
    } catch (error) {
      toast.error("Erro ao criar viagem");
      console.log(error);
    }
  };

  return (
    <TripContext.Provider
      value={{
        createTrip,
        getTripByID,
        updateTrip,
        tripUnderEdition,
        setTripUnderEdition,
      }}
    >
      {children}
    </TripContext.Provider>
  );
};

export { TripProvider };
