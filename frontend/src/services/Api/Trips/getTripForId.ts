import type { TripsIdResponse } from "@interfaces/trips.interface";
import { api } from "@services/api";
import { toast } from "react-toastify";


export async function getTripForID(id:string): Promise<TripsIdResponse | null> {
    
    try{
        const {data} = await api.get(`/trips/list/${id}`)

        return data

    }catch(error: any){
        const statusCode = error?.resp.status

        switch(statusCode){
            case 400:
                toast.error("ID inválido")
                break;
            case 403:
                toast.error("Não autorizado")
                break;
            case 404:
                toast.error("Viagem não encontrado")
                break
            default:
                toast.error("Erro inesperado, verifique sua conexão e tente novamente")
                break
        }
        return null
    }

}