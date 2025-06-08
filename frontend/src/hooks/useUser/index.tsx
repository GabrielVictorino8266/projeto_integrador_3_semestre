import { useEffect, useState } from "react";
type Usuario = {
    nome: string | null;
    cargo: string | null;
}

export function useUsuario(){
    const [user, setUser] = useState<Usuario | null>(null)
    
    useEffect( () => {

        const requisicao = async () => {
            const nomeCompleto = localStorage.getItem("nome")
            const primeiroNome = nomeCompleto ? nomeCompleto.split(" ")[0] : ""

            const teste: Usuario = {
                nome: primeiroNome,
                cargo: localStorage.getItem("cargo") 
            }
            setUser(teste)
        }

        requisicao();

    },[])

    return { user }
}
