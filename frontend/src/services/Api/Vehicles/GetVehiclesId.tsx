import { api } from "@services/api";
import { toast } from "react-toastify";
import type { DataProps } from "@schemas/CadsVeiculos";
import { MaskKm } from "@utils/Mask/MaskKm";
import { MaskLicensePlate } from "@utils/Mask/MaskLicensePlate";

export async function getVehiclesId(id: string): Promise<DataProps | null> {
    try {
        const { data } = await api.get(`/vehicles/${id}/`);

        const kmMask = new MaskKm();
        const plate = new MaskLicensePlate();

        const newData = {
            ...data,
            currentKm: kmMask.mask(String(data.currentKm)),
            warningKmLimit: kmMask.mask(String(data.warningKmLimit)),
            licensePlate: plate.mask(data.licensePlate)
        };

        return newData;
    } catch (error: any) {
        const status = error.response?.status;

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
