import { api } from "@services/api";
import { toast } from "react-toastify";

export async function deleteTrip(id: string) {
    try {
        await api.delete(`/trips/delete/${id}`);
        return true;
    } catch (error: any) {
        const statusCode = error?.response?.status;

        switch (statusCode) {
            case 400:
                toast.error("ID da viagem inválido");
                break;
            case 401:
                toast.error("Não autenticado");
                break;
            case 404:
                toast.error("Viagem não encontrada");
                break;
            case 500:
                toast.error("Erro ao processar a requisição");
                break;
            default:
                toast.error("Erro inesperado, verifique sua conexão e tente novamente!");
        }

        return false;
    }
}
