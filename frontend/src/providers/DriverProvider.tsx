import type { IDefaultChildrenProp } from "../interfaces";
import type { IDriverRegisterData } from "@schemas/driverRegisterSchema";
import type { AxiosResponse } from "axios";
import { api } from "@services/api";
import { toast } from "react-toastify";
import { DriverContext } from "@contexts/driver.context";
import { useState } from "react";
import { type IDriverListResponse } from "@interfaces/driver.interface";

const DriverProvider = ({ children }: IDefaultChildrenProp) => {
  const token = localStorage.getItem("@TOKEN") || null;
  const [driverList, setDriverList] = useState<IDriverListResponse | []>([]);
  const [driverQuantity, setDriverQuantity] = useState<number | 0>(0);
  const [driverActive, setDriverActive] = useState<number | 0>(0);
  const [driverInactive, setDriverInative] = useState<number | 0>(0);
  const [inputValue, setInputValue] = useState("");
  const [inputDate, setInputDate] = useState("");

  const headersAuth = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };

  const handleCreateDriver = async (newDriverData: IDriverRegisterData) => {
    try {
      const newDriverResponse: AxiosResponse =
        await api.post<IDriverRegisterData>(
          "/motorista",
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
      const driverListResponse = await api.get("/drivers/list");
      if (driverListResponse.status === 200) {
        const driverListApi: IDriverListResponse =
          driverListResponse.data.items;
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
    }
  };

  const cpfMask = (value: string) => {
    return value
      .replace(/\D/g, "")
      .replace(/(\d{3})(\d)/, "$1.$2")
      .replace(/(\d{3})(\d)/, "$1.$2")
      .replace(/(\d{3})(\d{1,2})/, "$1-$2")
      .replace(/(-\d{2})\d+?$/, "$1");
  };

  const dateMask = (value: string) => {
    return value
      .replace(/\D/g, "")
      .replace(/^(\d{2})(\d)/, "$1/$2")
      .replace(/^(\d{2})\/(\d{2})(\d)/, "$1/$2/$3")
      .slice(0, 10);
  };

  const handleInputMask = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(cpfMask(event.target.value));
  };

  const handleDateMask = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputDate(dateMask(event.target.value));
  };

  return (
    <DriverContext.Provider
      value={{
        driverList,
        handleCreateDriver,
        getDriverList,
        driverActive,
        driverInactive,
        driverQuantity,
        cpfMask,
        dateMask,
        handleInputMask,
        handleDateMask,
        inputDate,
        inputValue,
      }}
    >
      {children}
    </DriverContext.Provider>
  );
};

export { DriverProvider };
