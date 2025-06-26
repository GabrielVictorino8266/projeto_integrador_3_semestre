import { api } from "@services/api"
import { toast } from "react-toastify"

export async function DeleteVehicle(id:string) {
    try{
        api.delete(`/vehicles/delete/${id}/`)
        
        toast.success("Veículo deletado com sucesso!")
    }catch(error: any){
        const status = error.response?.status
        switch(status){
            case 400:
                toast.error("Requisição inválida")
                break
            case 401:
                toast.error("Não autorizado")
                break
            case 404:
                toast.error("Veículo não encontrado")
                break
            default:
                toast.error("Erro inesperado, verifique sua conexão")
        }
    }
}