import type { DataProps } from "@schemas/CadsVeiculos";
import { api } from "@services/api";
import { toast } from "react-toastify";

export async function VehiclesRegistration(
    data: DataProps,
    id?: string
): Promise<boolean> {
    try {
        console.log("Data", data);

        const newData = {
            ...data,
            manufacturingYear: Number(data.manufacturingYear),
            currentKm: Number(data.currentKm.replace(/\D/g, "")),
            warningKmLimit: Number(data.warningKmLimit.replace(/\D/g, "")),
        };

        const response = id
            ? await api.put(`/vehicles/update/${id}/`, newData)
            : await api.post("/vehicles/create/", newData);

        if (response.status === 200 || response.status === 201) {
            toast.success(
                id
                    ? "Veículo atualizado com sucesso!"
                    : "Veículos registrado com seucesso!"
            );
            return true;
        } else {
            toast.warn("Problem com servidor.");
            return false;
        }
    } catch (error: any) {
        const status = error.resposne?.status;
        console.log("Erro detalhado", error.response?.data);

        switch (status) {
            case 401:
                toast.error("Veículos não encontrado");
                break;
            case 500:
                toast.error(
                    "Erro interno do servidor. Tente novamente mais tarde."
                );
                break;
            default:
                toast.error("Erro inesperado. Verifique sua conexão.");
        }
        return false;
    }
}
