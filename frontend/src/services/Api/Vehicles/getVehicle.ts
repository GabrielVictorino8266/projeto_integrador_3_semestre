import type { IGetVehiclesResponse } from "@interfaces/vehicles.interface";
import { api } from "@services/api";
import { toast } from "react-toastify";

export async function getVehicles(): Promise<IGetVehiclesResponse | null> {
    try {
        const { data } = await api.get("/vehicles/");
        return data;
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
