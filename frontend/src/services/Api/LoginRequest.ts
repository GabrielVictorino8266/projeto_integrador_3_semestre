import type { DataProps } from "@schemas/LoginSchema";
import { api } from "@services/api";
import { ClearMask } from "@utils/Mask/ClearMask";
import { toast } from "react-toastify";

export async function LoginRequest(data: DataProps): Promise<boolean> {
    
    const cpf = ClearMask(data.cpf);
    localStorage.clear();

    try {
        const response = await api.post("/users/login/", {
            cpf: cpf,
            password: data.password,
        });

        if (response.status === 200) {
            toast.success(`Bem vinde, ${response.data.user.name}`);
            localStorage.setItem("token", response.data.access_token);
            localStorage.setItem("nome", response.data.user.name);
            localStorage.setItem("cargo", response.data.user.type);
            return true;
        } else {
            toast.warn("Problema com o servidor.");
            return false;
        }
    } catch (error: any) {
        const status = error.response?.status;
        switch (status) {
            case 401:
                toast.error("CPF ou senha inválidos.");
                break;
            case 500:
                toast.error("Erro interno do servidor. Tente novamente mais tarde.");
                break;
            default:
                toast.error("Erro inesperado. Verifique sua conexão.");
        }
        return false;
    }
}
