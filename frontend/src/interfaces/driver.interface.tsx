import type { IDriverRegisterData } from "@schemas/driverRegisterSchema";


export interface IDriverChildrenProps {
    children: React.ReactNode;
}

export interface IDriverContextProps {
    handleCreateDriver: (newDriverData: IDriverRegisterData) => Promise<void>
}