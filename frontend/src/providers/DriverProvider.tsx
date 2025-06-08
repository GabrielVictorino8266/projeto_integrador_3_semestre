import type { IDefaultChildrenProp } from "../interfaces";
import type { IDriverRegisterData } from "@schemas/driverRegisterSchema";
import type { AxiosResponse } from "axios";
import { api } from "@services/api";
import { toast } from "react-toastify";
import { DriverContext } from "@contexts/driver.context";

const DriverProvider = ({ children }: IDefaultChildrenProp) => {
    const token = localStorage.getItem('@TOKEN') || null;

    const headersAuth = {
        headers: {
            Authorization: `Bearer ${token}`
        }
    };

    const handleCreateDriver = async (newDriverData: IDriverRegisterData) => {
        try {
            const newDriverResponse: AxiosResponse = await api.post<IDriverRegisterData>(
                '/motorista',
                newDriverData,
                headersAuth
            );

            if (newDriverResponse.status === 201) {
                toast.success("Motorista criado com sucesso!")
            }

        } catch (error) {
            console.log(error);
            toast.error('Ops, verifique os dados e a internet e tente novamente...');
        }
    };

    return (
        <DriverContext.Provider
            value={{
                handleCreateDriver
            }}
        >
            {children}
        </DriverContext.Provider>
    );
};

export { DriverProvider };




