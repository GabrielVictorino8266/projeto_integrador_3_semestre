import type { IDefaultChildrenProp } from "../interfaces";
import type { AxiosResponse } from "axios";
import { api } from "@services/api";
import { toast } from "react-toastify";
import { DriverContext } from "@contexts/driver.context";
import { useState } from "react";
import {
  type ICreateDriverData,
  type ICreateDriverResponse,
  type IDriver,
  type IGetDriversResponse,
  type IUpdateDriverData,
} from "@interfaces/driver.interface";
import { useModal } from "@hooks/useModal";
import { useNavigate } from "react-router-dom";

const DriverProvider = ({ children }: IDefaultChildrenProp) => {
  const navigate = useNavigate();
  const token = localStorage.getItem("token") || null;
  const { handleCloseModal } = useModal();

  const [driverList, setDriverList] = useState<Array<IDriver>>([]);
  const [driverQuantity, setDriverQuantity] = useState<number | 0>(0);
  const [driverActive, setDriverActive] = useState<number | 0>(0);
  const [driverInactive, setDriverInative] = useState<number | 0>(0);
  const [driverUnderEdition, setDriverUnderEdition] = useState<IDriver | null>(
    null
  );

  const headersAuth = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };

  const handleCreateDriver = async (newDriverData: ICreateDriverData) => {
    try {
      const newDriverResponse: AxiosResponse<ICreateDriverResponse> =
        await api.post<ICreateDriverResponse>(
          "/drivers/create",
          newDriverData,
          headersAuth
        );

      if (newDriverResponse.status === 201) {
        toast.success("Motorista criado com sucesso!");
      }
    } catch (error) {
      console.log(error);
      toast.error("Ops, verifique os dados e a internet e tente novamente...");
    }
  };

  const getDriverList = async () => {
    try {
      const driverListResponse: AxiosResponse<IGetDriversResponse> =
        await api.get("/drivers/list");

      if (driverListResponse.status === 200) {
        const driverListApi: Array<IDriver> = driverListResponse.data.items;
        toast.success("Lista de motoristas carregada!");
        setDriverList(driverListApi);
        const quantity = driverListApi.length;
        const active = driverListApi.filter((driver) => driver.isActive).length;
        const inactive = quantity - active;
        setDriverQuantity(quantity);
        setDriverActive(active);
        setDriverInative(inactive);
      }
    } catch (error) {
      console.log(error);
      toast.error("Falha ao carregar lista de motoristas!");
    }
  };

  const getDriverByID = async (id: string) => {
    try {
      const driverResponse: AxiosResponse<IDriver> = await api.get(
        `/drivers/${id}`
      );

      console.log(driverResponse);
      if (driverResponse.status === 200) {
        const driverFound: IDriver = driverResponse.data;
        toast.success("Motorista encontrado");
        setDriverUnderEdition(driverFound);
      }
    } catch (error) {
      console.log(error);
      toast.error("Falha ao atualizar o motorista!");
    }
  };

  const deleteDriver = async (id: string) => {
    try {
      const driverResponse: AxiosResponse = await api.delete(
        `/drivers/delete/${id}`
      );

      if (driverResponse.status === 204) {
        handleCloseModal();
        getDriverList();
        toast.success("Motorista deletado");
      }
    } catch (error) {
      console.log(error);
      toast.error("Erro ao deletar motorista");
    }
  };

  const updateDriver = async (id: string, driverData: IUpdateDriverData) => {
    try {
      const driverListResponse: AxiosResponse<IUpdateDriverData> =
        await api.put<IUpdateDriverData>(`/drivers/update/${id}`, driverData);
      if (driverListResponse.status === 200) {
        toast.success("Motorista atualizado com sucesso");
        navigate("/dashboard/motoristas");
      }
    } catch (error) {
      console.log(error);
      toast.error("Falha ao atualizar o motorista!");
    }
  };

  return (
    <DriverContext.Provider
      value={{
        driverList,
        handleCreateDriver,
        getDriverList,
        getDriverByID,
        updateDriver,
        deleteDriver,
        driverActive,
        driverInactive,
        driverQuantity,
        driverUnderEdition,
        setDriverUnderEdition,
      }}
    >
      {children}
    </DriverContext.Provider>
  );
};

export { DriverProvider };
