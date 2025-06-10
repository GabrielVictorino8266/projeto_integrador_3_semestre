/* eslint-disable @typescript-eslint/no-unused-vars */
import type { IDriverContextProps } from "@interfaces/driver.interface";
import type { IDriverRegisterData } from "@schemas/driverRegisterSchema";
import { createContext } from "react";

const DriverContext = createContext<IDriverContextProps>({
  handleCreateDriver: function (
    _newDriverData: IDriverRegisterData
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
  handleInputMask: function (
    _event: React.ChangeEvent<HTMLInputElement>
  ): void {},
  handleDateMask: function (
    _event: React.ChangeEvent<HTMLInputElement>
  ): void {},
  cpfMask: function (_value: string): string {
    return "";
  },
  dateMask: function (_value: string): string {
    return "";
  },
  inputValue: "",
  inputDate: "",
});

export { DriverContext };
