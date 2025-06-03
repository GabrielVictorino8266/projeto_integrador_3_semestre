import type { IDefaultChildrenProp } from "@interfaces/default.interface";
import { DriverProvider } from "./DriverProvider";
import { ModalProvider } from "./ModalProvider";

const MainProvider = ({ children }: IDefaultChildrenProp) => {
  return <>
    <ModalProvider>
      <DriverProvider>
        {children}
      </DriverProvider>
    </ModalProvider>
  </>
};

export { MainProvider };
