import type { TripsResponse } from "@interfaces/trips.interface";
import { api } from "@services/api";
import { toast } from "react-toastify";

export interface GetVehicleParams {
    page?: number;
    limit?: number;
    status?: number;
}

export async function getTrips({ limit, page, status }: GetVehicleParams = {}): Promise<TripsResponse | null> {
    try {
        const params: GetVehicleParams = { limit, page, status };

        const { data } = await api.get<TripsResponse>("/trips/list", { params });
        console.log(data);
        return data;
    } catch (error: any) {
        const statusCode = error.response?.status;

        switch (statusCode) {
            case 400:
                toast.error("Tipo de requisição inválida");
                break;
            case 401:
                toast.error("Não autenticado");
                break;
            case 403:
                toast.error("Você não tem permissão necessária");
                break;
        }
        return null;
    }
}
