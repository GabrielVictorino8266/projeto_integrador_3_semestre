import type { DataProps } from "@schemas/CadsVeiculos";
import { api } from "@services/api";
import { toast } from "react-toastify";
import { InvertDate } from "@utils/Mask/InvertDate";

export async function VehiclesRegistration(
    data: DataProps,
    id?: string
): Promise<boolean> {
    try {
        data.anoVeiculo = InvertDate(data.anoVeiculo);
        console.log(data.anoVeiculo);
        
        const response = id
            ? await api.put("teste/teste/", data)
            : await api.post("teste/teste/", data);

        if (response.status === 200) {
            toast.success(
                id
                    ? "Veículo registrado com sucesso!"
                    : "Veículos atualizado com seucesso!"
            );
            return true;
        } else {
            toast.warn("Problem com servidor.");
            return false;
        }
    } catch (error: any) {
        const status = error.resposne?.status;

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
