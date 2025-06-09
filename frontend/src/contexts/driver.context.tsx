import type { IDriverContextProps } from "@interfaces/driver.interface";
import type { IDriverRegisterData } from "@schemas/driverRegisterSchema";
import { createContext } from "react";

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
});

export { DriverContext };
