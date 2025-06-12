import { api } from "@services/api";
import { toast } from "react-toastify";
import type { DataProps } from "@schemas/CadsVeiculos";

export async function getVehiclesId(id: string): Promise<DataProps | null> {
    try {
        const response = await api.get(`/vehicles/${id}/`);

        if (response.status === 200) {
            return response.data;
        }
    } catch (error: any) {
        const status = error.response?.status;
        console.log("Erro detalhado", error.response?.data);

        switch (status) {
            case 401:
                toast.error("Não autorizado.");
                break;
            case 404:
                toast.error("Veículo não encontrado.");
                break;
            case 500:
                toast.error("Erro interno do servidor.");
                break;
            default:
                toast.error("Erro inesperado.");
        }
    }

    return null;
}
