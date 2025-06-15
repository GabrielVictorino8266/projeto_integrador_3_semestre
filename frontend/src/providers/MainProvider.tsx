import type { IDefaultChildrenProp } from "@interfaces/default.interface";
import { DriverProvider } from "./DriverProvider";
import { ModalProvider } from "./ModalProvider";
import { VehicleProvider } from "./VehicleProvider"; 

const MainProvider = ({ children }: IDefaultChildrenProp) => {
  return (
    <ModalProvider>
      <DriverProvider>
        <VehicleProvider>
          {children}
        </VehicleProvider>
      </DriverProvider>
    </ModalProvider>
  );
};

export { MainProvider };
