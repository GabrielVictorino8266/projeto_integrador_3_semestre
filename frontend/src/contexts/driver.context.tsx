/* eslint-disable @typescript-eslint/no-unused-vars */
import type { IDriverContextProps } from "@interfaces/driver.interface";
import type { IDriverRegisterData } from "@schemas/driverRegisterSchema";
import { createContext, type SetStateAction } from "react";

const DriverContext = createContext<IDriverContextProps>({
  handleCreateDriver: function (
    newDriverData: IDriverRegisterData
  ): Promise<void> {
    throw new Error("Function not implemented.");
  },
  getDriverList: function (): void {
    throw new Error("Function not implemented.");
  },
  driverList: [],
  driverQuantity: 0,
  driverActive: 0,
  driverInactive: 0,
  handleInputMask: function (event: React.ChangeEvent<HTMLInputElement>): void {
    throw new Error("Function not implemented.");
  },
  handleDateMask: function (event: React.ChangeEvent<HTMLInputElement>): void {
    throw new Error("Function not implemented.");
  },
  cpfMask: function (value: string): string {
    throw new Error("Function not implemented.");
  },
  dateMask: function (value: string): string {
    throw new Error("Function not implemented.");
  },
  inputValue: "",
  inputDate: "",
  getDriverByID: function (id: string): Promise<void> {
    throw new Error("Function not implemented.");
  },
  driverUnderEdition: null,
  setDriverUnderEdition: function (
    value: SetStateAction<IDriverRegisterData | null>
  ): void {
    throw new Error("Function not implemented.");
  },
});

export { DriverContext };
