import type { IGetVehiclesResponse, VehicleStatus } from "@interfaces/vehicles.interface";
import { api } from "@services/api";
import { toast } from "react-toastify";

export interface GetVehiclesParams {
    page?: number;
    limit?: number;
    status?: VehicleStatus;
    licensePlate?: string;
}

export async function getVehicles({limit = 6,page, licensePlate, status,}: GetVehiclesParams = {}): Promise<IGetVehiclesResponse | null> {

    try {
        const params: any = { limit, page, licensePlate };
        if (status) params.status = status;

        const response = await api.get("/vehicles/", { params });
        return response.data;
    } catch (error: any) {
        const statusCode = error.response?.status;

        switch (statusCode) {
            case 400:
                toast.error(`Requisição inválida`);
                break;
            case 401:
                toast.error("Não autorizado");
                break;
            default:
                toast.error("Erro inesperado, verifique sua conexão");
        }
    }
    return null;
}
