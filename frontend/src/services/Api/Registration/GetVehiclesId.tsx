import { api } from "@services/api";
import { toast } from "react-toastify";

export async function getVehiclesId(id: string) {
    try {
        const response = await api.get(`/veiculos/${id}`);

        if (response.status === 200) {
            return response.data
        }
    } catch (error: any) {
        const status = error.response?.status;

        switch (status) {
            case 401:
                toast.error("Não foi possível encontrar o veículo");
                break;
            case 500:
                toast.error(
                    "Erro interno do servidor.Tente novamente mais tarde."
                );
                break;
            default:
                toast.error("Erro inesperado. Verifique sua conexão.");
        }
    }
}
