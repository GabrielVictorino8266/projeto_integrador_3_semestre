import type {
    IGetVehiclesResponse,
    VehicleStatus,
} from "@interfaces/vehicles.interface";
import { api } from "@services/api";
import { toast } from "react-toastify";

export interface GetVehiclesParams {
    page?: number;
    limit?: number;
    status?: VehicleStatus;
    licensePlate?: string;
}

export async function getVehicles({
    limit = 6,
    ...rest
}: GetVehiclesParams = {}): Promise<IGetVehiclesResponse | null> {
    try {
        const response = await api.get("/vehicles/", {
            params: { limit, ...rest },
        });

        return response.data;
    } catch (error: any) {
        const status = error.response?.status;
        switch (status) {
            case 400:
                toast.error("Requisição inválida");
                break;
            case 401:
                toast.error("Não autorizado");
                break;
            default:
                toast.error("Erro inesperado");
        }
    }
    return null;
}
